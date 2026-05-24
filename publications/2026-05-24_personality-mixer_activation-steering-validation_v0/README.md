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
v0.0.4 amendments. It does NOT yet satisfy the unit's tier-specific standards.
Specifically (per STANDARDS.md):

- No Gate-1 idea-capture lab-notebook entry
- No Gate-2 Scoping Memo
- No Gate-3 pre-registration or Exploration Plan (work pre-dates this gate)
- No `internal-review.md` (Gate 6) — only the drafting LLM's self-critique
- No `ai-use-disclosure.md` as a standalone artifact (only Author note in manuscript)
- No `deviations.md`
- No per-publication `coi-disclosure_*.md`
- No `reproducibility-bundle/` subfolder with environment.yml, seeds.json,
  PROVENANCE.md, replication-log.md, Makefile, code/, data/
- For ML methods work: no NeurIPS Paper Checklist (`neurips-checklist.md`)

These gaps are tracked for closure as the publication is prepared for arXiv /
TMLR submission. The pack is committed in its current state to make the gap
visible and to begin Gate 6 internal review against the v1 prompt.

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
