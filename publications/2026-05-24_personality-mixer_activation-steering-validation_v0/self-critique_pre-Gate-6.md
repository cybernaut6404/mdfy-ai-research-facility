# Self-analysis: my work on the publication pack
**Date:** 2026-05-24
**Author of this self-analysis:** Claude (Opus 4.7), the drafting LLM for the publication pack.
**Scope:** Just the publication-pack assembly (not the validation work that fed it, not the broader ecosystem build).
**Tone:** Honest, including where I fell short.

> *Note on this file's role in the v0 publication:* this self-critique was produced by the *drafting* LLM at the end of the pack-assembly Cowork session, BEFORE the publication was ingested into the unit. It is referenced by `deviations.md` §4, `ai-use-disclosure.md` §2.3, and `internal-review.md` §9 as source material. It is committed here as `self-critique_pre-Gate-6.md` to give those references a concrete file to point at and to preserve the drafting LLM's pre-Gate-6 self-assessment as historical context. It is NOT a Gate-6 review — Gate 6 is the canonical `internal-review.md` produced by a separate Claude session under the v1 prompt, with this self-critique as one of its inputs.

---

## What I was asked to do
Produce a publication-grade pack from the 20/24-channel validation results,
written to the standard of World Psychiatry / Lancet Psychiatry / Psychological
Bulletin / Annual Review of Psychology. Keep `.md` as the canonical/AI-friendly
source; generate the alternate formats authors actually need for submission.

## What I delivered
Five documents — MANUSCRIPT, SUPPLEMENTARY_TABLES, ROADMAP_TO_TOP_VENUES,
README, WORK_LOG — in four formats each (md, tex, docx, pdf) plus a Makefile.
Pack lives at the canonical path Rick specified; OVERFLOW backup; Downloads
copy of the work log.

---

## What I did well

**1. Format architecture was the right call.** Single canonical `.md`, all
other formats auto-generated from it via pandoc + a Makefile. That means the
science of the manuscript is never out of sync between formats, and edits flow
one-way (you only ever touch `.md`). This is what experienced researchers do
when they're maintaining a paper across arXiv + journal + supplementary;
nothing rots.

**2. Honest framing on the journal bar.** I pushed back, twice, on the
implicit "this is ready for World Psychiatry" framing. The honest position
— that this is methods/proof-of-concept work, publishable now at arXiv/TMLR,
with a quantified path to higher-tier venues — is the only position that
survives a real peer review. Telling you otherwise would have wasted your
time downstream.

**3. The Roadmap document is the most useful piece in the pack.** It lists
concrete, quantified requirements per venue tier with realistic timelines and
costs. Most researcher self-assessments handwave the gap to top venues; the
roadmap names the specific bundles (multi-subject + pre-reg + cross-model =
Tier 2; add inter-rater + indep replication = Tier 3; add clinical outcomes =
Tier 4) and time-budgets them. That's actually actionable.

**4. The manuscript's methods section is genuinely rigorous.** I documented
the substrate, extraction protocol, steering config, probe libraries, judge
design, safety analyses, and engineering scaffolding at the level a
methodologist could replicate from. The three substantive findings (probe-
instrument decisiveness, multi-layer rescue, vector-level H × Dark-Triad
coupling) are framed as findings, not asides — they each get their own
discussion subsection.

**5. Limitations section is specific, not boilerplate.** Eight numbered
limitations, each with a real consequence and (where possible) a fix. Most
manuscripts bury limitations as a single soft paragraph; this one front-loads
them and gives reviewers ammunition. That's strategically wise: better that
the *reviewer* doesn't have to find the limitations.

**6. The WORK_LOG is genuinely useful as a project chronicle.** Section 7
maps it onto a separate-repo file structure, so the next step (if Rick wants
that repo) is mechanical.

---

## What I did badly or had to redo

**1. I put the pack in the wrong place first.** I created
`/Users/richardweakley/ai-workspace/RESEARCH PUBLICATIONS/` (note: space,
not in mdfy-ai-research-facility) on the assumption that "RESEARCH
PUBLICATIONS" was a top-level workspace dir. Rick corrected me — the canonical
location is inside `mdfy-ai-research-facility/`. I should have asked one
question about location before creating the directory; that would have saved
the move + the backup re-point.

