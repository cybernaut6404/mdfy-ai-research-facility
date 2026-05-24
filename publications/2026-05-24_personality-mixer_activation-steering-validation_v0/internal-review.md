# Internal Review — A 24-Channel Activation-Steering Substrate for Personality Constructs in a Large Language Model: Single-Subject Validation, Methodological Findings, and a Roadmap to Multi-Subject Replication

## Recommendation
PROCEED WITH REVISIONS

## Review metadata
- Prompt version: v1
- AI reviewer: Anthropic Claude, `claude-opus-4-7-1m`
- Date of review: 2026-05-24
- Inputs provided:
  - Manuscript draft: `publications/2026-05-24_personality-mixer_activation-steering-validation_v0/MANUSCRIPT.md`
  - Pre-registration / exploration plan: NONE on disk (see `deviations.md`)
  - Reproducibility-bundle PROVENANCE: `reproducibility-bundle/PROVENANCE.md`
  - AI-use disclosure: `ai-use-disclosure.md`
  - Lab-notebook entries: NONE for this paper
  - Scoping memo: NONE
  - Deviations document: `deviations.md`
  - COI disclosure: `coi-disclosure_weakley.md`
  - Supplementary tables: `SUPPLEMENTARY_TABLES.md`
  - Roadmap: `ROADMAP_TO_TOP_VENUES.md`
  - NeurIPS checklist: `neurips-checklist.md`
  - Reproducibility-bundle README: `reproducibility-bundle/README.md`
  - Bundle subordinates: `reproducibility-bundle/{code,data}/README.md`, `environment.yml`, `seeds.json`, `Makefile`, `replication-log.md`
  - Work log: `WORK_LOG.md`
  - Tier-M checklist: `STANDARDS.md` §"Tier M — Methods and engineering"
  - Charter §4, §6, §7, §9, §10, §16: `CHARTER.md`
  - AI Use Policy: `AI_USE_POLICY.md`
  - Canonical v1 review prompt: `templates/internal-review-prompt_v1.md`
  - Unit README "Dependencies & tooling disclosure" block

## 1. Tier-checklist compliance

Tier-M assignment first. The author asserts Tier M (with secondary exploratory findings). The work fits the Tier-M frame: the primary deliverable is a validation methodology and a 24-channel substrate; performance claims are present but bounded and stated as proof-of-concept. Tier C is structurally inaccessible (no time-stamped pre-registration, per `deviations.md` §1, §5). Tier E is accessible but requires every result to be labelled exploratory and a dedicated "Limitations of Exploratory Inference" section — currently absent. The Tier-M assignment is the natural fit and is confirmed for this review.

Tier-M checklist walkthrough (verbatim items from `STANDARDS.md` §"Tier M — Methods and engineering"):

- **"Written specification of what the tool/method does and what it explicitly does not do."** — SATISFIED. MANUSCRIPT §2.1–§2.7 specify the method (CAA extraction, ML L12/16/20 steering, |c| ≤ 2 ceiling, D4 directional-accuracy protocol, κ ≥ 0.60 gate), and §8.1–§8.8 explicitly enumerate eight categories of things the method does not do (single-subject, single-model, no human IRR, small probes, not pre-registered, greedy decoding only, coefficient ceiling, channel-set omissions).

- **"Test suite or validation procedure, runnable from the reproducibility bundle."** — NOT SATISFIED. A validation procedure exists in concept (the D4 directional-accuracy harness), but `reproducibility-bundle/Makefile` is a stub that prints walkthrough instructions rather than executing the pipeline; `reproducibility-bundle/code/` contains only a `README.md` pointer to private source repos at SHA `f492844` etc.; `reproducibility-bundle/data/` is also pointer-only; `replication-log.md` records zero end-to-end runs. The artifact needed to close this is either a vendored `code/` tree or pinned git-submodules plus a real `make replicate` target, plus at least one entry in `replication-log.md` from an end-to-end run.

- **"Evaluation protocol specified before evaluation runs; any subsequent change documented."** — NOT SATISFIED (with partial mitigation). `deviations.md` §2 lists the protocol elements specified before the runs (κ ≥ 0.60 gate, rubrics, probe libraries, multi-layer config, position-randomisation seed, refusal-cosine thresholds), and §3 candidly states why this falls short of pre-registration (no external time-stamp, no analysis-plan lock-in commit hash, no falsification criteria stated as such). For Tier-M strictness, "specified before evaluation runs" is partially evidenced by the build-note timestamps and JUDGE_PROMPTS dict claim, but the analyse.py script iterated during the validation period (`deviations.md` §3.2), and no commit-hash freeze of the analyser pre-dates unblinding. The artifact needed to close this is either (a) a retrospective audit identifying the analyse.py commit that pre-dated the first judge run, or (b) acceptance that this gate is structurally only loosely satisfied, with the deviations.md disclosure standing as the closure record.

- **"Reproducibility bundle satisfying the bundle checklist."** — NOT SATISFIED. `reproducibility-bundle/README.md` §"Reproducibility checklist compliance" itself tallies multiple `❌ pointer-only` and `❌ pending` rows: source code not in bundle, raw/processed data not in bundle, data licenses TODO, FAIR metadata TODO, prompts not archived, replication log empty, Zenodo DOI pending. This is the dominant Tier-M defect.

- **"AI-use disclosure paragraph drafted and reviewed."** — SATISFIED. `ai-use-disclosure.md` exists, contains the manuscript-embedded paragraph (§1), an itemised Tier 3 / Tier 4 record (§2.3), and a Gate-6-specific reviewer note (§3). Calibration of the Tier 3 vs Tier 4 boundary is audited under §4 of this review.

- **"Internal review (Gate 6) completed and signed."** — SATISFIED (in progress by virtue of this review). This document is the Gate-6 internal-review artifact; the human counter-signature block follows.

