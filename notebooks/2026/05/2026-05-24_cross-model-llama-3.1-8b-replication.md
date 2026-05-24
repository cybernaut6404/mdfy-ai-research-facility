# 2026-05-24 — Gate-1: Cross-model replication of the 24-channel substrate on Llama-3.1-8B-Instruct

**Project:** `personality-mixer` ecosystem — cross-model phase
**Tier (anticipated):** C (Confirmatory) — this is the unit's first proper Tier-C-pipeline project, with pre-registration committed *before* any data collection.
**Time:** 2026-05-24 evening; written immediately after Rick's B7 decision in the post-checkpoint session.
**AI assistance this session:** Anthropic Claude (`claude-opus-4-7-1m`) drafted this Gate-1 entry under the autonomous-mode authorisation. Tier 3 per AI_USE_POLICY.md (executing Rick's specified project direction). Same publication-touching session as the personality-mixer v0 paper's intake; transcript-mirror category per CHARTER §10: publication-touching → full archive will live in the resulting publication's `ai-use-disclosure.md` once Gate-7 closure of *that* publication begins.

---

## What I set out to do

Open Gate 1 for the unit's next research project: replicate the v0 personality-mixer publication's 24-channel activation-steering validation on a non-Qwen base model — Llama-3.1-8B-Instruct.

The v0 paper (`publications/2026-05-24_personality-mixer_activation-steering-validation_v0/`) validated 20 of 24 channels at κ ≥ 0.60 on Qwen2.5-7B-Instruct, with eight numbered limitations including single-model-generalisation (§8.2). The ROADMAP (`publications/.../ROADMAP_TO_TOP_VENUES.md` §"Recommended sequencing" item 2) commits to cross-model replication on Llama-3.1-8B-Instruct as the short-term (1–3 month) next step. Rick explicitly picked this as the unit's next research project in the post-checkpoint session.

This Gate-1 entry captures the question and motivation; Gate-2 (Scoping Memo) follows in a subsequent notebook entry; Gate-3 (pre-registration) is drafted at `preregistrations/2026-05-24_personality-mixer_cross-model-llama-3.1-8b-replication_PREREG_v0.md` (status: DRAFT) and will be time-stamped on OSF before any extraction or validation runs begin.

## The question

> Do the 24 activation-steering channels validated on Qwen2.5-7B-Instruct in the v0 personality-mixer publication replicate on Llama-3.1-8B-Instruct under the same multi-layer steering recipe, probe libraries, and judge rubrics?

Three pre-specified hypotheses (full statement + falsification criteria in the pre-reg):

- **H1 (generalisation):** At least 12 of 20 v0 PASS-tier channels reach κ ≥ 0.60 on Llama.
- **H2 (probe-instrument finding generalises):** At least 3 of 4 Dark Tetrad channels show the generic→trait-eliciting flip on Llama.
- **H3 (sadism RLHF-floor is Qwen-specific):** Sadism reaches κ ≥ 0.60 on Llama at c=4.

## Why it matters

Three converging motivations:

1. **Tier-2+ submission gate.** The Psychological Bulletin / Psychological Review submission path requires cross-model replication (R4 in the v0 ROADMAP). Without it, the v0 paper tops out at arXiv + TMLR.

2. **First proper Tier-C pipeline test.** The v0 paper is Tier M precisely because it could not be Tier C — no pre-registration. This cross-model project is the unit's first chance to exercise the full Gate 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 pipeline with a proper OSF time-stamp before any data collection. That's a load-bearing operational test of the unit's standards.

3. **Substantive theoretical importance.** Whether the substrate is Qwen-specific or genuinely cross-model is the load-bearing claim for any generalisable methodological contribution. The H × Dark-Triad coupling finding (§3.7 / §4.3 of v0) only counts as "psychometrically coherent at the vector level" if the same coupling reproduces on a different base model; otherwise it could be a Qwen-architecture artefact.

## Expected tier

**Tier C (Confirmatory).** This is the unit's first project run start-to-finish under the v0.0.4-charter standards with all gates exercised in order. The pre-registration commits to specific hypotheses with falsification criteria before any data collection.

Substrate (the new model + the validation pipeline) is inherited; the *test* is whether the pre-specified expectations hold on a new model. That's the canonical confirmatory shape.

## Anticipated dependencies

- **Llama-3.1-8B-Instruct access:** Meta's gated open-weight model on HuggingFace. Rick's account needs to accept the license agreement; verified gates currently working as of 2026-05-24.
- **Modal L4 GPU compute:** ~2–3 hours per full 24-channel run; ~$2–4 in Modal time.
- **Anthropic Opus judge:** ~$5–10 in API calls per full validation run.
- **The vendored validation harness:** `publications/.../reproducibility-bundle/code/experiments/d4-fader-intervention/harness.py` and `analyse.py` — already supports `model_id` override per `harness.py` line 492 ("`model_id` defaults to Qwen-Instruct; pass EleutherAI/pythia-12b for the H2 test path"); Llama-3.1-8B-Instruct should work as a drop-in.
- **The local SHA f492844 closure for v0** — the v0 paper's headline data for 15 new channels and 4 KILL-rescued channels lives on the MacMini's local SHA f492844 (see `~/.claude/projects/.../memory/reference_macmini-local-sha-f492844.md`). Closing that gap is a precondition for the H1 test because H1 references the v0 PASS-tier as the baseline. Rick has committed (B4 in the post-checkpoint session) to pushing the local SHA from MacMini himself.

## Anticipated risks

1. **Layer-depth alignment heuristic** — Llama has 32 layers vs Qwen's 28. The pre-reg commits to L14/L18/L23 on Llama (matching Qwen's L12/L16/L20 at proportional model depth) but this is heuristic; an alternative layer choice could yield different κ. Mitigation: pre-register the choice; if H1 fails, run a sensitivity analysis post-hoc as a Tier-E follow-up.

