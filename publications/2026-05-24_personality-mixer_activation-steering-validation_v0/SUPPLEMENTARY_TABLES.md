# Supplementary materials

All numbers are read directly from the committed run artifacts; no estimation
or smoothing. Cross-references point to the source files under
`mg-digital-twin/experiments/d4-fader-intervention/` and
`mg-digital-twin/infra/steering-vectors/` at commit `f492844`.

---

## Table S1. Full 24-channel scorecard

ML steering at L12/16/20, |c| = 2.0 (psychopathy also at c = 4),
trait-eliciting D0 probes (12–14 directional + 2 QC per channel), blind-rater
Claude Opus 4.7. Random chance κ = 0.50. Pre-specified gate κ ≥ 0.60.

| # | Channel | Category | κ | High wins | Low wins | Ties | Verdict | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | narcissism | DARK_TETRAD | 1.000 | 7 | 0 | 9 | PASS | perfect |
| 2 | psychopathy | DARK_TETRAD | 1.000 (@c4) | 3 | 0 | 13 | PASS@c4 | RLHF-floored at c=2 |
| 3 | attachment_avoidant | ATTACHMENT | 1.000 | 3 | 0 | 9 | PASS | perfect |
| 4 | hexaco_emotionality | HEXACO | 1.000 | 3 | 0 | 9 | PASS | perfect |
| 5 | honesty_humility | HEXACO | 1.000 | 4 | 0 | 8 | PASS | perfect |
| 6 | machiavellianism | DARK_TETRAD | 0.857 | 6 | 1 | 9 | PASS | |
| 7 | hexaco_extraversion | HEXACO | 0.800 | 4 | 1 | 7 | PASS | |
| 8 | self_monitoring | SELF_CONSTRUCT | 0.800 | 4 | 1 | 7 | PASS | |
| 9 | openness | HEXACO | 0.750 | 3 | 1 | 8 | PASS | **overturns "may not be steerable" caveat** |
| 10 | hexaco_agreeableness | HEXACO | 0.750 | 6 | 2 | 4 | PASS | |
| 11 | achievement_striving | DRIVE | 0.740 | — | — | — | PASS | from prior validation, single-layer L16 c=0.5 |
| 12 | dospert_recreational | RISK | 0.722 | 13 | 5 | 12 | PASS | rescued from KILL by ML |
| 13 | cheerfulness | AFFECT | 0.700 | — | — | — | PASS | prior; vector now points to _ct variant |
| 14 | locus_of_control | AGENCY | 0.667 | 6 | 3 | 3 | PASS | |
| 15 | attachment_anxious | ATTACHMENT | 0.667 | 2 | 1 | 9 | PASS | |
| 16 | self_direction | AGENCY | 0.667 | 2 | 1 | 27 | PASS | rescued; very high tie count |
| 17 | dospert_financial | RISK | 0.660 | — | — | — | PASS | prior; refusal-cosine FLAG (clamp) |
| 18 | sociability | HEXACO | 0.640 | — | — | — | PASS | prior |
| 19 | conscientiousness_self_discipline | DISCIPLINE | 0.636 | 14 | 8 | 8 | PASS | rescued (v3 vector) |
| 20 | stimulation | DRIVE | 0.630 | — | — | — | PASS | prior |
| 21 | cautiousness | DISCIPLINE | 0.583 | 7 | 5 | 18 | borderline | just under gate |
| 22 | self_defeat | SELF_CONSTRUCT | 0.500 | 1 | 1 | 10 | borderline | high tie count |
| 23 | sycophancy | SELF_CONSTRUCT | 0.250 | 1 | 3 | 8 | sign-inverted | steerable, negate coef |
| 24 | sadism | DARK_TETRAD | 0.000 | 0 | 0 | 16 | RLHF-floored | indistinguishable at c=2 AND c=4 |

