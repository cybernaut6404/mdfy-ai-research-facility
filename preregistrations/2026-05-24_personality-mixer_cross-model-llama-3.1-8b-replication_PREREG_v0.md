# Pre-Registration — Cross-Model Replication of the 24-Channel Activation-Steering Substrate on Llama-3.1-8B-Instruct

**Tier:** C (Confirmatory)
**Source repo:** `personality-mixer` (specifically `cybernaut6404/mg-digital-twin` for the extraction + harness + judge)
**Project lead:** Rick Weakley ([rick@mdfy.co.uk](mailto:rick@mdfy.co.uk); ORCID [0009-0004-0799-1756](https://orcid.org/0009-0004-0799-1756))
**Date of registration (planned):** TBD — to be set when this pre-registration is time-stamped on OSF
**OSF link (planned):** TBD — to be filled in after OSF account setup
**AsPredicted link:** N/A (using OSF for this pre-reg)
**Time-stamp commit hash (this file):** TBD — will be filled in via a follow-up commit citing the git SHA at the moment of OSF time-stamping

> *Status:* DRAFT — this pre-registration is committed to the unit's `preregistrations/` directory in DRAFT form on 2026-05-24 as part of the unit's Tier-C pipeline. Per CHARTER §8, the canonical pre-registration is the one time-stamped on OSF before any data collection. This draft will be transcribed into the OSF Pre-Registration form and time-stamped before any Llama-3.1-8B-Instruct extraction / validation runs begin. After OSF time-stamping, this file is updated with the OSF link + DOI and the time-stamp commit hash, and the status changes to "REGISTERED."

> *This pre-registration is time-stamped at the date and commit above. Any data collection or analysis predating this time-stamp is, by definition, not part of the confirmatory study described here. Deviations from this plan in the eventual publication are reported in a dedicated "Deviations from Pre-Registration" section.*

---

## 1. Research question

Do the 24 activation-steering channels validated on Qwen2.5-7B-Instruct in the v0 personality-mixer publication ([https://github.com/cybernaut6404/mdfy-ai-research-facility/tree/main/publications/2026-05-24_personality-mixer_activation-steering-validation_v0](https://github.com/cybernaut6404/mdfy-ai-research-facility/tree/main/publications/2026-05-24_personality-mixer_activation-steering-validation_v0)) replicate on Llama-3.1-8B-Instruct under the same multi-layer steering recipe (L12/16/20, |c| ≤ 2), the same trait-eliciting probe libraries, and the same blind-rater judge?

## 2. Background and motivation

The v0 personality-mixer publication validated a 24-channel activation-steering substrate on a single open model (Qwen2.5-7B-Instruct), with explicit single-model-generalisation as one of the eight named limitations (§8.2). The publication's ROADMAP §"Recommended sequencing" item 2 commits to cross-model replication on a non-Qwen model as the short-term (1–3 month) next step. Llama-3.1-8B-Instruct was named as the natural choice because (a) the extraction scaffolding (`mg-digital-twin/infra/steering-vectors/extract_caa.py` and the harness `experiments/d4-fader-intervention/harness.py`) already supports it; (b) Llama-3.1-8B-Instruct is comparable in scale (8B vs 7B) and instruction-tuned posture; (c) different RLHF training history (Meta's posture differs from Qwen Team's) lets us test whether the v0 publication's sadism RLHF-floor finding is Qwen-specific or generalises.

The cross-model replication is also a load-bearing requirement for Tier-2+ submission (Psychological Bulletin / Psychological Review per the manuscript's ROADMAP R4).

## 3. Hypotheses

Three pre-specified hypotheses, with falsification criteria stated in §4. All three are tested and reported regardless of outcome.

- **H1 (primary, generalisation).** At least 12 of the 20 channels in the v0 publication's PASS tier (κ ≥ 0.60 under the ML L12/16/20 |c|=2 recipe on Qwen2.5-7B-Instruct) will replicate to κ ≥ 0.60 on Llama-3.1-8B-Instruct under the same recipe.

- **H2 (secondary, probe-instrument).** The v0 publication's §3.2 probe-instrument finding — that generic discriminability probes systematically false-zero dark-trait validation — will replicate on Llama-3.1-8B-Instruct: the four Dark Tetrad channels (machiavellianism, narcissism, psychopathy, sadism) will return κ = 0 on generic probes and κ ≥ 0.60 on trait-eliciting probes for at least three of the four (the Qwen result was 2 of 4 at c=2 with psychopathy at c=4 = 3 of 4).

- **H3 (secondary, RLHF-floor).** The v0 publication's §3.5 sadism RLHF-floor finding will *not* replicate on Llama-3.1-8B-Instruct: under trait-eliciting probes at c=4, sadism will achieve κ ≥ 0.60 on Llama-3.1-8B-Instruct (because Llama's RLHF training differs from Qwen's; the original finding was framed as Qwen-specific).

## 4. Falsification criteria

For each hypothesis, the result that would constitute disconfirmation:

- **H1 disconfirmation:** Fewer than 12 of 20 PASS-tier Qwen channels reach κ ≥ 0.60 on Llama-3.1-8B-Instruct. If this happens, the v0 finding of broad cross-channel steerability is model-specific to Qwen2.5-7B; we report the substrate as Qwen-specific and revise the manuscript's generalisation framing.

- **H2 disconfirmation:** Trait-eliciting probes for the Dark Tetrad channels on Llama-3.1-8B-Instruct yield κ values within ±0.10 of the same channels' generic-probe κ values (i.e., trait-eliciting probes don't materially improve over generic). If this happens, the probe-instrument finding is Qwen-specific.

- **H3 disconfirmation:** Sadism reaches κ ≥ 0.60 at c ≤ 4 on Llama-3.1-8B-Instruct. (NB: in the v0 paper this is the *expected* outcome under the interpretation that Llama's RLHF posture is more permissive; H3 is structured so that disconfirmation of H3 *supports* the Qwen-specific-RLHF-floor narrative. We are testing whether the v0 paper's framing is right.)

## 5. Design

**Substrate model:** `meta-llama/Llama-3.1-8B-Instruct` at HuggingFace revision `main` at run time (the exact revision SHA at run-start will be recorded in `replication-log.md` for the resulting publication).

**Steering recipe:** Multi-layer additive steering. For Llama-3.1-8B-Instruct's 32 decoder layers, the proportionally-equivalent layers to Qwen's L12/16/20 (28-layer model) are L14/L18/L23 — these positions sit at ~50% / ~64% / ~82% of model depth, matching Qwen's ~43% / ~57% / ~71%. (Note: alignment of layer-depth fractions across architectures is heuristic; pre-registering this choice rather than tuning post-hoc.)

**Coefficient ceiling:** |c| ≤ 2 for the main validation, matching v0. A c = 4 diagnostic run will additionally be performed on sadism only, to test H3 directly.

**Probe libraries:** The same 24 channel probe libraries from the v0 publication's vendored `code/experiments/d4-fader-intervention/probes/` (committed at `cybernaut6404/mdfy-ai-research-facility@v0.0.4-charter`). No new probes authored for this cross-model run; reusing the v0 probes is what makes this a replication.

**Judge:** Anthropic Claude. Model version selected at run-start and pinned in `seeds.json`; will be one of {`claude-opus-4-7`, `claude-opus-4-8` if released by run date}. Same channel-specific rubrics (`JUDGE_PROMPTS` dict in `analyse.py`) as v0; no rubric modifications.

## 6. Sampling plan

**Target n per channel:** Same as v0 — 12–14 trait-eliciting D0 probes per new channel + 2 QC probes per channel. The original 9 channels use their pre-existing channel-specific probe libraries (30 probes per channel). Per-channel binomial test power at α = 0.05 (uncorrected) is approximately 0.6 for an effect size of κ = 0.85 vs. chance κ = 0.50 at N=12 — below conventional power thresholds, mirrors v0's limitation. This pre-registration documents the limitation explicitly: per-channel statistical power is low, and ROADMAP item R5 (larger probe sets, separate work) is required for confidence-interval narrowing. **The H1 / H2 / H3 tests are family-level, not per-channel, so the relevant power is on the proportion of channels meeting the criterion, not per-channel κ significance.**

**Stopping rule:** Run all 24 channels under the pre-specified recipe; no per-channel early stopping. Abort the entire run only if Llama-3.1-8B-Instruct fails to load on Modal L4 (memory issue) or if HuggingFace gates the model access for the author's account — see §12.

## 7. Variables

For each per-channel per-coefficient row:
- **Channel** (categorical, 24 levels): the channel being steered. See v0 Table S1 for the full list.
- **Coefficient** (continuous, primary value c=2.0; diagnostic value c=4.0 for sadism only): the steering coefficient.
- **Layers** (fixed at L14/L18/L23): the decoder layers receiving the steering injection.
- **Probe** (categorical, 12–14 directional + 2 QC per channel): the trait-eliciting scenario presented to both high- and low-coefficient conditions.
- **High-low pair** (the unit of analysis): each (high-coef-response, low-coef-response) pair scored by the judge.

**Primary outcome (per channel):** directional accuracy κ = (high-wins) / (high-wins + low-wins), excluding ties, on the non-tie pairs.

**Secondary outcomes:**
- Refusal-direction cosine (per-channel, per-layer, against the Llama-3.1-8B-Instruct refusal vector — re-extracted on the new model).
- Inter-channel cosine matrix (full 24×24 at L14/L18/L23).
- Gram-Schmidt orthogonalisation report (extended to all 24 channels — the v0 publication only orthogonalised the original 9; this pre-reg commits to the full-24 expansion per the v0 manuscript §2.7's Tier-2-readiness follow-up).

**Quality-control:** QC probes (factual recall) inspected for steering-induced corruption; QC failures recorded but not folded into κ computation (as in v0).

## 8. Outcomes

- **Primary outcome:** per-channel κ on Llama-3.1-8B-Instruct.
- **Secondary outcomes:**
  - Refusal-direction cosine per channel (test for FLAG channels)
  - Inter-channel cosine matrix (test the H × Dark-Triad coupling reproduces)
  - Gram-Schmidt norm-preservation ratios for all 24 channels
  - QC-probe inspection

## 9. Analysis plan

**Pre-committed analysis script:** the same `analyse.py` script committed at `cybernaut6404/mdfy-ai-research-facility@v0.0.4-charter` under `publications/.../reproducibility-bundle/code/experiments/d4-fader-intervention/analyse.py`. No modifications to the rubrics or the κ-computation logic. The position-randomisation seed = 42 is reused for consistency with v0.

**Statistical tests:**
- Per-channel two-sided binomial test against chance (p = 0.50) on non-tie pairs.
- 95% Wilson score confidence intervals on the high-win proportion.
- Holm-Bonferroni and Benjamini-Hochberg (BH-FDR) corrections across the 18-channel family with non-blank W/L/T (the same 18 used in the v0 publication's §3.1.1).
- *Family-level tests* for H1, H2, H3 (NOT per-channel; see §6 power justification):
  - **H1 test:** binomial test on the proportion of 20 PASS-tier-channels that reach κ ≥ 0.60 on Llama, against the null hypothesis that the proportion is ≤ 12/20 = 0.60. Reject the null if at least 12 channels replicate (one-tailed; α = 0.05).
  - **H2 test:** binomial test on the proportion of 4 Dark Tetrad channels showing the probe-instrument flip (generic κ ≈ 0, trait-eliciting κ ≥ 0.60). Reject the null if at least 3 of 4 show the flip pattern (the Qwen result was 3 of 4 counting psychopathy@c=4; one-tailed; α = 0.05).
  - **H3 test:** binary outcome on sadism at c=4: does it reach κ ≥ 0.60? Yes = H3 confirmed (RLHF-floor is Qwen-specific). No = H3 disconfirmed (RLHF-floor may generalise).

**Pre-committed analysis script commit hash:** SHA of `analyse.py` at the v0.0.4-charter tag — to be recorded explicitly here once the OSF time-stamp is applied.

## 10. Inference

What conclusions follow from each possible outcome:

- **H1 confirmed (12/20+ replicate), H2 confirmed (3/4+ flip), H3 confirmed (sadism reaches 0.60 on Llama):** strongest possible outcome. The substrate generalises across models; the probe-instrument finding generalises; the Qwen-specific-RLHF-floor framing is supported. Recommendation: prepare Tier-C submission to TMLR; pursue Tier-2 venue (Psych Bulletin) work in parallel.
- **H1 confirmed, H2 confirmed, H3 disconfirmed (sadism stays at 0 on Llama):** the substrate generalises but the RLHF-floor effect is broader than Qwen-specific. Recommendation: rework §4.4 of the v0 manuscript to reframe the sadism finding as cross-RLHF rather than Qwen-specific.
- **H1 disconfirmed (fewer than 12/20 replicate):** the v0 finding is largely Qwen-specific. Recommendation: report this as a substantive negative result (per CHARTER §15's null-result-equal-effort commitment). Prepare a follow-up paper framing the substrate as Qwen-specific and exploring why.
- **H2 disconfirmed (fewer than 3/4 Dark Tetrad show the probe-instrument flip):** the probe-instrument methodological finding is Qwen-specific. Recommendation: substantial revision of the v0 manuscript's §4.1 framing; lower confidence on the methodological-caution-to-the-field framing in §4.1.

## 11. Exclusions and exceptions

- **QC failures:** a channel whose QC probes show steering-induced factual corruption is excluded from the κ computation but reported as a separate methodological observation. This rule is inherited from v0.
- **Unparseable judge outputs:** default to TIE per the `analyse.py::judge_pair` permissive parsing (inherited from v0).
- **Channels whose vector fails to extract on Llama-3.1-8B:** if extraction itself fails for a channel (e.g., the contrastive items produce a degenerate vector), record the failure and exclude the channel from H1's denominator. This is a structural exclusion, not a result-dependent one.

## 12. Abandonment conditions

The study is abandoned if any of the following occurs:

- Llama-3.1-8B-Instruct fails to load on Modal L4 due to memory or compatibility issues (will try L4 first; fall back to A10G if needed; abandon if neither works).
- HuggingFace gates the model access for `cybernaut6404`'s account (Llama-3.1-8B-Instruct requires accepting a license agreement; if Meta restricts access between this pre-reg and the run, abandon and pivot to Mistral-7B-Instruct as a Plan B model — would require an amendment to this pre-reg).
- Anthropic deprecates or significantly changes the `claude-opus-4-7` judge model between pre-reg and run, requiring substantial judge-rubric recalibration. Document the deprecation and pivot to whichever Anthropic model is current; the pre-reg amendment would identify the new judge and note the deviation.
- A serious dual-use concern surfaces (e.g., a Dark Tetrad channel produces credibly-uplift-relevant outputs on Llama that wasn't seen on Qwen). In that case, trigger a Responsible-Release Review per CHARTER §11 before continuing.

## 13. Dual-use and responsible-release notes

This study inherits the Broader Impacts mitigations from the v0 publication's §4.6: access-on-request gating of the steering vectors; refusal-cosine FLAG threshold + coefficient-clamping; |c| ≤ 2 ceiling; staged release. If Llama-3.1-8B-Instruct's RLHF posture is *more* permissive than Qwen's on the Dark Tetrad channels (i.e., dark traits steer more cleanly on Llama), the dual-use surface widens and the Responsible-Release Review will be re-run before any release of the Llama steering vectors.

The author intends to publish this work; the question of whether to *publicly release the Llama steering vectors* (vs. access-on-request) will be re-decided at Gate-2 / Scoping Memo for the Tier-C submission based on the resulting refusal-cosine profile and the Dark Tetrad κ outcomes.

## 14. AI-use plan

In advance of any data collection:

- **Judge:** Anthropic Claude (model version pinned at run-start). Same channel-specific rubrics as v0; no modifications.
- **Drafting:** Anthropic Claude expected to draft the resulting manuscript (Tier 3 execution per `AI_USE_POLICY.md`; potential Tier 4 originations to be disclosed per-element per the v0 publication's pattern).
- **Internal review (Gate 6):** Anthropic Claude under `templates/internal-review-prompt_v1.md`, counter-signed by Rick Weakley.
- **Code generation:** Anthropic Claude (Tier 3) for any analysis-script extensions (binomial-test family-level extensions, full-24 orthogonalisation expansion, cross-model layer-depth-alignment heuristic).
- **No AI involvement in:** the contrastive items + probes + rubrics (all inherited verbatim from v0); the Llama-3.1-8B-Instruct model weights (Meta's training).

## 15. Conflicts of interest

Inherited from `coi/2026_founder-disclosure.md` (annual snapshot) and the v0 publication's `coi-disclosure_weakley.md`:

- Anthropic dual-role caveat: drafter + judge. Mitigation: judge rubrics authored before any run; not modified after.
- Downstream commercial product (`mdfy-personality-registry`) intellectual interest in the substrate. Mitigation: pre-registration of falsification criteria.
- Single-author / self-experimentation single-subject: contrastive items inherited from v0 (so they still derive from Rick's psychometric battery). Mitigation: this pre-reg's H1/H2/H3 tests are family-level outcomes on the *model*, not on the subject.

No new COI relative to v0.

## 16. Signatures

- **Pre-registration prepared by:** Rick Weakley ([rick@mdfy.co.uk](mailto:rick@mdfy.co.uk); ORCID [0009-0004-0799-1756](https://orcid.org/0009-0004-0799-1756)), 2026-05-24 (draft)
- **Counter-signed (Gate 6 reviewer — to be filled in at Gate 6, post-execution):** to be set when the Tier-C manuscript reaches Gate-6 review; expected to be Claude (model version current at that time) counter-signed by Rick Weakley.

---

## Pre-registration workflow

1. Rick sets up an OSF account at https://osf.io (free; link ORCID 0009-0004-0799-1756 during signup).
2. Rick creates a new OSF Pre-Registration using the OSF Standard Pre-Registration template (https://osf.io/registries/osf/new).
3. Rick transcribes the content of this file into the OSF form, section-by-section.
4. OSF time-stamps the registration; Rick records the OSF DOI / URL.
5. Rick updates the front-matter of this file (date of registration, OSF link, time-stamp commit hash) and the status block, then commits as `preregistrations/2026-05-24_personality-mixer_cross-model-llama-3.1-8b-replication_PREREG_v0.md`. Status moves from DRAFT to REGISTERED.
6. **No data collection or extraction runs on Llama-3.1-8B-Instruct may begin until the REGISTERED status commit is on `main` and pushed to GitHub.** This is the operational gate; the OSF time-stamp is the canonical evidence.

For amendments to this pre-registration (e.g., judge-model deprecation, Plan-B substrate switch, additional channel additions), open a follow-up file `..._PREREG_v0-amendment-N.md`, commit, and add as an OSF amendment.