- **"Model Card (per Mitchell et al. 2019) committed per the reproducibility-bundle checklist's *Compliance artifacts* section (`model-card.md` in the publication folder), for any released model."** — N/A at this stage. Per `neurips-checklist.md` §11 and `reproducibility-bundle/README.md`, no model checkpoint is being released; only the steering vectors as derived artifacts, gated by access-on-request. If/when the vectors are publicly released (a Tier-2+ requirement), the Model Card becomes mandatory; the current publication does not trigger that gate. (Caveat: a strict reading of "any released model" could include the steering vectors as model-modifications; the manuscript should explicitly state that the v0 release is access-on-request to make the N/A justification load-bearing rather than implicit.)

- **"For benchmarks: clear statement of dataset provenance, license, and any contamination risk relative to large pretrained models."** — N/A. This is not a benchmark publication; the contrastive items and probes are evaluation materials for a method validation, not a benchmark dataset. Dataset-style provenance is nevertheless covered in PROVENANCE.md §"Inputs" and the licensing section.

**Tally:** SATISFIED: 3 / NOT SATISFIED: 3 / N/A: 2

## 2. Claim-evidence calibration

The manuscript is unusually candid; §8 quantifies eight categories of limitation, and the abstract names the n=1 / single-model / single-judge / small-probe / non-pre-registered limitations in a dedicated paragraph. Even so, several calibration defects are present.

**Over-claims:**

- **§3.4, SUPPLEMENTARY_TABLES.md Table S1 row 9, manuscript §4.2:** The verb "overturns" applied to the substrate paper's "may not be steerable" caveat for openness. This is identified by `ai-use-disclosure.md` §2.3 (last row) as a Tier-4 AI-originated framing flagged for revision, and `deviations.md` §4 quotes the drafting LLM's self-critique: "'overturns' overstates what one channel result supports." Confirmed over-claim. One channel reaching κ = 0.750 on 12 directional probes from a single subject's contrastive items, judged by a single LLM judge, on a single model, with no pre-registration, does not overturn a prior claim — it provides counter-evidence at most. Revision required: replace "overturns" with "provides counter-evidence to" or "challenges" in all three locations.

- **§1.2 "Hypotheses":** "We pre-specified three hypotheses, in the sense of 'stated in the build notes before the validation runs', though we did NOT formally pre-register (see §8.2)." The framing labels H1–H3 as "hypotheses" and §3.2/§3.3 headings then write "H2 confirmed" and "H1 confirmed." `deviations.md` §3 names the three reasons this is not equivalent to pre-registration (no external time-stamp, no analysis-plan lock-in, no falsification criteria), and §4 recommends reframing to "expectations stated in build notes before validation, presented here as exploratory findings rather than confirmatory tests" with "confirmed" replaced by "consistent with" or "supports." Confirmed over-claim; the Intro reads confirmatory under Tier-C conventions while the work is structurally Tier M / exploratory. Revision required.

- **Abstract, third paragraph ("Three methodological findings stand out: (i) generic discriminability probes systematically false-zero dark-trait validation…"):** The word "systematically" is doing strong work on a finding derived from four channels (the Dark Tetrad), with the strongest result driven by two of them (machiavellianism, narcissism). The pattern is striking and the finding is plausible, but "systematically" implies a level of generality the four-channel dataset does not establish. Suggested revision: "across the four Dark Tetrad channels" or "for the dark-trait channels in this study" qualifier.

- **§4.4, abstract "Limitations" paragraph:** The sadism null is framed as "consistent with strong base-RLHF refusal of sadistic content." This is a reasonable interpretation but is not the only one; alternatives (the contrastive items poorly captured the trait, the trait-eliciting probes still under-elicited, the vector polarity is flipped as it was for sycophancy, or judge-rubric ambiguity on sadism) are not discussed in §3.5 and only the RLHF interpretation is advanced in §4.4 ("a positive safety finding"). For a publishable safety claim about a specific model's robustness, the alternative explanations need explicit ruling-out (or, at minimum, explicit acknowledgement that they remain plausible). Revision recommended: add a one-paragraph alternative-explanations subsection under §3.5.

- **§3.7 / §4.3:** The H × Dark-Triad cosine of −0.32 at L16 is described as "empirical confirmation of the HEXACO H × Dark-Triad coupling at the vector level" and "matches the published psychometric literature." The supplementary table S3 notes the magnitude is "attenuated relative to the psychometric correlation" (vector −0.32 vs literature −0.55 to −0.65). The qualitative direction matches; the magnitude does not. "Confirmation" / "matches" is over-strong; "qualitatively consistent with" or "directionally consistent with" would better calibrate the claim. Revision recommended.

**Under-claims:** None material; the manuscript is generally candid.

**Hedge-language inconsistencies:**

- **Abstract → Discussion:** The abstract uses "matching the published psychometric literature (r ≈ −0.55 to −0.65)" for the vector-level −0.32; the supplementary tables explicitly note the attenuation. The abstract reads stronger than the supplementary tables. Bring the abstract into alignment with Table S3's "attenuated relative to" framing.

- **Abstract → §3.5:** Abstract: "Sadism scored 0.000 at every tested coefficient (0/16 wins both directions at c=4), consistent with strong base-RLHF refusal." §3.5 keeps the same framing. §4.4 escalates to "A base-instruction-tuned model that produces *indistinguishable* outputs … is exhibiting durable RLHF robustness on this trait. This is itself a publishable safety result." The escalation across sections without new evidence is the canonical hedge inconsistency pattern.

**Claims supported by the evidence at the strength stated** (positive confirmations):

