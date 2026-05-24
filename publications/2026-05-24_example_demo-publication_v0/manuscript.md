# DEMO — Reproducibility-bundle reference layout for mdfy-ai-research-facility v0

> **⚠ THIS IS A DEMO MANUSCRIPT.** It is a structural exemplar, not a research output. Sections are short and refer back to the folder's own structure. Do not cite this in external work.

**Tier:** M (methods)
**Date:** 2026-05-24
**Status:** DEMO; not for external release.

---

## Abstract

The `mdfy-ai-research-facility` v0 charter prescribes a publication-folder layout, AI-use disclosure schema, internal-review process, and reproducibility-bundle contents. To enable reviewers and future contributors to compare real publications against a known-good reference, this DEMO publication populates the layout end-to-end with non-research content. The contribution is the worked example itself.

## 1. Introduction

A publication-folder convention defined only on paper drifts over time. A worked example, committed to the repository alongside the charter, anchors the convention in observable practice. This DEMO provides such an anchor for v0.

## 2. Methods

The method is structural compliance. Every element required by the Charter (§6, §9) and the Tier-M checklist (STANDARDS.md) is present in this folder. The `reproducibility-bundle/` contains a `Makefile` whose `replicate` target invokes the repo-level CI script `scripts/check-publication-structure.sh` against this publication folder. A passing run is the headline result.

The folder was constructed manually during the founding session (2026-05-24). No data were collected. The "code" in the bundle is a single Python script that re-verifies structural compliance independently of the shell-script CI guard, providing a redundant check.

## 3. Results

The DEMO folder passes the v0 structure check (`scripts/check-publication-structure.sh`) with exit code 0. The independent Python verification (`reproducibility-bundle/code/01_verify_bundle_structure.py`) confirms the bundle's own required files are present.

There are no quantitative results in the conventional sense. The result is the existence and compliance of the folder.

## 4. Discussion

This DEMO will be retained in the repository indefinitely as a structural reference. When the charter advances to v1 (multi-human review) or v2 (formal review board), the DEMO will be regenerated with the corresponding standards or replaced with a new DEMO at the new tier.

A non-trivial real Tier-M publication producing a tool or benchmark would expand this layout: the `code/` directory would contain the actual tool source, `data/` would contain validation datasets or pointers, the manuscript would describe the tool's design and evaluation, and the internal review would assess against §STANDARDS.md Tier-M criteria.

## 5. Limitations

This is a DEMO and is not a research finding. The only thing it demonstrates is structural compliance with v0; it does not validate the standards themselves, nor the AI-mediated review process, nor the reproducibility-bundle conventions in any substantive sense.

## 6. AI assistance

See `ai-use-disclosure.md`. Tier 2 (drafting assistance only).

## 7. Conflicts of interest

See `coi-disclosure_demo.md`. No specific COI for this DEMO beyond the standing tooling disclosure in the repo README.

## 8. Acknowledgments

Anthropic's Claude assisted in drafting this DEMO manuscript. The structural conventions implemented here were specified in the founding-session charter (CHARTER.md v0.0.2).

---

*This DEMO is not for citation, distribution outside the unit's repository, or any inference about real research findings.*
