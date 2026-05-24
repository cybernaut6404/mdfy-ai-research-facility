# AI-Use Disclosure — [PUBLICATION TITLE]

**Disclosure tier (per AI_USE_POLICY.md):** [1 / 2 / 3 / 4]
**Date:** [YYYY-MM-DD]

---

## Disclosure paragraph as it appears in the manuscript

> *AI Assistance.* This work used [AI SYSTEM, MODEL VERSION] from [START DATE] to [END DATE] to assist with [OPERATIONS]. The full archive of prompts and substantive outputs is deposited at [ZENODO DOI]. [HUMAN AUTHOR] reviewed all AI-generated content and is accountable for its accuracy. No AI system is listed as an author of this work; the ICMJE authorship criteria require accountability that AI systems cannot bear.

## Internal review disclosure (where applicable)

> *Internal Review.* Internal review of this manuscript against the unit's tier-specific standards was performed by [AI SYSTEM, MODEL VERSION] under the structured review prompt at `templates/internal-review-prompt_v1.md` and counter-signed by [HUMAN REVIEWER]. This arrangement reflects v0 of the unit's governance and is acknowledged as a limitation; see Charter §16.

## Tier 4 accountability statement (where applicable)

Tier 4 disclosure (per `AI_USE_POLICY.md`) requires an explicit per-element accountability statement for each AI-originated intellectual contribution that the human author elected to accept into the work. Use this block once per AI-originated element; omit the section entirely for Tier 1/2/3 work.

> *Tier 4 accountability.* The following intellectual contributions in this manuscript were originated by [AI SYSTEM, MODEL VERSION] and were not specified by the human author in advance. The named human author has reviewed each, endorses each as their own published claim, and takes accountability for it under ICMJE authorship criterion 4.
>
> | Element | Where it appears | Originated by | Accepted by (human author) |
> |---------|------------------|---------------|----------------------------|
> | [hypothesis / interpretation / framing / methodological choice] | [§/page] | Claude [model] | [NAME] |

---

## AI use record (not for publication; for the unit's archive)

### Systems used

| AI system | Provider | Model version | Period of use | Operations |
|-----------|----------|---------------|---------------|------------|
| Claude    | Anthropic | [VERSION]    | [DATES]       | [OPS]      |

### Prompting strategy

Brief description of the prompting approach (zero-shot / few-shot / chain-of-thought / iterative refinement / structured-output / etc.) and any custom system prompts or instructions.

### Materials shaped by AI

List each manuscript section, figure, table, analysis, or code module where AI made a non-trivial contribution. For each: the AI's contribution in one sentence, and the human author who reviewed and approved it.

### Prompt archive

The complete prompt archive is in this folder as `prompts/` (one transcript per session, in chronological order). Any redactions are recorded in `prompts/REDACTIONS.md` with rationale.

### Sign-off

- Human author accountable for AI-contributed content: [NAME], [DATE]
- Internal reviewer: [NAME or "Claude (model) counter-signed by Rick Weakley"], [DATE]
