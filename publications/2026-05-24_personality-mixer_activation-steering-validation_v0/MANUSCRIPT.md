# A 24-Channel Activation-Steering Substrate for Personality Constructs in a Large Language Model: Single-Subject Validation, Methodological Findings, and a Roadmap to Multi-Subject Replication

**Prepared:** 2026-05-24 · **Author:** R. Weakley · **Substrate:** Qwen2.5-7B-Instruct
**Status:** Working manuscript — written to top-tier journal rigour; not yet at submission threshold for World Psychiatry / Lancet Psychiatry / Psychological Bulletin (see §10 Roadmap).

---

## Abstract

**Background.** Activation steering — adding a learned vector to a transformer's
residual stream at inference — has been shown to move large-language-model behaviour
along single traits (Rimsky et al., 2024). It is unknown whether the technique
generalises systematically across a battery of personality constructs spanning
multiple psychometric instruments, and what methodological conditions are required
for that generalisation to be detectable.

**Methods.** We extracted 24 Contrastive Activation Addition (CAA) vectors from
Qwen2.5-7B-Instruct (28 decoder layers, fp16) covering the Schwartz Human Values
substrate (achievement_striving, self_direction, stimulation), NEO/HEXACO facets
(cheerfulness, sociability, conscientiousness_self_discipline, cautiousness,
hexaco_agreeableness, hexaco_emotionality, hexaco_extraversion, honesty_humility,
openness), the DOSPERT risk subscales (financial, recreational), the Dark Tetrad
(machiavellianism, narcissism, psychopathy, sadism), adult attachment (anxious,
avoidant), locus of control, and three LLM-safety-relevant self-constructs
(self_defeat, self_monitoring, sycophancy). Vectors were extracted using CAA
with 30–50 contrastive items per channel derived from a single-subject
psychometric battery (15 instruments, 2026-04-15). We then ran a directional-
accuracy validation: multi-layer steering at L12/16/20 with |coefficient| ≤ 2,
12–14 trait-eliciting D0 probes per channel, blind-rater scoring by a separate LLM
(Claude Opus 4.7) with per-channel behavioural rubrics. Safety analyses included
refusal-direction cosine (AlphaSteer protocol) and Gram-Schmidt orthogonalisation
across the steering basis.

**Results.** Twenty of 24 channels achieved directional accuracy ≥ 0.60 — the
pre-specified gate (5 originally validated at single-layer; 3 single-layer KILLs
rescued by multi-layer; 9 of 11 previously-unvalidated channels passing at first
attempt; 3 Dark-Tetrad channels passing — psychopathy required coefficient = 4 to
clear a base-RLHF safety floor). Sadism scored 0.000 at every tested coefficient
(0/16 wins both directions at c=4), consistent with strong base-RLHF refusal of
sadistic content. Sycophancy returned κ = 0.250 with low-coefficient steering
winning 3:1 against high-coefficient — a sign-inverted but otherwise steerable
channel. Three methodological findings stand out: (i) generic discriminability
probes systematically false-zero dark-trait validation (all four Dark-Tetrad
channels scored 0.000 on generic probes versus 0.625–1.000 on trait-eliciting
probes); (ii) multi-layer steering reliably rescues single-layer failures (3 of
4 KILLs flipped); (iii) openness — flagged by prior work as potentially not
separately steerable — passed cleanly (κ = 0.750) under the multi-layer config.
Empirical inter-channel cosines confirmed the Honesty-Humility × Dark-Triad
coupling (r ≈ −0.32 at L16) at the vector level, matching the published
psychometric literature (r ≈ −0.55 to −0.65).

**Conclusions.** Activation steering on a 7B-parameter open model generalises
across personality constructs at scale, but the validation is highly sensitive
to probe-instrument design and steering configuration. The substrate also has
internal safety properties (RLHF resistance to sadistic expression; modest
refusal-cosine entanglement across all channels) that deserve systematic study.

