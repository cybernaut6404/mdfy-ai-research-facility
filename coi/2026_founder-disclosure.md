# Annual Conflict of Interest Disclosure — Rick Weakley — 2026

**Disclosure type:** annual snapshot (unit-level)
**As of date:** 2026-05-24
**Calendar year covered:** 2026
**Aligned with:** ICMJE Disclosure of Interest Form (current edition).

> *Per CHARTER §12: the unit commits an ICMJE-style disclosure on a per-publication basis AND an annual snapshot to `coi/YYYY_founder-disclosure.md` regardless of whether the venue requires it. This file is the annual snapshot for 2026; per-publication disclosures (in each publication folder) refine it for publication-specific elements.*

---

## 1. Author identification

- **Name:** Rick Weakley
- **Affiliation:** `mdfy-ai-research-facility` (the unit). Primary affiliation: independent researcher (no institutional employment relevant to research conducted under the unit's name).
- **GitHub account:** `cybernaut6404` (https://github.com/cybernaut6404)
- **Email (canonical for research-unit identity):** rick@mdfy.co.uk
- **ORCID:** [0009-0004-0799-1756](https://orcid.org/0009-0004-0799-1756) — registered 2026-05-24.

## 2. Relationships and activities — past 36 months

For each item below, "None" or itemised. Items a reasonable reviewer would want to know about, relating to the unit's research scope (AI / activation steering / interpretability / computational behavioural science / single-case experimental designs).

### 2.1 Financial relationships with commercial entities

Salary, consulting fees, advisory roles, board memberships, expert testimony, royalties, stock or stock options, paid travel, gifts, in-kind support relating to the unit's scope.

- **Anthropic (paid customer relationship, ongoing).** Paying subscriber to Anthropic's Claude. Used across the unit's research as drafting assistant, code generation assistant, blind-rater judge, and Gate-6 internal-review reviewer. Standard customer-vendor relationship; no advisory role, no equity, no beta-access privileges beyond what is available to any paying customer; no in-kind support.
- **GitHub (paid customer relationship, ongoing).** Paying customer; hosts the unit repository, the source repos that produce work for the unit, and downstream commercial repositories under the `cybernaut6404` account. Standard customer-vendor relationship.
- **Modal Labs (paid customer relationship, ongoing).** Paying customer; hosts compute for the personality-mixer ecosystem's vector-extraction and steering-server (the substrate for the 2026-05-24 publication and likely subsequent personality-construct research).
- **Supabase (paid customer relationship, ongoing).** Paying customer; hosts the central personality DB that backs the personality-mixer ecosystem.
- **Zenodo (free customer relationship, ongoing).** Free account; mints DOIs for the unit's tagged GitHub releases via the GitHub–Zenodo integration. No financial relationship.
- **OSF (Open Science Framework) (free customer relationship, ongoing).** Free account; will host pre-registrations for Tier C and Tier T meta-analyses going forward. No financial relationship as of this disclosure date (no pre-registrations have been committed yet).

No advisory roles, board memberships, expert testimony, royalties, stock options, paid travel, gifts, or in-kind support relating to the unit's research scope in the past 36 months.

### 2.2 Grants and research support

Research grants, contracts, awards from any source (government, foundation, commercial, personal).

**None.** All research conducted under the unit's name as of 2026-05-24 has been self-funded at the cost levels itemised in §2.1. No grant, contract, or award has supported any unit-attributed work.

### 2.3 Intellectual property

Patents (issued, pending, planned), licensing arrangements, royalties from IP.

**None pending or planned for the unit's research scope.** The author maintains a separate commercial product (`mdfy-personality-registry`) that consumes the personality-mixer substrate via a signed-push interface; this is a downstream product on top of unit-attributed research, not a patent or licence on the research methodology. All unit-released methodology is under Apache-2.0 (code) / CC-BY-4.0 (content) per CHARTER §13.

### 2.4 Editorial and review activities

Editorships, editorial board memberships, peer-review activities for venues likely to receive unit-attributed submissions.

**None** as of this disclosure date. The unit has not yet submitted to any peer-reviewed venue; no peer-review activity is in progress at venues the unit will target (per ROADMAP venue lists in the personality-mixer publication: arXiv, TMLR, Behavior Research Methods, Psychological Bulletin, Psychological Review, Annual Review of Psychology, World Psychiatry, The Lancet Psychiatry).

### 2.5 Personal relationships

Significant personal relationships with co-authors, reviewers, editors, or subjects of unit research.

**None** as of this disclosure date. The unit operates with the founder as sole researcher; no co-authors. No relationships with reviewers or editors at any target venue. The single human subject whose psychometric battery seeded the contrastive items in the 2026-05-24 publication **is the author**; this self-experimentation is disclosed prominently in that publication's abstract, methods §2.2, §8.1, and per-publication COI.

### 2.6 Other

Anything not captured above that a reasonable reviewer would want to know about, relating to the unit's research scope.

The author operates a separate commercial product (`mdfy-personality-registry`) that depends on the validated personality-mixer substrate. A successful publication of research from the personality-mixer ecosystem could increase the credibility or commercial value of that product. Per ICMJE conventions this is an "intellectual / commercial" interest that warrants disclosure at the annual-snapshot level, not only per-publication. The author asserts the unit's research is not biased toward the substrate's marketability and submits to the gating procedures in CHARTER §5–§16 to defend that assertion. Reviewers should consider whether the framings or claims in unit publications could be biased toward this commercial interest; the author's view is that the unit's transparency-over-polish standard (CHARTER §2) and the Gate-6 internal-review procedure are the mitigations in force.

## 3. AI-provider and tooling relationships (standing disclosure)

Per CHARTER §12 and README.md "Dependencies & tooling disclosure," the unit's standing dependence on AI providers (Anthropic Claude as primary) and infrastructure providers (GitHub, Modal, Supabase, Zenodo, OSF) is disclosed at the repo level and is repeated in §2.1 above. Specific to AI use across the unit's research scope:

- **Anthropic Claude is used as both manuscript-drafting assistant and blind-rater judge** in the personality-mixer work. This is a non-trivial dual role disclosed prominently in that publication's `ai-use-disclosure.md` and `coi-disclosure_weakley.md`. The unit's mitigating procedure is the v1 internal-review prompt (`templates/internal-review-prompt_v1.md`) run by a separate Claude session, with the human author counter-signing the review.
- **No model-provider relationship beyond paid customer subscription** exists. The author has no advisory, equity, or beta-access relationship with Anthropic, OpenAI, Google, Meta, or any other model provider.

## 4. Specific COI items current as of this disclosure

Per §2.6 above:

- The author has a non-trivial intellectual / commercial interest in research originating from the personality-mixer ecosystem via the downstream `mdfy-personality-registry` product.
- The AI judge and AI drafter are from the same vendor (Anthropic) — methodological caveat.
- The single human subject for the personality-mixer 2026-05-24 publication is the author — disclosed prominently in that publication's abstract and §8.1.

None of these constitute disqualifying conflicts under ICMJE. Each is disclosed prominently in this annual snapshot and in the per-publication COI of any publication they bear on.

## 5. Updates to this snapshot

This annual snapshot will be updated:

- (a) immediately upon any material change in the relationships disclosed in §2.1, §2.3, §2.4, §2.5, or §2.6;
- (b) immediately upon the addition of any new commercial relationship, grant, advisory role, equity stake, or board membership that bears on the unit's research scope;
- (c) at the start of each subsequent calendar year, when a new file `coi/YYYY_founder-disclosure.md` will supersede this one (with a back-pointer for the historical record);
- (d) upon any external incident, near-miss, or external criticism bearing on COI per CHARTER §16.

## 6. Statement

I have read this disclosure and confirm it is complete and accurate as of the date above. I will update this disclosure if any of the disclosed items change materially.

**Signed:** Rick Weakley
**Date:** 2026-05-24
**Account:** cybernaut6404 (GitHub) / rick@mdfy.co.uk (canonical email; git commit identity; ORCID-linked) / ORCID 0009-0004-0799-1756
