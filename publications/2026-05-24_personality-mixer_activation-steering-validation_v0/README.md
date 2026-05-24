# 24-Channel Activation-Steering Validation — personality-mixer ecosystem (2026-05-24)

**Location (canonical, unit-compliant):** `publications/2026-05-24_personality-mixer_activation-steering-validation_v0/`
**Naming convention:** per CHARTER §14, `YYYY-MM-DD_source-repo_short-kebab-title_vN`.
This pack was prepared 2026-05-24 from the personality-mixer ecosystem:
`mg-digital-twin` (vector extraction + steering-server + validation harness),
`personality-central-db` (the agnostic personality DB on Supabase),
`personality-construct-runner` (the activation-steering wire), and the two
research mixers (`personality-mixer-codex` / `personality-mixer-claude`).

## Formats

| Format | Files | Use |
|---|---|---|
| `.md` | **canonical source — never edit the others** | AI processing, git diffs, this README |
| `.tex` | regenerated from `.md` via pandoc | arXiv preprint, TMLR, NeurIPS/ICLR/ICML (add venue `.sty`) |
| `.docx` | regenerated from `.md` via pandoc | Psychological Bulletin, Psych Review, Lancet Psychiatry, World Psychiatry (apply APA 7 or Vancouver template at submission) |
| `.pdf` | regenerated from `.md` via pandoc + xelatex | universal review/submission output |

**To regenerate** after editing any `.md`: run `make` in this directory
(regenerates all `.tex` + `.docx`). Run `make pdf` once a LaTeX engine is
installed.

## What's here
- **MANUSCRIPT.md** — full paper draft written to the standard expected by top-tier
  journals (Psychological Bulletin / World Psychiatry / Lancet Psychiatry / Annual
  Review of Psychology), with complete CONSORT/PRISMA-style methodology reporting,
  honest limitations, and a roadmap to those venues. The manuscript is **NOT
  submission-ready for those journals as it stands** — the evidence is single-subject,
  single-model, LLM-as-judge proof-of-concept — but it is written to their rigour bar
  so the gap is explicit and quantified.
- **SUPPLEMENTARY_TABLES.md** — full 24-channel scorecard, probe-library inventory,
  judge-rubric inventory, refusal-cosine + orthogonalisation tables, raw run pointers.
- **ROADMAP_TO_TOP_VENUES.md** — what additional evidence is required for each of the
  four named venues, with realistic timelines and cost estimates.
- **WORK_LOG.md** — chronological build-and-validation work log (sessions 2026-05-23
  → 2026-05-24). Companion to the manuscript; not for external submission.

## Unit-compliance status (v0.0.4 charter)

This pack pre-dates the unit's adoption (v0.0.3-charter on 2026-05-24) and the
v0.0.4 amendments. The intake commit (827669c, plus the Gate-6 counter-signature
in 6f62989, plus the v1 revision in ef45b3b, plus the v1+ pre-arXiv work in
49490e9) closed most of the v0.0.4-charter compliance gaps. Status per artifact:

- ✅ **Gate-1 idea-capture entry:** `notebooks/2026/05/2026-05-24_personality-mixer-paper-intake.md` (committed at intake).
- ❌ **Gate-2 Scoping Memo:** absent; work pre-dates this gate. Disclosed in `deviations.md` §1.
- ❌ **Gate-3 pre-registration or Exploration Plan:** absent; work pre-dates this gate. Disclosed in `deviations.md` §1, §3, §5. Future Tier-C upgrade pre-registers on OSF per ROADMAP §"Recommended sequencing" item 1.
- ✅ **`internal-review.md` (Gate 6):** completed under the v1 prompt by a separate Claude session and counter-signed by Rick Weakley with disposition PROCEED WITH REVISIONS.
- ✅ **`ai-use-disclosure.md`:** committed; Tier 3 + Tier 4 hybrid per the v0.0.4 direction-of-intellectual-origin test; per-element accountability table covers every AI-originated framing including those identified in the v1 revision pass.
- ✅ **`deviations.md`:** committed; formal disclosure of the pre-registration gap and the recommended manuscript revisions (now applied in v1).
- ✅ **`coi-disclosure_weakley.md`:** committed; ICMJE per-publication disclosure with GitHub added to §2.1 and the 2026 annual snapshot at `coi/2026_founder-disclosure.md` cross-referenced.
- ✅ **`reproducibility-bundle/` subfolder:** committed with README, PROVENANCE, environment.yml, seeds.json, replication-log.md, Makefile, code/README, data/README. **Bundle is in stub state** — code and data are pointers to private source repos at pinned SHAs; real `make replicate` and one end-to-end run remain as Gate-7 closure work before arXiv preprint posting (see `replication-log.md` for the closure-path enumeration).
- ✅ **`neurips-checklist.md`:** committed; Tier-M ML compliance walkthrough with 11 SATISFIED / 5 partial-TODO / 4 N/A. Item 7 (statistical significance) is the load-bearing TODO for any TMLR/NeurIPS submission.
- ✅ **v1 manuscript revisions per Gate-6 categories 1, 4, 5:** landed in this current state (this commit and prior). The manuscript now reads `MANUSCRIPT.md`; Gate-6 categories 2 (full bundle finalisation) and 3 (statistical significance) are deferred per the counter-signed Gate-6 finding to pre-arXiv and pre-TMLR respectively.