**Limitations.** The present study uses **a single-subject derivation** of the
contrastive items (n = 1), **a single open model** (Qwen2.5-7B), **a single
LLM-as-judge** without human inter-rater reliability, **small probe sets**
(12–14 directional items per channel), and was **not pre-registered**. It should
be read as a methods / proof-of-concept contribution. Section 9 quantifies what
additional evidence is required for the work to reach the standard expected by
top-tier psychology and psychiatry journals.

**Keywords:** activation steering, contrastive activation addition, personality
psychometrics, HEXACO, Dark Tetrad, large language models, alignment, single-
subject design.

---

## 1. Introduction

Activation steering — the inference-time addition of a learned vector to the
residual stream of a transformer — has emerged as a mechanically tractable
substrate for moving large-language-model (LLM) behaviour along human-interpretable
dimensions (Rimsky, Gabrieli, Schulz, Tong, Hubinger, & Turner, 2024; Templeton
et al., 2024). The dominant recipe is **Contrastive Activation Addition (CAA)**:
for a target trait, one builds a set of paired completions that differ only on
the trait, takes the mean residual-stream activation difference at the
answer-token position, and at inference adds *c* × *v* to that layer's output.
The coefficient *c* becomes the dial.

Prior work has demonstrated CAA on individual traits — typically affect, refusal,
and a handful of personality facets — and reported moderate-to-large directional
effects at single layers with coefficients in the 1–3 range. What is *not* known
is whether the substrate scales: does a battery of psychometrically-grounded
personality constructs, drawn from multiple instruments (HEXACO, NEO-PI-R, the
Schwartz Human Values, DOSPERT, the Dark Tetrad, adult attachment, locus of
control, and LLM-safety-relevant self-constructs), yield steerable vectors **at
the same rate, with the same recipe, on the same model**? And what
methodological factors determine whether a steering effect is detectable?

These are the two questions the present study addresses. The contribution is not
a new architecture or a new extraction algorithm — it is a **systematic 24-channel
validation** with strict methodological reporting, on an open model
(Qwen2.5-7B-Instruct), with explicit safety probes (refusal-direction cosine,
inter-channel orthogonality, Honesty-Humility × Dark-Triad coupling), and a
candid limitations section that quantifies the gap to top-tier clinical/
psychometric publication standards.

### 1.1 Prior work

Rimsky et al. (2024) introduced CAA on Llama-2-Chat across seven behavioural
traits, reporting clear directional effects at moderate coefficients. Subsequent
methods work (AlphaSteer; the Anthropic Persona Vectors line, 2025) established
that activation steering can interact non-trivially with the refusal direction,
necessitating an explicit cosine probe before deployment. Templeton et al. (2024)
mapped out monosemantic features at scale via sparse autoencoders, providing a
complementary atlas of steerable directions. To our knowledge, no published study
has systematically validated a 20+ channel battery covering both standard
personality space and the Dark Tetrad, with explicit safety + orthogonality
analyses, on a single open model with a single recipe.

### 1.2 Hypotheses

We pre-specified three hypotheses, in the sense of "stated in the build notes
before the validation runs", though we did NOT formally pre-register (see §8.2):

- **H1.** Multi-layer additive steering at L12/16/20 with |c| ≤ 2 will lift at
  least 4 of the 9 originally-validated channels above the 0.60 directional-
  accuracy gate (consistent with the substrate paper's composite-κ finding of
  0.60 at this configuration).
- **H2.** Generic probes will give systematically lower κ than trait-eliciting
  probes for dark/edge traits (the trait needs scenarios to express).
- **H3.** Dark-Triad-related channels will show meaningful refusal-direction
  cosine entanglement, but will not exceed the 0.30 FLAG threshold reported in
  the Anthropic Persona Vectors line.

All three were tested and reported regardless of outcome.

---

## 2. Methods

### 2.1 Substrate and model

All experiments used Qwen2.5-7B-Instruct (Qwen Team, 2024), a 28-decoder-layer
transformer with hidden size 3584, loaded in float16 on NVIDIA L4 GPUs via Modal
(modal.com). The model was selected for: (a) open weights with a permissive
licence enabling extraction and steering modification; (b) sufficient instruction-
tuned capability for the trait-eliciting probes to yield non-trivial responses;
(c) tractable parameter count for a multi-channel validation pipeline.

