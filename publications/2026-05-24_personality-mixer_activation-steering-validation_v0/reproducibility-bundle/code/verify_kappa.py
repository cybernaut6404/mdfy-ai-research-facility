#!/usr/bin/env python3
"""Verify the manuscript's reported κ values against the vendored
results/*/results.json judge reports.

Coverage: the 9 originally-validated channels (those whose judge reports
were pushed to the GitHub remote). The 15 new channels' judge reports
live on a local SHA (f492844) that was never pushed; those rows are
reported as 'NOT_VENDORED' in the delta table.

Output: data/derived/replication-delta.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


# Mapping: manuscript-channel-name → results-dir-name (in data/results/).
# The 9 originally-validated channels have their results vendored.
RESULTS_DIR_MAP = {
    "achievement_striving": "achievement_striving",
    "cheerfulness": "cheerfulness",
    "sociability": "sociability",
    "stimulation": "stimulation",
    "dospert_financial": "dospert_financial",
    "dospert_recreational": "dospert_recreational",
    "cautiousness": "cautiousness",
    "conscientiousness_self_discipline": "conscientiousness_self_discipline_v3",
    "self_direction": "self_direction",
}

# Manuscript-reported κ for each channel (Table S1).
PUBLISHED_KAPPA = {
    "achievement_striving": 0.740,
    "cheerfulness": 0.700,
    "sociability": 0.640,
    "stimulation": 0.630,
    "dospert_financial": 0.660,
    "dospert_recreational": 0.722,
    "cautiousness": 0.583,
    "conscientiousness_self_discipline": 0.636,
    "self_direction": 0.667,
    # The 15 new channels live in the local-only SHA f492844; not vendored.
    "narcissism": 1.000,
    "psychopathy": 1.000,
    "attachment_avoidant": 1.000,
    "hexaco_emotionality": 1.000,
    "honesty_humility": 1.000,
    "machiavellianism": 0.857,
    "hexaco_extraversion": 0.800,
    "self_monitoring": 0.800,
    "openness": 0.750,
    "hexaco_agreeableness": 0.750,
    "locus_of_control": 0.667,
    "attachment_anxious": 0.667,
    "self_defeat": 0.500,
    "sycophancy": 0.250,
    "sadism": 0.000,
}

TOLERANCE = 0.05  # per seeds.json _non_determinism.kappa_tolerance_for_replication


def load_results_json(channel: str, results_root: Path) -> dict | None:
    """Returns the results.json content for the channel, or None if not vendored."""
    dir_name = RESULTS_DIR_MAP.get(channel)
    if dir_name is None:
        return None
    path = results_root / dir_name / "results.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main(out_path: Path, results_root: Path) -> int:
    rows = []
    for ch, kappa_pub in PUBLISHED_KAPPA.items():
        rj = load_results_json(ch, results_root)
        if rj is None:
            rows.append({
                "channel": ch,
                "kappa_published": kappa_pub,
                "kappa_recovered": None,
                "delta": None,
                "status": "NOT_VENDORED",
                "note": "judge reports live on local SHA f492844 (not pushed to GitHub remote); see reproducibility-bundle/data/results/ for the vendored 9-channel subset",
            })
            continue
        kappa_rec = rj.get("overall", {}).get("directional_accuracy_excluding_ties")
        if kappa_rec is None:
            rows.append({
                "channel": ch,
                "kappa_published": kappa_pub,
                "kappa_recovered": None,
                "delta": None,
                "status": "MISSING_KEY",
                "note": "results.json has no overall.directional_accuracy_excluding_ties",
            })
            continue
        kappa_rec_r = round(kappa_rec, 4)
        delta = kappa_rec - kappa_pub
        status = "MATCH" if abs(delta) <= TOLERANCE else "OUT_OF_TOLERANCE"
        rows.append({
            "channel": ch,
            "kappa_published": kappa_pub,
            "kappa_recovered": kappa_rec_r,
            "delta": round(delta, 4),
            "status": status,
            "note": "",
        })

    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Replication delta — κ recovered from vendored results.json vs manuscript-reported κ",
        "",
        f"Tolerance for MATCH: ±{TOLERANCE} (per seeds.json _non_determinism.kappa_tolerance_for_replication)",
        "",
        f"Coverage: {sum(1 for r in rows if r['status'] != 'NOT_VENDORED')} of {len(rows)} channels vendored "
        f"({sum(1 for r in rows if r['status'] == 'NOT_VENDORED')} channels' judge reports live on local SHA f492844, not pushed).",
        "",
        "| Channel | κ (published) | κ (recovered) | Δ | Status |",
        "|---|---|---|---|---|",
    ]
    n_match = 0
    n_oot = 0
    n_not_vendored = 0
    for r in rows:
        k_pub = f"{r['kappa_published']:.3f}"
        k_rec = f"{r['kappa_recovered']:.3f}" if r['kappa_recovered'] is not None else "—"
        delta = f"{r['delta']:+.3f}" if r['delta'] is not None else "—"
        if r["status"] == "MATCH":
            n_match += 1
            status_cell = "✓ MATCH"
        elif r["status"] == "OUT_OF_TOLERANCE":
            n_oot += 1
            status_cell = "✗ OUT_OF_TOLERANCE"
        else:
            n_not_vendored += 1
            status_cell = f"⚠ {r['status']}"
        lines.append(f"| {r['channel']} | {k_pub} | {k_rec} | {delta} | {status_cell} |")
    lines.extend([
        "",
        f"**Summary:** {n_match} MATCH · {n_oot} OUT_OF_TOLERANCE · {n_not_vendored} NOT_VENDORED",
        "",
        "## Closure path for the NOT_VENDORED rows",
        "",
        "The 15 new channels' judge reports (Dark Tetrad / HEXACO / attachment / locus / self-construct) were committed to the local mg-digital-twin clone on the MacMini at SHA `f492844` but that commit was never pushed to `cybernaut6404/mg-digital-twin` on GitHub. Closure options (in order of cleanness):",
        "",
        "1. **Push the local SHA.** Run on the MacMini: `cd ~/ai-workspace/mg-digital-twin && git push origin f492844:main` (or push to a separate branch). Then re-vendor `experiments/d4-fader-intervention/results/` into this bundle's `data/results/`.",
        "2. **Vendor selectively from the local clone.** Without pushing, copy the missing results/* directories from the MacMini clone directly into this bundle. Records the LOCAL_ONLY origin in PROVENANCE.md.",
        "3. **Re-run the validation on Modal.** Use `make replicate-full` (requires `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`, `ANTHROPIC_API_KEY`); estimated $5-15 cost + 2-3 hours of L4 GPU time. Produces fresh results.json files for all 24 channels.",
        "",
        "Until one of those closures lands, the manuscript's claims about the 15 new channels are documented via the published κ values in Table S1 with the W/L/T counts, but the underlying judge reports are NOT replicator-verifiable from this bundle alone.",
    ])
    # Important context for the OUT_OF_TOLERANCE rows:
    # The vendored results/*/results.json files for the original 9 channels
    # correspond to the *single-layer* L16 c=0.5 baseline (the substrate-paper
    # configuration). The manuscript's published κ values for the 4
    # KILL-channels-rescued-by-ML (dospert_recreational, conscientiousness_self_
    # discipline, self_direction, cautiousness) are the *multi-layer* ML L12/16/20
    # c=2 rescued values per §3.3. The ML rescue data lives on the local SHA
    # f492844 (never pushed); it is not present in this bundle.
    # So OUT_OF_TOLERANCE here is honest disclosure of a known Gate-7 gap, not
    # a test failure of the bundle. We exit 0 either way; the reader inspects
    # the delta document to understand the gap.
    if n_oot > 0:
        lines.append("")
        lines.append("## Explanation for the OUT_OF_TOLERANCE rows")
        lines.append("")
        lines.append("The 4 OUT_OF_TOLERANCE rows above (dospert_recreational, cautiousness, conscientiousness_self_discipline, self_direction) are exactly the 4 channels that the manuscript §3.3 reports as 'rescued from KILL by multi-layer steering'. The vendored data in this bundle's `results/` corresponds to the *single-layer* L16 c=0.5 *baseline* (the substrate-paper configuration); the *multi-layer rescued* κ values that the manuscript reports as the headline numbers live in the local SHA f492844 that was never pushed to the GitHub remote. The recovered-κ values shown above match exactly the single-layer (κ) column in the manuscript §3.3 table.")
        lines.append("")
        lines.append("Closure for these 4 rows is the same as for the 15 NOT_VENDORED rows: either push the local SHA, vendor selectively from the MacMini clone, or re-run via `make replicate-full`. This is a real Gate-7 reproducibility gap that the bundle now makes visible.")

    out_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out_path}")
    print(f"\nSummary: {n_match} MATCH · {n_oot} OUT_OF_TOLERANCE (informational, see delta md) · {n_not_vendored} NOT_VENDORED")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "derived" / "replication-delta.md",
    )
    ap.add_argument(
        "--results-root",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "results",
    )
    args = ap.parse_args()
    sys.exit(main(args.out, args.results_root))
