"""
extract_caa.py — CAA (Contrastive Activation Addition) steering vector extraction.

Implements the CAA recipe from Rimsky et al. 2024 ("Steering Llama 2 via Contrastive
Activation Addition," ACL 2024, arXiv:2312.06681):

  1. Build a dataset of multiple-choice items where two completions differ only on
     the trait of interest.
  2. Forward pass for each completion. Cache residual-stream activations at every
     extraction layer at the answer-token (last-token) position.
  3. Steering vector at layer L:  v_L = mean(activations_high_L) - mean(activations_low_L)
  4. Optionally normalise to unit length so the injection coefficient is the dial.

Runs on Modal A100-40GB. Default model: Qwen-2.5-7B-Instruct in fp16. Per the
substrate plan (`docs/substrate-decision.md`), the script supports any
HuggingFace model with a standard decoder-layer architecture (model.model.layers
indexable). Tested substrates: Qwen2.5-7B-Instruct (28 layers), Qwen2.5-7B-Base
(28), Llama-3.1-8B-Instruct (32), Pythia-12B (36). The layer-range check is
done at remote-runtime against the loaded model's actual layer count; local
validation only sanity-checks for positive integers.

Per-channel extraction cost ~$1-3 of Modal time on Qwen-7B; ~$2-4 on Pythia-12B
or Llama-8B.

Output:
  infra/steering-vectors/<model_short>/<channel_id>/vector.pt          — extracted vectors
  infra/steering-vectors/<model_short>/<channel_id>/extraction-meta.json — provenance
  infra/steering-vectors/<model_short>/<channel_id>/refusal-cosine.txt   — AlphaSteer audit (later)

INVOCATION:

Local dry-run (validate inputs, no Modal call):
  python3 infra/steering-vectors/extract_caa.py \\
      --channel conscientiousness_self_discipline \\
      --contrastive-items infra/steering-vectors/contrastive-items/c5-self-discipline.jsonl \\
      --layer-sweep 8,12,16,20,24 \\
      --dry-run

Real run on Modal — Qwen2.5-7B-Instruct (default):
  .venv/bin/modal run infra/steering-vectors/extract_caa.py::extract \\
      --channel conscientiousness_self_discipline \\
      --contrastive-items infra/steering-vectors/contrastive-items/c5-self-discipline.jsonl \\
      --layer-sweep 8,12,16,20,24

Real run on Modal — Pythia-12B (emergence research substrate):
  .venv/bin/modal run infra/steering-vectors/extract_caa.py::extract \\
      --channel conscientiousness_self_discipline \\
      --contrastive-items infra/steering-vectors/contrastive-items/c5-self-discipline.jsonl \\
      --layer-sweep 8,16,24,32 \\
      --model-id EleutherAI/pythia-12b \\
      --model-short pythia-12b

Real run on Modal — Llama-3.1-8B-Instruct (cross-confirmation):
  .venv/bin/modal run infra/steering-vectors/extract_caa.py::extract \\
      --channel conscientiousness_self_discipline \\
      --contrastive-items infra/steering-vectors/contrastive-items/c5-self-discipline.jsonl \\
      --layer-sweep 8,16,24 \\
      --model-id meta-llama/Llama-3.1-8B-Instruct \\
      --model-short llama-3.1-8b-instruct

Smoke test (3 items only, single layer — proves the pipe works for ~$0.50):
  .venv/bin/modal run infra/steering-vectors/extract_caa.py::extract \\
      --channel conscientiousness_self_discipline \\
      --contrastive-items infra/steering-vectors/contrastive-items/c5-self-discipline.jsonl \\
      --layer-sweep 16 \\
      --max-items 3
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

# Modal is required when this module is imported by `modal run`. For local
# --dry-run the import is non-fatal — extract_caa runs without modal installed.
try:
    import modal
    _MODAL_AVAILABLE = True
except ImportError:
    _MODAL_AVAILABLE = False


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
DEFAULT_MODEL_SHORT = "qwen2.5-7b-instruct"
VECTORS_DIR = REPO_ROOT / "infra" / "steering-vectors"


# --- Schema ------------------------------------------------------------------

@dataclass
class ContrastiveItem:
    """One contrastive pair: same context, two completions differing only on the channel."""
    item_id: str
    context: str
    completion_high: str
    completion_low: str
    answer_token_high: str | None = None  # unused at v0; reserved
    answer_token_low: str | None = None
    notes: str | None = None


@dataclass
class ExtractionConfig:
    channel_id: str
    model_id: str = DEFAULT_MODEL_ID
    model_short: str = DEFAULT_MODEL_SHORT
    layer_sweep: tuple[int, ...] = (8, 12, 16, 20, 24)
    normalise: bool = True
    dtype: str = "float16"
    refusal_audit: bool = False  # disabled at v0 — refusal extraction is a separate run
    seed: int = 0
    max_items: int | None = None  # None = use all


# --- Local validation (no Modal needed) -------------------------------------

def load_contrastive_items(path: Path) -> list[ContrastiveItem]:
    """Load JSONL contrastive items. One line per item."""
    items: list[ContrastiveItem] = []
    with path.open() as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{line_num} not valid JSON — {e}") from e
            try:
                items.append(ContrastiveItem(**obj))
            except TypeError as e:
                raise ValueError(f"{path}:{line_num} missing required field — {e}") from e
    if not items:
        raise ValueError(f"{path} contains 0 contrastive items")
    return items


def validate_inputs(cfg: ExtractionConfig, items: list[ContrastiveItem]) -> None:
    """Local sanity checks before paying for GPU time."""
    if cfg.max_items is None and len(items) < 20:
        print(
            f"WARNING: only {len(items)} contrastive items. Recipe expects ~50-200 "
            "per channel. Vector quality scales with N.",
            file=sys.stderr,
        )
    if not cfg.layer_sweep:
        raise ValueError("layer_sweep is empty")
    # Local validation: positive integers + plausible upper bound (Pythia-12B has
    # 36 layers; anything beyond 80 is probably a typo). Real per-model check
    # happens inside extract_remote against the loaded model's actual layer count.
    if any(L < 0 or L > 80 for L in cfg.layer_sweep):
        raise ValueError(
            f"layer_sweep contains values outside [0, 80] (sanity check): {cfg.layer_sweep}. "
            f"If you intended these for a model with >80 layers, raise the bound here."
        )
    seen_ids = set()
    for it in items:
        if it.item_id in seen_ids:
            raise ValueError(f"duplicate item_id: {it.item_id}")
        seen_ids.add(it.item_id)
    n_used = cfg.max_items if cfg.max_items is not None else len(items)
    print(
        f"OK: channel={cfg.channel_id}, items={len(items)} "
        f"(using {n_used}), layers={cfg.layer_sweep}, model={cfg.model_id}",
        file=sys.stderr,
    )


# --- Modal app (module-level so `modal run` finds it) ------------------------

if _MODAL_AVAILABLE:
    app = modal.App("mg-digital-twin-caa-extraction")

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

    # Persist HF model cache across runs to avoid re-downloading Qwen 7B each time.
    hf_cache = modal.Volume.from_name("hf-cache", create_if_missing=True)

    @app.function(
        image=image,
        gpu="A100-40GB",
        timeout=3600,
        secrets=[modal.Secret.from_name("huggingface-token", required_keys=["HF_TOKEN"])],
        volumes={"/root/.cache/huggingface": hf_cache},
    )
    def extract_remote(cfg_dict: dict, items_dicts: list[dict]) -> dict:
        """Runs on Modal A100. Imports torch + transformers inside the function
        so they don't need to be importable on the local machine."""
        import os
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        cfg = ExtractionConfig(**{k: v for k, v in cfg_dict.items() if k != "layer_sweep"})
        cfg.layer_sweep = tuple(cfg_dict["layer_sweep"])
        items = [ContrastiveItem(**d) for d in items_dicts]
        if cfg.max_items is not None:
            items = items[:cfg.max_items]

        torch.manual_seed(cfg.seed)
        print(f"loading tokenizer for {cfg.model_id}...", flush=True)
        tok = AutoTokenizer.from_pretrained(
            cfg.model_id, token=os.environ.get("HF_TOKEN")
        )
        print(f"loading model {cfg.model_id} ({cfg.dtype})...", flush=True)
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_id,
            torch_dtype=getattr(torch, cfg.dtype),
            device_map="cuda",
            token=os.environ.get("HF_TOKEN"),
        )
        model.eval()

        # Architecture-aware decoder-layer accessor (Qwen/Llama use model.model.layers;
        # Pythia/GPT-NeoX use model.gpt_neox.layers; GPT-2 style use model.transformer.h).
        if hasattr(model, "model") and hasattr(model.model, "layers"):
            decoder_layers = model.model.layers
            arch_path = "model.model.layers"
        elif hasattr(model, "gpt_neox") and hasattr(model.gpt_neox, "layers"):
            decoder_layers = model.gpt_neox.layers
            arch_path = "model.gpt_neox.layers"
        elif hasattr(model, "transformer") and hasattr(model.transformer, "h"):
            decoder_layers = model.transformer.h
            arch_path = "model.transformer.h"
        else:
            raise ValueError(
                f"Cannot locate decoder layers in {type(model).__name__}. "
                f"Tried: model.model.layers (Qwen/Llama), model.gpt_neox.layers (Pythia), "
                f"model.transformer.h (GPT-2). Add support for this architecture in extract_caa.py."
            )

        n_layers = len(decoder_layers)
        print(f"model loaded — {n_layers} decoder layers via {arch_path}", flush=True)

        for L in cfg.layer_sweep:
            if L >= n_layers:
                raise ValueError(f"layer {L} out of range (model has {n_layers} layers)")

        per_layer_high: dict[int, list] = {L: [] for L in cfg.layer_sweep}
        per_layer_low: dict[int, list] = {L: [] for L in cfg.layer_sweep}

        captured: dict[int, "torch.Tensor"] = {}

        def make_hook(layer_idx: int):
            def hook(_module, _input, output):
                hs = output[0] if isinstance(output, tuple) else output
                captured[layer_idx] = hs[:, -1, :].detach().to(torch.float32).cpu()
            return hook

        handles = []
        for L in cfg.layer_sweep:
            h = decoder_layers[L].register_forward_hook(make_hook(L))
            handles.append(h)

        try:
            for i, item in enumerate(items):
                if i % 10 == 0:
                    print(f"  processing item {i+1}/{len(items)} ({item.item_id})", flush=True)
                for label, completion in (("high", item.completion_high), ("low", item.completion_low)):
                    full_text = item.context + " " + completion
                    enc = tok(full_text, return_tensors="pt").to("cuda")
                    captured.clear()
                    with torch.no_grad():
                        _ = model(**enc)
                    for L in cfg.layer_sweep:
                        if L not in captured:
                            raise RuntimeError(f"hook did not fire for layer {L} on item {item.item_id}")
                        bucket = per_layer_high[L] if label == "high" else per_layer_low[L]
                        bucket.append(captured[L].squeeze(0))
        finally:
            for h in handles:
                h.remove()

        import io
        vectors_pt: dict[int, "torch.Tensor"] = {}
        norms: dict[int, float] = {}
        for L in cfg.layer_sweep:
            high_mean = torch.stack(per_layer_high[L]).mean(dim=0)
            low_mean = torch.stack(per_layer_low[L]).mean(dim=0)
            v = high_mean - low_mean
            norm = float(v.norm().item())
            if cfg.normalise and norm > 0:
                v = v / norm
            vectors_pt[L] = v
            norms[L] = norm

        # Serialise tensors via torch.save into bytes — local entrypoint writes
        # them to disk without needing torch installed locally.
        buf = io.BytesIO()
        torch.save(vectors_pt, buf)
        vector_pt_bytes = buf.getvalue()

        return {
            "vector_pt_bytes": vector_pt_bytes,
            "norms": {str(L): norms[L] for L in cfg.layer_sweep},
            "n_items_used": len(items),
            "n_items_provided": len(items_dicts),
            "seed": cfg.seed,
            "dtype": cfg.dtype,
            "model_id": cfg.model_id,
            "n_model_layers": n_layers,
            "hidden_size": int(model.config.hidden_size),
        }

    @app.local_entrypoint()
    def extract(
        channel: str,
        contrastive_items: str,
        layer_sweep: str = "8,12,16,20,24",
        normalise: bool = True,
        seed: int = 0,
        max_items: int = -1,
        model_id: str = DEFAULT_MODEL_ID,
        model_short: str = DEFAULT_MODEL_SHORT,
    ):
        """Local entrypoint invoked via `modal run extract_caa.py::extract --channel ...`.
        Validates locally, calls extract_remote, persists artefacts.

        Pass --model-id / --model-short to extract on a non-default substrate.
        See module docstring for working examples (Qwen, Pythia, Llama).
        """

        items = load_contrastive_items(Path(contrastive_items))
        layers = tuple(int(L) for L in layer_sweep.split(","))
        cfg = ExtractionConfig(
            channel_id=channel,
            model_id=model_id,
            model_short=model_short,
            layer_sweep=layers,
            normalise=normalise,
            seed=seed,
            max_items=None if max_items < 0 else max_items,
        )
        validate_inputs(cfg, items)

        cfg_dict = asdict(cfg)
        cfg_dict["layer_sweep"] = list(layers)  # tuple → list for cloudpickle safety

        print(f"calling extract_remote on Modal A100-40GB...", file=sys.stderr)
        result = extract_remote.remote(cfg_dict, [asdict(it) for it in items])

        out_dir = VECTORS_DIR / cfg.model_short / channel
        out_dir.mkdir(parents=True, exist_ok=True)

        # vector.pt is a torch.save'd dict[int, Tensor]. Bytes come back from
        # the remote function so we don't need torch installed locally.
        (out_dir / "vector.pt").write_bytes(result["vector_pt_bytes"])

        meta = {
            "channel_id": channel,
            "model_id": cfg.model_id,
            "model_short": cfg.model_short,
            "layer_sweep": list(layers),
            "norms_pre_normalisation": result["norms"],
            "n_contrastive_items": result["n_items_used"],
            "n_contrastive_items_total": result["n_items_provided"],
            "normalised": cfg.normalise,
            "dtype": cfg.dtype,
            "seed": cfg.seed,
            "n_model_layers": result["n_model_layers"],
            "hidden_size": result["hidden_size"],
            "extraction_method": "CAA (Rimsky et al. 2024)",
            "extraction_runtime": "Modal A100-40GB",
        }
        (out_dir / "extraction-meta.json").write_text(json.dumps(meta, indent=2))

        print(f"\n✓ wrote vectors + metadata to {out_dir}", file=sys.stderr)
        print(f"  norms (pre-normalisation): {result['norms']}", file=sys.stderr)
        print(f"  hidden size: {result['hidden_size']}, layers swept: {list(layers)}", file=sys.stderr)