- The 20-of-24 PASS rate at the uniform recipe is supported by the per-channel κ values in Table S1 and `runs/*/results.json`.
- The probe-instrument finding (κ = 0.000 generic vs κ = 0.857–1.000 trait-eliciting) is directly observable in the §3.2 table.
- The multi-layer rescue (3/4) is supported by the §3.3 table.
- The refusal-cosine SAFE/watch/FLAG summary is supported by Table S2.
- The QC-probes-passed claim (§3.8) is asserted but is the result of manual inspection; this is a flag for §5 below.

**Equivalence / "no effect" claims:** The sadism finding is, in effect, an equivalence-style claim ("the model produced *indistinguishable* outputs"). The unit's standard (per the v1 prompt §2) requires equivalence testing with a pre-specified SESOI for equivalence claims. None is reported. Either reframe the sadism finding as "directional-accuracy zero under all tested conditions" (a description, not an equivalence claim) and drop "indistinguishable," OR add an equivalence test with a SESOI. Revision required.

## 3. Pre-registration / exploration-plan adherence

**Structural finding:** No Gate-3 pre-registration or Exploration Plan exists for this work. `deviations.md` §1 states this explicitly: "No Gate-3 pre-registration or Exploration Plan was committed to this unit's `preregistrations/` directory, OSF, or AsPredicted before any data collection or judge run for this study." The unit's `preregistrations/` directory is empty (confirmed by `ls`). The work pre-dates the unit's adoption of pre-registration as a hard gate (v0.0.3-charter on 2026-05-24, the same day the publication pack was assembled).

Per the v1 prompt §3, "If the pre-registration was time-stamped after data collection (per lab-notebook entries), this is a serious defect; flag it explicitly." The situation here is one step worse: the pre-registration does not exist at all. Under the unit's tier framework, this rules out Tier C (confirmed by `deviations.md` §5), is incompatible with strict Tier E adherence (Tier E requires an Exploration Plan time-stamped before data collection), and is compatible with Tier M (which does not require pre-registration but does require the evaluation protocol to be specified before evaluation runs — see §1, Tier-M item 3).

**Analyses in the manuscript not in any pre-registration:** All of §3, since no pre-registration exists. The manuscript itself partially discloses this (§8.5), and `deviations.md` is the formal record. What remains undisclosed inside the manuscript:

- The H1–H3 framing in §1.2 reads confirmatory; the labels "H1 confirmed" / "H2 confirmed" in §3.2 / §3.3 headings carry the same problem. `deviations.md` §4 already recommends the revision; this Gate-6 finding adopts that recommendation as a required revision before any external submission.
- §3 currently does not have a per-result label of "exploratory" (as Tier E would require). Tier-M does not require this, but to make the §1.2 "exploratory secondary findings" framing honest, §3.2 and §3.3 should add an explicit "exploratory finding" annotation at minimum.

**Analyses in the pre-registration not in the manuscript:** N/A — no pre-registration.

**Time-stamping defect:** A more serious version of the v1-prompt's "time-stamped after data collection" defect is present: there is no time-stamp at all. The build-note timestamps in `mg-GSTACK/docs/audits/personality-mixer-audit-2026-05-23.md` (cited in `deviations.md` §2) are in author-controlled private repositories with no external witness; per the drafting LLM's own self-critique quoted in `deviations.md` §4, "if you didn't OSF-timestamp them, they're post-hoc framing — even if you mean well."

**Future commitment:** ROADMAP_TO_TOP_VENUES.md §"Recommended sequencing" item 1 and `deviations.md` §7 both commit to pre-registering the *next* validation run (cross-model replication on Llama-3.1-8B) on OSF or AsPredicted before any data collection. This is the correct closure for the gap going forward; it does not close it retroactively for this manuscript.

**Gate-6 finding:** the §1.2 confirmatory framing must be reworked before any external submission. `deviations.md` already provides the recommended revision text; the manuscript needs to land it.

## 4. AI-use disclosure completeness

`ai-use-disclosure.md` is unusually thorough for v0; the Tier 3 vs Tier 4 split is itemised at §2.3, and §3 explicitly invites the Gate-6 reviewer to audit the calibration. Audit findings:

**Tier assignment under the v0.0.4 direction-of-intellectual-origin test:** The disclosure assigns Tier 3 with a Tier 4 uplift for specific intellectual contributions. Per `AI_USE_POLICY.md` §"Tier 4 — Substantial generation (intellectual origination)": "The test that distinguishes Tier 4 from Tier 3 is *direction of intellectual origin*, not size of contribution." The Tier-4 items enumerated at `ai-use-disclosure.md` §2.3 (the three methodological-findings framings; the RLHF-floor interpretation; the four-tier roadmap structure; the "overturns" verb choice) are all defensibly direction-of-origin Tier 4. The Tier-3 items (κ-value judging, drafting of all manuscript sections from author-supplied notes and the validation outputs) are likewise direction-of-origin Tier 3 (the author decided what to analyse and what arguments to make; Claude implemented). **Calibration assessment: correct.**

**Additional Tier-4 candidates not enumerated:** Reading the manuscript against the disclosure, I flag the following as potentially Tier-4-origin material that should be either added to the §2.3 enumeration or explicitly endorsed by the human author as not-AI-originated:

- The "RLHF-floor" framing is already enumerated, good. But the *related* "publishable safety result" verb choice in §4.4 ("This is itself a publishable safety result and merits replication on other safety-trained models") goes a step further than the RLHF-floor interpretation and is plausibly AI-originated. Either fold into the existing entry or add as a separate sub-item.
- The "sycophancy sign-flip as a methodological reminder" framing (§4.5) and the "we recommend a 2-probe sign-validation step after any new extraction" recommendation read as AI-originated procedural prescription. Not enumerated. Flag for either inclusion or explicit not-AI-origin assertion.
- The "the multi-layer ML L12/16/20 c=2 recipe should arguably replace single-layer as the default validation configuration in this literature" verb choice in §4.2 is a literature-level prescriptive claim that the author would not have produced unaided in this form. Plausibly Tier-4-origin. Not enumerated.
- The "publishable AT A METHODS / ML VENUE under preprint conventions" assessment in `reproducibility-bundle/README.md` §"How to read this status honestly" is an editorial judgement about the work's publication readiness. Plausibly AI-originated. Not enumerated for that file; should be either consolidated into the manuscript's §9 (which is already enumerated as Tier 4 via the roadmap entry) or noted.

