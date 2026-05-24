# DEMO — Reproducibility-bundle reference layout for mdfy-ai-research-facility v0

> **⚠ THIS IS A DEMO PUBLICATION.** Every file in this folder is a worked example, not a real research output. The "study" reported here exists solely to demonstrate what a finished publication folder under the unit's standards looks like. Do not cite this DEMO in any external work. Do not interpret its content as a research finding.

**Publication folder:** `publications/2026-05-24_example_demo-publication_v0/`
**Source repo:** `example` (this folder is the example; there is no upstream source repo).
**Tier:** M (methods — the contribution is the structural example itself).
**Status:** DEMO. Will never be released to a preprint server or journal.
**Preprint DOI:** N/A (DEMO).
**Reproducibility bundle DOI (Zenodo):** N/A (DEMO).
**Date of creation:** 2026-05-24.

---

## Abstract

This DEMO publication exists to demonstrate the structural conventions of a finished publication folder under the v0 charter of `mdfy-ai-research-facility`. The "method" described is the publication-folder schema itself: a `README.md` (this file), a `manuscript.md`, an `ai-use-disclosure.md`, an `internal-review.md`, a `reproducibility-bundle/` directory with code, data, environment, seeds, provenance, and replication log, a `correspondence/` directory, and a per-publication COI disclosure. A `Makefile` in the bundle provides a `make replicate` target whose only operation is to verify the folder's structural compliance. This DEMO satisfies every Tier-M checklist item in `STANDARDS.md` and provides a known-good reference against which real publications can be compared.

## Authors

Rick Weakley (`mdfy-ai-research-facility`). ORCID: [placeholder].

## Cite this work

Do not cite this DEMO. Cite real publications from the unit instead.

## What's in this folder

- `README.md` — this file.
- `manuscript.md` — the DEMO manuscript (short).
- `ai-use-disclosure.md` — full AI-use disclosure for this DEMO.
- `internal-review.md` — the Gate-6 internal review of this DEMO, produced under the v1 review prompt.
- `deviations.md` — required for every Tier C; included here for completeness (this Tier-M DEMO had no deviations).
- `coi-disclosure_demo.md` — per-publication ICMJE disclosure.
- `reproducibility-bundle/` — code, environment, seeds, provenance, replication log.
- `correspondence/` — placeholder for review correspondence (empty in DEMO).

## How to reproduce

```
cd reproducibility-bundle
make replicate
```

This invokes `scripts/check-publication-structure.sh` from the repo root and verifies that this DEMO folder satisfies the structural requirements. The "headline result" of this DEMO is the exit code of that check: zero means the folder is structurally compliant.

## Pre-registration / Exploration Plan

This DEMO is Tier M and does not require a pre-registration. A Scoping Memo would normally accompany a Tier-M publication; for this DEMO, the Scoping Memo is implicit ("produce a structurally-compliant publication folder").

## AI assistance

This DEMO was prepared with assistance from Anthropic's Claude. See `ai-use-disclosure.md` for the full record. Tier 2 disclosure (drafting assistance only; no analysis or data generation).

## License

Code: Apache-2.0 (inherits from repo `LICENSE-CODE`).
Content, figures, data: CC-BY-4.0 (inherits from repo `LICENSE-CONTENT`).

## Contact

Rick Weakley — rick@minorgod.com.