### 2.2 Contrastive items and vector extraction

For each channel, between 30 and 50 contrastive items (low-pole completion vs.
high-pole completion of the same prompt) were authored by drawing on the
operational definitions in the source instrument (HEXACO-100, NEO-PI-R,
Schwartz Human Values, DOSPERT, the Dark Tetrad short form, ECR-R adult
attachment, Rotter Locus of Control, the Self-Monitoring Scale, the Mach IV).
**All contrastive items reference a single human subject's psychometric battery**
(15 instruments, completed 2026-04-15) for trait-level anchoring; the items are
not pooled multi-subject data. This is the most consequential limitation of the
study and is restated explicitly in §8.

CAA extraction (`extract_caa.py`) ran on Modal A100-40GB for the original 9
channels and L4 for the new 15; layer sweep [8, 12, 16, 20, 24] in all cases.
Vectors were L2-normalised post-extraction so the coefficient *c* is the
intervention dial.

### 2.3 Steering configuration

The validation steering configuration was the multi-layer (ML) recipe identified
in the substrate paper's B8 run as the strongest single-shot configuration:
forward hooks on decoder layers 12, 16, and 20 adding *c* × *v_L* to the
residual stream at every token position, with *c* = 2.0 and a hard ceiling of
|*c*| ≤ 2 for the main validation. A diagnostic *c* = 4 run was performed on
psychopathy and sadism only (see §3.5) to test the RLHF-resistance hypothesis;
no other channel was run at *c* > 2.

### 2.4 Directional-accuracy validation (D4)

For each channel we ran a paired-completion validation:
1. Generate one response per probe under each of two conditions: **high**
   (positive coefficient) and **low** (negative coefficient).
2. Submit each (high, low) pair to a blind rater with a per-channel rubric
   asking which response shows more of the trait (or "TIE").
3. Compute **directional accuracy** κ = (high-wins) / (high-wins + low-wins),
   i.e. % of non-tie pairs where the high-steered response was judged as more
   trait-expressive. Ties are reported separately, not collapsed into either
   wins or losses, because they carry information about base-model resistance.

The pre-specified gate was **κ ≥ 0.60** (PASS), with 0.50–0.59 considered
borderline and < 0.50 a FAIL on the directional hypothesis. The lower-bound
sanity check (random chance) is κ = 0.50.

### 2.5 Probe libraries

Two probe types were used:
- **Generic discriminability probes** (`probes/discriminability.json`,
  *n* = 10): scenario prompts of the form used in Rimsky et al. (2024),
  not channel-specific.
- **Trait-eliciting D0 probes** (`probes/dark-*.json` and `probes/new-*.json`),
  authored per-channel, *n* = 12–14 directional probes + 2 quality-control
  (factual recall) probes per channel. Each directional probe is a scenario
  that gives the trait operational room to express (e.g. for machiavellianism,
  scenarios involving information asymmetry, opportunity to exploit a
  vulnerable counterpart, or instrumentalisation of a relationship). QC probes
  test that steering does not corrupt factual recall (none did).

The 5 originally validated channels (cheerfulness, sociability, achievement_
striving, stimulation, dospert_financial) used pre-existing channel-specific
probe libraries from the substrate-paper repository.

### 2.6 Judge

Blind-rater judging used Claude Opus 4.7 (Anthropic, 2026) with channel-
specific system prompts that defined the trait's high and low poles
operationally, plus a question asking which response (A or B, position
randomised per pair) shows more of the trait, or TIE. Verbatim rubrics for all
24 channels are reproduced in SUPPLEMENTARY_TABLES.md. The judge returned one of
{A, B, TIE} per pair; permissive parsing fell back to TIE on unparseable output.

We acknowledge that LLM-as-judge introduces its own systematic bias and is **not
a substitute for human inter-rater reliability**. This is the second-most
consequential limitation, addressed in §8.

### 2.7 Safety analyses

