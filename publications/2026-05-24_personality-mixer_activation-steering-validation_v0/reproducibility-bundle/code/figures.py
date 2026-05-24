#!/usr/bin/env python3
"""Generate the three manuscript figures from MANUSCRIPT Table S1/S2/S3 data.

Output PNGs to ../data/figures/.

Run:
  python figures.py [--out-dir <dir>]
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
except ImportError as e:
    print(
        f"ERROR: missing dependency ({e}). Install with:",
        "  pip install matplotlib numpy",
        sep="\n",
        file=sys.stderr,
    )
    sys.exit(1)


# Re-use the same Table S1 data the stats script uses so figures and stats stay in sync.
sys.path.insert(0, str(Path(__file__).parent))
from compute_stats import CHANNELS, kappa_and_stats  # noqa: E402


CATEGORY_COLORS = {
    "DARK_TETRAD": "#8B0000",       # dark red
    "HEXACO": "#1f6f8b",            # steel blue
    "ATTACHMENT": "#5e3a8e",        # purple
    "SELF_CONSTRUCT": "#b8860b",    # dark goldenrod
    "AGENCY": "#2e7d32",            # green
    "RISK": "#d2691e",              # chocolate
    "DRIVE": "#4682b4",             # steel blue
    "AFFECT": "#ff7f50",            # coral
    "DISCIPLINE": "#708090",        # slate gray
}


def figure_1_forest_plot(out_path: Path):
    """κ forest plot for all 24 channels with 95% Wilson CI error bars,
    coloured by category, with the κ = 0.60 PASS gate and κ = 0.50 chance line."""
    rows = []
    for ch, cat, kappa_ref, hw, lw, ti, verdict, note in CHANNELS:
        stats = kappa_and_stats(hw, lw, ti)
        rows.append({
            "channel": ch,
            "category": cat,
            "kappa": kappa_ref,
            "ci_lo": stats["wilson_ci_95_low"],
            "ci_hi": stats["wilson_ci_95_high"],
            "verdict": verdict,
            "has_ci": stats["wilson_ci_95_low"] is not None,
        })
    # Sort by kappa descending
    rows.sort(key=lambda r: (-r["kappa"], r["channel"]))

    fig, ax = plt.subplots(figsize=(10, 11))
    y_positions = np.arange(len(rows))

    for i, r in enumerate(rows):
        colour = CATEGORY_COLORS.get(r["category"], "#444")
        if r["has_ci"]:
            ax.errorbar(
                r["kappa"], i,
                xerr=[[r["kappa"] - r["ci_lo"]], [r["ci_hi"] - r["kappa"]]],
                fmt="o", color=colour, ecolor=colour, capsize=3, markersize=7,
                alpha=0.85,
            )
        else:
            # "from prior validation" rows — no CI available; just plot kappa as a hollow circle.
            ax.scatter(
                r["kappa"], i,
                facecolors="none", edgecolors=colour, s=70, linewidths=1.4,
                label=None,
            )

    # Reference lines
    ax.axvline(0.50, color="#888", linestyle=":", linewidth=1.0, label="random chance (κ = 0.50)")
    ax.axvline(0.60, color="#222", linestyle="--", linewidth=1.2, label="PASS gate (κ ≥ 0.60)")

    ax.set_yticks(y_positions)
    ax.set_yticklabels([r["channel"] for r in rows], fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(-0.05, 1.05)
    ax.set_xlabel("Directional accuracy κ (high-win / (high-win + low-win), excl. ties)\nError bars: 95% Wilson score CI; hollow circles: per-channel W/L/T not in Table S1", fontsize=10)
    ax.set_title(
        "Figure 1. Directional-accuracy κ across the 24-channel substrate,\n"
        "with 95% Wilson CIs (post-correction significance: 0 of 18; see §3.1.1)",
        fontsize=11, pad=12,
    )

    # Legend: category colours + reference lines
    cat_handles = [
        patches.Patch(color=col, label=cat)
        for cat, col in CATEGORY_COLORS.items()
        if any(r["category"] == cat for r in rows)
    ]
    line_handles, line_labels = ax.get_legend_handles_labels()
    ax.legend(
        handles=cat_handles + line_handles,
        loc="lower right",
        fontsize=8,
        framealpha=0.9,
    )

    ax.grid(axis="x", linestyle=":", alpha=0.4)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {out_path}")


# Subset of inter-channel cosines from Table S3.
# Format: (row, col, value at L16).
INTER_CHANNEL_PAIRS_L16 = [
    ("machiavellianism", "sadism", 0.377),
    ("attachment_avoidant", "self_defeat", 0.512),
    ("psychopathy", "attachment_avoidant", 0.447),
    ("psychopathy", "self_defeat", 0.370),
    ("honesty_humility", "machiavellianism", -0.315),
    ("honesty_humility", "psychopathy", -0.321),
    ("honesty_humility", "self_defeat", -0.257),
    ("self_defeat", "dospert_financial", -0.407),
]


def figure_2_cosine_heatmap(out_path: Path):
    """Inter-channel cosine heatmap (selected pairs only, from Table S3 at L16).

    Note: this manuscript's Table S3 reports a curated subset, not the full
    15 × 15 (or 24 × 24) matrix. A future revision (per §3.7's reservation)
    would expand this to the full matrix; here we plot the curated subset
    as a symmetric heatmap so the H × Dark-Triad coupling is visible.
    """
    # Build the set of distinct channels in the selected pairs.
    channels = []
    seen = set()
    for r, c, _ in INTER_CHANNEL_PAIRS_L16:
        for ch in (r, c):
            if ch not in seen:
                channels.append(ch)
                seen.add(ch)
    # Order: dark cluster first, then honesty_humility, then negative-coupling pairs.
    order = [
        "machiavellianism", "psychopathy", "sadism",
        "attachment_avoidant", "self_defeat",
        "honesty_humility",
        "dospert_financial",
    ]
    channels = [c for c in order if c in seen]

    n = len(channels)
    mat = np.full((n, n), np.nan)
    # Diagonal = 1.0
    for i in range(n):
        mat[i, i] = 1.0
    # Fill known pairs symmetrically
    idx = {c: i for i, c in enumerate(channels)}
    for r, c, v in INTER_CHANNEL_PAIRS_L16:
        if r in idx and c in idx:
            mat[idx[r], idx[c]] = v
            mat[idx[c], idx[r]] = v

    fig, ax = plt.subplots(figsize=(8, 7))
    cmap = plt.get_cmap("RdBu_r")
    im = ax.imshow(mat, cmap=cmap, vmin=-1.0, vmax=1.0, aspect="equal")

    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(channels, rotation=45, ha="right", fontsize=9)
    ax.set_yticklabels(channels, fontsize=9)

    # Annotate cells with values
    for i in range(n):
        for j in range(n):
            v = mat[i, j]
            if np.isnan(v):
                ax.text(j, i, "·", ha="center", va="center", color="#888", fontsize=10)
            else:
                # Pick text colour for contrast
                txt_color = "white" if abs(v) > 0.5 else "black"
                ax.text(j, i, f"{v:.2f}", ha="center", va="center", color=txt_color, fontsize=8)

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("cos(channel_i, channel_j) at L16", fontsize=9)

    ax.set_title(
        "Figure 2. Selected inter-channel cosine pairs at L16\n"
        "(curated subset from Table S3; '·' = pair not in the reported subset)",
        fontsize=10, pad=12,
    )
    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {out_path}")


# Refusal-cosine values from Table S2 (15 new channels) + 9 from substrate paper.
# Threshold: SAFE < 0.1, watch 0.1-0.3, FLAG >= 0.3
REFUSAL_COSINES = [
    # (channel, worst_layer, abs_cos, status)
    ("narcissism", 12, 0.017, "SAFE"),
    ("attachment_anxious", 12, 0.058, "SAFE"),
    ("sycophancy", 12, 0.045, "SAFE"),
    ("hexaco_emotionality", 20, 0.087, "SAFE"),
    ("honesty_humility", 16, 0.103, "watch"),
    ("locus_of_control", 12, 0.108, "watch"),
    ("sadism", 16, 0.133, "watch"),
    ("hexaco_agreeableness", 12, 0.158, "watch"),
    ("psychopathy", 12, 0.160, "watch"),
    ("openness", 12, 0.171, "watch"),
    ("machiavellianism", 16, 0.218, "watch"),
    ("hexaco_extraversion", 16, 0.226, "watch"),
    ("self_monitoring", 12, 0.240, "watch"),
    ("attachment_avoidant", 12, 0.253, "watch"),
    ("self_defeat", 12, 0.295, "watch"),
    # Original 9 (per Table S2 narrative):
    ("cheerfulness", None, 0.133, "watch"),
    ("sociability", None, 0.150, "watch"),
    ("achievement_striving", None, 0.111, "watch"),
    ("stimulation", None, 0.046, "SAFE"),
    ("dospert_financial", None, 0.310, "FLAG"),
    ("cautiousness", None, 0.164, "watch"),
]


def figure_3_refusal_cosine_scatter(out_path: Path):
    """Per-channel worst-layer |cos(channel, refusal)| with FLAG threshold."""
    sorted_data = sorted(REFUSAL_COSINES, key=lambda r: r[2])
    channels = [r[0] for r in sorted_data]
    values = [r[2] for r in sorted_data]
    statuses = [r[3] for r in sorted_data]

    status_colors = {"SAFE": "#2e7d32", "watch": "#d2691e", "FLAG": "#b71c1c"}
    colours = [status_colors[s] for s in statuses]

    fig, ax = plt.subplots(figsize=(10, 8))
    y_positions = np.arange(len(channels))
    ax.barh(y_positions, values, color=colours, edgecolor="#333", linewidth=0.6, alpha=0.85)

    # Threshold lines
    ax.axvline(0.1, color="#666", linestyle=":", linewidth=1.0)
    ax.axvline(0.3, color="#b71c1c", linestyle="--", linewidth=1.4)
    ax.text(0.105, len(channels) - 0.5, "SAFE/watch", color="#666", fontsize=8, va="top")
    ax.text(0.305, len(channels) - 0.5, "watch/FLAG", color="#b71c1c", fontsize=8, va="top")

    ax.set_yticks(y_positions)
    ax.set_yticklabels(channels, fontsize=9)
    ax.set_xlim(0, max(0.35, max(values) * 1.1))
    ax.set_xlabel("Worst-layer |cos(channel, refusal)| across L8/12/16/20/24", fontsize=10)
    ax.invert_yaxis()
    ax.set_title(
        "Figure 3. Refusal-direction cosine across the 24-channel substrate\n"
        "(AlphaSteer protocol; SAFE < 0.1; watch 0.1–0.3; FLAG ≥ 0.3)",
        fontsize=11, pad=12,
    )

    # Legend
    handles = [patches.Patch(color=status_colors[s], label=s) for s in ["SAFE", "watch", "FLAG"]]
    ax.legend(handles=handles, loc="lower right", fontsize=9, framealpha=0.9)
    ax.grid(axis="x", linestyle=":", alpha=0.4)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {out_path}")


def main(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    figure_1_forest_plot(out_dir / "fig1_kappa_forest.png")
    figure_2_cosine_heatmap(out_dir / "fig2_cosine_heatmap_L16.png")
    figure_3_refusal_cosine_scatter(out_dir / "fig3_refusal_cosine.png")
    print(f"\nAll 3 figures written to {out_dir}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "figures",
        help="Output directory for figure PNGs",
    )
    args = ap.parse_args()
    sys.exit(main(args.out_dir))
