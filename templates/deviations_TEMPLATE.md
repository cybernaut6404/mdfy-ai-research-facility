# Deviations from Pre-Registration — [PUBLICATION TITLE]

**Publication:** [TITLE]
**Tier:** [C / E / M / T]
**Date:** [YYYY-MM-DD]

> *Per STANDARDS.md: every Tier C and Tier E manuscript under the unit's standards ships with a Deviations section regardless of outcome. Tier M and Tier T publications include a deviations document if they had a Gate-3 plan (pre-registration or Exploration Plan); when no Gate-3 plan existed, this file explicitly documents the pre-registration gap (see §1 below).*

---

## 1. Pre-registration status

Choose the variant that applies:

**Variant A — Pre-registered (Tier C, Tier T meta-analysis):**

> The pre-registration for this study is committed to `preregistrations/[FILENAME]` and was time-stamped on OSF at [URL/DOI] on [DATE] before any data collection began on [DATE]. Time-stamp evidence: [OSF commit hash, AsPredicted PDF, or signed-and-dated commit in this unit's `preregistrations/` directory].

**Variant B — Exploration Plan (Tier E):**

> The Exploration Plan for this study is committed to `preregistrations/[FILENAME]` and was time-stamped via signed-and-dated commit in this unit's `preregistrations/` directory at [SHA] on [DATE] before any data collection began on [DATE]. Per STANDARDS.md, an Exploration Plan is the Tier-E counterpart to a Tier-C pre-registration and is acceptable for exploratory work.

**Variant C — No Gate-3 plan (work pre-dates unit adoption or is Tier M / Tier T without Gate-3 requirement):**

> No Gate-3 pre-registration or Exploration Plan was committed for this study. [WORK PRE-DATES THE UNIT'S ADOPTION OF PRE-REGISTRATION AS A HARD GATE / WORK IS TIER M METHODS WITHOUT GATE-3 REQUIREMENT / OTHER REASON]. This is a [STRUCTURAL UNFIXABLE GAP / INTENTIONAL PER TIER FRAMEWORK]. Under the unit's tier framework: Tier C is structurally inaccessible without a pre-registration; Tier E requires a time-stamped Exploration Plan that does not exist here; Tier M does not require pre-registration but does require the evaluation protocol to be specified before evaluation runs, which is documented in §2 below; Tier T meta-analyses require pre-registration on PROSPERO or OSF — not applicable here.

## 2. What was pre-specified (applies to all variants)

For Variants A/B, this section enumerates what the pre-registration / Exploration Plan committed in advance. For Variant C, this section enumerates what was committed in author-controlled records *before* the evaluation runs, with an honest assessment of why that evidence does not substitute for a pre-registration.

Items to enumerate:

- The hypotheses (or expectations, in Variant C) under test.
- The pre-specified PASS / FAIL gates.
- The probe libraries / contrastive items / experimental materials.
- The rubrics / coding schemes / scoring procedures (committed verbatim, not modified after evaluation).
- The configuration parameters (steering coefficients, model versions, etc.).
- The randomisation seeds.
- The threshold conventions.

For each item, cite the source-of-truth commit SHA where it was committed before any evaluation run.

## 3. Why pre-registration matters (Variant C only)

A timestamped private-build-note statement of expectations is **not** equivalent to a Gate-3 pre-registration. Reasons:

1. **No external time-stamp.** Private repository commits are not independently witnessable.
2. **No analysis-plan lock-in.** Analyser scripts may iterate during the evaluation period.
3. **No falsification criteria stated as such.** Pre-registrations require explicit conditions that would constitute disconfirmation.

State these honestly in the document. Do not equivocate.

## 4. Consequence for the manuscript framing

Variants A/B: enumerate any deviations of the manuscript's claims from what the pre-registration committed. Any analysis in the manuscript not in the pre-reg must be labelled exploratory and disclosed here. Any analysis in the pre-reg not in the manuscript must be explained.

Variant C: enumerate the framings in the manuscript that read as confirmatory (e.g., "H1 confirmed", "hypothesis tested") and recommend revisions to softened language (e.g., "expectation E1 consistent with the data", "consistent with").

## 5. Consequence for tier assignment

State the tier-framework consequence explicitly. For Variant C, this typically means: Tier C is off the table; Tier E is accessible only with strict exploratory labelling and a "Limitations of Exploratory Inference" section; Tier M is the natural fit if the substantive contribution is methodological rather than hypothesis-test.

## 6. Within-execution deviations (applies to all variants)

For each deviation from the pre-specified protocol that occurred during execution (e.g., a probe was added; a coefficient was adjusted; a channel was dropped), document:

- What was changed.
- When (with commit SHA).
- Why.
- What if anything was learned that motivated the change.

If no within-execution deviations occurred, state so explicitly.

## 7. Future work

For Variants A/B/C: name the next study that will close any gaps identified here. For Variant C specifically: commit to pre-registering the *next* validation run on OSF / AsPredicted / `preregistrations/` directory before any data collection.

---

**Signed:** [NAME]
**Date:** [YYYY-MM-DD]
**Status:** [draft awaiting Gate-6 review counter-signature / Gate-6 review complete / final]