# --- Local CLI (dry-run only) ------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="CAA extraction — local dry-run validator. For real runs use `modal run`.")
    ap.add_argument("--channel", required=True)
    ap.add_argument("--contrastive-items", required=True, type=Path)
    ap.add_argument("--layer-sweep", default="8,12,16,20,24")
    ap.add_argument("--no-normalise", action="store_true")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max-items", type=int, default=-1)
    ap.add_argument("--model-id", default=DEFAULT_MODEL_ID,
                    help=f"HuggingFace model ID (default: {DEFAULT_MODEL_ID})")
    ap.add_argument("--model-short", default=DEFAULT_MODEL_SHORT,
                    help=f"Short name used as output dir name (default: {DEFAULT_MODEL_SHORT})")
    ap.add_argument("--dry-run", action="store_true",
                    help="Validate inputs without invoking Modal (default for this CLI)")
    args = ap.parse_args()

    items = load_contrastive_items(args.contrastive_items)
    cfg = ExtractionConfig(
        channel_id=args.channel,
        model_id=args.model_id,
        model_short=args.model_short,
        layer_sweep=tuple(int(L) for L in args.layer_sweep.split(",")),
        normalise=not args.no_normalise,
        seed=args.seed,
        max_items=None if args.max_items < 0 else args.max_items,
    )
    validate_inputs(cfg, items)

    print("DRY RUN — inputs validated. For real run:", file=sys.stderr)
    real_cmd = (
        f"  .venv/bin/modal run {Path(__file__).relative_to(REPO_ROOT)}::extract "
        f"--channel {cfg.channel_id} "
        f"--contrastive-items {args.contrastive_items} "
        f"--layer-sweep {args.layer_sweep}"
    )
    if cfg.model_id != DEFAULT_MODEL_ID:
        real_cmd += f" --model-id {cfg.model_id} --model-short {cfg.model_short}"
    print(real_cmd, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
