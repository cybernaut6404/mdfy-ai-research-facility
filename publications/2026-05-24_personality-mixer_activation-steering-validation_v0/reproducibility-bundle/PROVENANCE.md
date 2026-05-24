# Provenance — 24-Channel Activation-Steering Validation

The chain of derivation from raw inputs to every headline claim in the
manuscript. Cross-references use the commit SHAs of the source project
repos as committed at the time of pack assembly (2026-05-24).

## Headline claims and their derivation

| Manuscript artifact | Producing script | Inputs | Outputs |
|---|---|---|---|
| §3.1 "20 of 24 channels achieved κ ≥ 0.60" | `mg-digital-twin/experiments/d4-fader-intervention/analyse.py` | Generated response pairs (high/low steering condition) from `harness.py::eval` on Modal L4, processed against `JUDGE_PROMPTS` rubrics | Per-channel κ + win/loss/tie counts in `results/*/results.json` and `results/*/report.md`; aggregated into Tables S1 and §3.1 |
| §3.2 "Probe-instrument finding" — generic vs trait-eliciting κ for Dark Tetrad | `analyse.py` against the same channels run twice with two probe sets | Generic probes: `probes/discriminability.json` (10 generic scenarios). Trait-eliciting probes: `probes/dark-*.json` (14 per channel + 2 QC). Both against the same Dark-Tetrad steering vectors at c = 2 | `runs/<channel>_darkv2/` (trait-eliciting); `runs/<channel>_darkgeneric/` (generic). Both feed `analyse.py` producing two κ values per channel |
| §3.3 "Multi-layer rescue" — single-layer vs ML κ for the original 4 KILLs | `analyse.py` against the same channels run twice with two steering configurations | Single-layer config from the substrate paper's W4 run (L16, c = 0.5). Multi-layer config (L12/16/20, c = 2) re-run for this study | `runs/<channel>_mlretest/` and the substrate-paper's prior `runs/<channel>_w4/` results |
| §3.4 "New-channel scorecard" — κ for the 11 HEXACO / attachment / locus / self-construct channels | `analyse.py` | `probes/new-*.json` (10–12 trait-eliciting + 2 QC per channel); steering vectors from `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/<channel>/vector.pt` | `runs/<channel>_newval/`; aggregated κ values in Table S1 |
| §3.5 "Sadism RLHF-floor" — κ = 0.000 at c = 2 and c = 4 | `analyse.py` for sadism at c = 2 (trait-eliciting); separate diagnostic run at c = 4 | `probes/dark-sadism.json`; sadism vector at L16 from `infra/steering-vectors/qwen2.5-7b-instruct/sadism/vector.pt` | `runs/sadism_darkv2/` (c=2); `runs/sadism_darkv3hi/` (c=4); both 0/0/16 |
| §3.5 "Sycophancy sign-flip" — κ = 0.250 with low-coef winning 3:1 | `analyse.py` for sycophancy at c = 2 (trait-eliciting); analysis of the win-direction | `probes/new-sycophancy.json`; sycophancy vector at L16 | `runs/sycophancy_newval/`; 1W high / 3W low / 8T |
| §3.6 "No new channel reached FLAG" — refusal-direction cosines | `mg-digital-twin/infra/steering-vectors/cosine_probe.py` | Each new channel's vector at L8/12/16/20/24; the refusal-direction vector at the same layers | Per-channel worst-layer \|cos\|; Table S2 |
| §3.7 "H × Dark-Triad coupling −0.32 at L16" — empirical reproduction of the HEXACO finding at the vector level | `mg-digital-twin/infra/steering-vectors/inter_channel_cosines.py` | The 15 new channel vectors at L12/16/20 | Pairwise inter-channel cosine matrix; documented in `inter-channel-cosines-dark-2026-05-23.md` and Table S3 |
| §3.8 "QC probes passed" — no factual-recall degradation under steering | Manual inspection of the `_QC` rows in `results/*/report.md` | Steered generations on QC probes for all 24 channels at c = 2 | No QC failure documented across all 24 channels |
| Table S4 "Orthogonalisation report" | `mg-digital-twin/infra/steering-vectors/orthogonalise.py` (modified Gram-Schmidt) | The 9 validated channel vectors in the order [achievement_striving, cheerfulness, dospert_financial, sociability, stimulation, dospert_recreational, cautiousness, conscientiousness_self_discipline_v3, self_direction] | Min norm-preservation ratio per channel; documented in `orthogonalisation-report-2026-05-08.md` |
| Roadmap document — venue requirements R1–R7 | LLM-originated framework, accepted by the author | The author's "highest-standard methodology + honest limitations + roadmap-to-those-venues" intent | `ROADMAP_TO_TOP_VENUES.md` (Tier 4 contribution per `ai-use-disclosure.md` §2.3) |

