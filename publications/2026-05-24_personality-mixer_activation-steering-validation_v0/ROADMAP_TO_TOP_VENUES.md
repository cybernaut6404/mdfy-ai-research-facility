# Roadmap from the present study to top-tier publication

This document specifies what is required, in concrete and quantified terms, for
the work in MANUSCRIPT.md to be accepted at each of the four named target
journals. The current evidence is genuinely strong for what it is — a 20-of-24
channel validation with rigorous methodology reporting — but the named journals
require evidence categories the present study does not yet supply (multi-subject,
human inter-rater, pre-registration, clinical outcome).

The honest framing: we should treat this manuscript as a **research preprint and
methods foundation**, and the work below as the path to top-tier acceptance.
We list the venues in *ascending* order of additional requirements.

---

## Tier 1: Methods / ML / preprint venues — submittable as-is

The current manuscript can be submitted essentially without modification to any
of the following:

- **arXiv (cs.CL / cs.AI / cs.LG)** — companion preprint, immediate, no review.
  Recommended FIRST step regardless of downstream venue.
- **NeurIPS / ICLR workshop tracks** on Mechanistic Interpretability, Alignment,
  or Safe-by-Design ML (Workshops accept smaller-scope methods work that wouldn't
  fit the main track). Workshop submission cycles 2–4× per year.
- **TMLR (Transactions on Machine Learning Research)** — open peer review,
  rolling submission, accepts methods work; the 24-channel validation with
  honest limitations is a good TMLR fit.
- **Behavior Research Methods** — a respected psychology methods journal that
  publishes single-subject methodological contributions, especially around
  novel measurement instruments.

**Decision:** I recommend an arXiv preprint immediately + a TMLR submission as
the primary outlet, with the four named top-tier journals as later targets
once the requirements below are met. The preprint establishes priority and
visibility while we build toward those higher bars.

---

## Tier 2: Psychological Bulletin / Annual Review of Psychology

Both are top-tier general psychology journals, but with different formats and
requirements.

### Psychological Bulletin
**Format:** Quantitative reviews and meta-analyses; high-quality systematic
primary studies with broad theoretical implications.

**Minimum additional requirements:**
- **R1 — Multi-subject contrastive items.** The single-subject derivation is the
  show-stopper. At minimum: re-extract the 24 vectors from contrastive items
  derived from ≥ 30 independent human subjects' psychometric batteries
  (existing public datasets exist for several instruments), and demonstrate
  that the multi-subject vectors achieve comparable directional accuracy. This
  also lets us report inter-subject vector cosine — a construct-stability
  measure.
- **R3 — Pre-registration.** OSF or AsPredicted. Hypotheses, probes, rubrics,
  PASS gate, and analysis plan timestamped before any further validation run.
  Non-negotiable for this tier.
- **R5 — Larger probe sets.** Expand each channel's library to the
  substrate-paper standard of 30 probes (20 directional + 8 length-controlled
  + 2 QC). Length-controlled probes are particularly important to rule out
  length bias in the judge.
- **R4 — Cross-model replication (partial).** Run the full pipeline on at
  least one non-Qwen model (Llama-3.1-8B-Instruct is the natural choice; the
  extraction scaffold supports it). Report which channels replicate.

**Estimated scope:** 4–6 months of focused work. Compute cost: roughly
$200–500 in Modal time plus judge calls. Subject recruitment cost depends on
the route (existing datasets vs. new collection).

### Annual Review of Psychology
**Format:** Invitation-only review articles by established researchers.
**Realistic path:** Not a direct submission target. The route is to publish the
work as primary research (Psychological Bulletin / Psychological Review /
JPSP), establish the substrate paper as a citable foundation, and *then*
write or contribute to an invited review of activation-steering for
personality research several years later.

---

## Tier 3: Psychological Review

**Format:** Theoretical contributions of broad scope.

