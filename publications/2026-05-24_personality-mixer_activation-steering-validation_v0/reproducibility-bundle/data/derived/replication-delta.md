# Replication delta — κ recovered from vendored results.json vs manuscript-reported κ

Tolerance for MATCH: ±0.05 (per seeds.json _non_determinism.kappa_tolerance_for_replication)

Coverage: 9 of 24 channels vendored (15 channels' judge reports live on local SHA f492844, not pushed).

| Channel | κ (published) | κ (recovered) | Δ | Status |
|---|---|---|---|---|
| achievement_striving | 0.740 | 0.740 | +0.000 | ✓ MATCH |
| cheerfulness | 0.700 | 0.698 | -0.002 | ✓ MATCH |
| sociability | 0.640 | 0.645 | +0.005 | ✓ MATCH |
| stimulation | 0.630 | 0.635 | +0.005 | ✓ MATCH |
| dospert_financial | 0.660 | 0.658 | -0.002 | ✓ MATCH |
| dospert_recreational | 0.722 | 0.538 | -0.183 | ✗ OUT_OF_TOLERANCE |
| cautiousness | 0.583 | 0.500 | -0.083 | ✗ OUT_OF_TOLERANCE |
| conscientiousness_self_discipline | 0.636 | 0.522 | -0.114 | ✗ OUT_OF_TOLERANCE |
| self_direction | 0.667 | 0.353 | -0.314 | ✗ OUT_OF_TOLERANCE |
| narcissism | 1.000 | — | — | ⚠ NOT_VENDORED |
| psychopathy | 1.000 | — | — | ⚠ NOT_VENDORED |
| attachment_avoidant | 1.000 | — | — | ⚠ NOT_VENDORED |
| hexaco_emotionality | 1.000 | — | — | ⚠ NOT_VENDORED |
| honesty_humility | 1.000 | — | — | ⚠ NOT_VENDORED |
| machiavellianism | 0.857 | — | — | ⚠ NOT_VENDORED |
| hexaco_extraversion | 0.800 | — | — | ⚠ NOT_VENDORED |
| self_monitoring | 0.800 | — | — | ⚠ NOT_VENDORED |
| openness | 0.750 | — | — | ⚠ NOT_VENDORED |
| hexaco_agreeableness | 0.750 | — | — | ⚠ NOT_VENDORED |
| locus_of_control | 0.667 | — | — | ⚠ NOT_VENDORED |
| attachment_anxious | 0.667 | — | — | ⚠ NOT_VENDORED |
| self_defeat | 0.500 | — | — | ⚠ NOT_VENDORED |
| sycophancy | 0.250 | — | — | ⚠ NOT_VENDORED |
| sadism | 0.000 | — | — | ⚠ NOT_VENDORED |

**Summary:** 5 MATCH · 4 OUT_OF_TOLERANCE · 15 NOT_VENDORED

## Closure path for the NOT_VENDORED rows

The 15 new channels' judge reports (Dark Tetrad / HEXACO / attachment / locus / self-construct) were committed to the local mg-digital-twin clone on the MacMini at SHA `f492844` but that commit was never pushed to `cybernaut6404/mg-digital-twin` on GitHub. Closure options (in order of cleanness):

1. **Push the local SHA.** Run on the MacMini: `cd ~/ai-workspace/mg-digital-twin && git push origin f492844:main` (or push to a separate branch). Then re-vendor `experiments/d4-fader-intervention/results/` into this bundle's `data/results/`.
2. **Vendor selectively from the local clone.** Without pushing, copy the missing results/* directories from the MacMini clone directly into this bundle. Records the LOCAL_ONLY origin in PROVENANCE.md.
3. **Re-run the validation on Modal.** Use `make replicate-full` (requires `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`, `ANTHROPIC_API_KEY`); estimated $5-15 cost + 2-3 hours of L4 GPU time. Produces fresh results.json files for all 24 channels.

Until one of those closures lands, the manuscript's claims about the 15 new channels are documented via the published κ values in Table S1 with the W/L/T counts, but the underlying judge reports are NOT replicator-verifiable from this bundle alone.

## Explanation for the OUT_OF_TOLERANCE rows

The 4 OUT_OF_TOLERANCE rows above (dospert_recreational, cautiousness, conscientiousness_self_discipline, self_direction) are exactly the 4 channels that the manuscript §3.3 reports as 'rescued from KILL by multi-layer steering'. The vendored data in this bundle's `results/` corresponds to the *single-layer* L16 c=0.5 *baseline* (the substrate-paper configuration); the *multi-layer rescued* κ values that the manuscript reports as the headline numbers live in the local SHA f492844 that was never pushed to the GitHub remote. The recovered-κ values shown above match exactly the single-layer (κ) column in the manuscript §3.3 table.

Closure for these 4 rows is the same as for the 15 NOT_VENDORED rows: either push the local SHA, vendor selectively from the MacMini clone, or re-run via `make replicate-full`. This is a real Gate-7 reproducibility gap that the bundle now makes visible.
