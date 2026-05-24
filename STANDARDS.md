# Standards — Tier Definitions and Checklists

This document expands §4 of the Charter into concrete, line-item checklists. Every output of the unit is reviewed against the checklist for its tier before release.

## Tier C — Confirmatory

A study is Tier C when it tests a pre-specified hypothesis against pre-specified outcomes with a pre-specified analysis. Anything else is not Tier C.

**Checklist (all items required):**

- Pre-registration time-stamped on OSF (or AsPredicted for compact designs) before any data collection.
- Power analysis or sequential design justification documented in the pre-registration.
- Primary and secondary outcomes named in the pre-registration, with operational definitions.
- Analysis script committed before unblinding; the commit hash is referenced in the pre-registration or in a follow-up amendment.
- Reproducibility bundle satisfying the bundle checklist (`templates/reproducibility-bundle_CHECKLIST.md`).
- AI-use disclosure paragraph drafted and reviewed.
- Internal review (Gate 6) completed and signed.
- Deviations-from-Pre-Registration section present in the manuscript, whether or not deviations occurred.
- Falsification criteria stated in the manuscript.
- For ML work: full NeurIPS Paper Checklist completed and committed.
- For human-subjects work beyond founder self-experimentation: IRB approval letter committed.
- For self-experimentation work: SCRIBE 2016 reporting items satisfied where applicable.

## Tier E — Exploratory

A study is Tier E when it is intended to generate hypotheses, characterize a phenomenon, or open a new research direction. Tier E results are never reported as confirmatory.

**Checklist (all items required):**

- Exploration Plan committed to `preregistrations/` before any data collection; the plan states the research question, design, materials, and what counts as an interesting result.
- Reproducibility bundle satisfying the bundle checklist.
- Every result in the manuscript labelled as exploratory; no p-values reported without explicit "exploratory, uncorrected" annotation.
- AI-use disclosure paragraph drafted and reviewed.
- Internal review (Gate 6) completed and signed.
- A "Limitations of Exploratory Inference" section is present.
- Where the unit intends to upgrade a Tier E finding to Tier C, that intent is named in the discussion section.

## Tier M — Methods and engineering

A study is Tier M when its primary contribution is a tool, benchmark, instrument, or method. Performance claims are still subject to evaluation rigor.

**Checklist (all items required):**

- Written specification of what the tool/method does and what it explicitly does not do.
- Test suite or validation procedure, runnable from the reproducibility bundle.
- Evaluation protocol specified before evaluation runs; any subsequent change documented.
- Reproducibility bundle satisfying the bundle checklist.
- AI-use disclosure paragraph drafted and reviewed.
- Internal review (Gate 6) completed and signed.
- Model Card (per Mitchell et al. 2019) committed for any released model.
- For benchmarks: clear statement of dataset provenance, license, and any contamination risk relative to large pretrained models.

## Tier T — Theoretical and review

A study is Tier T when its primary contribution is conceptual, methodological-without-new-data, or a synthesis of existing literature.

**Checklist (all items required):**

- For meta-analyses and systematic reviews: pre-registered protocol on PROSPERO (where in scope) or OSF, with inclusion/exclusion criteria and analysis plan locked in.
- PRISMA 2020 reporting items satisfied for systematic reviews and meta-analyses.
- Full bibliography under version control; literature search strategy reproducible.
- COI disclosure (§12 of Charter) updated and committed.
- AI-use disclosure paragraph drafted and reviewed.
- Internal review (Gate 6) completed and signed.

## Review prompt (Gate 6) — v0 working draft

In v0, internal review is performed by an LLM under a structured prompt, counter-signed by the founder. The prompt is itself a versioned artifact. The current working version is described here and will be moved into `templates/internal-review-prompt_v0.md` at first use.

The reviewer is given: the manuscript draft, the tier checklist for the manuscript's tier, the pre-registration or exploration plan, the reproducibility bundle's PROVENANCE.md, and the relevant entries from the lab notebook. The reviewer is asked, in order:

1. Are all tier-checklist items satisfied? Identify each unsatisfied item by name.
2. Are the manuscript's claims supported by the evidence at the strength stated? Identify any over-claims or under-claims.
3. Do any analyses appear in the manuscript that are not in the pre-registration or exploration plan, and if so, are they correctly labelled exploratory and disclosed in a Deviations section?
4. Is the AI-use disclosure complete and accurate against the actual record?
5. Does the reproducibility bundle, on a spot-check, contain the artifacts named in its PROVENANCE.md?
6. Are there ethical, dual-use, or responsible-release concerns the Scoping Memo did not anticipate?
7. State any reservations not covered by the questions above.

The reviewer's response, the founder's counter-signature, and any resolution of reviewer points are committed to the publication folder as `internal-review.md` before release.
