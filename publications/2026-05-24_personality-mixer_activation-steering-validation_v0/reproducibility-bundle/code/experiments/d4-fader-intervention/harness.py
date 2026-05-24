"""
harness.py — D4 fader-intervention eval driver.

Runs Qwen-2.5-7B-Instruct with a forward hook on the extraction layer that adds
`coefficient * steering_vector` to the residual stream at every token position.
For each probe × condition × coefficient combination, generates one completion.

Two execution modes — both reach the same artefacts on disk:

  (1) Modal — fast, free under the Modal credit budget. Usage:
        .venv/bin/modal run experiments/d4-fader-intervention/harness.py::eval \\
            --channel conscientiousness_self_discipline \\
            --probes experiments/d4-fader-intervention/probes/conscientiousness-self-discipline.json \\
            --vectors infra/steering-vectors/qwen2.5-7b-instruct/conscientiousness_self_discipline/vector.pt \\
            --layer 16 \\
            --coefficients 0.5,1.0,1.5,2.0

  (2) Local M4 mini (MPS, fp16). Slower but free of Modal cost. Usage:
        python3 experiments/d4-fader-intervention/harness.py \\
            --channel ... --probes ... --vectors ... --layer 16 \\
            --coefficients 0.5,1.0,1.5,2.0 \\
            --device mps --max-probes 5

Output (both modes write the same shape):
  experiments/d4-fader-intervention/runs/<channel>/<probe>_<cond>_c<coef>_s<seed>.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    import modal
    _MODAL_AVAILABLE = True
except ImportError:
    _MODAL_AVAILABLE = False


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "experiments" / "d4-fader-intervention" / "runs"


# --- Schema ------------------------------------------------------------------

@dataclass
class HarnessConfig:
    channel_id: str
    layers: tuple[int, ...]
    coefficients: tuple[float, ...]
    conditions: tuple[str, ...] = ("low", "high")
    model_id: str = DEFAULT_MODEL_ID
    max_new_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    seed: int = 0


# --- Probe loader (no torch, no modal) ---------------------------------------

def load_probes(path: Path) -> list[dict]:
    with path.open() as f:
        obj = json.load(f)
    if "probes" not in obj or not isinstance(obj["probes"], list):
        raise ValueError(f"{path} missing 'probes' list")
    return obj["probes"]


def validate_inputs(cfg: HarnessConfig, probes: list[dict], vectors_path: Path, require_vectors: bool = True) -> None:
    if require_vectors and not vectors_path.exists():
        raise FileNotFoundError(f"steering vector not found: {vectors_path} — run extract_caa.py first")
    if not require_vectors and not vectors_path.exists():
        print(f"WARNING: vector path {vectors_path} does not exist (skipped under --dry-run)", file=sys.stderr)
    if not probes:
        raise ValueError("probe library is empty")
    if not cfg.layers:
        raise ValueError("layers tuple is empty")
    for L in cfg.layers:
        if L < 0 or L > 28:
            raise ValueError(f"layer {L} out of range for Qwen2.5-7B")
    if len(set(cfg.layers)) != len(cfg.layers):
        raise ValueError(f"duplicate layer in layers tuple: {cfg.layers}")
    for c in cfg.coefficients:
        if abs(c) > 10:
            raise ValueError(f"coefficient {c} unusually large; capability degrades sharply above ~50")
    print(
        f"OK: channel={cfg.channel_id}, probes={len(probes)}, "
        f"layers={cfg.layers} ({'multi' if len(cfg.layers)>1 else 'single'}), "
        f"conditions={cfg.conditions}, coefs={cfg.coefficients}",
        file=sys.stderr,
    )


# --- Steering hook + generation core (used by both Modal + local) ------------

def _generation_core(
    cfg_dict: dict,
    probes: list[dict],
    vector_pt_bytes: bytes,
    device: str,
):
    """Pure-torch generation loop. Called from both the Modal remote function and
    the local entrypoint when the user has torch installed locally."""
    import io
    import datetime
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    cfg = HarnessConfig(
        channel_id=cfg_dict["channel_id"],
        layers=tuple(cfg_dict["layers"]),
        coefficients=tuple(cfg_dict["coefficients"]),
        conditions=tuple(cfg_dict["conditions"]),
        model_id=cfg_dict["model_id"],
        max_new_tokens=cfg_dict["max_new_tokens"],
        temperature=cfg_dict["temperature"],
        top_p=cfg_dict["top_p"],
        seed=cfg_dict["seed"],
    )

    print(f"loading {cfg.model_id} on {device}...", flush=True)
    tok = AutoTokenizer.from_pretrained(cfg.model_id)
    dtype = torch.float16
    model = AutoModelForCausalLM.from_pretrained(cfg.model_id, torch_dtype=dtype)
    model.to(device)
    model.eval()

    print(f"loading steering vector...", flush=True)
    vectors = torch.load(io.BytesIO(vector_pt_bytes), map_location=device)
    # Build per-layer steering tensors. Vector file may be either a single tensor
    # (legacy single-layer extraction) or a dict[int, Tensor] (layer-sweep extraction).
    steering_by_layer: dict[int, "torch.Tensor"] = {}
    if isinstance(vectors, dict):
        missing = [L for L in cfg.layers if L not in vectors]
        if missing:
            raise KeyError(
                f"vector file missing layers {missing}; have {sorted(vectors.keys())}"
            )
        for L in cfg.layers:
            steering_by_layer[L] = vectors[L].to(device).to(dtype)
    else:
        if len(cfg.layers) > 1:
            raise ValueError(
                "vector file is a single tensor — cannot multi-layer steer; "
                "re-extract with layer-sweep covering the requested layers"
            )
        steering_by_layer[cfg.layers[0]] = vectors.to(device).to(dtype)

    def make_hook(coefficient: float, vec: "torch.Tensor"):
        def hook(_module, _input, output):
            if isinstance(output, tuple):
                hs = output[0]
                modified = hs + coefficient * vec.to(hs.device).to(hs.dtype)
                return (modified,) + output[1:]
            else:
                return output + coefficient * vec.to(output.device).to(output.dtype)
        return hook

    # Architecture-aware decoder-layer accessor (matches extract_caa.py).
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        decoder_layers = model.model.layers
    elif hasattr(model, "gpt_neox") and hasattr(model.gpt_neox, "layers"):
        decoder_layers = model.gpt_neox.layers
    elif hasattr(model, "transformer") and hasattr(model.transformer, "h"):
        decoder_layers = model.transformer.h
    else:
        raise ValueError(f"Cannot locate decoder layers in {type(model).__name__}")

    # Chat template is Qwen/Llama specific. Pythia base has no template.
    has_chat_template = hasattr(tok, "chat_template") and tok.chat_template is not None

    records: list[dict] = []
    total = len(probes) * len(cfg.conditions) * len(cfg.coefficients)
    n_done = 0
    for probe in probes:
        # Multi-turn support: if probe has "messages" field (list of {role, content}),
        # use that directly. Else fall back to single-turn from "prompt" field.
        if "messages" in probe and isinstance(probe["messages"], list):
            messages = probe["messages"]
        else:
            messages = [{"role": "user", "content": probe["prompt"]}]
        if has_chat_template:
            chat = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            # Base-model path (Pythia etc.): format as User/Assistant raw text completion.
            # Pythia has seen plenty of conversations in pretraining and completes naturally.
            parts = []
            for m in messages:
                role_label = "User" if m["role"] == "user" else "Assistant"
                parts.append(f"{role_label}: {m['content']}")
            chat = "\n\n".join(parts) + "\n\nAssistant:"
        inputs = tok(chat, return_tensors="pt").to(device)
        n_input = inputs["input_ids"].shape[1]

        for condition in cfg.conditions:
            sign = +1 if condition == "high" else (-1 if condition == "low" else 0)
            for coef in cfg.coefficients:
                signed_coef = sign * coef
                handles = []
                for L in cfg.layers:
                    h = decoder_layers[L].register_forward_hook(
                        make_hook(signed_coef, steering_by_layer[L])
                    )
                    handles.append(h)
                try:
                    torch.manual_seed(cfg.seed)
                    t0 = time.monotonic()
                    with torch.no_grad():
                        out_ids = model.generate(
                            **inputs,
                            max_new_tokens=cfg.max_new_tokens,
                            temperature=cfg.temperature,
                            top_p=cfg.top_p,
                            do_sample=True,
                            pad_token_id=tok.eos_token_id,
                        )
                    elapsed = time.monotonic() - t0
                    gen_ids = out_ids[0, n_input:]
                    text = tok.decode(gen_ids, skip_special_tokens=True)
                finally:
                    for h in handles:
                        h.remove()

                records.append({
                    "channel_id": cfg.channel_id,
                    "probe_id": probe["id"],
                    "probe_category": probe.get("category", ""),
                    "probe_subtype": probe.get("subtype", ""),
                    "prompt": probe["prompt"],
                    "condition": condition,
                    "coefficient": signed_coef,
                    "layers": list(cfg.layers),
                    "output": text,
                    "output_tokens": int(gen_ids.shape[0]),
                    "elapsed_seconds": elapsed,
                    "model_id": cfg.model_id,
                    "seed": cfg.seed,
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                })
                n_done += 1
                print(f"  [{n_done}/{total}] {probe['id']} {condition} c={coef} ({int(gen_ids.shape[0])} tok, {elapsed:.1f}s)", flush=True)
    return records


def write_records(records: list[dict], out_root: Path) -> int:
    out_root.mkdir(parents=True, exist_ok=True)
    n = 0
    for rec in records:
        path = out_root / f"{rec['probe_id']}_{rec['condition']}_c{abs(rec['coefficient']):.2f}_s{rec['seed']}.json"
        path.write_text(json.dumps(rec, indent=2))
        n += 1
    return n


# --- Modal app ---------------------------------------------------------------

if _MODAL_AVAILABLE:
    app = modal.App("mg-digital-twin-d4-eval")

    image = (
        modal.Image.debian_slim(python_version="3.11")
        .apt_install("git")
        .pip_install(
            "torch==2.4.0",
            "transformers==4.45.0",
            "accelerate==0.34.0",
            "huggingface_hub==0.25.0",
        )
    )
    hf_cache = modal.Volume.from_name("hf-cache", create_if_missing=True)

    @app.function(
        image=image,
        gpu="A100-40GB",
        timeout=7200,  # 2 hr — 240 gens × ~25s = 6000s for 512-token outputs
        secrets=[modal.Secret.from_name("huggingface-token", required_keys=["HF_TOKEN"])],
        volumes={"/root/.cache/huggingface": hf_cache},
    )
    def generate_remote(cfg_dict: dict, probes: list[dict], vector_pt_bytes: bytes) -> list[dict]:
        """Runs on Modal A100. Loads model from cached HF volume."""
        return _generation_core(cfg_dict, probes, vector_pt_bytes, device="cuda")

    @app.function(
        image=image,
        gpu="A100-40GB",
        timeout=7200,
        secrets=[modal.Secret.from_name("huggingface-token", required_keys=["HF_TOKEN"])],
        volumes={"/root/.cache/huggingface": hf_cache},
    )
    def generate_dialogue_remote(
        cfg_dict: dict,
        starters: list[dict],
        followups: list[str],
        vector_pt_bytes: bytes,
    ) -> list[dict]:
        """Multi-turn dialogue mode. For each starter, runs `1 + len(followups)`
        turns sequentially, accumulating conversation history. Steering applied
        identically at every turn. Returns one record per (starter, turn)."""
        import io
        import datetime
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        cfg = HarnessConfig(
            channel_id=cfg_dict["channel_id"],
            layers=tuple(cfg_dict["layers"]),
            coefficients=tuple(cfg_dict["coefficients"]),
            conditions=tuple(cfg_dict["conditions"]),
            model_id=cfg_dict["model_id"],
            max_new_tokens=cfg_dict["max_new_tokens"],
            temperature=cfg_dict["temperature"],
            top_p=cfg_dict["top_p"],
            seed=cfg_dict["seed"],
        )

        device = "cuda"
        dtype = torch.float16
        print(f"loading {cfg.model_id} for multi-turn dialogue...", flush=True)
        tok = AutoTokenizer.from_pretrained(cfg.model_id)
        model = AutoModelForCausalLM.from_pretrained(cfg.model_id, torch_dtype=dtype)
        model.to(device)
        model.eval()

        vectors = torch.load(io.BytesIO(vector_pt_bytes), map_location=device)
        steering_by_layer: dict[int, "torch.Tensor"] = {}
        if isinstance(vectors, dict):
            for L in cfg.layers:
                if L not in vectors:
                    raise KeyError(f"vector file missing layer {L}; have {sorted(vectors.keys())}")
                steering_by_layer[L] = vectors[L].to(device).to(dtype)
        else:
            steering_by_layer[cfg.layers[0]] = vectors.to(device).to(dtype)

        def make_hook(coefficient: float, vec):
            def hook(_module, _input, output):
                if isinstance(output, tuple):
                    hs = output[0]
                    return (hs + coefficient * vec.to(hs.device).to(hs.dtype),) + output[1:]
                return output + coefficient * vec.to(output.device).to(output.dtype)
            return hook

        records = []
        # Each construct uses signed_coef = +1.0 (HIGH) × cfg.coefficients[0] applied
        # to the composite vector. cfg.coefficients[0] is the runtime scaling.
        coef = cfg.coefficients[0] if cfg.coefficients else 1.0

        for starter in starters:
            conversation = [{"role": "user", "content": starter["starter_prompt"]}]
            n_turns_total = 1 + len(followups)

            for turn_idx in range(n_turns_total):
                chat = tok.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
                inputs = tok(chat, return_tensors="pt").to(device)
                n_input = inputs["input_ids"].shape[1]

                handles = []
                for L in cfg.layers:
                    h = model.model.layers[L].register_forward_hook(
                        make_hook(coef, steering_by_layer[L])
                    )
                    handles.append(h)
                try:
                    torch.manual_seed(cfg.seed + turn_idx)  # different seed per turn for variety
                    t0 = time.monotonic()
                    with torch.no_grad():
                        out_ids = model.generate(
                            **inputs,
                            max_new_tokens=cfg.max_new_tokens,
                            temperature=cfg.temperature,
                            top_p=cfg.top_p,
                            do_sample=True,
                            pad_token_id=tok.eos_token_id,
                        )
                    elapsed = time.monotonic() - t0
                    gen_ids = out_ids[0, n_input:]
                    text = tok.decode(gen_ids, skip_special_tokens=True)
                finally:
                    for h in handles:
                        h.remove()

                records.append({
                    "channel_id": cfg.channel_id,
                    "starter_id": starter["id"],
                    "turn_idx": turn_idx,
                    "conversation_so_far": list(conversation),  # snapshot before assistant turn
                    "output": text,
                    "output_tokens": int(gen_ids.shape[0]),
                    "elapsed_seconds": elapsed,
                    "coefficient": coef,
                    "layers": list(cfg.layers),
                    "model_id": cfg.model_id,
                    "seed": cfg.seed + turn_idx,
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                })
                print(f"  starter={starter['id']} turn={turn_idx} ({int(gen_ids.shape[0])} tok, {elapsed:.1f}s)", flush=True)

                # Append assistant response and next user followup
                conversation.append({"role": "assistant", "content": text})
                if turn_idx < len(followups):
                    conversation.append({"role": "user", "content": followups[turn_idx]})

        return records

    @app.local_entrypoint()
    def eval_dialogue(
        channel: str,
        starters: str,  # JSON file with [{id, starter_prompt}, ...]
        followups: str,  # JSON file with [str, ...]
        vectors: str,
        layers: str = "16",
        coefficient: float = 1.0,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.9,
        seed: int = 0,
        out_suffix: str = "_multiturn",
    ):
        """Multi-turn dialogue evaluation. Each construct's responses accumulate
        in its own conversation history; user-side messages are deterministic
        (shared starter + shared followups). Tests whether persona discriminability
        emerges as turns accumulate (vs single-shot)."""
        starters_path = Path(starters)
        followups_path = Path(followups)
        vectors_path = Path(vectors)

        starter_list = json.loads(starters_path.read_text())
        if isinstance(starter_list, dict) and "starters" in starter_list:
            starter_list = starter_list["starters"]
        followup_list = json.loads(followups_path.read_text())
        if isinstance(followup_list, dict) and "followups" in followup_list:
            followup_list = followup_list["followups"]

        layer_tuple = tuple(int(L) for L in layers.split(","))
        cfg = HarnessConfig(
            channel_id=channel,
            layers=layer_tuple,
            coefficients=(coefficient,),
            conditions=("high",),
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            seed=seed,
        )
        # Skip standard validate_inputs (it expects probes list); minimal checks instead.
        if not vectors_path.exists():
            raise FileNotFoundError(f"vectors not found: {vectors_path}")
        if not starter_list:
            raise ValueError("starters empty")
        if not followup_list:
            raise ValueError("followups empty")

        cfg_dict = asdict(cfg)
        cfg_dict["layers"] = list(layer_tuple)
        cfg_dict["coefficients"] = list(cfg.coefficients)
        cfg_dict["conditions"] = list(cfg.conditions)
        vector_bytes = vectors_path.read_bytes()

        n_total = len(starter_list) * (1 + len(followup_list))
        print(f"running {len(starter_list)} starters × {1+len(followup_list)} turns "
              f"= {n_total} sequential generations on Modal A100...", file=sys.stderr)
        records = generate_dialogue_remote.remote(cfg_dict, starter_list, followup_list, vector_bytes)

        out_root = DEFAULT_OUTPUT_DIR / (channel + out_suffix)
        out_root.mkdir(parents=True, exist_ok=True)
        for rec in records:
            path = out_root / f"{rec['starter_id']}_t{rec['turn_idx']:02d}.json"
            path.write_text(json.dumps(rec, indent=2))
        print(f"\n✓ wrote {len(records)} dialogue records to {out_root}", file=sys.stderr)

    @app.local_entrypoint()
    def eval(
        channel: str,
        probes: str,
        vectors: str,
        layers: str = "16",
        coefficients: str = "0.5,1.0,1.5,2.0",
        conditions: str = "low,high",
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.9,
        seed: int = 0,
        max_probes: int = -1,
        out_suffix: str = "",
        model_id: str = DEFAULT_MODEL_ID,
    ):
        """Local entrypoint — sends vector + probes to Modal, persists generations.
        `layers` accepts a comma-separated list, e.g. '16' (single) or '12,16,20' (multi).
        `model_id` defaults to Qwen-Instruct; pass EleutherAI/pythia-12b for the H2 test path."""
        probes_path = Path(probes)
        vectors_path = Path(vectors)
        all_probes = load_probes(probes_path)
        if max_probes > 0:
            all_probes = all_probes[:max_probes]

        coefs = tuple(float(c) for c in coefficients.split(","))
        conds = tuple(conditions.split(","))
        layer_tuple = tuple(int(L) for L in layers.split(","))
        cfg = HarnessConfig(
            channel_id=channel, layers=layer_tuple, coefficients=coefs, conditions=conds,
            max_new_tokens=max_new_tokens, temperature=temperature, top_p=top_p, seed=seed,
            model_id=model_id,
        )
        validate_inputs(cfg, all_probes, vectors_path)
        vector_bytes = vectors_path.read_bytes()

        cfg_dict = asdict(cfg)
        cfg_dict["layers"] = list(layer_tuple)
        cfg_dict["coefficients"] = list(coefs)
        cfg_dict["conditions"] = list(conds)

        print(f"sending {len(all_probes)} probes × {len(conds)} conditions × {len(coefs)} coefs "
              f"= {len(all_probes)*len(conds)*len(coefs)} generations to Modal A100...", file=sys.stderr)
        records = generate_remote.remote(cfg_dict, all_probes, vector_bytes)

        out_root = DEFAULT_OUTPUT_DIR / (channel + out_suffix)
        n_written = write_records(records, out_root)
        print(f"\n✓ wrote {n_written} generation records to {out_root}", file=sys.stderr)


# --- Local CLI (M4 mini eval) ------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="D4 eval harness — local mode (MPS/CPU). For Modal, use `modal run`.")
    ap.add_argument("--channel", required=True)
    ap.add_argument("--probes", required=True, type=Path)
    ap.add_argument("--vectors", required=True, type=Path)
    ap.add_argument(
        "--layers",
        required=True,
        help="Comma-separated layer indices; '16' for single, '12,16,20' for multi.",
    )
    ap.add_argument("--coefficients", default="0.5,1.0,1.5,2.0")
    ap.add_argument("--conditions", default="low,high")
    ap.add_argument("--max-new-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--top-p", type=float, default=0.9)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="mps", choices=["mps", "cuda", "cpu"])
    ap.add_argument("--max-probes", type=int, default=-1)
    ap.add_argument("--out-suffix", default="",
                    help="Optional suffix on the channel output dir, e.g. '_multi' to keep runs apart.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    coefs = tuple(float(c) for c in args.coefficients.split(","))
    conds = tuple(args.conditions.split(","))
    layer_tuple = tuple(int(L) for L in args.layers.split(","))
    cfg = HarnessConfig(
        channel_id=args.channel, layers=layer_tuple, coefficients=coefs, conditions=conds,
        max_new_tokens=args.max_new_tokens, temperature=args.temperature, top_p=args.top_p, seed=args.seed,
    )
    probes = load_probes(args.probes)
    if args.max_probes > 0:
        probes = probes[:args.max_probes]
    validate_inputs(cfg, probes, args.vectors, require_vectors=not args.dry_run)

    if args.dry_run:
        print("DRY RUN — inputs validated. Not loading model.", file=sys.stderr)
        return 0

    cfg_dict = asdict(cfg)
    cfg_dict["layers"] = list(layer_tuple)
    cfg_dict["coefficients"] = list(coefs)
    cfg_dict["conditions"] = list(conds)
    vector_bytes = args.vectors.read_bytes()

    records = _generation_core(cfg_dict, probes, vector_bytes, device=args.device)
    out_root = DEFAULT_OUTPUT_DIR / (args.channel + args.out_suffix)
    n_written = write_records(records, out_root)
    print(f"\n✓ wrote {n_written} generation records to {out_root}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
