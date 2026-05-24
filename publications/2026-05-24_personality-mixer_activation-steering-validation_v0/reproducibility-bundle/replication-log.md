# Replication Log — 24-Channel Activation-Steering Validation

This file records every end-to-end replication run of this bundle on a
fresh machine. Per the unit's reproducibility-bundle standard (CHARTER §9,
STANDARDS.md), every Tier-C/E/M publication's bundle must be end-to-end
run by the author (or, where available, an independent third party) before
release, with the recovered headline numbers within the documented
tolerance of the published numbers.

---

## Status as of 2026-05-24

**`make replicate` runs locally and exits 0.** The bundle's local verification
target — stats regeneration, figure regeneration, and κ-delta verification
against the manuscript's published values — completes in ~10 seconds with
no API calls (see Replication-run records below for the first entry).

**`make replicate-full` has not yet been run.** The Modal end-to-end re-run
target requires `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`, and
`ANTHROPIC_API_KEY` plus a ~$10 spend on a real Modal+Anthropic run. This
is the Gate-7 closure path for any external (arXiv or otherwise) submission;
it is documented and exercisable but has not been triggered.

**Honest gap surfaced by the local replicate:** 4 of the 9 vendored channels
report `OUT_OF_TOLERANCE` because the vendored `results/` corresponds to the
*single-layer baseline* (substrate-paper configuration), while the
manuscript's headline numbers for those 4 channels are the *multi-layer
rescued* values from the local SHA f492844 that was never pushed to GitHub.
See `data/derived/replication-delta.md` for the full per-channel delta.
The 15 new channels' judge reports are likewise on that unpushed SHA, so
they show as `NOT_VENDORED`. Closure path for both gaps is the same: push
the local SHA, vendor selectively from the MacMini, or run
`make replicate-full`.

## What an end-to-end run would need

For a replication to count under the unit's standard, the following
operations must succeed from a clean clone of this publication folder
(plus the project repos at the pinned SHAs):

1. `conda env create -f environment.yml && conda activate mdfy-personality-mixer-validation`
2. Set credentials: `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`, `ANTHROPIC_API_KEY`
3. `make replicate` from this directory, which (once finalised) will:
   - Pull the source-repo code at the pinned SHAs into `code/`
   - Run `harness.py::eval` on Modal L4 for each of the 24 channels at the
     pre-specified configurations (ML L12/16/20 c=2; sadism + psychopathy
     also at c=4)
   - Run `analyse.py` over the resulting response pairs against the
     committed `JUDGE_PROMPTS` rubrics
   - Emit `recovered-results.json` and `recovered-results.md`
