#!/usr/bin/env python3
"""Compute statistical-significance values for the 24-channel scorecard
in the personality-mixer publication.

Inputs are the high-win / low-win / tie counts from MANUSCRIPT.md Table S1.
For each channel:
  - Directional accuracy kappa = high_wins / (high_wins + low_wins)  (excluding ties)
  - 95% confidence interval on the high-win proportion (Wilson score interval)
  - Two-sided binomial test against chance (p = 0.5) on non-tie pairs
  - Holm-Bonferroni and Benjamini-Hochberg (BH-FDR) corrections across the
    24-channel family.

Output:
  - `stats.json` with per-channel rows + family-level summary
  - `stats.md` with the human-readable table

Run:
  python compute_stats.py [--out-dir <dir>]

The defaults write to `../data/derived/` of the publication's
reproducibility-bundle.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Iterable

try:
    from scipy.stats import binomtest
    from statsmodels.stats.multitest import multipletests
except ImportError as e:
    print(
        f"ERROR: missing dependency ({e}). Install with:",
        "  pip install scipy statsmodels",
        sep="\n",
        file=sys.stderr,
    )
    sys.exit(1)


# Source-of-truth: MANUSCRIPT.md Table S1, transcribed verbatim from
# SUPPLEMENTARY_TABLES.md. Each row: (channel, category, kappa, high_wins,
# low_wins, ties, verdict). For original-9 channels (cheerfulness, sociability,
# achievement_striving, stimulation, dospert_financial) the W/L/T per the
# overall-coefficient summary is recomputed by the manuscript pipeline; the
# Supplementary Table S1 reports the multi-layer-equivalent W/L/T for the
# rescued + new channels and the "from prior validation" κ for the others.
# Where Table S1 left W/L/T blank ("—"), we cannot compute binomial p; those
# rows are marked NA and excluded from the Holm/BH correction family.

CHANNELS = [
    # channel, category, kappa, high_wins, low_wins, ties, verdict, note
    ("narcissism",              "DARK_TETRAD",   1.000, 7,  0,  9,  "PASS",          "perfect"),
    ("psychopathy",             "DARK_TETRAD",   1.000, 3,  0, 13,  "PASS@c4",       "RLHF-floored at c=2; numbers are c=4 diagnostic"),
    ("attachment_avoidant",     "ATTACHMENT",    1.000, 3,  0,  9,  "PASS",          "perfect"),
    ("hexaco_emotionality",     "HEXACO",        1.000, 3,  0,  9,  "PASS",          "perfect"),
    ("honesty_humility",        "HEXACO",        1.000, 4,  0,  8,  "PASS",          "perfect"),
    ("machiavellianism",        "DARK_TETRAD",   0.857, 6,  1,  9,  "PASS",          None),
    ("hexaco_extraversion",     "HEXACO",        0.800, 4,  1,  7,  "PASS",          None),
    ("self_monitoring",         "SELF_CONSTRUCT",0.800, 4,  1,  7,  "PASS",          None),
    ("openness",                "HEXACO",        0.750, 3,  1,  8,  "PASS",          "challenges 'may not be steerable' caveat"),
    ("hexaco_agreeableness",    "HEXACO",        0.750, 6,  2,  4,  "PASS",          None),
    ("achievement_striving",    "DRIVE",         0.740, None, None, None, "PASS",    "from prior validation, single-layer L16 c=0.5; W/L/T not in TableS1"),
    ("dospert_recreational",    "RISK",          0.722, 13, 5, 12,  "PASS",          "rescued from KILL by ML"),
    ("cheerfulness",            "AFFECT",        0.700, None, None, None, "PASS",    "prior; vector now points to _ct variant"),
    ("locus_of_control",        "AGENCY",        0.667, 6,  3,  3,  "PASS",          None),
    ("attachment_anxious",      "ATTACHMENT",    0.667, 2,  1,  9,  "PASS",          None),
    ("self_direction",          "AGENCY",        0.667, 2,  1, 27,  "PASS",          "rescued; very high tie count"),
    ("dospert_financial",       "RISK",          0.660, None, None, None, "PASS",    "prior; refusal-cosine FLAG (clamp)"),
    ("sociability",             "HEXACO",        0.640, None, None, None, "PASS",    "prior"),
    ("conscientiousness_self_discipline", "DISCIPLINE", 0.636, 14, 8, 8, "PASS",     "rescued (v3 vector)"),
    ("stimulation",             "DRIVE",         0.630, None, None, None, "PASS",    "prior"),
    ("cautiousness",            "DISCIPLINE",    0.583, 7,  5, 18,  "borderline",    "just under gate"),
    ("self_defeat",             "SELF_CONSTRUCT",0.500, 1,  1, 10,  "borderline",    "high tie count"),
    ("sycophancy",              "SELF_CONSTRUCT",0.250, 1,  3,  8,  "sign-inverted", "steerable, negate coef"),
    ("sadism",                  "DARK_TETRAD",   0.000, 0,  0, 16,  "RLHF-floored",  "indistinguishable at c=2 AND c=4"),
]


def wilson_ci(successes: int, trials: int, alpha: float = 0.05) -> tuple[float, float]:
    """Two-sided Wilson score interval for a binomial proportion.
    Returns (lower, upper). When trials == 0, returns (NaN, NaN)."""
    if trials == 0:
        return (float("nan"), float("nan"))
    z = 1.959963984540054  # z-score for two-sided 95%
    p = successes / trials
    denom = 1.0 + z * z / trials
    centre = (p + z * z / (2 * trials)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials))
    return (max(0.0, centre - half), min(1.0, centre + half))


def kappa_and_stats(high_wins, low_wins, ties):
    """Compute kappa + binomial test + Wilson CI for one channel.
    Returns dict with kappa, n_nontie, n_total, ci_lo, ci_hi, p_value, observed_kappa.
    If high_wins/low_wins/ties is None, returns dict with NaN-equivalents."""
    if high_wins is None or low_wins is None:
        return {
            "kappa": None,
            "n_nontie": None,
            "n_total": None,
            "wilson_ci_95_low": None,
            "wilson_ci_95_high": None,
            "binomial_p_two_sided": None,
            "_note": "TableS1 left W/L/T blank — original-9 channel; per-coef breakdown is in the prior substrate-paper validation, not re-aggregated here",
        }
    n_nontie = high_wins + low_wins
    n_total = n_nontie + ties
    kappa = high_wins / n_nontie if n_nontie > 0 else float("nan")
    ci_lo, ci_hi = wilson_ci(high_wins, n_nontie)
    if n_nontie > 0:
        p_two = binomtest(k=high_wins, n=n_nontie, p=0.5, alternative="two-sided").pvalue
    else:
        p_two = float("nan")
    return {
        "kappa": round(kappa, 4) if not math.isnan(kappa) else None,
        "n_nontie": n_nontie,
        "n_total": n_total,
        "wilson_ci_95_low": round(ci_lo, 4) if not math.isnan(ci_lo) else None,
        "wilson_ci_95_high": round(ci_hi, 4) if not math.isnan(ci_hi) else None,
        "binomial_p_two_sided": round(p_two, 6) if not math.isnan(p_two) else None,
    }


def main(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    p_values = []
    p_indices = []
    for i, (ch, cat, kappa_ref, hw, lw, ti, verdict, note) in enumerate(CHANNELS):
        stats = kappa_and_stats(hw, lw, ti)
        # Sanity-check: published kappa vs recomputed kappa.
        if stats["kappa"] is not None and abs(stats["kappa"] - kappa_ref) > 0.005:
            print(
                f"WARNING: channel '{ch}' recomputed kappa {stats['kappa']} differs from manuscript-reported {kappa_ref} by > 0.005",
                file=sys.stderr,
            )
        row = {
            "channel": ch,
            "category": cat,
            "kappa_reported_in_manuscript": kappa_ref,
            "high_wins": hw,
            "low_wins": lw,
            "ties": ti,
            "verdict": verdict,
            "note": note,
            **stats,
        }
        rows.append(row)
        if stats["binomial_p_two_sided"] is not None:
            p_values.append(stats["binomial_p_two_sided"])
            p_indices.append(i)

    # Multiple-comparisons correction across the channels with non-blank counts.
    if p_values:
        holm = multipletests(p_values, alpha=0.05, method="holm")
        bh = multipletests(p_values, alpha=0.05, method="fdr_bh")
        for i, p_idx in enumerate(p_indices):
            rows[p_idx]["holm_bonferroni_p_adj"] = round(float(holm[1][i]), 6)
            rows[p_idx]["holm_bonferroni_reject"] = bool(holm[0][i])
            rows[p_idx]["bh_fdr_p_adj"] = round(float(bh[1][i]), 6)
            rows[p_idx]["bh_fdr_reject"] = bool(bh[0][i])

    # Emit JSON
    out_json = out_dir / "stats.json"
    family_size = len(p_values)
    sig_holm = sum(1 for r in rows if r.get("holm_bonferroni_reject") is True)
    sig_bh = sum(1 for r in rows if r.get("bh_fdr_reject") is True)
    payload = {
        "_schema": "personality-mixer stats v0",
        "_method": (
            "Per-channel two-sided binomial test against chance (p=0.5) on non-tie pairs; "
            "95% Wilson score interval on the high-win proportion; "
            "Holm-Bonferroni and Benjamini-Hochberg (BH-FDR) correction across "
            f"the {family_size} channels with non-blank W/L/T in Table S1. "
            "Channels with blank W/L/T (the 5 'from prior validation' rows) are "
            "excluded from the correction family because the per-coefficient "
            "breakdown for those rows lives in the substrate paper, not in "
            "this manuscript's Table S1."
        ),
        "family_size_for_correction": family_size,
        "alpha": 0.05,
        "n_significant_holm_bonferroni": sig_holm,
        "n_significant_bh_fdr": sig_bh,
        "rows": rows,
    }
    out_json.write_text(json.dumps(payload, indent=2))

    # Emit Markdown table for the manuscript / supplementary
    lines = [
        "# Statistical-significance table (computed from MANUSCRIPT Table S1 counts)",
        "",
        f"Family-correction size: {family_size} channels (excludes 5 'from prior validation' rows with blank W/L/T)",
        f"Alpha: 0.05",
        f"Significant under Holm-Bonferroni: {sig_holm} of {family_size}",
        f"Significant under BH-FDR: {sig_bh} of {family_size}",
        "",
        "| Channel | κ | n (non-tie) | 95% CI (Wilson) | p (binomial, 2-sided) | Holm-adj. p | BH-adj. p | Holm sig? | BH sig? |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        ci = (
            f"[{r['wilson_ci_95_low']:.3f}, {r['wilson_ci_95_high']:.3f}]"
            if r["wilson_ci_95_low"] is not None
            else "—"
        )
        kappa = f"{r['kappa']:.3f}" if r["kappa"] is not None else "—"
        n = str(r["n_nontie"]) if r["n_nontie"] is not None else "—"
        p_two = f"{r['binomial_p_two_sided']:.4f}" if r["binomial_p_two_sided"] is not None else "—"
        p_holm = (
            f"{r['holm_bonferroni_p_adj']:.4f}"
            if r.get("holm_bonferroni_p_adj") is not None
            else "—"
        )
        p_bh = f"{r['bh_fdr_p_adj']:.4f}" if r.get("bh_fdr_p_adj") is not None else "—"
        holm_sig = "✓" if r.get("holm_bonferroni_reject") else "—" if r.get("holm_bonferroni_reject") is None else "✗"
        bh_sig = "✓" if r.get("bh_fdr_reject") else "—" if r.get("bh_fdr_reject") is None else "✗"
        lines.append(
            f"| {r['channel']} | {kappa} | {n} | {ci} | {p_two} | {p_holm} | {p_bh} | {holm_sig} | {bh_sig} |"
        )
    out_md = out_dir / "stats.md"
    out_md.write_text("\n".join(lines) + "\n")

    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")
    print()
    print(f"Summary: {sig_holm} of {family_size} channels significant under Holm-Bonferroni, {sig_bh} under BH-FDR.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "derived",
        help="Output directory for stats.json and stats.md",
    )
    args = ap.parse_args()
    sys.exit(main(args.out_dir))
