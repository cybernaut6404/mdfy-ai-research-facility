# Deviations from Pre-Registration — 24-Channel Activation-Steering Validation

**Publication:** *A 24-Channel Activation-Steering Substrate for Personality Constructs in a Large Language Model.*
**Tier:** M (methods/engineering); see README.md §"Unit-compliance status" and the Gate-6 internal review for the tier assignment.
**Date:** 2026-05-24

---

## 1. Pre-registration status

**No Gate-3 pre-registration or Exploration Plan was committed to this unit's `preregistrations/` directory, OSF, or AsPredicted before any data collection or judge run for this study.** The work pre-dates the unit's adoption of pre-registration as a hard gate (v0.0.3-charter, 2026-05-24); the unit's repository was initialised on the same day this publication pack was assembled. This is a structural, unfixable gap for this publication.

This section exists not because the pre-registration was deviated *from* (it does not exist) but because every Tier-C / Tier-E manuscript under the unit's standards ships with a Deviations section regardless of outcome (per STANDARDS.md). For this Tier-M publication, the section serves as the formal record of the pre-registration *gap*.

## 2. What was actually pre-specified

Per the manuscript §1.2 and §8.5, three hypotheses were stated in the originating project's build notes (`mg-GSTACK/docs/audits/*-2026-05-23.md` and the work log) **before** the validation runs that produced the κ values in §3:

- **H1.** Multi-layer additive steering at L12/16/20 with |c| ≤ 2 will lift at least 4 of the 9 originally-validated channels above the 0.60 directional-accuracy gate.
- **H2.** Generic probes will give systematically lower κ than trait-eliciting probes for dark/edge traits.
- **H3.** Dark-Triad-related channels will show meaningful refusal-direction cosine entanglement, but will not exceed the 0.30 FLAG threshold.

Additionally pre-specified before any judge run:
- The κ ≥ 0.60 PASS gate
- The per-channel blind-rater rubrics (verbatim in `analyse.py::JUDGE_PROMPTS`, no modification after seeing any validation result)
- The probe libraries (`probes/dark-*.json`, `probes/new-*.json`)
- The multi-layer steering configuration (L12/16/20, |c| ≤ 2 main; c = 4 diagnostic only on psychopathy and sadism)
- The judge-position randomisation seed
- The refusal-cosine SAFE/watch/FLAG thresholds (0.1 / 0.3, per Anthropic Persona Vectors 2025)

The build-note timestamps and commit SHAs that anchor "before any validation run" are recorded in WORK_LOG.md §3 (commit chronology) and `mg-GSTACK` audit doc `personality-mixer-audit-2026-05-23.md`.

## 3. Why this is not equivalent to a pre-registration

A timestamped build-note statement of expectations is **not** equivalent to a Gate-3 pre-registration for three reasons that any external reviewer will identify:

1. **No external time-stamp.** The build notes are in author-controlled private repositories. There is no independent witness that the notes existed and were unchanged before the validation runs. An external pre-registration (OSF, AsPredicted, or a signed commit to this unit's public `preregistrations/` directory at a known time) provides that witness; a private build note does not.
2. **No analysis-plan lock-in.** The build notes describe expected directional outcomes but do not pre-commit the analysis script (the script is `mg-digital-twin/experiments/d4-fader-intervention/analyse.py`, and its commit history shows iteration *during* the validation period; the JUDGE_PROMPTS dict was finalised before judge runs, but the surrounding analysis logic was not frozen at a single commit hash before unblinding).
3. **No falsification criteria stated as such.** The build notes describe what would happen if expectations held; they do not state explicit falsification criteria of the form "if X happens we abandon H1." Pre-registrations require this; this work does not have it.

## 4. Consequence for the manuscript

The manuscript's §1.2 framing of "we pre-specified three hypotheses, in the sense of 'stated in the build notes before the validation runs', though we did NOT formally pre-register" is honest but reads slightly stronger than the evidence supports. Per the drafting LLM's own self-critique (committed alongside this pack as historical context):

> A strict reviewer would say: if you didn't OSF-timestamp them, they're post-hoc framing — even if you mean well. I flagged this in the Limitations (§8.5) which is the right place, but the Intro framing reads slightly stronger than the timestamp evidence supports.

**Recommended manuscript revision** before any external submission: §1.2 reframed as "expectations stated in build notes before validation, presented here as exploratory findings rather than confirmatory tests"; all H1–H3 results (§3) labelled "exploratory" where claimed as confirmation; "confirmed" in §3.2 and §3.3 headings replaced with "consistent with" or "supports."

This revision is tracked as a Gate-6 finding and will land in the manuscript before any preprint posting.

## 5. Consequence for tier assignment

Under the unit's tier framework (STANDARDS.md):
- **Tier C (confirmatory) is structurally inaccessible** for this work — no pre-registration exists, and one cannot be created retroactively.
- **Tier E (exploratory) is accessible but requires labelling every result as exploratory** and a "Limitations of Exploratory Inference" section. The current manuscript partially satisfies this through §8 but does not have the explicit exploratory-inference section, and the H1–H3 framing in §1.2 reads confirmatory.
- **Tier M (methods/engineering) is the natural fit:** the substantive contribution is the validation methodology itself (the probe-instrument finding, the multi-layer rescue pattern, the empirical vector-level reproduction of H × Dark-Triad coupling), with the H1–H3 results as exploratory secondary findings that motivate and validate the methodology. The Tier-M checklist does not require pre-registration; the methodology specification, evaluation protocol, and reproducibility-bundle requirements take its place.

The tier assignment for this publication is **Tier M with secondary exploratory findings**. Gate-6 internal review will verify this assignment against the checklist.

## 6. No protocol deviations during execution

Within the bounds of what was pre-specified in the build notes:
- The probe libraries were authored before any judge run and not modified after seeing results.
- The blind-rater rubrics were authored before any judge run and not modified after seeing results.
- The multi-layer steering configuration (L12/16/20, |c| ≤ 2) was applied uniformly to all 24 channels.
- The c = 4 diagnostic on psychopathy and sadism was named in advance as an RLHF-resistance test.
- The κ ≥ 0.60 PASS gate was applied uniformly.

No within-execution deviations from the pre-specified protocol have been identified.

## 7. Future Tier-C work

The Roadmap document (ROADMAP_TO_TOP_VENUES.md §"Recommended sequencing", item 1) commits to pre-registering the *next* validation run (cross-model replication on Llama-3.1-8B) on OSF or AsPredicted before any data collection. That pre-registration will be the unit's first proper Gate-3 artifact for this line of research, and a subsequent Tier-C upgrade of these findings on the new model is the path forward.

---

**Signed:** R. Weakley
**Date:** 2026-05-24
**Status:** draft awaiting Gate-6 review counter-signature