**2. The first naming was less descriptive than it could be.**
`2026-05-24_personality-mixer-ecosystem` was just date + workspace. The
corrected `2026-05-24_personality-mixer_activation-steering-validation`
includes the *research topic* — which is what someone scanning a research
archive actually wants. I should have included the topic in v1.

**3. The PDF chain had four avoidable iterations.** I shipped PDFs that:
(a) failed because pdflatex doesn't do Unicode (had to switch to xelatex);
(b) had missing-glyph warnings for κ, ≤, ≥, →, ↔ in Latin Modern Roman (had to
switch to STIX Two Text); (c) STIX Two Text still missing ≤/≥/↔/→ in text mode
(had to add sed-substitution to LaTeX math mode); (d) the `→` substitution
broke on a `&` in "Lee & Ashton, 2014" (had to use ASCII fallback instead);
(e) ● ○ ⚠ legend glyphs missing in WORK_LOG (had to add another sed pass).
Five PDF generation passes when ONE could have done it if I'd thought through
the Unicode + font + math-mode chain up front. The right pre-flight: enumerate
the non-ASCII codepoints in all the source `.md` files, build the substitution
table once, then build PDFs. I did it iteratively instead.

**4. The MacTeX install assumed background sudo would work.** It didn't —
brew's installer requires a terminal for the password prompt and silently
failed. I should have flagged that up front when I proposed the install,
not after it failed. This cost 15 minutes of round-trip with you.

**5. Two monitor counters had bugs.** The first KILL-retest counter died on
a `grep -c | xargs` arithmetic edge case; the Step 2 filesystem-counter logic
had a malformed conditional that always returned 0. Both eventually self-
healed (the underlying background tasks completed and notified you anyway),
but the counters were meant to be the foreground status you asked for and they
weren't reliable. I should have unit-tested the counter shell with synthetic
state before arming it.

**6. The pre-registration claim in the manuscript is borderline.** I wrote
that "H1–H3 were stated in build notes prior to the validation runs but were
not pre-registered." That's true. But framing them as "hypotheses" in §1.2
gives them more methodological weight than they earn. A strict reviewer would
say: if you didn't OSF-timestamp them, they're post-hoc framing — even if you
mean well. I flagged this in the Limitations (§8.5) which is the right place,
but the Intro framing reads slightly stronger than the timestamp evidence
supports.

---

## What's genuinely weak about the manuscript itself (against the bar I claimed)

I want to be specific about where it would actually fall short at a real
top-tier review, beyond the limitations I already wrote into §8.

**a. No figures.** A real Psych Bulletin paper would have at least:
(i) a κ-distribution forest plot across the 24 channels; (ii) an inter-channel
cosine heatmap visualising the H × Dark-Triad coupling; (iii) a refusal-cosine
scatter with the FLAG threshold drawn. I shipped tables only. Tables are
sufficient for arXiv; they're not sufficient for the named journals.
**Fix cost:** ~2 hours with matplotlib.

**b. No bibliography that actually compiles.** The reference list (§) is
*illustrative* — no DOIs, no real BibTeX, no in-text citation style applied.
For any submission this needs a real `.bib` file with verified references and
the right citation format (APA 7 / Vancouver / etc.). **Fix cost:** ~3 hours
to track down DOIs + write the .bib + add `--bibliography` to pandoc.

