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
- For ML work: NeurIPS Paper Checklist committed per the reproducibility-bundle checklist's *Compliance artifacts* section (`neurips-checklist.md` in the publication folder).
- For human-subjects work beyond founder self-experimentation: IRB approval letter committed.
- For self-experimentation work and other single-case experimental designs: SCRIBE 2016 checklist committed per the reproducibility-bundle checklist's *Compliance artifacts* section (`scribe-checklist.md` in the publication folder).

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
- Model Card (per Mitchell et al. 2019) committed per the reproducibility-bundle checklist's *Compliance artifacts* section (`model-card.md` in the publication folder), for any released model.
- For benchmarks: clear statement of dataset provenance, license, and any contamination risk relative to large pretrained models.

## Tier T — Theoretical and review

A study is Tier T when its primary contribution is conceptual, methodological-without-new-data, or a synthesis of existing literature.

**Checklist (all items required):**

- For meta-analyses and systematic reviews: pre-registered protocol on PROSPERO (where in scope) or OSF, with inclusion/exclusion criteria and analysis plan locked in.
- PRISMA 2020 checklist and flow diagram committed per the reproducibility-bundle checklist's *Compliance artifacts* section (`prisma-checklist.md` and `prisma-flow.[png|svg|pdf]` in the publication folder) for systematic reviews and meta-analyses.
- Full bibliography under version control; literature search strategy reproducible.
- COI disclosure (§12 of Charter) updated and committed.
- AI-use disclosure paragraph drafted and reviewed.
- Internal review (Gate 6) completed and signed.

## Review prompt (Gate 6)

In v0, internal review is performed by an LLM under a structured prompt, counter-signed by the founder. The prompt is itself a versioned artifact.

The canonical Gate-6 review prompt lives at [`templates/internal-review-prompt_v1.md`](templates/internal-review-prompt_v1.md). It supersedes the seven-question working draft that previously appeared in this section. Reviews cite the prompt version they were performed under (e.g., `v1`), and any non-cosmetic change to the prompt is a new `vN` file rather than an edit-in-place.

The v1 prompt covers, in order: (1) tier-checklist compliance, (2) claim–evidence calibration, (3) pre-registration / exploration-plan adherence, (4) AI-use disclosure completeness, (5) reproducibility-bundle spot check, (6) ethics / dual-use / responsible-release, (7) conflicts of interest, (8) internal consistency, (9) reservations not covered above, and (10) recommendation (`PROCEED` / `PROCEED WITH REVISIONS` / `HOLD` / `ABANDON OR RESCOPE`). The prompt specifies a mandatory output schema and includes a human counter-signature block.

The reviewer's response, the founder's counter-signature, and any resolution of reviewer points are committed to the publication folder as `internal-review.md` before release.