## Manual steps

None within the validation pipeline. Every κ value in §3 is produced by
`analyse.py` from `harness.py::eval` outputs, which are produced by the
Modal-deployed `harness.py` on Modal L4. No spreadsheet operations, no
manual coding, no expert-judgment steps within the validation pipeline.

**Manual steps OUTSIDE the validation pipeline** (transparency):
- The contrastive items (n = 30–50 per channel) were authored by hand,
  drawing on the operational definitions in the source instrument (HEXACO-100,
  NEO-PI-R, Schwartz Human Values, DOSPERT, Dark Tetrad short form, ECR-R,
  Rotter Locus of Control, Self-Monitoring Scale, Mach IV), with reference to
  the author's single-subject psychometric battery (15 instruments, completed
  2026-04-15).
- The blind-rater rubrics in `JUDGE_PROMPTS` were authored by hand before
  any judge run.
- The probe libraries (`probes/dark-*.json`, `probes/new-*.json`) were
  authored by hand before any validation run.

These manual artifacts are committed to the source repos at the SHAs named
in §"Inputs" and are not modified after the validation runs began.

## Inputs

The "inputs" to this study are:

1. **Qwen2.5-7B-Instruct** (Qwen Team, 2024) at the Hugging Face checkpoint
   used by Modal (loaded via `transformers` at the version pinned in
   `environment.yml`). The Hugging Face revision SHA is committed in the
   source repo at `mg-digital-twin/infra/extract/qwen_model_card.md`.
2. **The 24 contrastive-item sets**, one per channel, in
   `mg-digital-twin/experiments/contrastive-items/` at commit `f492844`.
3. **The 24 trait-eliciting probe libraries**, in
   `mg-digital-twin/experiments/d4-fader-intervention/probes/` at commit
   `f492844`. The generic-probe library is `probes/discriminability.json`
   at the same commit.
4. **The 24 channel steering vectors** (`vector.pt`), in
   `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/<channel>/`
   at commit `f492844`. Each `vector.pt` carries a SHA-256 used as the
   `steering_vector_ref` in the central DB.
5. **The refusal-direction vector** at the same layers, in
   `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/_refusal/`
   at commit `f492844`.
6. **The judge prompts** (`JUDGE_PROMPTS` dict) in
   `mg-digital-twin/experiments/d4-fader-intervention/analyse.py` at commit
   `f492844`.
7. **The validation harness** (`harness.py`) and the analyser
   (`analyse.py`) in the same directory at the same commit.

## Determinism

- **Decoding:** greedy (`do_sample=False`); see `seeds.json` and manuscript §8.6.
- **Position-randomisation seed:** see `seeds.json`.
- **GPU non-determinism:** Qwen2.5-7B-Instruct inference on Modal L4 is not
  bitwise-deterministic across runs due to floating-point reduction order
  in CUDA kernels. Documented in `seeds.json` §"Non-determinism" and in
  the manuscript §8.6. The κ values are stable under this jitter at the
  reported precision (no κ-value rounding-sensitivity was observed during
  the validation runs).

## Tolerance

For a re-run, the documented tolerance is:

- **κ values:** ±0.05 at the reported precision (3 significant figures).
  This is the tolerance the author would accept as a successful
  replication. Larger deviations would indicate either an environment
  drift or a real change in the underlying substrate behaviour that
  warrants investigation.
- **Refusal-cosine values:** ±0.01.
- **Inter-channel cosines:** ±0.01.

If the replicator finds a κ value outside ±0.05 of the reported value,
they should record the deviation in their own `replication-log.md`
following the unit's replication-log convention.

## License of artifacts

Code (extraction, harness, analyser, steering-server, runner): Apache-2.0,
per the unit's `LICENSE-CODE`.

Content (manuscript, supplementary tables, roadmap, this provenance doc):
CC-BY-4.0, per the unit's `LICENSE-CONTENT`.

Contrastive items + probe libraries + judge rubrics + run artifacts: these
are textual artifacts authored by the author. Released under CC-BY-4.0 per
the unit's content license. **Important caveat:** the contrastive items are
derived from a single-subject psychometric battery (the author's own).
Release of the items implies release of the author's operational
identification of each trait. The author has elected to do this (the
manuscript and bundle are publication-intent), but reviewers should note
that no third-party PII is in the contrastive items.

Steering vectors (`vector.pt` per channel): these are derived from
Qwen2.5-7B-Instruct under its open-weights licence. The vectors themselves
are released under CC-BY-4.0 per the unit's content license; downstream use
is bounded by the original Qwen licence.