**AI involvement evident in the lab notebook / work log not reflected in the disclosure:** WORK_LOG.md describes Claude as "assistant: Claude (Opus 4.7)" throughout. WORK_LOG.md §10 ("Phase 10 — Publication pack assembly") records that the manuscript, supplementary tables, roadmap, README, and Makefile-pandoc tooling were produced in this session. The disclosure's §2.3 Tier-3 table itemises MANUSCRIPT §1–§8, SUPPLEMENTARY_TABLES.md S1–S7, README, and WORK_LOG.md, but does *not* itemise:
- The `Makefile` (pandoc-conversion target) — minor, plausibly Tier-1 editorial.
- The pandoc-derived `.tex` / `.docx` / `.pdf` regenerated artifacts — Tier-1 editorial.
- The `deviations.md` document itself — this is plausibly Tier-3 (executed under human direction) and should be enumerated to be complete.
- The `coi-disclosure_weakley.md` document — likewise plausibly Tier-3, not enumerated.
- This very `internal-review.md` — explicitly noted in §2.5 as "Gate 6 in progress at the time of this disclosure draft."
- The `neurips-checklist.md` — produced under the Gate-6 workflow per its footer ("Completed by: Claude (`claude-opus-4-7-1m`)"). Not in the §2.3 Tier-3 table.

Recommendation: extend the §2.3 Tier-3 table with rows for `deviations.md`, `coi-disclosure_weakley.md`, `neurips-checklist.md`, and the bundle's `PROVENANCE.md` + `replication-log.md` + `code/README.md` + `data/README.md`. This is a completeness fix, not a substantive change in disclosure tier.

**Prompt-archive deposition status:** `ai-use-disclosure.md` §2.4 explicitly flags this as "prompt archive **not yet deposited**" and names it as a "Gate-7 (reproducibility-bundle finalisation) blocker for external submission." Per `AI_USE_POLICY.md` §"Archive requirements," the archive is required for every Tier 3 and Tier 4 publication. **Gate-6 finding: the prompt-archive deposition is a hard prerequisite for any external (arXiv or otherwise) release.** The current disclosure correctly self-identifies the gap; the gap itself remains open.

**Internal Review disclosure paragraph** (`ai-use-disclosure.md` §1, second paragraph): correctly written, names the model and the prompt-version artifact, names the human counter-signer, names CHARTER §16 as the limitation acknowledgement. Acceptable.

**Cross-model judge agreement caveat:** `ai-use-disclosure.md` §2.1 candidly notes that two judge model versions (claude-opus-4-6 and claude-opus-4-7-1m) were used across disjoint subsets of the 24 channels and that "inter-model rater agreement was not measured." This is a methodological limitation that is consistent with manuscript §8.3 but is **not** explicitly mentioned in the manuscript itself. The manuscript names only "Claude Opus 4.7" in §2.6, eliding the fact that 9 of 24 channels were judged by the prior model version. Revision required: §2.6 should disclose that two judge-model versions were used across disjoint subsets, with a one-sentence acknowledgement that inter-model judge agreement was not measured.

## 5. Reproducibility-bundle spot check

Spot-check against PROVENANCE.md and the bundle's manifest, for each headline result:

| Manuscript artifact | Bundle script named? | Inputs named with paths/checksums? | Environment spec sufficient? |
|---|---|---|---|
| §3.1 "20 of 24 channels achieved κ ≥ 0.60" | YES (`mg-digital-twin/experiments/d4-fader-intervention/analyse.py` at SHA `f492844`) | Partial — paths named, no checksums for `vector.pt` files in bundle (the SHA-256 lives in `personality-central-db.catalog.channels.steering_vector_ref`, not mirrored into the bundle) | NO — `environment.yml` lists top-level deps but does not pin transitive deps; `seeds.json` has TODOs for HuggingFace revision SHA, judge temperature, and position-randomisation seed |
| §3.2 probe-instrument finding | YES (same `analyse.py` against two probe sets) | Paths named, no checksums | Same gaps |
| §3.3 multi-layer rescue | YES (`analyse.py` against two configs) | Paths named, no checksums | Same gaps |
| §3.4 new-channel scorecard | YES (`analyse.py`) | Paths named, no checksums | Same gaps |
| §3.5 sadism RLHF-floor; sycophancy sign-flip | YES (`analyse.py` for sadism c=2 and c=4, sycophancy at c=2) | Paths named, no checksums | Same gaps |
| §3.6 refusal-direction cosine | YES (`infra/steering-vectors/cosine_probe.py`) | Paths named, no checksums | Same gaps |
| §3.7 inter-channel cosines, H × Dark-Triad coupling | YES (`infra/steering-vectors/inter_channel_cosines.py`) | Paths named, no checksums | Same gaps |
| §3.8 QC probes passed | NO — PROVENANCE.md explicitly notes this is via "Manual inspection of the `_QC` rows" — there is no script. This is the only manual step in the validation. | N/A | N/A |
| Table S2 refusal-direction cosine | YES (`cosine_probe.py`) | Paths named | Same gaps |
| Table S3 inter-channel cosines | YES (`inter_channel_cosines.py`) | Paths named | Same gaps |
| Table S4 orthogonalisation | YES (`orthogonalise.py`) | Paths named | Same gaps |