**Additional requirements on top of Tier 2:**
- **R2 — Human inter-rater reliability.** Recruit N ≥ 3 trained human raters
  (graduate-level personality psychologists). Each rater scores a stratified
  sample (~30%) of the full pair set blind. Report Cohen's κ (or
  Krippendorff's α) for human–human agreement, and the agreement between the
  LLM judge and the human consensus. Recalibrate LLM-judge weight by the
  agreement coefficient.
- **R6 — Independent-lab replication.** Reach out to one or more independent
  groups working on activation steering or psychometric LLMs (e.g.
  Anthropic's persona vectors group, Redwood Research, the Apollo Research
  evaluations team) to replicate the core 24-channel finding on a different
  base model with their own probes and judges.
- A theoretical contribution: situate the substrate within a broader theory of
  steerable personality (e.g. integrate with whole-trait theory, social-
  cognitive theory, or process accounts of personality).

**Estimated scope:** an additional 6–12 months on top of Tier 2; total ~12–18
months from the current state.

---

## Tier 4: World Psychiatry / The Lancet Psychiatry

These are **clinical** journals. They publish clinical trials, epidemiological
studies, and clinically-significant intervention reports.

**The fundamental requirement for either journal: a clinical outcome.**
Activation-steering of a personality channel, in itself, is not a clinical
outcome. To publish in either, we would need to show that:

- (a) A specific clinical context exists where steering a personality channel
  produces a measurable clinical benefit, with the benefit assessed by
  trained clinicians blind to condition.
- (b) The intervention is reproducible and the substrate is mature enough to
  deploy in a study context.
- (c) The study is fully ethics-approved (IRB / REC) — activation steering
  applied to an LLM that interacts with patients is currently *not*
  established as ethical without explicit protocol approval.

**Candidate clinical applications** (each would be a separate paper, downstream):
- **Honesty-Humility on financial-exploitation risk in clinical populations**
  (the H × Dark-Triad coupling we empirically confirmed has clinical analogues).
- **Attachment-anxious / -avoidant steering in supportive dialogue agents**
  for clients in attachment-focused therapy training (rater = trained
  psychotherapist).
- **Sycophancy reduction in clinical LLM assistants** — the sycophancy
  sign-flip finding has direct clinical-safety implications for any LLM
  deployed in patient-facing contexts.

**Estimated scope:** 18–36 months from the current state, with a clinical
collaborator on the team from the outset. World Psychiatry / Lancet Psych
typically require multi-site studies and Phase II–III clinical evidence;
neither journal will publish single-investigator methods work, however
rigorous.

**Honest assessment:** the realistic World Psych / Lancet Psych path runs
through 2–3 intermediate clinical-pilot papers in venues like Translational
Psychiatry or NPJ Mental Health Research first, accumulating the evidence the
top clinical journals require. Activation steering for personality constructs
is currently 3–5 years from primary acceptance at those venues, in our
estimate.

---

## Recommended sequencing

1. **Immediate (next 1–2 weeks):**
   - Polish MANUSCRIPT.md to camera-ready arXiv quality
   - Pre-register the protocol that's already specified (the *next* run, not
     this past one — we cannot retroactively pre-register completed validation)
   - arXiv preprint with all data + code links

2. **Short-term (1–3 months):**
   - Cross-model replication on Llama-3.1-8B
   - Expand probe sets to 30/channel for the new 15
   - Recruit one external collaborator (multi-subject contrastive items)

3. **Medium-term (4–9 months):**
   - Multi-subject extraction + re-validation (R1)
   - Human inter-rater reliability on a stratified sample (R2)
   - TMLR submission of the methods contribution

4. **Long-term (12–24 months):**
   - Independent-lab replication (R6)
   - Psychological Bulletin / Psychological Review submission with the
     multi-subject, multi-model, multi-rater data
   - Begin clinical collaboration for Tier 4

5. **Aspirational (24–48 months):**
   - World Psych / Lancet Psych via clinical-pilot intermediate papers

This is the realistic, honest, top-tier path. Anything faster requires
shortcuts that would not survive peer review at the named journals.
