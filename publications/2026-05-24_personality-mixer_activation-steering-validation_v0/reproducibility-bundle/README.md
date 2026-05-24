# Reproducibility Bundle — 24-Channel Activation-Steering Validation

This bundle accompanies the manuscript at `../MANUSCRIPT.md`. It contains
the artifacts a third party needs to re-derive the headline κ values in §3
of the manuscript from raw inputs, end-to-end, on a fresh machine.

**Status:** *partial.* This bundle was assembled retroactively from a study
that pre-dates the unit's adoption of its reproducibility-bundle standard
(CHARTER §9, STANDARDS.md, `templates/reproducibility-bundle_CHECKLIST.md`).
Several items are pointers-into-source-repos rather than committed-in-bundle
artifacts. See §"Known gaps" below. This is a Gate-7 (reproducibility-bundle
finalisation) blocker for external submission.

## What's in this bundle

- `README.md` — this file.
- `PROVENANCE.md` — the chain of derivation from raw inputs to every
  headline figure/claim in the manuscript.
- `environment.yml` — conda environment specification (Python 3.11 + the
  ML / validation dependencies). Versions pinned where known; TODO markers
  where they need to be lifted from the source repos' lockfiles.
- `seeds.json` — random seeds, decoding parameters, and judge-position
  randomisation seed used in the validation runs.
- `replication-log.md` — record of any end-to-end replication run of this
  bundle.
- `Makefile` — the `replicate` target that re-derives the headline κ values
  from raw inputs (currently a stub pointing at the source-repo entry
  points; see §"Known gaps").
- `code/` — code that produced the manuscript's results (currently a
  pointer to source repos; see `code/README.md`).
- `data/` — contrastive items, probe libraries, judge rubrics, and run
  artifacts that fed the validation (currently a pointer to source repos;
  see `data/README.md`).

## How to replicate (target end state)

From this directory:

```
conda env create -f environment.yml
conda activate mdfy-personality-mixer-validation
make replicate
```

This is the target end state. As of 2026-05-24 the `make replicate` target
is a stub that walks the operator through the pointers in
`code/README.md` and `data/README.md`. A future finalisation pass will
either vendor the source code into `code/` or pin a specific commit of each
project repo as a git submodule and have `make replicate` clone the
submodules at the pinned SHAs.

## Compute and cost

Per SUPPLEMENTARY_TABLES.md §"Compute and cost provenance":

- **GPU:** Modal L4 (24 GB) at ~$0.80/hr per-second-billed (validation runs)
  and Modal A100-40GB (extraction of the original 9 channels, predating the
  L4 migration).
- **Total Modal cost for the original study:** approximately $8–15 across
  ~21 validation and re-test runs.
- **Judge cost (Anthropic Opus):** approximately $5–8 across all judge runs.
- **Steering-server deploy + idle:** scales to zero between requests;
  near-zero standing cost.

A complete replication on Modal L4 is estimated at 2–3 hours of L4 GPU time
(~$2–4) plus ~$5–10 of Anthropic Opus judge calls. Replicators without a
Modal account can run the same harness locally on any 24 GB GPU.

## Known gaps (as of 2026-05-24)

The bundle does not yet satisfy every item of the unit's reproducibility-
bundle checklist (`templates/reproducibility-bundle_CHECKLIST.md`). The
specific gaps:

- **Code:** the extraction, validation harness, judge, and steering-server
  code lives in private project repos
  (`mg-digital-twin@f492844`, `personality-central-db@2bdf13b`,
  `personality-construct-runner@d55296b`, `personality-mixer-codex@5462733`,
  `personality-mixer-claude@3963ce4`). At Gate 7 these will either be
  vendored into `code/` or attached as git submodules pinned at those
  SHAs.
- **Data:** the contrastive items (n = 30–50 per channel), probes (12–14
  directional + 2 QC per channel for the new 15; 30 each for the original
  9), judge rubrics, and run artifacts live in
  `mg-digital-twin/experiments/d4-fader-intervention/` at commit
  `f492844`. The steering vectors (`vector.pt` per channel) live in
  `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/`. None of
  these have been mirrored into `data/` yet. The contrastive items are
  derived from the author's single-subject psychometric battery and are
  considered the most sensitive: PII review is required before any
  external release.
