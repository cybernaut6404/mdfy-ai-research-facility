# NeurIPS Paper Checklist — 24-Channel Activation-Steering Validation

Per `mdfy-ai-research-facility` STANDARDS.md Tier-M (methods/engineering)
ML-work checklist, completed against the NeurIPS Paper Checklist
Guidelines. This is the unit's reproducibility floor for any ML
methods publication.

Items are completed where the manuscript and bundle provide the evidence;
TODO markers indicate gaps that must close before any NeurIPS / NeurIPS-
adjacent venue submission. For arXiv preprint posting, the TODO items are
acceptable to flag-and-disclose rather than close.

---

## 1. Claims

**Q:** Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?

**Answer:** Yes, with one calibration flag.

**Evidence:** The abstract and §1 frame the contribution as a *systematic 24-channel validation* of activation steering on Qwen2.5-7B with explicit safety probes, with the explicit honesty that the work is single-subject / single-model / single-judge / non-pre-registered proof-of-concept. The §1.2 "Hypotheses" framing reads slightly stronger than the timestamp evidence supports (per the drafting LLM's self-critique and `deviations.md`); a revision to soften H1–H3 from "pre-specified hypotheses" to "expectations stated in build notes presented as exploratory findings" is tracked as a Gate-6 finding and will land before any submission.

## 2. Limitations

**Q:** Does the paper discuss the limitations of the work performed by the authors?

**Answer:** Yes — extensively.

**Evidence:** §8 has 8 numbered limitations: §8.1 single-subject derivation; §8.2 single open model; §8.3 single LLM judge / no human inter-rater reliability; §8.4 small probe sets (12–14 not 30); §8.5 not pre-registered; §8.6 sampling and decoding; §8.7 coefficient ceiling; §8.8 channel-set limitations. Each limitation includes a one-paragraph elaboration and (where applicable) the path to closure in §9 / Roadmap.

## 3. Theory assumptions and proofs

**Q:** For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

**Answer:** N/A — this is an empirical-methods paper. No theoretical results are claimed.

## 4. Experimental result reproducibility

**Q:** Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper?

**Answer:** Partially — the description in the paper is complete; the bundle is in stub state.

**Evidence:**
- Manuscript §2 fully describes substrate, model, contrastive-item derivation, extraction (CAA at the named layer sweep), steering configuration (ML L12/16/20, |c| ≤ 2; c = 4 diagnostic), validation protocol (D4 directional accuracy with κ ≥ 0.60 gate), probe libraries (counts and types), judge (Claude Opus 4.6 and 4.7 with channel-specific rubrics reproduced in Table S6), and safety analyses.
- The bundle (`reproducibility-bundle/`) provides PROVENANCE.md naming every input and producing script with SHAs; environment.yml; seeds.json; replication-log.md acknowledging the bundle has not yet been run end-to-end; and code/ + data/ pointing at the source repos at pinned SHAs.
- **TODO before NeurIPS submission:** vendor the source code into `code/` (or pin git submodules), run end-to-end once, record in `replication-log.md`, lift the judge-position randomisation seed and HuggingFace revision SHA into seeds.json. Gate-7 finalisation.

## 5. Open access to data and code

**Q:** Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

**Answer:** Partially — instructions exist; the artifacts themselves are not yet public.

**Evidence:** Per `reproducibility-bundle/code/README.md` and `reproducibility-bundle/data/README.md`, the source repos are private at the time of writing; access is provided on request to verifiers. The unit's defaults are Apache-2.0 (code) and CC-BY-4.0 (content). **For NeurIPS-level openness, the source repos must be made public before submission.** This is a hard requirement; for arXiv preprint posting it can be deferred with a prominent "available on request" disclosure. Per ROADMAP Tier 2+ requirements, public release of data + code is non-negotiable for any psychology-journal submission.

## 6. Experimental setting/details

**Q:** Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

**Answer:** Yes.

**Evidence:**
- Model: Qwen2.5-7B-Instruct, fp16, 28 decoder layers, hidden size 3584 (§2.1).
- Decoding: `do_sample=False` (greedy), max_new_tokens=512, Qwen default chat template (§8.6).
- Extraction: CAA at layer sweep [8, 12, 16, 20, 24], L2-normalised post-extraction so the coefficient is the intervention dial (§2.2).
- Steering: forward hooks on L12/16/20, additive on the residual stream at every token position, |c| ≤ 2 main and c = 4 diagnostic only on psychopathy + sadism (§2.3).
- Validation: pre-specified κ ≥ 0.60 gate; ties reported separately (§2.4).
- Probes: 10 generic + 12–14 trait-eliciting per new channel + 2 QC; 30 per original channel (§2.5).
- Judge: Claude Opus 4.6 / 4.7 with per-channel rubrics, position randomised per pair via a fixed seed (§2.6).
- Safety: refusal-cosine SAFE < 0.1 / watch 0.1–0.3 / FLAG ≥ 0.3 (§2.7).
- Compute: Modal A100 for extraction of original 9; Modal L4 for the new 15 + all validation runs (§2.8; bundle PROVENANCE.md + environment.yml).

## 7. Experiment statistical significance

**Q:** Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

**Answer:** No — and this is a **load-bearing TODO** for any Tier-2+ submission.

**Evidence:** §3 reports κ + raw win/loss/tie counts but no confidence intervals, no binomial significance tests, no multiple-comparisons correction across the 24 channels. Per the drafting LLM's self-critique:

> Real psychometric work reports confidence intervals, effect sizes (Cohen's d at minimum), binomial tests against chance, multiple-comparisons correction across the 24 channels (Bonferroni or BH-FDR). I reported κ + win/loss/tie counts — that's the raw data, not the analysis. A reviewer would ask for at least binomial significance per channel.

**Required closure before NeurIPS / TMLR submission:** add binomial significance per channel against chance (κ = 0.50) with Bonferroni or BH-FDR correction across the 24-channel family; report 95% confidence intervals on κ; compute Cohen's h or equivalent effect size. Estimated work: half a day with scipy.stats. Tracked in ROADMAP.

## 8. Experiments compute resources

**Q:** For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

**Answer:** Yes.

**Evidence:** §2.8 names Modal L4 (24 GB, ~$0.80/hr); §7 estimates 2–3 hours L4 GPU time + $5–10 Anthropic Opus for a complete replication. SUPPLEMENTARY_TABLES.md §"Compute and cost provenance" reports the original study's cumulative cost: ~$8–15 Modal + $5–8 Anthropic across ~21 runs.

## 9. Code of ethics

**Q:** Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics?

**Answer:** Yes, with the caveats below.

**Evidence:**
- Human subjects: the single subject is the author; no third-party recruitment. Disclosed in abstract, §2.2, §8.1.
- Dual use: §3.5 reports that sadism is RLHF-floored (a positive safety finding); §3.6 reports refusal-cosine entanglement values for every Dark-Tetrad channel; no channel reached the FLAG threshold (the only FLAG in the broader substrate is dospert_financial at 0.310, deployment-clamped). The work does not enable substantive jailbreaking of the base model on the dimensions tested (sadism is unbudgeable; the other dark channels steer but stay below FLAG).
- Privacy / data protection: no third-party PII in the artifacts.
- Consent: N/A — author-only single-subject derivation.

## 10. Broader impacts

**Q:** Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

**Answer:** Partial — the sadism RLHF-floor finding (§3.5, §4.4) is framed as a positive safety signal. Negative-impact discussion is implicit in §6 (operational implications) and the dual-use considerations in the Dark Tetrad work, but is not gathered into a dedicated "Broader impacts" subsection.

**TODO:** Add a dedicated "Broader impacts" subsection at §4.6 before NeurIPS submission. Frame:
- *Positive:* tools for evaluating RLHF robustness; demonstration that activation steering is sensitive to probe instrument (a methodological caution that improves future evaluations); methodology for probing personality-construct coupling at the vector level.
- *Negative:* the substrate enables tuning models toward Dark-Tetrad-coupled behaviour at moderate effort; the sycophancy sign-flip finding is a deployment-relevant safety result (an LLM steered the wrong way on sycophancy is more sycophantic, not less); the methodology lowers the bar for downstream actors to extract and apply personality-construct vectors to open models.
- *Mitigations:* the manuscript publishes the safety-floor findings (sadism, refusal-cosine clamp on dospert_financial) prominently; the substrate is not released as a model checkpoint, only as vectors gated by access on request to the source repos.

## 11. Safeguards

**Q:** Does the paper describe safeguards that have been put in place for responsible release of data or models with a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)?

**Answer:** Partially.

**Evidence:**
- The steering vectors are NOT released as a public checkpoint at this stage. Per `code/README.md` §"Access procedure", access is by request to the author.
- The refusal-cosine FLAG threshold and deployment-side coefficient-clamping policy (§2.7, §3.6) are reported in detail so downstream consumers can apply equivalent safeguards.
- The sadism RLHF-floor finding is reported as a positive safety result.
- **TODO:** Before any public release of the steering vectors (Tier-2+ requirement), add a Model Card per Mitchell et al. 2019 (the unit's `templates/reproducibility-bundle_CHECKLIST.md` §"Compliance artifacts" requires this for Tier-M model release). The Model Card is N/A at the current stage because the vectors are not publicly released; it becomes mandatory if/when the vectors are released.

## 12. Licenses for existing assets

**Q:** Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

**Answer:** Yes.

**Evidence:**
- Qwen2.5-7B-Instruct: cited (§2.1, references). Open-weights license respected; the model is not redistributed.
- Rimsky et al. (2024) CAA recipe: cited (§1.1, §2.2, references).
- AlphaSteer refusal-cosine protocol: cited (§2.7, references — Anthropic Persona Vectors line).
- Templeton et al. (2024) SAEs: cited (§1.1, references; not directly used but acknowledged as complementary).
- HEXACO / NEO-PI-R / Schwartz / DOSPERT / Dark Tetrad / ECR-R / Rotter LOC / Self-Monitoring / Mach IV: cited (§2.2, references). No instrument is reproduced verbatim; the items are *the author's operationalisation* of the underlying constructs, not copies.

## 13. New assets

**Q:** Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

**Answer:** Partially.

**Evidence:** The new assets are: (i) the 24 steering vectors for Qwen2.5-7B-Instruct; (ii) the 24 contrastive-item sets; (iii) the 11 + 4 new probe libraries; (iv) the blind-rater rubrics; (v) the validation harness + analyser code; (vi) the steering-server code. Documentation:
- This bundle's README + PROVENANCE + bundle data/README + bundle code/README documents the assets at the file-name level.
- The actual asset files live in private source repos at pinned SHAs.
- **TODO before public release:** vendor the assets into the bundle with per-asset README files. Currently this is access-on-request.

## 14. Crowdsourcing and research with human subjects

**Q:** For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

**Answer:** N/A — no crowdsourced or human-subjects experiments. Single human subject is the author; no other subjects involved. The single-subject limitation is the dominant limitation of the study (§8.1).

## 15. Institutional review board (IRB) approvals

**Q:** Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

**Answer:** N/A — author-only self-experimentation. Per the unit's CHARTER §11, the v0 scope is explicitly limited to founder self-experimentation, computational studies, and analyses of public data; no IRB partner is engaged at v0; an IRB partner will be sought if/when the unit's scope expands to recruit non-author subjects (the R1 multi-subject extraction in the ROADMAP).

## 16. Author contributions

**Q:** (For multi-author work) Does the paper specify the contributions of each author?

**Answer:** N/A — sole-authored.

R. Weakley contributed all of: research questions and design; contrastive-item authoring; probe-library authoring; blind-rater rubric authoring; build of the central DB, mixers, construct-runner, steering-server, and validation harness; gating decisions; review and approval of all AI-generated content. AI-contributed elements are disclosed in `ai-use-disclosure.md`.

---

## Summary

| Item | Status |
|---|---|
| 1. Claims | ✓ (calibration flag on §1.2 H1–H3 framing — Gate-6 finding) |
| 2. Limitations | ✓ |
| 3. Theory / proofs | N/A |
| 4. Experimental reproducibility | ⚠ partial — bundle is stub; Gate-7 closure |
| 5. Open access to data and code | ⚠ access-on-request at v0; public release required Tier-2+ |
| 6. Experimental setting/details | ✓ |
| 7. Statistical significance | ❌ — load-bearing TODO (CIs, binomial tests, FDR correction) |
| 8. Compute resources | ✓ |
| 9. Code of ethics | ✓ |
| 10. Broader impacts | ⚠ implicit; dedicated subsection TODO before NeurIPS submission |
| 11. Safeguards | ⚠ Model Card TODO if/when vectors released publicly |
| 12. Licenses for existing assets | ✓ |
| 13. New assets | ⚠ documented in README only at v0; per-asset docs TODO |
| 14. Crowdsourcing / human subjects | N/A |
| 15. IRB | N/A (author self-experimentation) |
| 16. Author contributions | N/A (sole-authored) |

**Bottom line:** the manuscript is **acceptable at arXiv** with the flagged gaps disclosed; **not yet acceptable at NeurIPS main track or TMLR** until items 4, 7, 10, 11, 13 are closed. Per the ROADMAP, items 7 (statistical significance) and 10 (broader impacts) are the cheapest closures and should land in the first revision pass.

---

*Completed by:* Claude (`claude-opus-4-7-1m`) per `templates/internal-review-prompt_v1.md` workflow; counter-signed by R. Weakley as the v0.0.4 Gate-6 procedure.
*Date:* 2026-05-24