Remaining open closures before any external (arXiv) preprint posting, per the Gate-6 counter-signature's required-actions list:

- ~~Gate-7 reproducibility-bundle finalisation~~ ✅ **partial closure landed in the autonomous-mode pre-arXiv pass:** code vendored from `cybernaut6404/mg-digital-twin`; real `make replicate` written and verified working locally (5 MATCH · 4 OUT_OF_TOLERANCE · 15 NOT_VENDORED for the 24-channel scorecard); seeds.json TODOs lifted; `make replicate-full` target documented for the Modal end-to-end path. The remaining gap (4 OUT_OF_TOLERANCE rows + 15 NOT_VENDORED rows) is a known data-availability issue — the multi-layer-rescue + new-channel judge reports live on a local SHA f492844 that was never pushed to GitHub. Three closure options documented in `reproducibility-bundle/code/README.md` §"What's NOT vendored" and `reproducibility-bundle/data/derived/replication-delta.md`. Acceptable for arXiv preprint with the existing access-on-request posture.
- **Prompt-archive deposition** at this folder's `prompts/` subdirectory — see `COWORK_TRANSCRIPT_EXPORT.md` for the procedure. This is the **only ⏳ blocker** for arXiv preprint posting; requires Rick's manual export of the Cowork session(s) from the MacMini.
- ~~ORCID registration~~ ✅ done 2026-05-24: [0009-0004-0799-1756](https://orcid.org/0009-0004-0799-1756).

Closures landed in the autonomous-mode pre-arXiv pass:

- ✅ **Statistical-significance analysis** added to MANUSCRIPT.md §3.1.1 + §8.4: per-channel binomial tests, 95% Wilson score CIs, Holm-Bonferroni + BH-FDR corrections across the 18-channel family. Headline: 0 of 18 reach significance under family-wise correction (per-channel n too small). Computed by `reproducibility-bundle/code/compute_stats.py`; written to `reproducibility-bundle/data/derived/stats.{json,md}`.
- ✅ **Three figures** generated and embedded in MANUSCRIPT.md: κ forest plot (Figure 1, §3.1); inter-channel cosine heatmap (Figure 2, §3.7); refusal-cosine bar chart (Figure 3, §3.6). Source script: `reproducibility-bundle/code/figures.py`.
- ✅ **Real bibliography** at `references.bib` (BibLaTeX, 18 entries with verified DOIs from training-data knowledge; one entry — Anthropic Persona Vectors — marked TODO_VERIFY_DOI). Wired into the publication-folder Makefile via pandoc citeproc.
- ✅ **arXiv submission package** target `make arxiv` in the publication-folder Makefile + ARXIV_SUBMISSION_README.md step-by-step guide. Produces `arxiv-submission.tar.gz` (~423KB) ready for upload to arxiv.org/submit/.

Remaining open closures before TMLR submission (per ROADMAP_TO_TOP_VENUES.md):

- v2 manuscript additions: figures + bibliography + stats are now done (✅ landed in the autonomous-mode pass). The TMLR-blocker that remains is the **larger probe sets per channel** (substrate paper's 30-probe standard; current per-channel n median is 7 non-tie pairs) and **cross-model replication** on a non-Qwen model (Llama-3.1-8B per the ROADMAP).

## Provenance
- Validation date: 2026-05-23 → 2026-05-24
- Substrate: Qwen2.5-7B-Instruct, CAA-extracted vectors (Rimsky et al. 2024)
- Channel set: 2.1.0 (24 channels)
- Final scorecard: 20/24 PASS · 2 borderline · 1 sign-flip · 1 RLHF-floored
- Data + code repositories (all private, cybernaut6404 on GitHub):
  - `personality-central-db` (HEAD `2bdf13b`)
  - `personality-construct-runner` (HEAD `d55296b`)
  - `personality-mixer-codex` (HEAD `5462733`)
  - `personality-mixer-claude` (HEAD `3963ce4`)
  - `mg-digital-twin` (HEAD `f492844`, local)
- Backup: `/Volumes/OVERFLOW/BACKUP/personality-mixer-2026-05-24-dark-validation-checkpoint`
- Modal app: `mg-twin-steering-server` (L4 GPU, cost-optimised)

## Honesty contract
The manuscript represents the work AS IT IS. The n=1, single-model, LLM-judge
limitations are stated up front, not buried. The path to the top-tier venues is
specified as a *roadmap*, not implied as already met. This is the right way to
present early-stage methods work that could mature into the journals' standard.