- **Environment lockfile:** `environment.yml` lists the top-level
  dependencies but does not pin every transitive dependency. A `uv.lock`
  or equivalent should be lifted from the source repos before any
  external submission.
- **Replication log:** the bundle has not been run end-to-end on a fresh
  machine. `replication-log.md` records what would need to be true for the
  bundle to pass an independent replication; it does not record an
  actual run.
- **AI-use prompt archive:** the full prompt-and-output transcripts that
  produced the manuscript and the judge ratings are not yet deposited.
  Per `../ai-use-disclosure.md` §2.4, these are required before any
  arXiv preprint posting.
- **License files:** this bundle inherits the unit's defaults (Apache-2.0
  for code via `../../../LICENSE-CODE`, CC-BY-4.0 for content via
  `../../../LICENSE-CONTENT`). Per-publication license deviations are
  documented in the publication folder's README; none are present here.

## Reproducibility checklist compliance

See `templates/reproducibility-bundle_CHECKLIST.md` for the unit's standard
checklist. Per-item compliance for this bundle:

| Section | Item | Status |
|---------|------|--------|
| Code | Full source for collection / analysis / figures | ❌ pointer-only; see `code/README.md` |
| Code | No code in manuscript missing from bundle | ❌ same |
| Code | `make replicate` reproduces headline figures from raw inputs | ❌ stub Makefile |
| Environment | Complete dependency specification with pinned versions | ⚠ partial — `environment.yml` lists deps, lockfile TODO |
| Environment | Python/runtime version pinned | ✓ Python 3.11 |
| Environment | System-level dependencies documented | ✓ CUDA / Modal L4 named |
| Environment | Dockerfile / container spec | ⚠ Modal app spec exists in `mg-digital-twin/infra/steering-server/`; not mirrored here |
| Data | Raw data in bundle OR documented access + checksums | ❌ pointer-only |
| Data | Processed data in bundle OR reconstructable | ⚠ judge reports + run artifacts live in source repo |
| Data | Data licenses in `data/LICENSE.md` | ❌ TODO |
| Data | FAIR-aligned metadata | ❌ TODO |
| Determinism | Seeds in `seeds.json` | ⚠ partial — see `seeds.json` |
| Determinism | Non-determinism documented | ✓ greedy decoding, fixed position-randomisation seed; GPU non-determinism noted |
| Determinism | Hyperparameters and config | ✓ multi-layer L12/16/20, |c| ≤ 2, c = 4 diagnostic |
| Prompts | All prompts archived in `ai-use-disclosure.md` | ❌ pending Gate-7 deposition |
| Prompts | Prompt templates / scripts in code | ✓ in source repo |
| Prompts | AI outputs archived alongside prompts | ❌ pending |
| Provenance | `PROVENANCE.md` describes chain from raw inputs to figures | ✓ see `PROVENANCE.md` |
| Provenance | Every figure/table maps to a script | ✓ see `PROVENANCE.md` |
| Provenance | Manual steps documented | ✓ none — fully scripted |
| Replication log | End-to-end run on fresh machine | ❌ not yet — this bundle's `replication-log.md` reflects this honestly |
| Replication log | Headline numbers within documented tolerance | ❌ tolerance not yet specified |
| Compliance artifacts | NeurIPS Paper Checklist (`../neurips-checklist.md`) | ⚠ in progress — Tier-M ML work |
| Compliance artifacts | SCRIBE 2016 checklist | N/A — not a single-case behavioural intervention; the n=1 derivation is methodological, not a behavioural study |
| Compliance artifacts | Model Card | N/A — no model released; steering vectors are released artifacts but not a model in the Mitchell et al. 2019 sense |
| Compliance artifacts | PRISMA 2020 checklist + flow diagram | N/A — not a systematic review or meta-analysis |
| Sign-off | Bundle preparer reviewed every item | ⚠ in progress |
| Sign-off | Gate-6 internal review verified spot-checked items | ⚠ in progress |
| Sign-off | Zenodo DOI in manuscript | ❌ pending preprint posting |

## How to read this status honestly

The pack is publishable AT A METHODS / ML VENUE under preprint conventions
(arXiv) with explicit acknowledgement that the reproducibility-bundle work
is still in progress. It is **not** publishable at any of the four named
top-tier journals until the gaps above are closed. The ROADMAP document
sequences which gaps must close in which window for which venue.