**c. No statistical analysis beyond directional accuracy.** Real psychometric
work reports confidence intervals, effect sizes (Cohen's d at minimum),
binomial tests against chance, multiple-comparisons correction across the 24
channels (Bonferroni or BH-FDR). I reported κ + win/loss/tie counts — that's
the raw data, not the analysis. A reviewer would ask for at least binomial
significance per channel. **Fix cost:** ~half a day with scipy.stats.

**d. Single-author / single-LLM-judge combination is publishable nowhere top-
tier.** I noted this in Limitations. But it's worth stating again: the
substantive bar isn't "have you stated the limitation"; it's "have you fixed
it." For Tier 2+, this is the load-bearing requirement.

**e. The manuscript itself was drafted by an LLM.** ICMJE 2026 guidance (and
most journal policies) require authors to: (i) declare any AI assistance in
the manuscript-preparation; (ii) take responsibility for every claim; (iii) NOT
list an LLM as an author. The Author Note at the end of MANUSCRIPT.md does
declare this honestly — which is the right call — but it's a non-trivial
disclosure that many reviewers will scrutinise. Not a blocker, but a
foreseeable point of friction.

**f. The "overturns" language is stronger than one channel result supports.**
"Openness PASSED, overturning the substrate paper's caveat" is technically
true at this configuration on this model with these probes — but a single
result, single-subject, single-judge does not *overturn* anything in any
universalisable sense. Replication is required. "Provides counter-evidence to"
or "challenges" would be more defensible than "overturns."

**g. Code/data availability statement is weak.** Repos are private. "Available
on request" doesn't pass top-tier open-science requirements. For any
submission targeting journals with open-data policies (Psych Bulletin
encourages it; Lancet Psychiatry has formal policies), the artifacts need
public availability — at minimum the probe libraries, judge rubrics, and run
artifacts (the vectors themselves carry IP considerations and could be
withheld with justification). **Fix cost:** decide which repos go public + add
a real availability statement.

---

## How the pack compares to my own stated standard

I wrote in README.md: *"the manuscript is **NOT submission-ready for those
journals as it stands** — the evidence is single-subject, single-model,
LLM-as-judge proof-of-concept — but it is written to their rigour bar so the
gap is explicit and quantified."*

Re-reading the manuscript against that standard, I'd grade it:
- **Structure + section coverage:** A (matches a Psych Bulletin paper's
  shape)
- **Methods rigour:** B+ (good on protocol; missing figures, real stats)
- **Results presentation:** B (tables are clear; needs forest plot)
- **Discussion depth:** B (three findings well-developed; could engage more
  with the broader interpretability literature)
- **Limitations honesty:** A (specific, numbered, fix-able)
- **Roadmap usefulness:** A (concrete + quantified)
- **References:** D (illustrative only — would not compile)
- **Reproducibility statement:** B− (repos are private; recipe is documented
  but not all artifacts public)

**Overall: I'd put it at B+ as a methods-paper draft, A− once figures + real
bibliography + stats analysis are added.** That's good enough for arXiv as-is,
needs the three additions before TMLR submission, needs the full Tier-2
bundle (multi-subject + pre-reg + cross-model + larger probes) before
Psychological Bulletin.

---

## What I'd do differently if I were starting this pack from scratch

1. Ask one location-question before creating any directory.
2. Build the Unicode-substitution table up front from a quick `python3` scan
   of all `.md` source files, not iteratively.
3. Generate figures alongside tables (matplotlib + 2 hours).
4. Build the bibliography as a real `.bib` from the start — even with TODO
   markers for DOIs to chase down later.
5. Flag the MacTeX-needs-sudo issue *before* attempting the background install.
6. Make the WORK_LOG.md its own concern from the start (Rick separately asked
   for it; I bolted it on at the end).
7. Add per-channel binomial significance + Bonferroni-corrected gate, alongside
   raw κ.
8. Be more conservative with verbs: "passed at this configuration" rather than
   "rescued" / "overturns" wherever possible.

---

## Bottom-line assessment

The pack is **professionally usable**: structured to the right standard,
honestly framed, format-complete, durably backed up. It is **not yet
submission-ready** at any of the four target journals — and I've documented
exactly what makes that gap.

If you submit to arXiv this week, the pack works. If you submit to TMLR in a
month, fix items (a)–(c) above first. If you want to target Psychological
Bulletin in 4–6 months, the ROADMAP_TO_TOP_VENUES.md document is the right
checklist; follow it.

The single most valuable next step — both for the manuscript's quality and
for the scientific contribution — is the **cross-model replication on
Llama-3.1-8B**. That single addition would let the manuscript credibly claim
substrate generality, which is the highest-leverage claim it currently can't
make.

---

*— Claude (Opus 4.7), self-analysis on the publication-pack assembly,
2026-05-24.*
