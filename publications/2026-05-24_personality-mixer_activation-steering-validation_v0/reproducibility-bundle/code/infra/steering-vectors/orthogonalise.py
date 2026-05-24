"""
orthogonalise.py — Gram-Schmidt orthogonalise a set of channel vectors per layer.

Per W10 finding: the 9-channel CAA basis at L16 has 4 inter-channel pairs at
FLAG (|cos| ≥ 0.30); the multi-channel composite is non-additive in residual
space because composite vectors are pulled in a "diagonal" of overlapping axes.

This script orthogonalises the channel basis at each layer using QR decomposition
(numerically equivalent to Gram-Schmidt but more stable). Channel ORDER controls
which channel keeps its original direction and which get projected onto the
orthogonal complement of the prior channels. Order is by single-channel
directional accuracy (W1-W4 PASS scores), so the highest-quality vectors keep
their direction and lower-quality vectors absorb the orthogonalisation cost.

Each orthogonalised vector is RESCALED to the L2 norm of its original. This
preserves the trait-to-coef calibration (compile_construct.py's coef logic
assumes vectors of comparable magnitude) without breaking orthogonality
(scaling preserves orthogonality of zero-mean directions).

USAGE:
  python3 infra/steering-vectors/orthogonalise.py \\
      --channels-order achievement_striving,cheerfulness,dospert_financial,sociability,stimulation,dospert_recreational,cautiousness,conscientiousness_self_discipline_v3,self_direction \\
      --src-dir infra/steering-vectors/qwen2.5-7b-instruct \\
      --dst-dir infra/steering-vectors/qwen2.5-7b-instruct-orth \\
      --layers 8,12,16,20,24

Verification: post-orthogonalisation max |cos| should be ≤ 1e-5 (machine epsilon).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def cosine(a, b) -> float:
    return float((a @ b) / (a.norm() * b.norm() + 1e-9))


def orthogonalise_layer(vectors_in_order, eps=1e-8):
    """Modified Gram-Schmidt on a list of (name, tensor) pairs.

    Returns list of (name, orthogonalised_tensor) preserving input order.
    Each output has unit dot product with prior outputs ≤ eps.
    """
    import torch
    out = []
    Q = []  # list of unit vectors (orthonormal basis built so far)
    for name, v in vectors_in_order:
        v = v.to(torch.float32).clone()
        original_norm = float(v.norm().item())
        # subtract projections onto each existing q
        for q in Q:
            v = v - (v @ q) * q
        new_norm = float(v.norm().item())
        if new_norm < eps:
            print(
                f"WARNING: channel {name!r} collapsed to ~0 after orthogonalisation "
                f"(remaining norm {new_norm:.2e}); was likely already in span of prior channels.",
                file=sys.stderr,
            )
            # still append a tiny vector so the channel doesn't vanish from pipeline
            unit = v / (new_norm + 1e-12)
            rescaled = unit * original_norm
        else:
            unit = v / new_norm
            Q.append(unit)
            rescaled = unit * original_norm  # preserve original magnitude
        out.append((name, rescaled, original_norm, new_norm))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channels-order", required=True,
                    help="Comma-separated channel names IN ORDER. Earlier channels "
                         "keep their direction; later channels get projected onto "
                         "the orthogonal complement.")
    ap.add_argument("--src-dir", type=Path,
                    default=REPO_ROOT / "infra/steering-vectors/qwen2.5-7b-instruct")
    ap.add_argument("--dst-dir", type=Path,
                    default=REPO_ROOT / "infra/steering-vectors/qwen2.5-7b-instruct-orth")
    ap.add_argument("--layers", default="8,12,16,20,24",
                    help="Comma-separated layer indices to orthogonalise")
    ap.add_argument("--report", type=Path,
                    default=REPO_ROOT / "infra/steering-vectors/orthogonalisation-report-2026-05-08.md")
    args = ap.parse_args()

    try:
        import torch
    except ImportError:
        print("ERROR: torch required", file=sys.stderr)
        return 2

    channels = [c.strip() for c in args.channels_order.split(",") if c.strip()]
    layers = [int(L) for L in args.layers.split(",") if L.strip()]
    if len(channels) < 2:
        print("ERROR: need at least 2 channels", file=sys.stderr)
        return 2

    # Load all source vectors
    src_data = {}  # {channel: dict[layer]=Tensor}
    for ch in channels:
        path = args.src_dir / ch / "vector.pt"
        if not path.exists():
            print(f"ERROR: source vector not found: {path}", file=sys.stderr)
            return 2
        v = torch.load(path, map_location="cpu", weights_only=False)
        if not isinstance(v, dict):
            print(f"ERROR: {path} is not a dict[layer]=Tensor", file=sys.stderr)
            return 2
        src_data[ch] = v

    args.dst_dir.mkdir(parents=True, exist_ok=True)

    report_rows = []  # (layer, channel, orig_norm, post_orth_norm, max_cos_to_prior)
    out_data = {ch: {} for ch in channels}

    for L in layers:
        # Verify all channels have this layer
        ordered = []
        for ch in channels:
            if L not in src_data[ch]:
                print(f"WARNING: channel {ch} missing layer {L}; skipping channel", file=sys.stderr)
                continue
            ordered.append((ch, src_data[ch][L]))
        if len(ordered) < 2:
            print(f"WARNING: layer {L} has <2 channels available; skipping layer", file=sys.stderr)
            continue

        results = orthogonalise_layer(ordered)

        # Verification: compute pairwise cosines on the orthogonalised vectors
        orth_vecs = [(name, vec) for name, vec, _, _ in results]
        max_cos = 0.0
        for i in range(len(orth_vecs)):
            for j in range(i + 1, len(orth_vecs)):
                c = abs(cosine(orth_vecs[i][1], orth_vecs[j][1]))
                if c > max_cos:
                    max_cos = c
        print(f"L{L}: orthogonalisation max |cos| post-orth = {max_cos:.3e}", file=sys.stderr)

        for name, vec, orig_norm, post_norm in results:
            out_data[name][L] = vec
            report_rows.append((L, name, orig_norm, post_norm, max_cos))

    # Save orthogonalised vectors per channel
    for ch in channels:
        out_path = args.dst_dir / ch / "vector.pt"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(out_data[ch], out_path)
        print(f"  wrote {out_path}", file=sys.stderr)

    # Write report
    lines = [
        "# Channel orthogonalisation report",
        "",
        "_Generated by infra/steering-vectors/orthogonalise.py_",
        "",
        "## Method",
        "",
        f"- Source vectors: `{args.src_dir.relative_to(REPO_ROOT) if args.src_dir.is_relative_to(REPO_ROOT) else args.src_dir}`",
        f"- Destination: `{args.dst_dir.relative_to(REPO_ROOT) if args.dst_dir.is_relative_to(REPO_ROOT) else args.dst_dir}`",
        f"- Layers: {layers}",
        f"- Channels (in orthogonalisation order): {channels}",
        "",
        "Modified Gram-Schmidt: for each channel in order, subtract its projection onto",
        "every prior orthogonalised channel. Post-orthogonalisation, rescale each vector",
        "to its original L2 norm (preserves trait-to-coef calibration; scaling preserves",
        "orthogonality).",
        "",
        "Order rationale: highest single-channel directional accuracy first (W1-W4 PASS",
        "ranking) so the strongest-evidence vectors keep their direction; lower-quality",
        "vectors absorb the orthogonalisation cost.",
        "",
        "## Per-channel norm preservation + residual after projection",
        "",
        "`norm_before` = original L2 norm. `norm_post_GS` = L2 norm AFTER Gram-Schmidt",
        "subtraction but BEFORE rescaling. `norm_after` is rescaled = `norm_before` by",
        "construction (preserved). The ratio `norm_post_GS / norm_before` shows how much",
        "of the channel was already in the span of prior channels: ratio ≈ 1.0 means",
        "the channel was already orthogonal; ratio ≈ 0.0 means the channel was redundant.",
        "",
        "| Layer | Channel | Norm before | Norm post-GS | Ratio | Max \\|cos\\| post-orth |",
        "|---|---|---|---|---|---|",
    ]
    for L, name, orig, post, max_cos in report_rows:
        ratio = (post / orig) if orig > 0 else 0.0
        lines.append(
            f"| {L} | {name} | {orig:.3f} | {post:.3f} | {ratio:.3f} | {max_cos:.2e} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "Post-orthogonalisation max |cosine| should be at machine epsilon (~1e-7 for",
        "fp32 on a 3584-dim vector). Larger values indicate numerical loss; verify the",
        "Gram-Schmidt loop is using float32 throughout.",
        "",
        "A channel with low `norm_post_GS / norm_before` ratio (e.g. < 0.5) was largely",
        "redundant with prior channels — its orthogonalised version is mostly noise after",
        "projection-out. Such channels have lost most of their original semantics and",
        "their effective trait-direction may now be different from what was extracted.",
        "Treat their results in B4 cautiously: if an orthogonalised channel produces a",
        "different behavioural effect than the original, that's expected.",
        "",
        "## Provenance",
        "",
        f"- Source: `{args.src_dir}`",
        f"- Destination: `{args.dst_dir}`",
        f"- Order: {', '.join(channels)}",
        f"- Layers: {layers}",
    ]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines))
    print(f"\n✓ wrote {args.report}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
