# Annotated References — v0

This bibliography backs the Charter and Standards documents of `mdfy-ai-research-facility`. Each entry is the canonical source for a standard the unit adopts. Where the canonical source is genuinely uncertain, the entry says so explicitly.

---

## Pre-registration and Registered Reports

- **OSF Preregistration Templates (Center for Open Science).** The standard template covers Study Information, Hypotheses, Design Plan, Sampling Plan, Variables, and Analysis Plan. Adopted as the unit's default Tier-C registration template. https://www.cos.io/blog/choosing-preregistration-template-guide-for-researchers
- **AsPredicted (Wharton Credibility Lab).** Nine short questions producing a time-stamped PDF; used where the OSF template is disproportionate to the study. https://aspredicted.org/messages/faq.php
- **Registered Reports (Center for Open Science).** Stage 1 peer-reviewed protocol earns in-principle acceptance before data collection. The unit's preferred mechanism for Tier-C work where the venue supports it. https://www.cos.io/initiatives/registered-reports

## Reproducibility (ML)

- **NeurIPS Paper Checklist Guidelines.** Mandatory for NeurIPS submissions; covers claims, limitations, theory, experimental reproducibility, code/data access, compute disclosure, broader impacts, and safeguards for released models. Adopted as the unit's reproducibility floor for ML work. https://neurips.cc/public/guides/PaperChecklist
- **Pineau et al., ML Reproducibility Checklist v2.0.** The widely-adopted itemized checklist that covers algorithm description, dataset preprocessing, dependencies, training/eval code, run counts, and central tendency reporting. https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf
- **Pineau et al. (2021), "Improving Reproducibility in Machine Learning Research," JMLR 22.** The rationale paper behind the checklist. https://www.jmlr.org/papers/v22/20-303.html

## AI use and authorship

- **ICMJE — AI Use by Authors (current edition, Jan 2024, reaffirmed 2025).** Consensus minimum: no AI as author; disclose in cover letter; writing assistance → Acknowledgments; data/analysis/figure generation → Methods; authors take full accountability. Adopted as the unit's baseline. https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html
- **ICMJE — Defining Authors and Contributors.** The four authorship criteria; AI fails criterion 4. https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html
- **Nature Portfolio AI Editorial Policy.** LLMs cannot be authors; document in Methods. https://www.nature.com/nature-portfolio/editorial-policies/ai
- **NeurIPS LLM Policy (within annual Call for Papers).** Authors fully responsible for LLM-assisted content; disclosure required when LLM is methodologically material. https://neurips.cc/Conferences/2025/CallForPapers

## Reproducibility and open-science standards (general)

- **Munafò et al. (2017), "A manifesto for reproducible science," Nature Human Behaviour 1: 0021.** The unit's conceptual frame: methods, reporting, reproducibility, evaluation, incentives. https://www.nature.com/articles/s41562-016-0021
- **TOP Guidelines (Center for Open Science).** Eight transparency standards across three tiers (disclose, require, verify). The unit operates at Level 2 by default. https://www.cos.io/initiatives/top-guidelines
- **Lakens, Scheel, Isager (2018), "Equivalence Testing for Psychological Research: A Tutorial," AMPPS.** Adopted for any claim of "no effect" the unit ever makes. https://journals.sagepub.com/doi/10.1177/2515245918770963

## Data principles

- **Wilkinson et al. (2016), "The FAIR Guiding Principles for scientific data management and stewardship," Scientific Data 3: 160018.** Canonical statement of FAIR. https://www.nature.com/articles/sdata201618
- **GO FAIR — FAIR Principles (operational guidance).** Persistent IDs, rich metadata, machine-readable schema, clear license. https://www.go-fair.org/fair-principles/
- **GIDA — CARE Principles for Indigenous Data Governance.** Collective Benefit, Authority to Control, Responsibility, Ethics. Relevant when community data is involved; otherwise out-of-scope for v0. https://www.gida-global.org/careprinciples

## Single-case / single-subject designs

- **Tate, Perdices, Rosenkoetter et al. (2016), "The Single-Case Reporting Guideline In BEhavioural interventions (SCRIBE) 2016 Statement."** The canonical reporting standard for single-case experimental designs. Mandatory for the unit's self-experimentation studies where applicable. https://pmc.ncbi.nlm.nih.gov/articles/PMC4873717/
- **Kazdin, A. E. (2020). *Single-Case Research Designs: Methods for Clinical and Applied Settings* (3rd ed.). Oxford University Press.** Methodology reference for ABAB, multiple-baseline, and changing-criterion designs.
- **What Works Clearinghouse Single-Case Design Standards.** Independent design-quality criteria. https://ies.ed.gov/ncee/wwc/

## Model documentation and responsible release

- **Mitchell et al. (2019), "Model Cards for Model Reporting," FAccT 2019.** Nine-section template adopted by the unit for any released model. https://arxiv.org/abs/1810.03993
- **Anthropic Responsible Scaling Policy.** Useful as a tiered-release template, even at small scale. https://www.anthropic.com/responsible-scaling-policy
- **US Government Dual Use Research of Concern policy.** Federal policy is in transitional state as of mid-2026; the unit defers to current NIH guidance where applicable. https://oir.nih.gov/sourcebook/ethical-conduct/special-research-considerations/dual-use-research **[FLAG — uncertain/transitional]**

## Citation and release infrastructure

- **Citation File Format (CFF) specification.** YAML `CITATION.cff` in the repo root; GitHub renders "Cite this repository." Adopted. https://citation-file-format.github.io/
- **Zenodo–GitHub integration (Zenodo Help).** Tag release → Zenodo mints versioned DOI plus a concept DOI spanning all versions. The unit's release flow. https://help.zenodo.org/docs/github/describe-software/citation-file/
- **Smith et al. (2016), "Software citation principles," FORCE11.** Importance, credit, identification, persistence, accessibility, specificity. https://peerj.com/articles/cs-86/

## Systematic reviews and meta-analyses

- **PRISMA 2020 Statement (Page et al., BMJ 2021).** The unit's reporting standard for any systematic review or meta-analysis (Tier T). https://www.bmj.com/content/372/bmj.n71

## Lab manuals worth emulating

- **The Turing Way (community handbook).** A living handbook on reproducible, ethical, and collaborative data science. https://book.the-turing-way.org/
- **Lakens, *Improving Your Statistical Inferences* (open course materials).** Closest public approximation of a "Lakens lab manual"; no single canonical handbook artifact exists. https://lakens.github.io/statistical_inferences/ **[FLAG — no single canonical artifact]**
- **Allen Institute Open Science.** A precedent for "open by default" releases at scale. https://alleninstitute.org/division/open-science/

## Conflicts of interest

- **ICMJE Disclosure of Interest Form.** Adopted as the unit's COI standard regardless of venue requirements. https://www.icmje.org/disclosure-of-interest/

---

## Flagged uncertainties

The following references in this charter rest on sources where the canonical statement is genuinely uncertain or in flux. These are honest gaps for v1 to resolve.

1. **US federal dual-use research policy.** The 2025 federal landscape was in transition; the unit defers to current NIH guidance and the most recent stable framework by analogy. To revisit in v1.
2. **A formally published lab manual for the Lakens lab.** No single canonical document; public materials serve as a de facto manual.
3. **IP-assignment norms for solo and independent labs.** No tight canonical source. v0 defaults to written assignment of authorship-of-record and copyright (CC-BY), code (Apache-2.0), and explicit reservation of patentable inventions; a one-page contributor agreement at the first external collaboration.