**Aggregate:** 20 PASS · 2 borderline (cautiousness, self_defeat) · 1 sign-flip
(sycophancy) · 1 RLHF-floored (sadism).

---

## Table S2. Refusal-direction cosine probe (AlphaSteer protocol)

Worst-layer |cos(channel, refusal)| across L8/12/16/20/24. Threshold convention
(Anthropic Persona Vectors 2025 §6): SAFE < 0.1, watch 0.1–0.3, FLAG ≥ 0.3.

| Channel | Worst layer | \|cos\| | Status |
|---|---|---|---|
| narcissism | 12 | 0.017 | SAFE |
| attachment_anxious | 12 | 0.058 | SAFE |
| sycophancy | 12 | 0.045 | SAFE |
| hexaco_emotionality | 20 | 0.087 | SAFE |
| honesty_humility | 16 | 0.103 | watch |
| locus_of_control | 12 | 0.108 | watch |
| sadism | 16 | 0.133 | watch |
| hexaco_agreeableness | 12 | 0.158 | watch |
| psychopathy | 12 | 0.160 | watch |
| openness | 12 | 0.171 | watch |
| machiavellianism | 16 | 0.218 | watch |
| hexaco_extraversion | 16 | 0.226 | watch |
| self_monitoring | 12 | 0.240 | watch |
| attachment_avoidant | 12 | 0.253 | watch |
| self_defeat | 12 | 0.295 | watch |

The 9 originally-validated channels' refusal-cosine values are reported in the
substrate paper (refusal-cosines-w4-2026-05-07.md): cheerfulness 0.133 watch,
sociability 0.150 watch, achievement_striving 0.111 watch, stimulation 0.046
SAFE, dospert_financial **0.310 FLAG** (the only FLAG in the full 24-channel
substrate; coefficient-clamped to |c| ≤ 1 in deployment), cautiousness 0.164
watch.

**No new channel reached FLAG.** Maximum |cos| in the new 15 was 0.295
(self_defeat at L12), just under threshold.

---

## Table S3. Inter-channel cosine — selected pairs (L16)

Full matrix (15 channels × 15 channels) at L12, L16, L20 in
`infra/steering-vectors/inter-channel-cosines-dark-2026-05-23.md`. Selected
pairs that bear on construct validity:

| Pair | cos(L16) | Interpretation |
|---|---|---|
| machiavellianism × sadism | +0.377 | dark-tetrad cluster (expected) |
| attachment_avoidant × self_defeat | +0.512 | strongest non-trivial pair |
| psychopathy × attachment_avoidant | +0.447 | callousness ↔ detachment |
| psychopathy × self_defeat | +0.370 | dark cluster |
| **honesty_humility × machiavellianism** | **−0.315** | **H × Dark-Triad coupling, empirically confirmed at the vector level** |
| **honesty_humility × psychopathy** | **−0.321** | **H × Dark-Triad coupling** |
| honesty_humility × self_defeat | −0.257 | H × negative-self coupling |
| self_defeat × dospert_financial | −0.407 | self-defeat ↔ financial risk (inverse) |

The negative honesty_humility × dark-tetrad cosines at the vector level
correspond to the published psychometric H × Dark-Triad correlation of
r ≈ −0.55 to −0.65 (Lee & Ashton, 2014). The vector-level magnitude (−0.32) is
attenuated relative to the psychometric correlation, consistent with each
vector capturing only a subset of the corresponding latent construct's variance.

---

## Table S4. Orthogonalisation report (Gram-Schmidt, validated 9)

Norm preservation ratios from the modified Gram-Schmidt orthogonalisation in
order [achievement_striving, cheerfulness, dospert_financial, sociability,
stimulation, dospert_recreational, cautiousness, conscientiousness_self_discipline_v3,
self_direction], rescaled to original L2 norm.

