# [PAPER TITLE]

**Publication folder:** `publications/YYYY-MM-DD_source-repo_short-title_vN/`
**Source repo:** [REPO SLUG]
**Tier:** [C/E/M/T]
**Status:** [draft / preprint / submitted / published]
**Preprint DOI:** [DOI or URL]
**Journal/Venue:** [if applicable]
**Reproducibility bundle DOI (Zenodo):** [DOI]
**Date of release:** [YYYY-MM-DD]

---

## Abstract

[Abstract as it appears in the manuscript.]

## Authors

[Author list in published order, with affiliations and ORCIDs.]

## Cite this work

[Suggested citation, including DOI(s).]

## What's in this folder

- `manuscript.pdf` — the final manuscript.
- `manuscript.md` (or `.tex`) — manuscript source.
- `reproducibility-bundle/` — code, data, environment, seeds, prompts, provenance.
- `ai-use-disclosure.md` — full AI-use record per `AI_USE_POLICY.md`.
- `internal-review.md` — the Gate 6 internal review record (under the v1 prompt).
- `deviations.md` — deviations from the pre-registration or exploration plan, if any (Tier C: required even if empty; other tiers: required where the work had a Gate-3 plan).
- `coi-disclosure_<author>.md` — per-publication ICMJE disclosure of interest for each author.
- `correspondence/` — review correspondence, journal letters, response-to-reviewers.

Compliance artifacts (include where the publication's tier and study type call for them; see the *Compliance artifacts* section of `templates/reproducibility-bundle_CHECKLIST.md` for the canonical list):

- `neurips-checklist.md` — Tier C ML work.
- `scribe-checklist.md` — Tier C / Tier E self-experimentation and other single-case experimental designs.
- `model-card.md` — Tier M, where a model is released.
- `prisma-checklist.md` plus `prisma-flow.[png|svg|pdf]` — Tier T systematic reviews and meta-analyses.

## How to reproduce

From the reproducibility bundle:

```
cd reproducibility-bundle
make replicate
```

See `reproducibility-bundle/README.md` for full instructions.

## Pre-registration / Exploration Plan

This work was pre-registered at: [URL or path].
Deviations from the pre-registration are documented in §[N] of the manuscript and summarized in `deviations.md`.

## AI assistance

This work used AI assistance at Tier [N] of `AI_USE_POLICY.md`. See `ai-use-disclosure.md` for the full record.

## License

Code: [LICENSE]
Content, figures, data: [LICENSE]

## Contact

Corresponding author: [NAME, EMAIL].
