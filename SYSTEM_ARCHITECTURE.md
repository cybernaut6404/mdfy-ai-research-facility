# System Architecture

Companion to [`CHARTER.md`](./CHARTER.md). The Charter is *what we promise to do*; this document is *how the pieces fit together to deliver it*. Updated as the system evolves.

**Last updated:** 2026-05-24 (post-checkpoint after the autonomous-mode pre-arXiv run for the personality-mixer publication).

---

## 1. What this unit actually is

`mdfy-ai-research-facility` is a public, single-author, AI-assisted research unit that produces small batches of AI-related research to publication-grade standards. Three things define it operationally:

1. **A repo** (this one) where research is published, archived, and certified. Not where research is executed — that's project repos.
2. **A charter** (`CHARTER.md`) plus enforced standards (`STANDARDS.md`) plus an AI-use policy (`AI_USE_POLICY.md`) that bind the unit's behaviour.
3. **A set of templates and tooling** that automate the gates between project work and published research.

The unit is intentionally a *thin* central archive. Project repos do the experiments; the unit ingests, verifies, archives, and publishes.

## 2. The 9 gates (CHARTER §5)

Every project's lifecycle passes through nine gates. Each produces a committed artifact in the unit repo; nothing is informal.

```
Gate 1 — Idea capture        → notebooks/YYYY/MM/YYYY-MM-DD_short-title.md
Gate 2 — Scoping memo        → preregistrations/ or in-project repo
Gate 3 — Pre-reg / Expl-Plan → OSF (Tier C/T) / AsPredicted / preregistrations/
Gate 4 — Execution           → project repo (continuous)
Gate 5 — Analysis            → project repo (analysis script + outputs)
Gate 6 — Internal review     → publications/<pub>/internal-review.md  (under templates/internal-review-prompt_v1.md)
Gate 7 — Reproducibility-    → publications/<pub>/reproducibility-bundle/  (per templates/reproducibility-bundle_CHECKLIST.md)
         bundle finalisation
Gate 8 — Release             → tagged git release + Zenodo DOI + preprint
Gate 9 — Archival + lessons  → notebooks/YYYY/MM/ (post-publication entry)
```

**Tier matrix** (CHARTER §4 + STANDARDS.md): every output carries one of four tiers — C (confirmatory), E (exploratory), M (methods/engineering), T (theoretical/review). Tier C requires Gate 3 pre-registration on OSF; Tier E requires an Exploration Plan committed to `preregistrations/`; Tier M and T have lighter Gate-3 requirements but stricter substantive-content requirements.

## 3. Repo layout

```
mdfy-ai-research-facility/
├── CHARTER.md              ← what we promise
├── STANDARDS.md            ← detailed tier checklists
├── AI_USE_POLICY.md        ← Tier 1/2/3/4 AI-use boundary
├── README.md               ← entry point + DOI badge + standing tooling COI
├── CITATION.cff            ← citable repo metadata (concept + version DOIs)
├── LICENSE-CODE            ← Apache-2.0
├── LICENSE-CONTENT         ← CC-BY-4.0
├── CHANGELOG.md            ← charter version history
├── BOOTSTRAP.md            ← one-time setup procedure
├── SYSTEM_ARCHITECTURE.md  ← this file
│
├── .github/workflows/      ← structure-check CI on every PR
├── scripts/                ← v0 CI guard (check-publication-structure.sh)
│
├── publications/           ← finished research, one folder per output
│   ├── YYYY-MM-DD_source-repo_short-title_vN/
│   │   ├── MANUSCRIPT.md (canonical) + .tex/.docx/.pdf (regenerated)
│   │   ├── SUPPLEMENTARY_TABLES.md
│   │   ├── README.md
│   │   ├── ai-use-disclosure.md
│   │   ├── deviations.md
│   │   ├── coi-disclosure_<author>.md
│   │   ├── internal-review.md
│   │   ├── neurips-checklist.md (Tier M ML work)
│   │   ├── scribe-checklist.md (single-case)
│   │   ├── model-card.md (released model)
│   │   ├── prisma-checklist.md + flow (Tier T review)
│   │   ├── references.bib
│   │   ├── Makefile (pandoc render + arxiv package)
│   │   ├── reproducibility-bundle/
│   │   │   ├── README.md
│   │   │   ├── PROVENANCE.md
│   │   │   ├── environment.yml
│   │   │   ├── seeds.json
│   │   │   ├── replication-log.md
│   │   │   ├── Makefile (replicate + replicate-full + verify)
│   │   │   ├── code/ (vendored or submodule-pinned)
│   │   │   └── data/ (input + derived + figures)
│   │   └── correspondence/   ← review correspondence (post-submission)
│   └── 2026-05-24_example_demo-publication_v0/   ← worked example DEMO
│
├── preregistrations/       ← Gate-3 artifacts (one per study)
├── notebooks/YYYY/MM/      ← lab notebook (Gate-1 + Gate-9 + ad-hoc)
├── coi/                    ← annual COI snapshots (one per year)
│
├── templates/              ← reusable templates referenced by the charter
│   ├── publication-folder_GUIDE.md        ← operator's guide for ingesting publications
│   ├── pre-registration_TEMPLATE.md
│   ├── exploration-plan_TEMPLATE.md
│   ├── scoping-memo_TEMPLATE.md
│   ├── lab-notebook-entry_TEMPLATE.md
│   ├── paper-README_TEMPLATE.md
│   ├── ai-use-disclosure_PARAGRAPH.md
│   ├── coi-disclosure_TEMPLATE.md
│   ├── deviations_TEMPLATE.md
│   ├── neurips-checklist_TEMPLATE.md
│   ├── reproducibility-bundle_CHECKLIST.md
│   ├── internal-review-prompt_v1.md       ← Gate-6 canonical prompt
│   ├── internal-review-counter-signature_TEMPLATE.md
│   └── reproducibility-bundle_TEMPLATE/   ← 8-file sub-skeleton for bundles
│
└── references/             ← annotated bibliography of standards
    └── references_v0.md
```