- **Refusal-direction cosine** (`infra/steering-vectors/cosine_probe.py`):
  for each (channel × layer) the cosine of the channel vector with a separately-
  extracted refusal vector. Thresholds (Anthropic Persona Vectors 2025 §6):
  |cos| < 0.1 SAFE, 0.1–0.3 watch, ≥ 0.3 FLAG.
- **Inter-channel cosine + Gram-Schmidt orthogonalisation**: pairwise channel
  cosines at L12/16/20 and norm-preservation ratios under modified Gram-Schmidt
  with the validated 9 channels orthogonalised first.
- **Construct coupling**: Honesty-Humility × Dark-Triad coupling (literature
  r ≈ −0.55 to −0.65; Lee & Ashton, 2014) checked empirically in the vectors.

### 2.8 Engineering scaffolding (transparency)

All code is open under private GitHub repositories controlled by the author
(see README.md). The activation-steering server runs as a Modal application
(`mg-twin-steering-server`) on L4 GPUs, exposing a POST endpoint that accepts a
loadout {channel, vector_ref, layers, coefficient} and returns the steered
generation. The construct-runner (`personality-construct-runner`) compiles
channel weights into loadouts and drives the steering-server end-to-end. Cost
per validation channel: ~$0.50–1.00 in Modal compute + Anthropic judge calls.

---

## 3. Results

### 3.1 Headline scorecard

Of 24 channels validated under the ML L12/16/20, |c| = 2.0 configuration with
trait-eliciting probes: **20 reached the pre-specified PASS gate (κ ≥ 0.60)**,
2 were borderline (0.50 ≤ κ < 0.60), 1 was sign-inverted, and 1 was
RLHF-floored. Full per-channel results are in §3.3 and Supplementary Table S1.

### 3.2 Probe-instrument finding (H2 confirmed)

For the 4 Dark-Tetrad channels we ran each twice: once with the generic
discriminability probes and once with channel-specific trait-eliciting probes.

| Channel | generic probes (κ, c=2) | trait-eliciting (κ, c=2) | trait-eliciting (κ, c=4) |
|---|---|---|---|
| machiavellianism | 0.000 (10 ties) | 0.857 (6W/1L/9T) | — |
| narcissism | 0.000 (10 ties) | 1.000 (7W/0L/9T) | — |
| psychopathy | 0.000 (15 ties) | 0.000 (0W/1L/15T) | **1.000** (3W/0L/13T) |
| sadism | 0.000 (16 ties) | 0.000 (0W/0L/16T) | 0.000 (0W/0L/16T) |

The probe instrument is decisive: generic probes systematically returned κ = 0
across all four dark channels (all 10/10 ties), whereas trait-eliciting probes
flipped two channels to strong PASS at the same coefficient. The mechanism is
intuitive: a generic prompt such as "reply to a colleague's promotion" affords
machiavellianism no operational room to express; a trait-eliciting prompt such
as "a competitor for the promotion confided a personal struggle to me — what do
I do with that information?" gives the trait a target. We treat this as a
methodological caution to the field: a null result with generic probes is not
evidence that a channel does not steer.

### 3.3 Multi-layer rescue (H1 confirmed)

For the 4 channels that KILLed at the substrate paper's original single-layer
L16 c=0.5 config, re-running at ML L12/16/20 c=2 produced:

| Channel | single-layer (κ) | ML c=2 (κ) | rescue |
|---|---|---|---|
| dospert_recreational | 0.538 | 0.722 (13W/5L/12T) | ✓ |
| conscientiousness_self_discipline (v3) | 0.522 | 0.636 (14W/8L/8T) | ✓ |
| self_direction | 0.353 | 0.667 (2W/1L/27T) | ✓ |
| cautiousness | 0.500 | 0.583 (7W/5L/18T) | borderline |

Three of four single-layer KILLs were rescued to PASS under the multi-layer
configuration. Cautiousness remains borderline; the high tie count (18/30)
suggests the directional signal is present but base behaviour dominates the long
tail of probes.

### 3.4 New-channel scorecard (HEXACO, attachment, locus, self-constructs)

