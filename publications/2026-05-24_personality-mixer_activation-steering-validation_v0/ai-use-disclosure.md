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
| MANUSCRIPT.md §1 (Introduction, §1.1 Prior work, §1.2 Expectations) | Initial draft from author's notes on the substrate paper and prior literature; v1 revision per Gate-6 §3 reframing hypotheses as exploratory expectations | R. Weakley |
| MANUSCRIPT.md §2 (Methods) | Drafted from validation harness code and the work log; v1 revision per Gate-6 §8 added dual-judge disclosure (§2.6), κ-gate justification (§2.4), orthogonalisation-scope clarification (§2.7), and QC-probe-count convention (§2.5) | R. Weakley |
| MANUSCRIPT.md §3 (Results) | Drafted from judge reports and bias_tests artifacts; v1 revision per Gate-6 §2 added sadism alternative-explanations paragraph (§3.5) and softened the honesty_humility cosine prose (§3.7) | R. Weakley |
| MANUSCRIPT.md §4 (Discussion) | Drafted; v1 revision per Gate-6 §2 softened "decisive"/"universally adopt"/"empirical confirmation" language and added the Broader Impacts subsection (§4.6) per Gate-6 §6 | R. Weakley |
| MANUSCRIPT.md §5 (Comparison to prior work), §6 (Operational implications), §7 (Code, data, reproducibility), §8 (Limitations) | Drafted from author-supplied positioning and limitation list; v1 revision per Gate-6 §9 reconciled the operational-research-tooling claim (§6) with the commercial-product COI disclosure | R. Weakley |
| SUPPLEMENTARY_TABLES.md S1–S7 | Tables compiled from results artifacts; v1 revision per Gate-6 §2 changed Table S1 row 9 "overturns" → "challenges" and softened Table S3 narrative | R. Weakley |
| README.md (this pack's README) | Drafted from pack provenance | R. Weakley |
| WORK_LOG.md | Drafted from session-by-session work record | R. Weakley |
| `deviations.md` | Drafted at unit-intake (2026-05-24 afternoon session) as the formal disclosure of the pre-registration gap that pre-dates unit adoption | R. Weakley |
| `coi-disclosure_weakley.md` | Drafted at unit-intake from ICMJE conventions and the unit's CHARTER §12 / README standing-tooling-disclosure framework | R. Weakley |
| `neurips-checklist.md` | Drafted at unit-intake against the NeurIPS Paper Checklist Guidelines (Tier-M ML compliance) | R. Weakley |
| `reproducibility-bundle/PROVENANCE.md` | Drafted at unit-intake as the chain-of-derivation document linking every headline claim to a producing script + pinned SHA | R. Weakley |
| `reproducibility-bundle/replication-log.md` | Drafted at unit-intake as the honest "not yet end-to-end run" disclosure with closure-path enumeration | R. Weakley |
| `reproducibility-bundle/code/README.md` | Drafted at unit-intake as a pointer to the five source repos at pinned SHAs, with three Gate-7 closure options enumerated | R. Weakley |
| `reproducibility-bundle/data/README.md` | Drafted at unit-intake as a pointer to data artifacts plus PII / sensitivity analysis | R. Weakley |
| `reproducibility-bundle/README.md` | Drafted at unit-intake with per-item compliance table against the unit's `templates/reproducibility-bundle_CHECKLIST.md` | R. Weakley |
| `reproducibility-bundle/Makefile` (stub) | Drafted at unit-intake as a walk-the-operator stub until Gate-7 finalisation | R. Weakley |
| `reproducibility-bundle/environment.yml` | Drafted at unit-intake with top-level deps pinned and transitive-lockfile TODO marker | R. Weakley |
| `reproducibility-bundle/seeds.json` | Drafted at unit-intake with decoding params and randomisation seeds; three TODO markers for values requiring source-repo access | R. Weakley |
| `correspondence/README.md` | Drafted at unit-intake as an empty-placeholder with naming convention for future submission correspondence | R. Weakley |
| `Makefile` (publication-folder manuscript-render) | Drafted by the Cowork-session Claude in 2026-05-24 morning; cleaned of mojibake-sed scaffolding at unit-intake | R. Weakley |
| Pandoc-regenerated `.tex` / `.docx` / `.pdf` outputs | Tier-1 editorial (format conversion only) | R. Weakley |

#### Tier 4 — intellectual origination accepted by the human author

For each element below, R. Weakley reviewed the AI-originated content, endorses it as his own published claim, and takes accountability under ICMJE authorship criterion 4. Per AI_USE_POLICY.md §"Tier 4 — Substantial generation (intellectual origination)":

| Element | Where it appears | Originated by | Accepted by (human author) |
|---------|------------------|---------------|----------------------------|
| The three "methodological findings" framing: now softened to "Probe-instrument matters more than expected" (§4.1) | MANUSCRIPT.md §4.1; ABSTRACT; CONCLUSIONS | Claude `claude-opus-4-7-1m` (proposed this framing while drafting §4 from the raw probe-comparison results) | R. Weakley |
| Now softened to "Multi-layer outperformed single-layer in this study" (§4.2) | MANUSCRIPT.md §4.2; ABSTRACT | Claude `claude-opus-4-7-1m` (synthesised the three-of-four-rescue + openness-pass results into this generalisation) | R. Weakley |
| Now softened to "The vector basis is qualitatively psychometrically coherent" (§4.3) | MANUSCRIPT.md §4.3; CONCLUSIONS | Claude `claude-opus-4-7-1m` (proposed the construct-validity framing for the −0.32/−0.26 H × Dark-Triad cosines) | R. Weakley |
| Now framed as "candidate safety signal, with alternatives" interpretation of the sadism null (§3.5, §4.4) | MANUSCRIPT.md §3.5; §4.4 | Claude `claude-opus-4-7-1m` (proposed the "positive safety finding" framing; v1 revision broadened to enumerate four alternative interpretations) | R. Weakley |
| Four-tier publication-venue roadmap (Tier 1: arXiv/TMLR/BRM; Tier 2: Psych Bulletin; Tier 3: Psych Review; Tier 4: World Psych/Lancet Psych) and the R1–R7 requirement enumeration | ROADMAP_TO_TOP_VENUES.md | Claude `claude-opus-4-7-1m` (originated the tier structure and requirement enumeration) | R. Weakley |
| Now softened: "challenges" / "provides counter-evidence to" verb choice for openness (was "overturns" in v0; revised in v1 per Gate-6 §2) | MANUSCRIPT.md §3.4; §4.2; SUPPLEMENTARY_TABLES.md Table S1 row 9 | Claude `claude-opus-4-7-1m` (initially chose "overturns"; v1 revision changed to "challenges"/"provides counter-evidence to" per Gate-6) | R. Weakley |
| "Sycophancy sign-flip as a methodological reminder" framing AND its deployment-safety annotation (§4.5) | MANUSCRIPT.md §4.5 | Claude `claude-opus-4-7-1m` (proposed both the methodological-reminder framing and the v1-added deployment-safety risk annotation) | R. Weakley |
| The "multi-layer should be tested before declaring a channel un-steerable at single-layer" recommendation (§4.2) — softened from v0's "should arguably replace single-layer as the default" | MANUSCRIPT.md §4.2 | Claude `claude-opus-4-7-1m` (originated the procedural recommendation; v1 revision softened it from a universal-default claim to a study-conditional suggestion) | R. Weakley |
| "Publishable at a methods or ML venue under preprint conventions" editorial assessment | `reproducibility-bundle/README.md` §"How to read this status honestly" | Claude `claude-opus-4-7-1m` (proposed the publication-readiness judgement) | R. Weakley |
| Broader Impacts subsection content (§4.6) — positive impacts, negative impacts, mitigations-in-force, mitigations-not-yet-executed | MANUSCRIPT.md §4.6 (added in v1 revision per Gate-6 §6) | Claude `claude-opus-4-7-1m` (originated the dual-use framing, the four-bucket structure, and the specific mitigations enumeration) | R. Weakley |

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
