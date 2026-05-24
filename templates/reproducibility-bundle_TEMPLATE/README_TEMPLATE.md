# Reproducibility Bundle — [PUBLICATION TITLE]

This bundle accompanies the manuscript at `../manuscript.md` (or `MANUSCRIPT.md`).
It contains the artifacts a third party needs to re-derive the headline
results in the manuscript from raw inputs, end-to-end, on a fresh machine.

**Status:** [complete / partial — stub state, see Gate-7 closure path below]

## What's in this bundle

- `README.md` — this file.
- `PROVENANCE.md` — the chain of derivation from raw inputs to every headline figure / table / claim in the manuscript.
- `environment.yml` — conda environment specification (Python + ML/validation dependencies). Versions pinned where known; TODO markers for unpinned transitive deps.
- `seeds.json` — random seeds, decoding parameters, and any non-deterministic operation parameters used in the runs.
- `replication-log.md` — record of any end-to-end replication run of this bundle.
- `Makefile` — the `replicate` target that re-derives the headline figures from raw inputs.
- `code/` — code that produced the manuscript's results (or pointer to source repos at pinned SHAs; see `code/README.md`).
- `data/` — input data + run artifacts that fed the results (or pointer to source repos; see `data/README.md`).

## How to replicate (target end state)

From this directory:

```
conda env create -f environment.yml
conda activate [ENV_NAME]
make replicate
```

This regenerates the headline numerical results in the manuscript's Tables and Figures.

## Reproducibility checklist compliance

Per-item table against `templates/reproducibility-bundle_CHECKLIST.md`:

| Section | Item | Status |
|---------|------|--------|
| Code | Full source for collection / analysis / figures | [✓ vendored / ❌ pointer-only — Gate-7 TODO] |
| Code | No code in manuscript missing from bundle | [✓ / ❌] |
| Code | `make replicate` reproduces headline figures from raw inputs | [✓ / ❌ stub Makefile] |
| Environment | Complete dependency specification with pinned versions | [✓ / ⚠ partial — env.yml lists deps, lockfile TODO] |
| Environment | Python/runtime version pinned | [✓ Python X.Y / ❌] |
| Environment | System-level dependencies documented | [✓ / ❌] |
| Environment | Dockerfile / container spec | [✓ / ⚠ partial / N/A] |
| Data | Raw data in bundle OR documented access + checksums | [✓ vendored / ❌ pointer-only] |
| Data | Processed data in bundle OR reconstructable | [✓ / ⚠ partial] |
| Data | Data licenses in `data/LICENSE.md` | [✓ / ❌ TODO] |
| Data | FAIR-aligned metadata | [✓ / ❌ TODO] |
| Determinism | Seeds in `seeds.json` | [✓ / ⚠ partial — see seeds.json TODO markers] |
| Determinism | Non-determinism documented | [✓ / ⚠] |
| Determinism | Hyperparameters and config | [✓] |
| Prompts | All prompts archived in `ai-use-disclosure.md` | [✓ deposited / ❌ pending Gate-7] |
| Prompts | Prompt templates / scripts in code | [✓ / ❌] |
| Prompts | AI outputs archived alongside prompts | [✓ / ❌ pending] |
| Provenance | `PROVENANCE.md` describes chain from raw inputs to figures | [✓] |
| Provenance | Every figure/table maps to a script | [✓] |
| Provenance | Manual steps documented | [✓ / ⚠] |
| Replication log | End-to-end run on fresh machine | [✓ logged / ❌ not yet run] |
| Replication log | Headline numbers within documented tolerance | [✓ / ❌ tolerance not yet specified] |
| Compliance artifacts | NeurIPS Paper Checklist (`../neurips-checklist.md`) | [✓ / ⚠ partial / N/A] |
| Compliance artifacts | SCRIBE 2016 checklist | [✓ / N/A] |
| Compliance artifacts | Model Card | [✓ / N/A] |
| Compliance artifacts | PRISMA 2020 checklist + flow diagram | [✓ / N/A] |
| Sign-off | Bundle preparer reviewed every item | [✓ / ⚠ in progress] |
| Sign-off | Gate-6 internal review verified spot-checked items | [✓ / ⚠] |
| Sign-off | Zenodo DOI in manuscript | [✓ / ❌ pending preprint posting] |

## Known gaps

Enumerate honestly. Pointer-only vs vendored vs end-to-end-run is a real distinction; a reviewer or replicator can see exactly what's missing and what closing the gap looks like.

## Compute and cost

- **GPU:** [model + memory + per-hour cost]
- **Total compute for original study:** [approximate]
- **Replication cost:** [approximate]
- **Other costs:** [judge API calls, etc.]

## License

Code: [LICENSE — typically Apache-2.0 per the unit's defaults via `../../../LICENSE-CODE`]
Content: [LICENSE — typically CC-BY-4.0 per the unit's defaults via `../../../LICENSE-CONTENT`]