**Replication-log check:** `reproducibility-bundle/replication-log.md` records **zero end-to-end runs**: "The bundle has not yet been run end-to-end on a fresh machine from this folder." The log is candid about this and lists the six blockers to a real end-to-end run (lift HuggingFace revision SHA, lift judge seed, vendor/submodule source repos, pre-populate published-results.json, implement real `make replicate`, run end-to-end). Per the v1 prompt §5: "If `replication-log.md` is missing or stale, this is a Tier-C/E/M defect." The log is present, but it records zero successful replications. This is a Tier-M defect.

**`make replicate` is a stub.** `reproducibility-bundle/Makefile` is explicitly labelled as a stub: it prints walkthrough instructions instead of executing the pipeline. Per CHARTER §9 ("a runnable replication script (`make replicate` or equivalent) that re-derives the headline figures from raw inputs"), this is unsatisfied.

**Code and data subdirectories are pointer-only.** `reproducibility-bundle/code/` and `reproducibility-bundle/data/` contain only `README.md` files describing what would live there if the bundle were vendored or git-submoduled. The source repos are private; per `code/README.md` §"Gate-7 finalisation options," three closure options are listed and the author has not yet selected one. Per the v1 prompt §5 and Charter §9, this fails the Tier-M reproducibility-bundle requirement.

**Gaps in `reproducibility-bundle/README.md` §"Known gaps" are accurate.** Cross-referencing the named gaps against actual artifact state:
- "Code: pointer-only" — confirmed (`code/` contains only README.md).
- "Data: pointer-only, contrastive items derived from author's psychometric battery and need PII review before release" — confirmed.
- "Environment lockfile: not pinning transitive deps, TODO" — confirmed (`environment.yml` lists `>=,<` ranges, not exact versions).
- "Replication log: not run end-to-end" — confirmed.
- "AI-use prompt archive: not deposited" — confirmed.
- "License files: inherits unit defaults" — confirmed (no per-publication license file present; this is acceptable per CHARTER §13).

The gap inventory is honest and complete.

**Stat-significance gap (cross-flag with §2):** Per `neurips-checklist.md` §7, no confidence intervals, no binomial tests against chance, no multiple-comparisons correction across the 24-channel family are reported. The closure cost ("half a day with scipy.stats") is acknowledged but not yet executed. This is independent of the bundle plumbing but is a Tier-M defect for any submission beyond raw arXiv.

**Summary of bundle-spot-check defects requiring closure before external release:**
1. Either vendor source code into `code/` or pin git-submodules, plus make the source repos accessible.
2. Implement the real `make replicate` target.
3. Run the bundle end-to-end at least once and record the run in `replication-log.md`.
4. Lift `huggingface_revision_sha`, `judge_temperature`, `position_randomisation_seed` into `seeds.json`.
5. Pin transitive dependencies (uv.lock or equivalent).
6. Compute checksums for the released steering vectors and contrastive-item sets, add to PROVENANCE.md.
7. Add a published-results.json file with the manuscript κ values to enable delta-comparison on replication.
8. Add binomial significance tests + Bonferroni / BH-FDR correction + 95% CIs on κ (cross-flag with §2; addresses NeurIPS checklist item 7).
9. Deposit the prompt archive (cross-flag with §4).

## 6. Ethics, dual-use, and responsible-release

