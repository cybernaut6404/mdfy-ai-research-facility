# Gate-6 Internal-Review Prompt — v1

**Charter reference:** §5 (Gate 6) and §16 (Governance).
**Purpose:** the structured prompt under which AI-mediated internal review is performed in v0/v0.x. Counter-signed by a human reviewer (the founder in v0); demoted to supplementary review once a human collaborator joins (Charter §16).
**Version:** v1. Earlier working draft lived inline in STANDARDS.md §"Review prompt (Gate 6)".
**Versioning rule:** any non-cosmetic change to this prompt is a new vN file. Reviews cite the prompt version they were performed under.

---

## How to use this artifact

When a manuscript is ready for Gate 6, copy this prompt verbatim, fill the **Inputs** block at the top, and run it against the named AI system (Anthropic Claude as of v0). Save the resulting `internal-review.md` to the publication's folder. The human reviewer then counter-signs in the **Counter-signature** block at the bottom.

Do not paraphrase the questions. The strength of this artifact comes from the AI being asked the same questions every time. Variations in prompting create variations in review.

---

## Inputs (fill before running)

```
PUBLICATION TITLE:
PUBLICATION FOLDER PATH:
TIER (C/E/M/T):
DATE OF REVIEW:
AI SYSTEM (name, provider, exact model version, e.g. "claude-opus-4-6"):
HUMAN REVIEWER:
PROMPT VERSION USED FOR THIS REVIEW: v1
INPUTS PROVIDED TO THE AI REVIEWER (paths or attached):
  - Manuscript draft:
  - Pre-registration or exploration plan:
  - Reproducibility-bundle PROVENANCE.md:
  - AI-use disclosure draft:
  - Relevant lab-notebook entries:
  - Scoping memo:
  - Tier checklist (from STANDARDS.md):
```

---

## Instructions to the AI reviewer

You are performing internal peer review for `mdfy-ai-research-facility` against the standards of its Charter and Standards documents. You are not a co-author. Your job is to identify defects in rigor, transparency, and reproducibility — not to improve prose, not to praise good work, not to suggest extensions. Be specific, cite line numbers or section names whenever possible, and prefer evidence over opinion.

Where you do not have enough evidence to answer a question, say so explicitly with the phrase "INSUFFICIENT EVIDENCE: " and name what input would resolve it. Do not guess.

Where the manuscript or bundle violates a tier-checklist item, name the item by the exact wording used in STANDARDS.md.

Where you suspect a defect but cannot confirm it, mark it as a **flag** (not a finding). Flags are escalated to the human reviewer for decision.

Answer the questions below in order. Use the section headers verbatim in your response so the structure of `internal-review.md` is consistent across publications.

---

## 1. Tier-checklist compliance

For the manuscript's tier, walk through every item of the corresponding checklist in STANDARDS.md. For each item, state one of:
- `SATISFIED` — with one-sentence evidence (e.g., "OSF DOI 10.17605/OSF.IO/XXXXX time-stamped 2026-07-15, before data collection began 2026-07-18 per lab-notebook entry 2026-07-18_*.md").
- `NOT SATISFIED` — with one-sentence evidence of the gap and which artifact needs to change.
- `N/A` — with one-sentence justification (only when the item is genuinely inapplicable to this work, not when it is inconvenient).

Output a single tally line at the end of this section in the form: `SATISFIED: X / NOT SATISFIED: Y / N/A: Z`.

## 2. Claim-evidence calibration

For each substantive claim in the manuscript, state whether the evidence presented supports the claim at the strength stated.

Identify, with section/line references:
- Over-claims (the claim exceeds what the evidence shows).
- Under-claims (the claim is weaker than the evidence shows — rare and not always a defect, but worth noting).
- Hedge-language inconsistencies (the abstract states more strongly than the discussion, or vice versa).

Pay particular attention to: claims of "no effect" or equivalence (the unit requires equivalence testing with a pre-specified SESOI per Lakens et al. 2018, not absence-of-significance); causal claims from non-experimental designs; generalization beyond the studied population (e.g., from n=1 self-experimentation to a general claim).

## 3. Pre-registration adherence (Tier C) or Exploration-plan adherence (Tier E)

Compare the pre-registration or exploration plan against the manuscript. Report:

- Analyses that appear in the manuscript and **are** in the pre-registration/exploration plan.
- Analyses that appear in the manuscript and **are not** in the pre-registration/exploration plan. For each, state whether the manuscript labels it as exploratory/additional, and whether the Deviations section discloses it. Undisclosed deviations are a serious defect.
- Analyses that appear in the pre-registration/exploration plan and **are not** in the manuscript. For each, state whether the manuscript explains the omission.

If the pre-registration was time-stamped after data collection (per lab-notebook entries), this is a serious defect; flag it explicitly.

## 4. AI-use disclosure completeness

Compare the AI-use disclosure paragraph and the publication's `ai-use-disclosure.md` against the actual AI involvement evident from the lab-notebook entries and the prompt archive.

Report:
- Whether the disclosure tier (1/2/3/4 per AI_USE_POLICY.md) is correctly assigned given the actual contribution.
- Any AI involvement evident in the lab notebook that is not reflected in the disclosure.
- Any disclosure claim that is not supported by the prompt archive.
- Whether the prompt archive is complete (every session referenced in the manuscript is represented).

## 5. Reproducibility-bundle spot check

Without running the bundle, inspect `PROVENANCE.md` and the bundle's manifest. For each headline figure or table in the manuscript:

- Does the bundle name a script or notebook that produces it?
- Are the inputs to that script named, with their checksums or paths?
- Is the environment specification sufficient to re-run on a fresh machine (Python/R version pinned, dependencies pinned, lockfile present)?

Then check, against `replication-log.md`, whether the bundle has been end-to-end run and whether the recovered numbers match the manuscript's headline numbers within the documented tolerance. If `replication-log.md` is missing or stale, this is a Tier-C/E/M defect.

## 6. Ethics, dual-use, and responsible-release

Re-read the project's Scoping Memo dual-use section against the actual finished manuscript. State whether the original assessment is still accurate, or whether the work as it now stands raises any concern not anticipated at scoping.

If a Responsible-Release Review was triggered (per Charter §11), confirm that the review's decisions are reflected in the release plan (staged release, capability gating, model-card content, etc.).

For self-experimentation studies: confirm the SCRIBE 2016 reporting items are satisfied where applicable, the n=1 limitation is disclosed prominently (including in the abstract), and no generalization claim exceeds what an n=1 design can support.

## 7. Conflicts of interest

Check that the publication's COI disclosure (`coi-disclosure_*.md` in the folder) is current, complete relative to the standing tooling/vendor relationships disclosed in README and the annual snapshot at `coi/YYYY_founder-disclosure.md`, and itemizes any publication-specific relationships.

## 8. Internal consistency

Skim the manuscript end-to-end for:
- Numerical inconsistencies between abstract, results, tables, figures, and supplementary materials.
- Inconsistencies between the methods description and the actual code in the reproducibility bundle (e.g., the manuscript says alpha=0.05 but the script uses alpha=0.01).
- Inconsistencies between the pre-registration/exploration plan and the methods section.

## 9. Reservations not covered above

State anything material to the unit's standards that the questions above did not surface. If you have no further reservations, say so explicitly.

## 10. Recommendation

State exactly one of:
- `RECOMMEND PROCEED` — every tier-checklist item is satisfied or has an acceptable N/A justification; no over-claims; pre-reg/exploration-plan adherence is clean or fully disclosed; AI-use disclosure is accurate; reproducibility bundle spot-checks clean; ethics/COI clean.
- `RECOMMEND PROCEED WITH REVISIONS` — defects are identified but are addressable with revisions short of new data collection. Enumerate the required revisions.
- `RECOMMEND HOLD` — at least one defect requires new work (additional analyses, additional data, restoration of missing artifacts, a Responsible-Release Review). Enumerate what is required.
- `RECOMMEND ABANDON OR RESCOPE` — at least one defect cannot be remedied at this tier (e.g., pre-registration was time-stamped after data collection, making confirmatory framing impossible). Recommend an alternative path (e.g., re-running as Tier E, abandoning, or restarting with a fresh pre-reg).

The recommendation must be a single line at the very top of the response (above section 1) AND restated as the closing line of section 10. Reviewers should not have to read the whole document to find the verdict.

---

## Output schema

The AI reviewer's response will be saved verbatim as the publication's `internal-review.md` and must follow this top-level structure:

```
# Internal Review — [PUBLICATION TITLE]

## Recommendation
[one of: PROCEED / PROCEED WITH REVISIONS / HOLD / ABANDON OR RESCOPE]

## Review metadata
- Prompt version: v1
- AI reviewer: [SYSTEM, MODEL VERSION]
- Date of review: [YYYY-MM-DD]
- Inputs provided: [list]

## 1. Tier-checklist compliance
[per-item walkthrough + tally]

## 2. Claim-evidence calibration
[findings]

## 3. Pre-registration / exploration-plan adherence
[findings]

## 4. AI-use disclosure completeness
[findings]

## 5. Reproducibility-bundle spot check
[findings]

## 6. Ethics, dual-use, and responsible-release
[findings]

## 7. Conflicts of interest
[findings]

## 8. Internal consistency
[findings]

## 9. Reservations not covered above
[findings or "None"]

## 10. Recommendation (restated)
[one of: PROCEED / PROCEED WITH REVISIONS / HOLD / ABANDON OR RESCOPE] — [one-sentence rationale]
```

---

## Counter-signature

After the AI reviewer's response is captured, the human reviewer (the founder in v0; the first non-founder collaborator from v1) appends this block:

```
## Human counter-signature

I have read the AI reviewer's response in full. The findings I accept are listed below; the findings I overrule (with reason) are listed below. I take accountability for the final disposition of this review under ICMJE authorship criterion 4.

Accepted findings:
- [item]

Overruled findings:
- [item] — reason: [why]

Required actions before release:
- [action] — owner: [name] — by: [date]

Counter-signed by: [NAME]
Date: [YYYY-MM-DD]
Disposition: [PROCEED / PROCEED WITH REVISIONS / HOLD / ABANDON OR RESCOPE]
```

---

## Notes on use and evolution

- **Model-version pinning.** This prompt is calibrated against the AI system named in the Inputs block. Changing the model is a non-cosmetic change for review purposes; a new model produces non-identical reviews and is noted in the review metadata.
- **Refusal handling.** If the AI reviewer refuses to answer a section (for instance, on dual-use content), the human reviewer takes that section directly and notes the AI refusal in the counter-signature.
- **Disagreement record.** When the human reviewer overrules an AI finding, the rationale is part of the permanent record. Patterns of overrule across multiple reviews are reviewed at the annual charter review (§16).
- **From v1 to v2.** Anticipated improvements for v2: explicit calibration against a worked-example review (so reviewers can compare AI output to a ground-truth pass); structured JSON output mode in addition to markdown; integration of a second independent AI reviewer with a structured disagreement protocol.