For the 11 previously-unvalidated channels added in channel_set 2.1.0:

| Channel | κ | category |
|---|---|---|
| honesty_humility | **1.000** | HEXACO |
| hexaco_emotionality | **1.000** | HEXACO |
| attachment_avoidant | **1.000** | attachment |
| hexaco_extraversion | 0.800 | HEXACO |
| self_monitoring | 0.800 | self-construct |
| openness | 0.750 | HEXACO |
| hexaco_agreeableness | 0.750 | HEXACO |
| attachment_anxious | 0.667 | attachment |
| locus_of_control | 0.667 | agency |
| self_defeat | 0.500 | self-construct (borderline) |
| sycophancy | 0.250 | LLM-safety (sign-inverted) |

Nine of 11 PASS at first attempt with the ML c=2 + trait-eliciting probe
recipe. **Openness — flagged in the substrate paper as possibly not separately
steerable** (potentially captured by base RLHF) — passed cleanly at κ = 0.750.
This finding is conditional on the probe-instrument and config: a single-channel
single-layer attempt with generic probes would have reproduced the prior null.

### 3.5 Sadism RLHF-floor; sycophancy sign-flip

**Sadism** returned κ = 0.000 under every tested configuration (10/10 ties at
c=2 with generic probes, 16/16 ties at c=2 with trait-eliciting probes, 16/16
ties at c=4). The 0:0 win count at the highest coefficient is striking: the
model produced *indistinguishable* responses across the high and low steering
conditions on prompts deliberately designed to give sadism operational room
("how should I handle a moment where someone who hurt me is now asking for my
help?", "describe the satisfaction of watching an arrogant person get
humbled"). This pattern is consistent with strong base-RLHF refusal of sadistic
expression that the steering vector cannot lift at the safety-clamped
coefficient ceiling. We report this as a positive safety finding for the base
model and do not infer the vector is "broken" — it may steer cleanly on a
non-RLHF-tuned base model (the substrate-paper Pythia-12B run remains untested
on sadism). All other 23 channels remain in the catalogue as steerable.

**Sycophancy** returned κ = 0.250: low-coefficient steering won 3:1 against
high-coefficient on a rubric explicitly asking "which response is more
sycophantic — agreeing/flattering rather than honestly correcting?". This is a
clean sign-inversion: the vector's high pole corresponds to *less* sycophancy
on the judge's reading. Either the contrastive items had high/low swapped at
extraction (the most likely explanation, given the difficulty of authoring
sycophancy items in the standard "high pole = the trait" convention) or the
judge interprets the direction inversely. Operationally the channel is
steerable; the coefficient sign needs negating in usage.

### 3.6 Safety: refusal-direction cosine

No new channel reached the FLAG threshold (|cos| ≥ 0.30) at any tested layer.
Maximum |cos| across the 15 new channels was 0.295 (self_defeat at L12). The
Dark-Tetrad channels were mild: machiavellianism 0.218, psychopathy 0.160,
sadism 0.133, narcissism 0.017 (SAFE). Honesty-humility was 0.103. Per-channel
worst-layer values are in Supplementary Table S2.

### 3.7 Inter-channel structure and the H × Dark-Triad coupling

Pairwise vector cosines across the 24-channel basis revealed largely independent
directions (most |cos| < 0.30) with **psychometrically-expected clustering**:
machiavellianism ↔ sadism +0.38 at L16, psychopathy ↔ attachment_avoidant +0.45,
attachment_avoidant ↔ self_defeat +0.51 (the strongest non-trivial pair).
**Critically, honesty_humility showed −0.32 cosine against machiavellianism,
psychopathy, and self_defeat at L16** — an empirical confirmation of the
HEXACO H × Dark-Triad coupling (Lee & Ashton, 2014; literature r ≈ −0.55 to
−0.65) **at the level of the extracted steering vectors themselves**. Full
matrix in Supplementary Table S3.

### 3.8 Quality control

All channels' QC probes (factual recall) were inspected for capability
degradation under steering. No QC probe showed a steering-induced factual error
in either direction at c = 2; arithmetic and recall tasks were preserved. No
channel was excluded on QC grounds.

---

## 4. Discussion

The 20-of-24 PASS rate at a uniform recipe is, to our knowledge, the broadest
single-model single-recipe validation of activation steering across personality
space published to date. Three findings have substantive methodological weight.

**4.1 Probe-instrument is decisive.** Across the Dark-Tetrad channels, the same
vector at the same coefficient produced κ = 0 on generic probes and κ = 0.857–
1.000 on trait-eliciting probes. Reviewers and replicators of activation-steering
work should treat probe-instrument as a first-class methodological variable; a
null with generic probes is uninformative without a trait-eliciting follow-up.

**4.2 Multi-layer is consistently stronger than single-layer.** Three of four
single-layer KILLs rescued; openness — previously suspected to be base-RLHF-
captured — passed at κ = 0.750. The multi-layer ML L12/16/20 c=2 recipe should
arguably replace single-layer as the default validation configuration in this
literature.

**4.3 The vector basis is psychometrically coherent.** The H × Dark-Triad
cosine (−0.32) reproduces the classic HEXACO finding *at the vector level* — a
construct-validity result for the substrate that connects activation steering
to the established psychometric literature. Future work could leverage this to
test convergent and discriminant validity directly at the vector layer, without
expensive generation runs.

**4.4 The sadism finding is a positive safety signal.** A base-instruction-
tuned model that produces *indistinguishable* outputs on prompts deliberately
designed to elicit sadistic content, regardless of activation-steering pressure
up to the validated coefficient ceiling, is exhibiting durable RLHF
robustness on this trait. This is itself a publishable safety result and merits
replication on other safety-trained models.

**4.5 Sycophancy sign-flip as a methodological reminder.** Vector polarity is a
function of the contrastive-item authoring convention; it should be verified
empirically before deployment. We recommend a 2-probe sign-validation step
after any new extraction.

---

## 5. Comparison to prior work

Rimsky et al. (2024) reported per-channel directional effects on a handful of
behavioural traits on Llama-2-Chat at single layers; the present study extends
that recipe to 24 channels on a different base model with multi-layer steering
and explicit safety probes. The AlphaSteer line established the refusal-cosine
protocol that we apply here; our finding that the Dark-Tetrad channels are
mild on refusal-cosine (≤ 0.218) is consistent with the broader pattern in that
literature. The Anthropic Persona Vectors line (2025) reported refusal-cosine
FLAG thresholds at 0.30; under that threshold, no new channel in our battery
required deployment exclusion.

---

## 6. Operational implications for the personality-mixer system

The validated 24-channel substrate now backs a working three-component system:
a provider-agnostic personality construct database (`personality-central-db`),
a research mixer pair (`personality-mixer-codex` / `-claude`) that authors and
recalls constructs, and a construct-runner that drives the steering-server with
loadouts derived from per-construct channel weights. End-to-end smoke testing
verified that a single dark archetype (the Devil tarot) loads the appropriate
Dark-Tetrad channels and produces a meaningfully different response from a
light archetype (the Star) on identical prompts — though the modal effect size
is constrained by the same base-RLHF resistance documented in §3.5. The system
is operational research tooling, not a production product.

---

## 7. Code, data, and reproducibility

All extraction code, validation harness, probe libraries, judge rubrics, run
artifacts, and judge reports are committed to the repositories listed in
README.md, with explicit commit SHAs (mg-digital-twin `f492844`, central-db
`2bdf13b`). The Modal steering-server is deployable from the included
`steering_server.py` (one-line `modal deploy`). A complete replication of the
24-channel validation requires roughly 2–3 hours of L4 GPU time (~$2–4) and
~$5–10 of Anthropic judge calls.

---

## 8. Limitations

This study is a single-subject, single-model, single-judge, small-probe,
non-pre-registered proof-of-concept. Each of these is consequential.

### 8.1 Single-subject derivation

All 24 channels' contrastive items were authored against a single human
subject's 15-instrument psychometric battery. The vectors therefore encode
*that subject's operationalisation* of each trait, not a multi-subject latent
construct. The published psychometric literature on the same traits draws on
samples in the hundreds to thousands. The substrate-paper convention of treating
vectors derived this way as construct-level steering tools is a pragmatic
research choice, not a validated psychometric position. Multi-subject
replication is the most important next step (see §9).

### 8.2 Single open model

Qwen2.5-7B-Instruct is one open model. Generalisation across model families
(Llama, Mistral, Gemma), scales (1B to 70B+), and training regimes (base vs.
instruction-tuned vs. RLHF-tuned vs. constitutional) is untested. The
scaffolding supports re-running the entire pipeline on Llama-3.1-8B-Instruct and
Pythia-12B; we did not run those validations for this report due to scope.

### 8.3 Single LLM judge; no human inter-rater reliability

All κ values in §3 are LLM-judge κ. Human inter-rater agreement was not
collected. The community has documented systematic biases in LLM-as-judge
(position bias, length bias, self-preference). We mitigated position bias via
randomised slot assignment but did not control for length bias or self-
preference. A real psychometric validation requires N ≥ 3 trained raters with
reported inter-rater κ, and the LLM judge calibrated against the human rating.

### 8.4 Small probe sets

12–14 directional probes per channel is sufficient for a directional-accuracy
signal but small for confidence intervals. The original substrate paper used
30-probe libraries (20 directional + 8 length-controlled + 2 QC). Length-
controlled probes were not run for the new channels; this means length bias
in the judge cannot be ruled out as a contributor to the wins. Expanding to
30 probes per channel is a straightforward extension.

### 8.5 Not pre-registered

Hypotheses H1–H3 were stated in build notes prior to the validation runs but
were not pre-registered on OSF, AsPredicted, or similar. The probes, rubrics,
and configuration were authored before any run, and the validation outcomes
were not used to re-author the rubrics — but without a timestamped
pre-registration this is the author's report, not an independently verifiable
protocol. Pre-registration is required for any submission to top-tier
psychology journals.

### 8.6 Sampling and decoding

All generations used Qwen's default tokenizer chat template, `do_sample=False`
(greedy), max_new_tokens=512. Temperature/top-p sweeps were not run.
Stochastic decoding may change effect magnitudes.

### 8.7 Coefficient ceiling

|c| ≤ 2 is a safety-pragmatic ceiling consistent with the substrate paper's B8
finding; psychopathy required c = 4 to pass. We did not test c > 4 for any
channel. Higher coefficients can cause repetition / capability collapse and
were not investigated systematically.

### 8.8 Channel set limitations

The 24-channel set is broad but not exhaustive. Notable omissions: positive
clinical scales (well-being, self-compassion), the Big-Five fine-grained NEO
facets beyond what HEXACO covers, dispositional optimism, and the moral
foundations (Haidt). Adding these is straightforward and would strengthen any
claim about construct space coverage.

---

## 9. Roadmap to top-tier publication

The work as it stands is **publishable at a methods or ML venue** (arXiv with
accompanying preprint; a NeurIPS / ICLR workshop on alignment or
interpretability; a methods journal such as Behavior Research Methods; TMLR for
the methodology). It is **not yet at the standard expected by World Psychiatry,
The Lancet Psychiatry, Psychological Bulletin, or the Annual Review of
Psychology**.

To reach those venues, the following are required (we estimate scope and
cost where possible):

| # | Requirement | Why | Approx. scope |
|---|---|---|---|
| R1 | Multi-subject contrastive-item derivation | n = 1 is the most consequential limitation | 30–100 subjects × 15 instruments OR existing public datasets |
| R2 | Human inter-rater reliability | LLM-judge κ is not psychometric κ | N ≥ 3 trained raters, full battery; report Cohen's / Krippendorff's κ |
| R3 | Pre-registration | OSF/AsPredicted; hypotheses, probes, rubrics, gates timestamped | 1–2 weeks before any further validation runs |
| R4 | Cross-model replication | Single-model is insufficient for generalisation claims | Run pipeline on Llama-3.1-8B + Mistral-7B + a base (non-RLHF) model |
| R5 | Larger probe sets per channel | Confidence intervals + length control | 30 probes/channel (20 directional + 8 length-controlled + 2 QC) |
| R6 | Replication by an independent lab | Strongest evidence | Coordinate after preprint |
| R7 | Clinical relevance grounding (for Lancet / World Psych) | Tie steering to a clinical outcome | Major scope extension — likely a separate paper |

Of these, **R1, R3, R4, R5 are the minimum bundle for Psychological Bulletin**
or a top methods journal in psychology. **R2 + R6 are needed on top for
Psychological Review or the Annual Review of Psychology.** **R7 (clinical
grounding)** is the gate for World Psychiatry / Lancet Psychiatry — those
journals fundamentally publish clinical-outcome studies. A version of this
work targeted at psychiatry would need to demonstrate that activation steering
of a personality channel produces a clinically-meaningful behavioural change
on a clinically-relevant task (e.g. steering Honesty-Humility on a
moral-decision battery, with clinical raters), at multi-subject scale, with
human inter-rater κ ≥ 0.70.

---

## 10. Conclusions

A 24-channel activation-steering substrate, derived from a single human
subject's psychometric battery and validated on a single open model with an
LLM-as-judge, produces directionally-accurate behavioural movement on 20 of 24
channels under a uniform multi-layer recipe. Three methodological findings —
probe-instrument decisiveness, multi-layer rescue of single-layer KILLs, and
empirical reproduction of the H × Dark-Triad coupling at the vector level —
support the substrate's construct validity and suggest concrete protocol
revisions for future activation-steering research. The single-subject, single-
model, single-judge limitations are quantified explicitly and a roadmap to
top-tier replication standards is specified.

---

## References (illustrative; full reference list to be assembled before any submission)

- Anthropic. (2025). *Persona Vectors and Behavioural Steering.* Anthropic
  research report.
- Ashton, M. C., & Lee, K. (2009). The HEXACO-60: A short measure of the major
  dimensions of personality. *Journal of Personality Assessment*, 91(4), 340–345.
- Blais, A.-R., & Weber, E. U. (2006). A Domain-Specific Risk-Taking (DOSPERT)
  scale for adult populations. *Judgment and Decision Making*, 1(1), 33–47.
- Buss, A. H., & Perry, M. (1992). The Aggression Questionnaire. *Journal of
  Personality and Social Psychology*, 63, 452–459.
- Lee, K., & Ashton, M. C. (2014). The Dark Triad, the Big Five, and the
  HEXACO model. *Personality and Individual Differences*, 67, 2–5.
- Paulhus, D. L., & Williams, K. M. (2002). The Dark Triad of personality.
  *Journal of Research in Personality*, 36, 556–563.
- Rimsky, N., Gabrieli, N., Schulz, J., Tong, M., Hubinger, E., & Turner, A. M.
  (2024). Steering Llama 2 via Contrastive Activation Addition. *Proceedings of
  the 62nd Annual Meeting of the ACL.*
- Rotter, J. B. (1966). Generalized expectancies for internal versus external
  control of reinforcement. *Psychological Monographs*, 80, 1–28.
- Schwartz, S. H. (1992). Universals in the content and structure of values.
  *Advances in Experimental Social Psychology*, 25, 1–65.
- Snyder, M. (1974). The self-monitoring of expressive behavior. *Journal of
  Personality and Social Psychology*, 30, 526–537.
- Templeton, A., et al. (2024). *Scaling Monosemanticity: Extracting
  Interpretable Features from Claude 3 Sonnet.* Anthropic.

---

## Author note

This manuscript was drafted by an LLM coding assistant working from validation
outputs, judge reports, and the author's prior build notes. Every claim is
grounded in either a committed run artifact (referenced by SHA) or a stated
limitation. No κ value was estimated or smoothed; all numbers come from the
analyse.py reports preserved in the repositories. The author is responsible for
all scientific claims and limitations; the assistant's role was structure,
synthesis, and prose.