## 4. Cross-repo handoff

Project repos (private, under `cybernaut6404` — e.g. `mg-digital-twin`, `personality-central-db`) produce experimental work continuously. When a project is publication-ready, it hands off to this unit by:

1. Creating a publication folder under `publications/` with the canonical naming (`YYYY-MM-DD_source-repo_short-kebab-title_vN`).
2. Copying the manuscript source + supplementary materials into the folder (`.md` canonical).
3. Filling in the 11 compliance artifacts per the per-tier matrix in `templates/publication-folder_GUIDE.md`.
4. Running `bash scripts/check-publication-structure.sh` to verify minimum structure.
5. Running Gate-6 internal review via a separate Claude session under `templates/internal-review-prompt_v1.md`.
6. Counter-signing the review and applying any required revisions.
7. Committing the intake as a single coherent commit.

The personality-mixer publication is the canonical worked example for this workflow.

Project repos optionally add the unit pointer to their READMEs (BOOTSTRAP §8):

> *"Research from this repo publishes to `mdfy-ai-research-facility` (https://github.com/cybernaut6404/mdfy-ai-research-facility). See `CHARTER.md` there for standards."*

## 5. Tooling architecture

### 5.1 Structure-check CI (Light CI tier)

`scripts/check-publication-structure.sh` runs on every PR touching `publications/`. Verifies that every folder under `publications/` has `README.md`, `ai-use-disclosure.md`, `internal-review.md`, and a `reproducibility-bundle/` directory. Triggered by `.github/workflows/structure-check.yml`.

Per CHARTER §18's ratified CI progression triggers:
- Light → Medium triggers on the first published DOI/link 404 or first dependency-drift replication failure.
- Medium → Heavy triggers on the first silent bundle breakage or three concurrent Tier-C/E/M publications under active maintenance.

Each upgrade requires a charter amendment with the triggering incident named.

### 5.2 Reproducibility-bundle Makefile pattern

Every publication's `reproducibility-bundle/Makefile` exposes three replicate targets:

- `make replicate` — local verification only. Recomputes stats from vendored data, regenerates figures, verifies κ against published values. $0 cost, no API calls, ~10 seconds wall-clock.
- `make replicate-full` — end-to-end on cloud GPU. Regenerates raw runs/, calls the judge API. Spends real money on the operator's accounts; documented per publication.
- `make verify-only` — fastest κ delta sanity check.

The `make replicate` exit-code 0 doesn't mean "all numbers match" — it means "the verification ran cleanly." The honest delta report (e.g., `data/derived/replication-delta.md`) names MATCH / OUT_OF_TOLERANCE / NOT_VENDORED status per channel.

### 5.3 Publication-folder Makefile pattern

Every publication's `Makefile` exposes:

- `make all` — regenerate `.tex` + `.docx` from canonical `.md` via pandoc.
- `make pdf` — additionally regenerate `.pdf` via xelatex.
- `make arxiv` — build an arXiv-ready submission tarball (manuscript + supplementary + figures + bibliography in flat layout).
- `make clean` — remove all derived format outputs.

Pandoc citeproc auto-engages when `references.bib` is present in the folder.

### 5.4 Local venv pattern

Bundle-local Python venvs live at `reproducibility-bundle/.venv-stats/`, gitignored. The bundle Makefile auto-creates and populates them on first use. Dependencies are scipy + statsmodels + matplotlib + numpy for the typical Tier-M ML methods publication.

### 5.5 Template extraction pattern

When a publication intake produces new compliance artifacts that weren't in the existing template set, the intake operator extracts the patterns into `templates/` so future intakes don't retrofit. The personality-mixer intake produced 11 reusable templates (the `publication-folder_GUIDE.md` plus 4 standalone templates plus the 8-file `reproducibility-bundle_TEMPLATE/` sub-skeleton).

## 6. External integrations

