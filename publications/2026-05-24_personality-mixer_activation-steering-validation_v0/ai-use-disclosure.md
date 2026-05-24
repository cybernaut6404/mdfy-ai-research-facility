# AI-Use Disclosure — 24-Channel Activation-Steering Validation (personality-mixer)

**Disclosure tier (per AI_USE_POLICY.md):** 3 (analytical / methodological contribution) with a **Tier 4 (substantial generation)** uplift for the per-element intellectual contributions enumerated in §3 below.
**Date:** 2026-05-24
**Publication:** *A 24-Channel Activation-Steering Substrate for Personality Constructs in a Large Language Model: Single-Subject Validation, Methodological Findings, and a Roadmap to Multi-Subject Replication.*
**Status:** Pre-submission draft; this disclosure is the canonical record for the unit's archive and will be reproduced (in part) in the manuscript itself before any submission.

---

## 1. Disclosure paragraph as it appears in the manuscript

> *AI Assistance.* This work used Anthropic's Claude (model: `claude-opus-4-7-1m` for manuscript drafting and judging; model `claude-opus-4-6` for an earlier portion of the validation runs) between 2026-05-23 and 2026-05-24. Claude contributed to: (i) blind-rater judging of every steered/unsteered response pair underlying the κ values in §3 (Tier 3 — execution of human-specified rubrics); (ii) drafting of every section of this manuscript and the supplementary tables from validation outputs and judge reports (Tier 3 — execution of human-specified structure); and (iii) origination of the three "methodological findings" framings (§4.1–§4.3), the "RLHF-floor" interpretation of the sadism null (§3.5, §4.4), the four-tier publication-venue roadmap structure (ROADMAP_TO_TOP_VENUES.md), and the comparative-claim verbs throughout §3–§5 (Tier 4 — intellectual origination accepted by the human author). The full archive of prompts and substantive AI outputs is deposited at [ZENODO DOI — to be minted at preprint posting]. R. Weakley reviewed all AI-generated content, originated the research questions and experimental design, took every gating decision on protocol and policy, and is accountable for the accuracy and appropriateness of all content in the manuscript. No AI system is listed as an author; the ICMJE authorship criteria require accountability that AI systems cannot bear.

> *Internal Review.* Internal review of this manuscript against the unit's tier-specific standards was performed by Anthropic's Claude (model: `claude-opus-4-7-1m`) under the structured review prompt at `templates/internal-review-prompt_v1.md` (mdfy-ai-research-facility v0.0.4-charter) and counter-signed by R. Weakley. This arrangement reflects v0 of the unit's governance and is acknowledged as a limitation; see CHARTER.md §16.

---

## 2. AI use record (for the unit's archive)

### 2.1 Systems used

| AI system | Provider | Model version | Period of use | Operations |
|-----------|----------|---------------|---------------|------------|
| Claude | Anthropic | `claude-opus-4-6` | 2026-05-23 → 2026-05-24 (early validation) | Blind-rater judging of paired completions for 9 of 24 channels under the original judge runs |
| Claude | Anthropic | `claude-opus-4-7-1m` | 2026-05-24 (later validation + drafting) | Blind-rater judging for the remaining 15 channels; manuscript drafting; supplementary tables drafting; roadmap document drafting; this disclosure drafted; will perform Gate-6 internal review |

Both model versions are calibrated against the same blind-rater rubrics committed verbatim to `mg-digital-twin/experiments/d4-fader-intervention/analyse.py::JUDGE_PROMPTS`. Inter-model rater agreement was not measured; the two models judged disjoint subsets of the 24 channels rather than the same set, so a direct agreement coefficient is not estimable from these runs.

### 2.2 Prompting strategy

**For judging:** structured-output forced-choice prompts. Each (high, low) response pair was submitted to the judge with a per-channel system prompt defining the trait's high and low poles operationally, plus a single forced-choice question of the form "Which response shows more {trait}? A, B, or TIE." Position (A vs. B) was randomised per pair via a fixed seed to control position bias. Rubrics were authored before any judge run, were not modified after seeing validation results, and are reproduced verbatim in SUPPLEMENTARY_TABLES.md (Table S6). Permissive parsing fell back to TIE on unparseable output.

**For drafting:** iterative refinement in a Cowork session. The author supplied: the substrate-paper findings; the new validation outputs; a target rigour bar ("highest-standard methodology + honest limitations + roadmap-to-those-venues"); and section-by-section direction. Claude produced full drafts of each section; the author reviewed, requested revisions where claims drifted from evidence, and approved each section before it moved to the pack.

### 2.3 Materials shaped by AI

#### Tier 3 — execution of human-specified work

