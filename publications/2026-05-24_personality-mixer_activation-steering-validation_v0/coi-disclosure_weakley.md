# Conflict of Interest Disclosure — R. Weakley

**Disclosure type:** per-publication
**As of date:** 2026-05-24
**For publication:** *A 24-Channel Activation-Steering Substrate for Personality Constructs in a Large Language Model: Single-Subject Validation, Methodological Findings, and a Roadmap to Multi-Subject Replication.*
**Aligned with:** ICMJE Disclosure of Interest Form (current edition).

> *Per Charter §12: every publication of the unit ships with a current ICMJE disclosure, and an annual snapshot is committed to `coi/YYYY_founder-disclosure.md` regardless of publication activity. This per-publication disclosure cross-references the standing tooling/vendor disclosure in the unit's `README.md` and itemises anything publication-specific.*

---

## 1. Author identification

- **Name:** Rick Weakley
- **Affiliation:** `mdfy-ai-research-facility` (the unit). Primary affiliation: independent researcher (no institutional employment relevant to this publication).
- **ORCID:** [0009-0004-0799-1756](https://orcid.org/0009-0004-0799-1756) (registered 2026-05-24).
- **Email:** rick@mdfy.co.uk

## 2. Relationships and activities — past 36 months

### 2.1 Financial relationships with commercial entities

Salary, consulting fees, advisory roles, board memberships, expert testimony, royalties, stock or stock options, paid travel, gifts, in-kind support.

**None** specifically relating to the subject matter of this publication. The author's general professional financial history is not relevant to declare in full; only items a reasonable reviewer would consider relevant to *this work* are itemised:

- **Anthropic (paid customer relationship).** The author is a paying subscriber to Anthropic's Claude (used in this work as both the manuscript-drafting assistant and the blind-rater judge). The relationship is the standard customer-vendor relationship of a paid subscription / API account; no advisory role, no equity, no beta-access privileges beyond what is available to any paying customer, no in-kind support. Approximate cumulative spend during the work period (2026-05-23 → 2026-05-24): ~US $5–15 in judge API calls (per the cost provenance in SUPPLEMENTARY_TABLES.md). This relationship is the unit's standing tooling disclosure (CHARTER §12, README.md "Dependencies & tooling disclosure") and is repeated here per ICMJE convention.
- **GitHub (paid customer relationship).** The author hosts source code under the `cybernaut6404` GitHub account, including the unit repository, the five source repos that produced this work, and downstream commercial repos. Standard customer-vendor relationship of a paid subscription; no advisory role, no equity, no beta-access privileges beyond what is available to any paying customer. This relationship is the unit's standing tooling disclosure (CHARTER §12, README.md "Dependencies & tooling disclosure") and is repeated here per Gate-6 §7 finding.
- **Modal Labs (paid customer relationship).** The author is a paying customer of Modal Labs (used in this work to host the steering-server and run all GPU validation jobs). Standard customer-vendor relationship; no advisory role, no equity, no beta-access privileges. Approximate cumulative spend during the work period: ~US $8–15 in validation compute.
- **Supabase (paid customer relationship).** The author hosts the central personality DB on Supabase. Standard customer-vendor relationship; no other ties.

### 2.2 Grants and research support

Research grants, contracts, awards from any source (government, foundation, commercial, personal).

**None.** This work was self-funded by the author at the cost itemised in §2.1. No grant, contract, or award supported the work.

### 2.3 Intellectual property

Patents (issued, pending, planned), licensing arrangements, royalties from IP.

**None pending or planned for the work described in this manuscript.** The author maintains a separate commercial product (`mdfy-personality-registry`) that consumes the substrate built in this work via a signed-push interface; this is a downstream product, not a patent or licence on the methodology. The methodology is released under Apache-2.0 (code) / CC-BY-4.0 (content), the unit's defaults (CHARTER §13).

### 2.4 Editorial and review activities

Editorships, editorial board memberships, peer-review activities for the venue this work is submitted to.

**None.** No editorial or review role at any of the venues named in ROADMAP_TO_TOP_VENUES.md (arXiv is not editorialised; TMLR, Behavior Research Methods, Psychological Bulletin, Psychological Review, World Psychiatry, The Lancet Psychiatry — no role).

### 2.5 Personal relationships

Significant personal relationships with co-authors, reviewers, editors, or subjects of the work that a reasonable observer would consider relevant.

**None.** This is a sole-authored manuscript. The single human subject whose psychometric battery seeded the contrastive items (manuscript §2.2) **is the author**. This self-derivation is the most consequential limitation of the study and is disclosed prominently in the abstract, methods, and §8.1. The author is not in a relationship with any anticipated reviewer or editor at the target venues.

### 2.6 Other

Anything not captured above that a reasonable reviewer would want to know.

The author operates a downstream commercial product (`mdfy-personality-registry`) that depends on the steering substrate validated in this manuscript. A successful publication of this work could increase the credibility or commercial value of that product. Per ICMJE conventions this is an "intellectual" interest that warrants disclosure even where no direct financial benefit is contingent on a specific publication outcome; reviewers should consider whether the framings or claims in the manuscript could be biased toward the substrate's marketability. The author asserts they are not, but flagging the relationship so the reviewer can judge.

## 3. AI-provider and tooling relationships

Per CHARTER §12 and README.md, the unit's standing dependence on AI providers (Anthropic Claude as primary), GitHub, Zenodo, and OSF is disclosed at the repo level. Specific to this publication:

- **Anthropic Claude** is used both as the manuscript-drafting assistant (Tier 3 + Tier 4 contributions per `ai-use-disclosure.md`) and as the blind-rater judge for the validation κ values reported in §3. This is a non-trivial dual role: the judge is provided by the same vendor as the drafter. The author has not measured cross-model judge agreement (e.g. would a GPT-4 judge produce the same κ values?) and this is a real methodological limitation noted in `ai-use-disclosure.md` §2.1 and in the manuscript §8.3.
- **No deviation from the unit's standing tooling disclosure.** The relationships in §2.1 are exactly what is disclosed at the repo level; this publication does not introduce a new sponsorship, advisory role, equity, or beta-access privilege that the standing disclosure does not already cover.

## 4. Specific COI for this publication

Per §2.6 and §3 above:

- The author has a non-trivial intellectual / commercial interest in the substrate validated by this manuscript via the downstream `mdfy-personality-registry` product.
- The AI judge and the AI drafter are from the same vendor (Anthropic).
- The single human subject is the author.

None of these constitute disqualifying conflicts under ICMJE; each is disclosed prominently in this document and (where load-bearing) in the manuscript itself. The author has taken the standard mitigating actions: the judge rubrics were authored before any validation run and not modified after; the contrastive items were authored before any validation run; the κ ≥ 0.60 PASS gate was pre-specified; the limitations are reported prominently.

## 5. Statement

I have read this disclosure and confirm it is complete and accurate as of the date above. I will update this disclosure if any of the disclosed items change materially before publication.

**Note on the 2026 annual COI snapshot:** Per CHARTER §12, the unit commits a per-publication ICMJE disclosure (this file) AND an annual snapshot at `coi/YYYY_founder-disclosure.md`. The 2026 annual snapshot has been committed at `coi/2026_founder-disclosure.md` to satisfy this convention; this per-publication disclosure is consistent with that annual snapshot. Any deviation between the two would be a reportable inconsistency under the unit's standards.

**Signed:** Rick Weakley
**Date:** 2026-05-24