| Service | Role | Account / endpoint |
|---|---|---|
| GitHub | Source hosting; release tagging; PR review | `cybernaut6404` (rick@mdfy.co.uk) |
| Zenodo | DOI minting via GitHub-Zenodo OAuth | toggled on for `cybernaut6404/mdfy-ai-research-facility`; concept DOI `10.5281/zenodo.20365321` |
| ORCID | Author identity | `0009-0004-0799-1756` |
| OSF | Tier C pre-registrations + Tier T meta-analysis pre-regs | Rick's OSF account; no pre-registrations posted yet (first will be the cross-model replication per ROADMAP) |
| AsPredicted | Alternative compact-design pre-reg venue (Tier C) | unused yet |
| Anthropic Claude (API + Cowork) | Drafting + Gate-6 internal review + κ judging | paid customer, `rick@mdfy.co.uk` |
| Modal Labs | GPU compute for `make replicate-full` + steering-server hosting | account `cybernaut6404`; current GPU = L4 (cost-optimised) |
| Supabase | personality-central-db hosting | project `nhzaawsdddkycaxragvz` (eu-west-2) |

External-integration relationships are disclosed in:
- `README.md` "Dependencies & tooling" section (standing disclosure)
- `coi/YYYY_founder-disclosure.md` annual snapshot (current: `coi/2026_founder-disclosure.md`)
- Each publication's `coi-disclosure_<author>.md` (per-publication ICMJE form)

## 7. Identity + auth

Rick Weakley is the sole author / operator of the unit in v0. Identity is anchored at:

- ORCID: `0009-0004-0799-1756` (canonical research-identity)
- Email: `rick@mdfy.co.uk` (git commits, ORCID, COI)
- GitHub: `cybernaut6404`
- All commits on `main` are attributed to `Rick Weakley <rick@mdfy.co.uk>` (history was rewritten on 2026-05-24 via filter-branch to canonicalise from the older `rick@minorgod.com`)

Per CHARTER §16, when the first non-founder collaborator joins, the unit transitions to v1 governance: Gate-6 review duty transfers to the human collaborator (AI review becomes supplementary), and an external advisor is recruited at the same time.

## 8. Knowledge-accumulation pattern

Each publication produces:
- A manuscript + reproducibility bundle (the primary research output).
- A set of compliance artifacts that double as evidence of the unit's standards being applied.
- Optional template extractions if the intake produced reusable patterns.
- A Gate-9 lessons entry in the lab notebook recording what went well, what failed, what should change next time.

The unit's knowledge compounds across publications via:
- The annotated bibliography in `references/references_v0.md` accumulating standards citations.
- The CHANGELOG.md recording charter amendments triggered by lessons learned.
- The templates in `templates/` getting tightened by each intake's pattern-extraction.
- The lab notebook entries in `notebooks/YYYY/MM/` forming a chronological audit trail.

Each new publication should be cheaper to ingest than the previous one as the templates absorb more of the pattern.

## 9. Evolution

The unit currently sits at **v0.0.4-charter**. The CHARTER's annual-review cycle (§16) means a v0.0.5 or v1 amendment is expected ~2027-05. Triggers for an early amendment:
- An incident, near-miss, or external criticism bearing on the unit's standards
- A first non-founder collaborator joining (triggers v1 governance per §16)
- A CI-progression trigger firing (per §18: first DOI/link 404 → Medium CI; first silent bundle breakage → Heavy CI)
- Substantive learnings from the personality-mixer publication's external submission

Each amendment is recorded in `CHANGELOG.md`, tagged as `vX.Y.Z-charter`, and mints a new versioned DOI under the existing concept DOI `10.5281/zenodo.20365321`.

## 10. What's *not* in scope

This unit explicitly is NOT:

- A code-hosting / experiment-execution platform. Project repos do that; the unit only archives finished work.
- A general-purpose AI lab management product. It's purpose-built for Rick's research portfolio.
- A peer-review service for external authors. Gate-6 is internal to the unit's own publications.
- A model-card registry or model-hosting service. Released models would have their own Model Card per publication, not unit-level.
- A community / collaborative-research framework. v0 is solo; v1+ governance addresses collaboration explicitly.

## 11. Open questions / future architecture

Per CHARTER §18 all v0/v1 open questions are closed as of v0.0.4. Future architectural questions that may arise:

- **Sub-projects vs separate publications.** When work spans multiple Tier C/E/M outputs (e.g. a Tier-C confirmation of a Tier-E exploration), should they live as one publication folder with versioned sub-papers, or separate publication folders cross-referencing each other? Current pattern: separate folders, cross-reference via the source-repo slug in the naming convention.

- **Cross-publication meta-analyses (Tier T).** A future Tier-T meta-analysis pooling across multiple unit publications would need a different folder structure than primary studies — possibly `publications/meta/YYYY-MM-DD_..._vN/`. Not yet exercised.

- **External-collaborator authentication.** When v1 governance arrives, the unit will need a contributor-agreement template and an authorship-credit structure (CRediT taxonomy per CHARTER §12). The template inventory has `coi-disclosure_TEMPLATE.md` but not a contributor-agreement template yet.

- **Release-engineering for the unit's own tooling.** As `templates/` and `scripts/` grow, the unit's own *tooling* may warrant its own version + DOI cadence separate from the charter's. Currently bundled under the charter version.

Future versions of this file document any architectural decisions taken in response to these or other questions.
