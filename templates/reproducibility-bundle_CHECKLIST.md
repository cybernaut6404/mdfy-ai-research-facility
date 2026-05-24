# Reproducibility Bundle — Checklist

> *Every Tier C, E, and M publication ships with a Reproducibility Bundle satisfying every item below. Items that genuinely do not apply are marked N/A with a one-line justification.*

**Publication:** [TITLE]
**Tier:** [C/E/M]
**Bundle prepared by:** [NAME]
**Date:** [YYYY-MM-DD]
**Zenodo DOI (assigned at release):** [DOI]

---

## Code

- [ ] Full source code for data collection, analysis, and figure generation is included, at the tagged commit of release.
- [ ] No code referenced in the manuscript is missing from the bundle.
- [ ] A `Makefile`, `tasks.py`, or equivalent provides a single `replicate` command that reproduces the headline figures from raw inputs.

## Environment

- [ ] A complete dependency specification is included: `environment.yml` (conda), `requirements.txt` + lockfile, `pyproject.toml` + lockfile, or `uv.lock`. Versions are pinned to the exact patch.
- [ ] Python/runtime version is pinned.
- [ ] Any system-level dependencies (CUDA, BLAS, compiler) are documented with versions tested.
- [ ] A `Dockerfile` or container spec is provided where the environment is non-trivial.

## Data

- [ ] Raw data is included in the bundle, or — where it cannot be redistributed — a documented access procedure plus cryptographic checksums (SHA-256) of every file used is included.
- [ ] Processed/derived data is included or fully reconstructable from raw data via the provided code.
- [ ] Data licenses are documented in `data/LICENSE.md`.
- [ ] FAIR-aligned metadata (Wilkinson et al. 2016): persistent ID, rich metadata, machine-readable schema, clear license.

## Determinism

- [ ] All random seeds are recorded in `seeds.json` (or equivalent) and referenced from the code.
- [ ] Sources of non-determinism (e.g., GPU non-determinism, parallel scheduling) are documented and, where possible, mitigated.
- [ ] Hyperparameters and configuration files are included.

## Prompts and AI artifacts

- [ ] All prompts that materially shaped the published work are archived in `ai-use-disclosure.md`.
- [ ] Prompt templates and any prompt-engineering scripts are included in the code.
- [ ] Where AI was used for analysis, the AI outputs are archived alongside the prompts.

## Provenance

- [ ] `PROVENANCE.md` describes the chain from raw inputs to each published figure and table.
- [ ] Every figure and table in the manuscript maps to a script or notebook in the bundle.
- [ ] Any manual steps (e.g., manual coding, expert judgment) are documented.

## Replication log

- [ ] The bundle has been run end-to-end on a fresh machine by the founder (or, where available, an independent third party). The log is in `replication-log.md`.
- [ ] The headline numerical results in the manuscript match the bundle's reproduction within the documented tolerance.

## Compliance artifacts (where applicable)

Every compliance artifact below lives in the publication folder (not the reproducibility-bundle subfolder, so reviewers can find it without unpacking the bundle), at the canonical path listed. "Where applicable" means: include the artifact if the tier and study type below describe this publication; otherwise the item is N/A with a one-line justification.

- [ ] **NeurIPS Paper Checklist** — Tier C ML work — committed as `neurips-checklist.md`. Every item completed; items marked "N/A" carry a one-line justification.
- [ ] **SCRIBE 2016 Checklist** — Tier C / Tier E self-experimentation and other single-case experimental designs — committed as `scribe-checklist.md`. The SCRIBE 2016 reporting items are enumerated with the manuscript section or line that satisfies each.
- [ ] **Model Card (Mitchell et al. 2019)** — Tier M, where a model is released — committed as `model-card.md`. Covers intended use, training data, evaluation, known limitations, ethical considerations.
- [ ] **PRISMA 2020 Checklist + Flow Diagram** — Tier T systematic reviews and meta-analyses — committed as `prisma-checklist.md` plus a flow diagram at `prisma-flow.png` (or `.svg` / `.pdf`). Both required; the checklist alone is insufficient for PRISMA 2020 compliance.

## Model release (Tier M, where a model is released)

- [ ] License terms for the model are stated.
- [ ] Known limitations and intended use are explicit.
- [ ] Responsible-release considerations (Charter §11) have been reviewed.

(The Model Card itself is listed in *Compliance artifacts* above.)

## Sign-off

- [ ] Bundle preparer has reviewed every item above.
- [ ] Internal review (Gate 6) has verified spot-checked items.
- [ ] Bundle is archived at Zenodo and the DOI is in the manuscript.