4. Compare `recovered-results.json` against `data/published-results.json`
   (pre-populated with the manuscript's reported κ values) within the
   tolerance specified in `PROVENANCE.md` §"Tolerance" (κ ±0.05).

When this succeeds with zero out-of-tolerance deviations, an entry is
appended to this file with: date, replicator name, machine
specification, environment hash, list of κ deltas, and the
`recovered-results.md` summary.

## What's blocking a real end-to-end run

In order, by closure cost:

1. **Lift the `huggingface_revision_sha`** for Qwen2.5-7B-Instruct from
   the source repo into `seeds.json`. ~5 minutes.
2. **Lift the judge `position_randomisation_seed`** and `judge_temperature`
   from `analyse.py` at commit `f492844` into `seeds.json`. ~5 minutes.
3. **Vendor or git-submodule the source repos at the pinned SHAs** into
   `code/`. ~30 minutes to set up; pinned SHAs already known.
4. **Pre-populate `data/published-results.json`** with the manuscript's
   reported κ values for delta comparison. ~30 minutes (24 channels × a
   handful of fields).
5. **Implement the real `make replicate` target** that chains the above.
   ~1 hour.
6. **Run end-to-end** on Modal L4 with a fresh environment (Modal will
   build the image from scratch). Estimated 2–3 hours of GPU time +
   ~$2–4 in Modal + ~$5–10 in Anthropic judge calls.

Total to clear this blocker: roughly half a day of focused work plus the
real money cost of one end-to-end run.

## Replication-run records

### 2026-05-24 — replicator: Rick Weakley (via Claude `claude-opus-4-7-1m`, autonomous-mode)

- Machine: MacBook Pro (Apple Silicon), macOS 25.5
- GPU: N/A — this is the local-only `make replicate` target (stats + figures + κ delta against vendored results), not `make replicate-full`
- Environment: `.venv-stats/` with scipy, statsmodels, matplotlib, numpy
- Run wall-clock time: ~10 seconds
- Run cost: $0 (no API calls; local computation only)
- Outputs produced:
  - `data/derived/stats.{json,md}` — per-channel binomial tests + Wilson CIs + Holm/BH-FDR corrections
  - `data/derived/replication-delta.md` — recovered-vs-published κ for the 9 originally-validated channels
  - `data/figures/fig{1,2,3}_*.png` — manuscript figures regenerated
- κ-delta summary: **5 MATCH · 4 OUT_OF_TOLERANCE · 15 NOT_VENDORED**
  - 5 MATCH: achievement_striving, cheerfulness, sociability, stimulation, dospert_financial (the substrate-paper baseline channels whose published κ values come from single-layer runs that ARE vendored).
  - 4 OUT_OF_TOLERANCE: dospert_recreational, cautiousness, conscientiousness_self_discipline, self_direction. The vendored data is the *single-layer baseline* (which the manuscript §3.3 reports as the "single-layer (κ)" column); the manuscript's headline κ values for these channels are the *multi-layer rescued* values from the unpushed local SHA f492844. This is honest disclosure of a Gate-7 gap, not a build failure.
  - 15 NOT_VENDORED: the new channels (narcissism through sadism) — judge reports live on the same unpushed local SHA.
- Stats summary: 0 of 18 channels reach significance under Holm-Bonferroni or BH-FDR correction at α = 0.05 (per-channel n is too small; see §3.1.1 of the manuscript).
- Signature: Rick Weakley (decisions); Claude `claude-opus-4-7-1m` (execution under autonomous-mode authorisation)
- Status: PARTIAL — bundle is reproducible for the substrate-paper baseline subset; full reproducibility requires either the local-SHA-f492844 push, the MacMini selective vendor, or `make replicate-full` on Modal.

Template for future entries (delete this template once the second entry lands):

```
### YYYY-MM-DD — replicator: NAME

- Machine: macOS / Linux / WSL2 + chip + RAM
- GPU: Modal L4 / local GPU / CPU-only / N/A
- Environment hash: SHA256 of the resolved environment lockfile
- Modal account: cybernaut6404 / other
- Anthropic account: rick@mdfy.co.uk / other
- Run wall-clock time: HH:MM
- Run cost: $X Modal + $Y Anthropic
- κ deltas (per channel, recovered vs published):
  - narcissism: 1.000 vs 1.000 → 0.000 ✓
  - ... (all 24 channels)
- κ deltas outside ±0.05 tolerance: [none | list]
- Refusal-cosine deltas outside ±0.01 tolerance: [none | list]
- Inter-channel-cosine deltas outside ±0.01 tolerance: [none | list]
- QC probes pass: YES / NO (per channel)
- Notes: [any deviations, warnings, or environment issues encountered]

Signature: [REPLICATOR NAME]
Status: PASS / PARTIAL / FAIL
```

When the first end-to-end run completes (whether by the author or by an
independent third party), the entry below template is appended:

```
### YYYY-MM-DD — replicator: NAME

- Machine: macOS / Linux / WSL2 + chip + RAM
- GPU: Modal L4 / local GPU / CPU-only
- Environment hash: SHA256 of the resolved environment lockfile
- Modal account: cybernaut6404 / other
- Anthropic account: rick@mdfy.co.uk / other
- Run wall-clock time: HH:MM
- Run cost: $X Modal + $Y Anthropic
- κ deltas (per channel, recovered vs published):
  - narcissism: 1.000 vs 1.000 → 0.000 ✓
  - ... (all 24 channels)
- κ deltas outside ±0.05 tolerance: [none | list]
- Refusal-cosine deltas outside ±0.01 tolerance: [none | list]
- Inter-channel-cosine deltas outside ±0.01 tolerance: [none | list]
- QC probes pass: YES / NO (per channel)
- Notes: [any deviations, warnings, or environment issues encountered]

Signature: [REPLICATOR NAME]
Status: PASS / PARTIAL / FAIL
```

---

## Acknowledgement of the gap

This empty log is, by the unit's standards (CHARTER §9), an honest
disclosure that the bundle is not yet fully reproducible by an
independent third party. The manuscript §7 reports an estimated 2–3
hours of L4 GPU time for a complete replication; that estimate is
based on the original validation runs from inside the source project,
not on a bundle-driven replication from a clean clone.

A successful end-to-end run from this bundle, recorded here, is a hard
requirement before any preprint posting under the unit's standards.