**Scoping Memo dual-use review:** No Scoping Memo exists for this work (per the v1 prompt's input block: "Scoping memo: NONE (work pre-dates unit adoption)"). The work pre-dates the unit's gating framework. Per CHARTER §11, every project's Scoping Memo should include a Dual-Use and Responsible-Release section. The original assessment therefore cannot be checked against the finished manuscript because the original assessment does not exist.

**Dual-use audit of the manuscript as it stands:** The work has non-trivial dual-use surface:

- The Dark Tetrad channels (machiavellianism κ=0.857, narcissism κ=1.000, psychopathy κ=1.000@c=4) constitute a method for steering an open-weight 7B model toward dark-trait expressions. Per `neurips-checklist.md` §10 ("Broader impacts"), this is partially addressed in the manuscript via the sadism RLHF-floor framing (§3.5, §4.4) and the refusal-cosine FLAG threshold reporting, but **no dedicated "Broader impacts" subsection exists** in MANUSCRIPT.md. `neurips-checklist.md` §10 flags this as a TODO and suggests text for it. This Gate-6 review confirms the gap: before any external (arXiv or otherwise) release, add a dedicated subsection (§4.6 or §11) covering positive impacts, negative impacts (including the dual-use concern named explicitly), and mitigations (vectors gated by access-on-request; sadism RLHF-robust at tested coefficients; coefficient ceiling).

- The sycophancy sign-flip finding (§3.5) has direct deployment-relevant safety implications — an LLM mistakenly using positive-coefficient sycophancy steering will become more sycophantic, not less. The manuscript names this as "a methodological reminder" (§4.5); it should be re-framed as also a deployment-safety risk that any downstream consumer of these vectors must know about. Add a one-sentence "deployment warning" annotation alongside the methodological-reminder framing.

- The work releases (or will release; the disposition is "access-on-request" per `code/README.md`) 24 contrastive-item sets derived from the author's single-subject psychometric battery. PROVENANCE.md §"License of artifacts" disclosed this: "Release of the items implies release of the author's operational identification of each trait. The author has elected to do this." This is a personal-data release decision by the author and is acceptable under CHARTER §11 (founder self-experimentation); no third-party PII is exposed.

**Responsible-Release Review (per Charter §11):** Not triggered formally because no Scoping Memo gate was passed. Should one be triggered retroactively? My read is yes-but-low-stakes: the substrate as released is access-on-request (not a public model checkpoint), the dark channels are bounded by refusal-cosine reporting (machiavellianism at 0.218 watch is the strongest of the four), and sadism is RLHF-floored. A retroactive Responsible-Release Review at the v0 stage would consist of (a) staged release: the access-on-request posture is already a staged release; (b) capability gating: the |c| ≤ 2 ceiling and refusal-cosine clamps already act as capability gates; (c) model-card content: the steering vectors are not currently a public artifact; if they become public, a Model Card is required (cross-flag with §1 Tier-M N/A justification). Recommendation: rather than retroactively running a full Responsible-Release Review, the manuscript's new "Broader impacts" subsection should explicitly enumerate the dual-use considerations and the mitigations in force.

**SCRIBE 2016 (single-case experimental design) check:** Per the v1 prompt §6: "For self-experimentation studies: confirm the SCRIBE 2016 reporting items are satisfied where applicable, the n=1 limitation is disclosed prominently (including in the abstract), and no generalization claim exceeds what an n=1 design can support."

- The n=1 limitation is disclosed prominently in the abstract ("a single-subject derivation of the contrastive items (n = 1)"), in the methods (§2.2 "All contrastive items reference a single human subject's psychometric battery"), in §8.1, and in the keywords ("single-subject design"). This satisfies the prominent-disclosure standard.

- SCRIBE 2016 itself: per `reproducibility-bundle/README.md` checklist row, "SCRIBE 2016 checklist: N/A — not a single-case behavioural intervention; the n=1 derivation is methodological, not a behavioural study." I concur with this N/A justification: SCRIBE 2016 is for single-case experimental designs that intervene on a single human subject and measure that subject's response. Here, the single subject's psychometric battery is the *source* of the contrastive items, not the experimental unit; the experimental unit is the model. SCRIBE does not apply.

- Generalisation: the abstract correctly says "should be read as a methods / proof-of-concept contribution." §8.1 explicitly states that "the vectors therefore encode *that subject's operationalisation* of each trait, not a multi-subject latent construct." §10 conclusions stay calibrated. The H × Dark-Triad coupling §3.7 / §4.3 framing as "empirical confirmation" / "matches the published psychometric literature" is the closest the manuscript comes to generalisation beyond n=1; per §2 of this review, that framing needs softening but is not a SCRIBE-relevant generalisation violation.

## 7. Conflicts of interest

`coi-disclosure_weakley.md` is unusually thorough for v0. Audit:

**Currentness:** "As of date: 2026-05-24" — current.

**Completeness against standing tooling disclosure (unit README "Dependencies & tooling disclosure"):** README lists Anthropic Claude, GitHub, Zenodo, OSF as standing tooling. The COI disclosure §2.1 itemises Anthropic, Modal Labs, Supabase as paying customer-vendor relationships. Modal and Supabase are work-specific (not in the unit's standing tooling) and correctly itemised here. GitHub is not in §2.1 — should be added for completeness, even though the relationship is trivial paying customer-vendor. Zenodo and OSF are not itemised — both are listed in the unit README as standing dependencies with no financial relationship; the disclosure could state "see the unit's standing tooling disclosure in README.md" for those rather than restating, but the per-publication standard per ICMJE convention is to itemise. Minor revision recommended.

**Annual snapshot cross-reference:** The COI disclosure references "CHARTER §12, README.md 'Dependencies & tooling disclosure'" and "(CHARTER §12, README.md \"Dependencies & tooling disclosure\")." The unit's annual snapshot at `coi/YYYY_founder-disclosure.md` is empty (the `coi/` directory is empty — confirmed by `ls`). The disclosure does not explicitly state that the annual snapshot is not yet present, which means the reader cannot tell whether the per-publication disclosure is the *only* disclosure or whether it's a per-publication refinement of an existing snapshot. Per CHARTER §12: "Conflicts of interest are disclosed using the ICMJE Disclosure Form on a per-publication basis (committed to each publication folder) and as an annual snapshot (committed to the repo root each calendar year in `coi/YYYY_founder-disclosure.md`), regardless of whether the venue requires it." The annual snapshot is therefore due. Recommendation: either create `coi/2026_founder-disclosure.md` before external release, or amend the per-publication disclosure to note its absence and the schedule for closure.

**Dual-role disclosure of Claude as drafter and judge:** §3 of the COI disclosure explicitly names this: "Anthropic Claude is used both as the manuscript-drafting assistant ... and as the blind-rater judge for the validation κ values reported in §3. This is a non-trivial dual role." This is the correct disclosure. The mitigating note (rubrics authored before any judge run, not modified after) is repeated. This is acceptable.

**Publication-specific COI:** §2.6 candidly discloses the downstream commercial product (`mdfy-personality-registry`) that consumes the validated substrate. This is an "intellectual" COI per ICMJE conventions; the disclosure flags it explicitly. Acceptable.

**ORCID:** §1 notes "ORCID: not yet registered — to be obtained before any external submission." Hard requirement for any peer-reviewed venue submission, less critical for arXiv. Track for closure.

**Sign-off:** §5 statement signed and dated. Acceptable.

**Single human subject identity:** §2.5 states "The single human subject whose psychometric battery seeded the contrastive items ... **is the author**." This is the most consequential single piece of COI information in the document, and is correctly disclosed. Cross-checked against manuscript §2.2 ("a single human subject's psychometric battery"), §8.1, and PROVENANCE.md — all consistent.

## 8. Internal consistency

End-to-end numerical / claim consistency audit:

**Abstract vs §3 vs Table S1:**
- "20 of 24 channels achieved directional accuracy ≥ 0.60" (abstract) — consistent with Table S1 (20 PASS, 2 borderline, 1 sign-inverted, 1 RLHF-floored = 20+2+1+1=24).
- "9 of 11 previously-unvalidated channels passing at first attempt" (abstract) — §3.4 says "Nine of 11 PASS at first attempt" — consistent. Table S1 rows 4 (hexaco_emotionality), 5 (honesty_humility), 7 (hexaco_extraversion), 8 (self_monitoring), 9 (openness), 10 (hexaco_agreeableness), 14 (locus_of_control), 15 (attachment_anxious), 3 (attachment_avoidant): that's 9 PASS, with self_defeat (κ=0.500) and sycophancy (κ=0.250) being the 2 not passing. Consistent.
- "3 Dark-Tetrad channels passing — psychopathy required coefficient = 4" (abstract) — consistent with Table S1: narcissism PASS, psychopathy PASS@c4, machiavellianism PASS, sadism RLHF-floored. Three of four. Consistent.
- "3 single-layer KILLs rescued by multi-layer" (abstract) — consistent with §3.3 table (dospert_recreational, conscientiousness_self_discipline_v3, self_direction rescued; cautiousness borderline). Consistent.
- "5 originally validated at single-layer" (abstract) — consistent with §2.5 ("The 5 originally validated channels (cheerfulness, sociability, achievement_striving, stimulation, dospert_financial) used pre-existing channel-specific probe libraries"). Consistent.
- Sycophancy "κ = 0.250" (abstract, §3.5) — Table S1 row 23 confirms κ=0.250, 1 high-win / 3 low-wins / 8 ties. Consistent.
- Sadism "0/16 wins both directions at c=4" (abstract) — §3.5 says "16/16 ties at c=2 with trait-eliciting probes, 16/16 ties at c=4." Table S1 row 24 says "0 high wins / 0 low wins / 16 ties." Consistent.

**One minor consistency issue: openness probe-count.**
- §2.5: "Trait-eliciting D0 probes... *n* = 12–14 directional probes + 2 quality-control"
- §3.2 table: "1.000 (7W/0L/9T)" for narcissism; "(6W/1L/9T)" for machiavellianism — both totals = 16, consistent with 14 directional + 2 QC counted-in being scored, OR 16 trait-eliciting (no QC counted). Need to clarify whether QC probes are counted toward W/L/T totals.
- §3.3 table for dospert_recreational: "13W/5L/12T" = 30 total. Original 9 used 30-probe libraries per §2.5 — consistent.
- §3.4 table for openness: κ = 0.750 with 3W/1L/8T (from Table S1 row 9) = 12 total — matches "12 trait-eliciting + 2 QC, with QC not counted in W/L/T totals" reading. But the supplementary tables row says "3 / 1 / 8" totalling 12, while the manuscript §3.4 lists openness κ at 0.750 without breakdown.
- This is internally consistent but the manuscript should clarify in §2.5 whether the 12–14 directional count includes or excludes QC probes (PROVENANCE.md §"Headline claims" says probes are "12–14 directional + 2 QC" — i.e. QC is separate). Recommend a one-sentence clarification.

**Manuscript prose vs supplementary tables vs PROVENANCE:**
- §3.4 "Openness 0.750" vs Table S1 row 9 "openness 0.750" — consistent.
- §3.7 "honesty_humility showed −0.32 cosine against machiavellianism, psychopathy, and self_defeat at L16" — Table S3 lists honesty_humility × machiavellianism at −0.315, honesty_humility × psychopathy at −0.321, honesty_humility × self_defeat at −0.257. The first two are ≈ −0.32; the self_defeat value is −0.257 (closer to −0.26, not −0.32). The manuscript prose generalises three values when only two are ≈ −0.32. Minor: revise the prose to read "honesty_humility showed cosines of −0.32 against machiavellianism and psychopathy, and −0.26 against self_defeat at L16" — or restructure the sentence to not imply all three are −0.32.

**Methods vs code (in PROVENANCE.md):**
- §2.7 "Inter-channel cosine + Gram-Schmidt orthogonalisation": pairwise channel cosines at L12/16/20 — consistent with PROVENANCE.md inter_channel_cosines.py.
- §2.6 judge: "Claude Opus 4.7" — but `ai-use-disclosure.md` §2.1 lists both claude-opus-4-6 (9 channels) and claude-opus-4-7-1m (15 channels). Inconsistency between manuscript-stated judge identity and disclosure-stated judges. The manuscript should disclose both judge versions and which channel subset each judged. Cross-flagged with §4 of this review.

**Seeds.json TODO markers vs PROVENANCE.md determinism section:**
- PROVENANCE.md §"Determinism" lists "Decoding: greedy ... Position-randomisation seed: see seeds.json."
- `seeds.json` `judge.position_randomisation_seed` is the literal string `"TODO_lift_from_source_repo:mg-digital-twin/experiments/d4-fader-intervention/analyse.py"`.
- The PROVENANCE pointer to seeds.json is dishonestly affirming — it implies the seed is recorded, but seeds.json is itself a TODO. Either the seed should be lifted now (the source repo and commit SHA are pinned), or PROVENANCE should say "to be lifted before external release; see seeds.json TODO markers."

## 9. Reservations not covered above

- **No Gate-1 lab-notebook entry:** Per CHARTER §5, Gate 1 ("Idea capture") produces a short Lab Notebook entry. None exists for this paper (input block: "Relevant lab-notebook entries: NONE for this paper"). For Tier M this is not a strict checklist item, but it does mean the manuscript has no Gate-1, Gate-2 (Scoping Memo), or Gate-3 (pre-reg / exploration plan) artifact behind it. The workflow gate compliance of this publication runs Gate 6 → Gate 7 → Gate 8, with the upstream gates retroactively disclosed via `deviations.md`. This is the right disposition for a pre-adoption publication but should be explicitly named in this review as a one-time exception: this is the first non-DEMO publication of the unit, and the workflow gaps are tracked as one-time-only.

- **Unit notebook for the Gate-6 review itself:** Per CHARTER §10, every AI-assisted session that materially shapes a forthcoming publication is a "publication-touching session," and its transcript is committed to that publication's `ai-use-disclosure.md`. This internal review is itself an AI-assisted session shaping the publication; the prompt + this response should be added to the publication's `ai-use-disclosure.md` archive (or to a parallel `internal-review/` archive) before the prompt-archive deposition closes. The drafting Claude's `ai-use-disclosure.md` §2.5 anticipates this ("Internal reviewer: Claude `claude-opus-4-7-1m` ... counter-signature will follow on a subsequent commit"); the operational record should follow.

- **Cross-model judge agreement was not measured:** This is acknowledged in `ai-use-disclosure.md` §2.1 ("Inter-model rater agreement was not measured; the two models judged disjoint subsets") but is not in the manuscript. Cross-flag with §8 and §4 of this review. Material because: if claude-opus-4-7-1m systematically scores higher κ than claude-opus-4-6 (or vice versa), the new-15 vs original-9 PASS-rate comparison is confounded. The original 9's κ values come from prior runs with one judge family; the new 15's come from a different (or partially different) judge family.

- **The orthogonalisation report (Table S4) is over the original 9, not the full 24:** Table S4 reports norm-preservation ratios for 9 channels; the 15 new channels are not orthogonalised in Table S4. Manuscript §2.7 ("Inter-channel cosine + Gram-Schmidt orthogonalisation: pairwise channel cosines at L12/16/20 and norm-preservation ratios under modified Gram-Schmidt with the validated 9 channels orthogonalised first") states this implicitly ("the validated 9 channels orthogonalised first") but does not say explicitly that the new 15 were never orthogonalised. For a manuscript whose contribution is a "24-channel substrate," this is a Tier-M specification gap: the orthogonalisation report covers only 9 of 24 channels. Either expand the report to cover all 24, or explicitly note in §2.7 that orthogonalisation has not been performed on the new 15 (and why).

- **Inter-channel coupling values that *exceed* 0.30 are reported as "expected" without analytic justification:** Table S3 reports machiavellianism × sadism +0.377 and psychopathy × attachment_avoidant +0.447 with interpretations "dark-tetrad cluster (expected)" and "callousness ↔ detachment." attachment_avoidant × self_defeat +0.512 is labelled "the strongest non-trivial pair." Above-0.30 inter-channel cosines, by the manuscript's own refusal-cosine convention (§2.7), would be in FLAG territory if applied to refusal. For inter-channel coupling there is no equivalent threshold convention, but the "expected" qualifier is doing rhetorical work without a literature citation that quantifies the expectation. Recommend either citing the specific HEXACO / dark-tetrad inter-correlation literature with quantitative comparison or softening to "consistent with cluster structure."

- **No discussion of how the κ ≥ 0.60 gate was chosen:** §2.4 states the gate but does not justify it. A reader will want to know whether 0.60 is the substrate-paper convention, an a priori choice, or post-hoc. `deviations.md` §2 names it as pre-specified; the manuscript should add a one-sentence justification (e.g., "consistent with the substrate paper's composite-κ finding of 0.60 at this configuration" — which is alluded to at §1.2 H1 but not at §2.4).

- **The "drafting LLM's self-critique" referenced by `deviations.md` and `ai-use-disclosure.md`:** Multiple documents reference "the drafting LLM's own self-critique" as a source of revision recommendations. This self-critique is committed "alongside this pack as historical context" per `ai-use-disclosure.md` §2.3 but I cannot identify the file in the publication folder listing (the listing shows MANUSCRIPT.md, SUPPLEMENTARY_TABLES.md, ROADMAP_TO_TOP_VENUES.md, WORK_LOG.md, README.md, deviations.md, ai-use-disclosure.md, coi-disclosure_weakley.md, neurips-checklist.md, Makefile, correspondence/, reproducibility-bundle/). The self-critique should either be added as a named file (e.g., `self-critique_pre-Gate-6.md`) or the references to it should be removed in favour of paraphrased content.

- **Operational research tooling claim (§6):** §6 "The system is operational research tooling, not a production product." This is a useful disclosure but partially conflicts with §2.6 of the COI disclosure, which names `mdfy-personality-registry` as a "downstream commercial product that depends on the steering substrate validated in this manuscript." The relationship between the operational-research-tooling claim (§6 manuscript) and the commercial-product disclosure (§2.6 COI) should be reconciled in one sentence: e.g., "The unit's research tooling described here is operationally research-only; downstream consumption by a separate commercial product is disclosed in the COI document."

## 10. Recommendation (restated)

PROCEED WITH REVISIONS — the work is honestly reported, the manuscript is candid about its limitations, the COI and AI-use disclosures are unusually thorough, and `deviations.md` correctly identifies the structural pre-registration gap; but five categories of revision are required before external release: (1) reframe §1.2 H1–H3 and the "confirmed" headings in §3.2/§3.3 as exploratory per `deviations.md` §4, and replace "overturns" in §3.4 / §4.2 / Table S1 with "challenges" or "provides counter-evidence to"; (2) finalise the reproducibility bundle (vendor or submodule the source code, implement real `make replicate`, run end-to-end once and record in `replication-log.md`, lift the TODO markers in `seeds.json`, deposit the prompt archive); (3) add statistical-significance reporting (95% CIs on κ, binomial tests vs chance, Bonferroni or BH-FDR correction across the 24-channel family) as `neurips-checklist.md` §7 already names as a load-bearing TODO; (4) add a dedicated "Broader impacts" subsection covering the dual-use considerations and mitigations; (5) reconcile the cross-section inconsistencies surfaced in §8 of this review, including the dual-judge disclosure, the seeds.json TODOs vs PROVENANCE's implication that seeds are recorded, the orthogonalisation report's 9-vs-24 scope, and the openness probe-count convention.

---

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