2. **Judge model drift** — `claude-opus-4-7` may deprecate before the run completes. Mitigation: pin the judge model at run-start in `seeds.json`; if Anthropic deprecates, amend the pre-reg with the new judge.

3. **Llama RLHF posture wider dual-use surface** — if Dark Tetrad channels are *more* steerable on Llama (because Llama's RLHF is more permissive), the Broader Impacts mitigations (§4.6 of v0) may need re-running before any vector release. Mitigation: per the pre-reg §13, trigger a Responsible-Release Review per CHARTER §11 if this is observed.

4. **HuggingFace gate changes** — Meta could change the Llama-3.1-8B-Instruct access policy between pre-reg and run. Mitigation: pre-reg §12 names Plan B (Mistral-7B-Instruct as a substrate fallback) requiring an amendment.

## Decisions taken in this Gate-1 entry

1. **Project selected from the v0 ROADMAP** rather than starting an unrelated new research line. Rick chose Cross-Model Replication (B7 = Recommended) in the post-checkpoint session.
2. **Tier assignment C, pre-registered.** Not Tier M or Tier E this time. The unit's first proper Tier-C-pipeline run.
3. **Pre-registration draft committed at the same time as this Gate-1 entry** (rather than waiting for Gate 2 / Scoping Memo). Reason: the question is well-defined enough that the pre-reg structure was achievable in one pass; Scoping Memo will follow but won't gate the pre-reg time-stamping.
4. **OSF as the time-stamp venue** (rather than AsPredicted). Reason: this is a non-trivial design with structured H1/H2/H3 family-level binomial tests; OSF's Standard Pre-Registration template accommodates the detail better than AsPredicted's 9-question form.
5. **Cadence sequential after v0 arXiv** per Rick's B8 decision. No extraction or validation runs begin until: (a) the OSF pre-reg time-stamps; (b) the v0 paper is on arXiv; (c) the local SHA f492844 closure lands (so the H1 baseline is verifiable).

## Open threads

- **OSF account setup** (B5): Rick to sign up at osf.io and link ORCID 0009-0004-0799-1756. ~10 min.
- **Pre-reg transcription** to OSF: Rick (or me with copy-paste assistance) transcribes the DRAFT pre-reg into the OSF form. ~30 min.
- **v0 arXiv submission** (B2 + B3): Rick to handle Cowork transcript deposit + browser submission. The cross-model project does not start until v0 is on arXiv.
- **Local SHA f492844 closure** (B4): Rick to push from MacMini.
- **Gate-2 Scoping Memo** for this cross-model project: not yet drafted. Will be written before any data collection, after Rick confirms the OSF pre-reg is time-stamped. Will include: dependencies on the v0 closures, Modal compute budget, expected wall-clock, dual-use Responsible-Release plan.

## AI session notes

This Gate-1 entry was drafted in the same Claude Code session that produced the v0 paper's pre-arXiv work, the autonomous-mode pre-arXiv deliverables, and this checkpoint session. Per CHARTER §10 categorisation, this is a **charter/standards-touching session** (the project this entry opens will exercise the full Tier-C pipeline for the first time, which is operationally significant for the unit's standards). The transcript will be mirrored to `notebooks/2026/05/_transcripts/` if/when Rick exports the Claude Code session — the same procedure as the v0 founding-session entry.

Prompting strategy: Rick set the project ("B7 = Cross-model replication on Llama-3.1-8B"); I drafted the Gate-1 entry against the pre-reg draft I'd written immediately before. Iterative refinement not yet applied — this is the first draft; revisions land via follow-up entries citing this one per CHARTER §10's "Corrections take the form of a new entry that cites the original, not by editing this entry."

---

*This entry is a permanent record. Corrections are made by adding a follow-up entry that cites this one, not by editing this entry.*