| Channel | Min norm-preservation ratio | Interpretation |
|---|---|---|
| achievement_striving | 1.000 | orthogonal first (anchor) |
| cheerfulness | 0.979 | mostly orthogonal |
| dospert_financial | 0.984 | mostly orthogonal |
| cautiousness | 0.940 | mostly orthogonal |
| conscientiousness_self_discipline_v3 | 0.886 | moderate prior overlap |
| sociability | 0.879 | moderate prior overlap |
| stimulation | 0.825 | moderate prior overlap |
| self_direction | 0.792 | largest projection-out — interpretation requires care |
| dospert_recreational | 0.788 | largest projection-out — risk-cluster overlap with financial |

Post-orthogonalisation max |cos| ≈ 1e-7 (machine epsilon for fp32 on 3584-dim
vectors). Full per-layer table in
`infra/steering-vectors/orthogonalisation-report-2026-05-08.md`.

---

## Table S5. Probe library inventory

Channel-specific probe libraries in `mg-digital-twin/experiments/d4-fader-intervention/probes/`:

**Original 9 (channel-specific, pre-existing):**
achievement-striving.json, cheerfulness.json, sociability.json, stimulation.json,
dospert-financial.json, dospert-recreational.json, cautiousness.json,
self-direction.json, conscientiousness-self-discipline.json.

**Dark-Tetrad (new, this study):**
dark-machiavellianism.json, dark-narcissism.json, dark-psychopathy.json,
dark-sadism.json — 14 directional + 2 QC each.

**HEXACO / attachment / locus / self-construct (new, this study):**
new-honesty_humility.json, new-hexaco_agreeableness.json, new-hexaco_emotionality.json,
new-hexaco_extraversion.json, new-openness.json, new-attachment_anxious.json,
new-attachment_avoidant.json, new-locus_of_control.json, new-self_defeat.json,
new-self_monitoring.json, new-sycophancy.json — 10–12 directional + 2 QC each.

**Generic (for the contrast finding in §3.2):**
discriminability.json — 10 generic scenario probes from Rimsky et al. recipe.

---

## Table S6. Judge rubric inventory (verbatim system + question)

All 24 channels' blind-rater rubrics are in
`mg-digital-twin/experiments/d4-fader-intervention/analyse.py`, dict
`JUDGE_PROMPTS`. Format per channel: system prompt defining high/low pole
behaviourally + a single forced-choice question "Which response shows more
{trait}? A, B, or TIE." Position (A vs B) randomised per pair via a fixed seed
to control position bias.

**The rubrics are reproduced verbatim in the source file** to enable
independent replication. No rubric was modified after seeing any validation
result.

---

## Table S7. Run artifact pointers

For independent verification, raw run artifacts are committed to
`mg-digital-twin/experiments/d4-fader-intervention/`:

- `runs/<channel>_darkv2/` — Dark-Tetrad gen at c=2 with trait-eliciting probes
- `runs/<channel>_darkv3hi/` — Dark-Tetrad gen at c=4 (psych+sadism only)
- `runs/<channel>_mlretest/` — Original 4 KILL channels at ML c=2
- `runs/<channel>_newval/` — 11 new channels at ML c=2
- `results/*/report.md` — Per-channel judge reports with full per-coef tables
- `results/*/results.json` — Machine-readable κ + per-probe breakdowns

Each `report.md` includes the per-coefficient table from which Table S1 numbers
are drawn, plus all individual high/low/tie counts.

---

## Compute and cost provenance

- **GPU:** all validation runs on Modal L4 (24 GB, ~$0.80/hr per-second-billed)
  except the original 9-channel single-layer runs which used A100-40GB
  (predates the L4 migration).
- **Total Modal cost for this study:** approximately $8–15 across all
  validation and re-test runs (4 dark + 4 KILL re-test + 11 new + 2 dark
  diagnostic c=4 = ~21 runs, average ~2–3 min generation each).
- **Judge cost (Anthropic Opus):** approximately $5–8 across all judge runs.
- **Steering-server deploy + idle:** scales to zero between requests; near-zero
  standing cost.