| Artifact | AI contribution | Human reviewer |
|----------|-----------------|----------------|
| All κ values in §3, Tables S1–S2 | Blind-rater judging per pre-authored rubrics | R. Weakley (reviewed every judge report; spot-checked individual ratings against the originating pairs) |
| MANUSCRIPT.md §1 (Introduction, §1.1 Prior work, §1.2 Hypotheses) | Initial draft from author's notes on the substrate paper and prior literature | R. Weakley |
| MANUSCRIPT.md §2 (Methods) | Drafted from validation harness code and the work log | R. Weakley |
| MANUSCRIPT.md §3 (Results) | Drafted from judge reports and bias_tests artifacts | R. Weakley |
| MANUSCRIPT.md §5 (Comparison to prior work), §6 (Operational implications), §7 (Code, data, reproducibility), §8 (Limitations) | Drafted from author-supplied positioning and limitation list | R. Weakley |
| SUPPLEMENTARY_TABLES.md S1–S7 | Tables compiled from results artifacts | R. Weakley |
| README.md (this pack's README) | Drafted from pack provenance | R. Weakley |
| WORK_LOG.md | Drafted from session-by-session work record | R. Weakley |

#### Tier 4 — intellectual origination accepted by the human author

For each element below, R. Weakley reviewed the AI-originated content, endorses it as his own published claim, and takes accountability under ICMJE authorship criterion 4. Per AI_USE_POLICY.md §"Tier 4 — Substantial generation (intellectual origination)":

| Element | Where it appears | Originated by | Accepted by (human author) |
|---------|------------------|---------------|----------------------------|
| The three "methodological findings" framing: "Probe-instrument is decisive" (§4.1) | MANUSCRIPT.md §4.1; ABSTRACT; CONCLUSIONS | Claude `claude-opus-4-7-1m` (proposed this framing while drafting §4 from the raw probe-comparison results) | R. Weakley |
| "Multi-layer is consistently stronger than single-layer" (§4.2) | MANUSCRIPT.md §4.2; ABSTRACT | Claude `claude-opus-4-7-1m` (synthesised the three-of-four-rescue + openness-pass results into this generalisation) | R. Weakley |
| "The vector basis is psychometrically coherent" (§4.3) | MANUSCRIPT.md §4.3; CONCLUSIONS | Claude `claude-opus-4-7-1m` (proposed the construct-validity framing for the −0.32 H × Dark-Triad cosine) | R. Weakley |
| "RLHF-floor" interpretation of the sadism null (§3.5, §4.4) | MANUSCRIPT.md §3.5; §4.4 | Claude `claude-opus-4-7-1m` (proposed the "positive safety finding rather than broken vector" interpretation) | R. Weakley |
| Four-tier publication-venue roadmap (Tier 1: arXiv/TMLR/BRM; Tier 2: Psych Bulletin; Tier 3: Psych Review; Tier 4: World Psych/Lancet Psych) and the R1–R7 requirement enumeration | ROADMAP_TO_TOP_VENUES.md | Claude `claude-opus-4-7-1m` (originated the tier structure and requirement enumeration) | R. Weakley |
| The "overturns the substrate paper's 'may not be steerable' caveat" verb choice for openness | MANUSCRIPT.md §3.4; §4.2; SUPPLEMENTARY_TABLES.md S1 | Claude `claude-opus-4-7-1m` (chose "overturns" rather than "challenges" or "provides counter-evidence to") | R. Weakley — **flagged for calibration**: per the drafting LLM's own self-critique, "overturns" overstates what one channel result supports; recommended revision to "challenges" before any external submission |

### 2.4 Prompt archive

The complete prompt-and-output transcripts for the sessions that produced this pack live in the Cowork interface (Cowork-side artifact, not directly retrievable from this archive at the time of writing). Per CHARTER §10's transcript-mirror procedure (introduced in v0.0.4-charter), this work is a **publication-touching session**, so the full prompt archive must be committed alongside this disclosure before external submission. The archive is to be deposited at `prompts/` in this folder and at Zenodo with the rest of the reproducibility bundle.

**Status:** prompt archive **not yet deposited.** Required before arXiv preprint posting per AI_USE_POLICY.md §"Archive requirements." The archive includes every session that materially shaped the published work, in chronological order, with the AI's response, in a form a third party could inspect. Any redactions (e.g. operational secrets like Supabase credentials) are documented in `prompts/REDACTIONS.md` with rationale.

### 2.5 Sign-off

- **Human author accountable for AI-contributed content:** R. Weakley, 2026-05-24
- **Internal reviewer:** Claude `claude-opus-4-7-1m` under `templates/internal-review-prompt_v1.md`, counter-signed by R. Weakley — *Gate 6 in progress at the time of this disclosure draft; counter-signature will follow on a subsequent commit*

---

## 3. Notes for the Gate-6 reviewer

When reviewing this disclosure against the actual AI involvement (per v1 prompt §4 "AI-use disclosure completeness"), please verify:

1. The Tier 3 vs. Tier 4 distinctions above are calibrated correctly under the direction-of-intellectual-origin test (AI_USE_POLICY.md v0.0.4): the test is *who decided the content,* not how large the contribution.
2. The Tier 4 enumeration is complete relative to the manuscript's actual content. If you find an intellectual contribution in the manuscript that originated with Claude and is not enumerated above, flag it.
3. The "overturns" calibration flag (§2.3, last row) is consistent with the manuscript's actual wording. If the manuscript has been revised since this disclosure was drafted, the flag may be resolved or moved.
4. The prompt-archive deposition status (§2.4) is unresolved. This is a known gap that must close before external submission. Flag it as a Gate-7 (reproducibility-bundle finalisation) blocker.
