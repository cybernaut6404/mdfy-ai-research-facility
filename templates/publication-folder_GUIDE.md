# Publication-folder structure — operator's guide

This file is the canonical guide to the structure of every publication folder
under `publications/` in this unit. It is the answer to "what files do I need
to create when a project repo hands off a publication to the unit?"

Folder naming convention (CHARTER §14): `YYYY-MM-DD_source-repo_short-kebab-title_vN`

---

## File-by-file requirements

| File / dir | Required for | Template / pattern source | Notes |
|---|---|---|---|
| `README.md` | every publication | `templates/paper-README_TEMPLATE.md` | The first thing a reviewer or replicator reads. Includes provenance, format inventory, unit-compliance status against this guide. Update the unit-compliance section explicitly as artifacts are added; don't leave it stale. |
| `manuscript.md` (and `.tex` / `.docx` / `.pdf` regenerated) | every publication | original draft from the source project | The canonical source is `.md`. Generated formats via the `Makefile`. |
| `ai-use-disclosure.md` | Tier 3 + Tier 4 publications (i.e. all publications with non-trivial AI assistance) | `templates/ai-use-disclosure_PARAGRAPH.md` | Itemise Tier-3 and Tier-4 contributions per-element. Tier 4 needs a per-element accountability table per `AI_USE_POLICY.md`. |
| `deviations.md` | every Tier C / Tier E publication; also any Tier M / Tier T that had a Gate-3 plan | `templates/deviations_TEMPLATE.md` | If no Gate-3 plan existed (work pre-dates unit adoption, etc.), the file *still exists* and explicitly documents the pre-registration gap. |
| `coi-disclosure_<author>.md` | every publication, one per human author | `templates/coi-disclosure_TEMPLATE.md` | Per-publication ICMJE-style disclosure. Cross-reference the annual `coi/YYYY_founder-disclosure.md` snapshot. |
| `internal-review.md` | every publication | produced by the Gate-6 reviewer, NOT a fill-in template | The Gate-6 reviewer (an AI under `templates/internal-review-prompt_v1.md` in v0; a human collaborator from v1 governance) writes this in full; the human counter-signature template is appended via `templates/internal-review-counter-signature_TEMPLATE.md`. |
| `neurips-checklist.md` | Tier M ML work | `templates/neurips-checklist_TEMPLATE.md` | The 16-item NeurIPS Paper Checklist completed against this publication's claims. |
| `scribe-checklist.md` | Tier C / Tier E self-experimentation or other single-case experimental designs | (SCRIBE 2016 Statement — author authors per the published reporting items) | N/A if the work is not a single-case behavioural intervention. |
| `model-card.md` | Tier M where a model is released publicly | (Mitchell et al. 2019 Model Card template — see `references/references_v0.md`) | If the publication does NOT release a public model checkpoint, this is N/A. |
| `prisma-checklist.md` + `prisma-flow.[png|svg|pdf]` | Tier T systematic reviews and meta-analyses | (PRISMA 2020 Statement) | N/A for primary studies and methods publications. |
| `self-critique_pre-Gate-6.md` | optional but recommended for Tier M and Tier E | n/a — drafting LLM's self-assessment from the source project | Historical context for the Gate-6 reviewer; closes a Gate-6 finding pattern where the review references self-critique material that would otherwise be uncommitted. |
| `correspondence/README.md` + correspondence files | every publication once submission begins | `correspondence/README.md` template inline (this guide; copy from a recent publication) | Naming convention: `YYYY-MM-DD_venue_kind_v<N>.{md,pdf,eml}`. Empty at intake. |
| `reproducibility-bundle/` (directory) | Tier C / Tier E / Tier M | `templates/reproducibility-bundle_TEMPLATE/` | Subfolder structure documented below. |

## Reproducibility-bundle subfolder (`reproducibility-bundle/`)

| File / dir | Template / pattern source | Notes |
|---|---|---|
| `README.md` | `templates/reproducibility-bundle_TEMPLATE/README_TEMPLATE.md` | Per-item compliance table against `templates/reproducibility-bundle_CHECKLIST.md`. Be honest — pointer-only vs vendored vs end-to-end-run is a real distinction. |
| `PROVENANCE.md` | `templates/reproducibility-bundle_TEMPLATE/PROVENANCE_TEMPLATE.md` | Chain of derivation from every input artifact to every headline figure / table / claim. Name producing script + pinned commit SHA for each row. |
| `environment.yml` | `templates/reproducibility-bundle_TEMPLATE/environment_TEMPLATE.yml` | Conda env spec. Pin Python version and direct dependencies; lift a transitive lockfile (`uv.lock` or `conda-lock.yml`) from the source repo before any external submission. |
| `seeds.json` | `templates/reproducibility-bundle_TEMPLATE/seeds_TEMPLATE.json` | Schema includes model loading params, decoding params, randomisation seeds. TODO markers acceptable at v0; must close before external submission. |
| `replication-log.md` | `templates/reproducibility-bundle_TEMPLATE/replication-log_TEMPLATE.md` | Records every end-to-end run of the bundle on a fresh machine. Honest "not yet run" entry is acceptable at v0 with the closure path enumerated. |
| `Makefile` | `templates/reproducibility-bundle_TEMPLATE/Makefile_TEMPLATE` | The `replicate` target re-derives the headline figures from raw inputs. Stub `walk-the-operator` Makefile is acceptable at v0 if Gate-7 finalisation is pending; real `replicate` is required before any external submission. |
| `code/README.md` | `templates/reproducibility-bundle_TEMPLATE/code/README_TEMPLATE.md` | If the bundle vendors source code: standard package layout. If pointer-only: lists source-repo SHAs and access procedure. |
| `data/README.md` | `templates/reproducibility-bundle_TEMPLATE/data/README_TEMPLATE.md` | Data inventory with provenance, license, FAIR-aligned metadata, and (if pointer-only) access procedure. |

## Per-tier matrix

| File | Tier C | Tier E | Tier M | Tier T |
|---|---|---|---|---|
| README.md | ✓ | ✓ | ✓ | ✓ |
| manuscript.md + renders | ✓ | ✓ | ✓ | ✓ |
| ai-use-disclosure.md | ✓ | ✓ | ✓ | ✓ |
| deviations.md | ✓ | ✓ | recommended | recommended |
| coi-disclosure_*.md | ✓ | ✓ | ✓ | ✓ |
| internal-review.md (Gate 6) | ✓ | ✓ | ✓ | ✓ |
| reproducibility-bundle/ | ✓ | ✓ | ✓ | (where data exists) |
| neurips-checklist.md | ✓ (ML work) | ✓ (ML work) | ✓ (ML work) | — |
| scribe-checklist.md | ✓ (single-case) | ✓ (single-case) | — | — |
| model-card.md | (released model) | (released model) | ✓ (released model) | — |
| prisma-checklist.md + flow | — | — | — | ✓ (systematic review / meta-analysis) |
| correspondence/ | ✓ | ✓ | ✓ | ✓ |
| self-critique_pre-Gate-6.md | optional | optional | optional | optional |

## Operator workflow at intake

When a project repo hands off a publication to the unit:

1. Create the publication folder under `publications/` with the canonical name.
2. Copy the source manuscript + supplementary materials into the folder (`.md` canonical).
3. For each file in the *Per-tier matrix* applicable to the publication's tier, either:
   - copy the source-project's existing artifact (if it has one), or
   - copy the corresponding template from `templates/` and fill it in.
4. Generate the reproducibility-bundle subfolder structure from `templates/reproducibility-bundle_TEMPLATE/`.
5. Write a Gate-1 idea-capture entry in `notebooks/YYYY/MM/YYYY-MM-DD_short-title.md`. If the work pre-dates the Gate-1 step, write a *retrospective* Gate-1 entry that explicitly disclaims the gap (see the personality-mixer publication's intake notebook entry for the pattern).
6. Run `bash scripts/check-publication-structure.sh` from the repo root. Fix any structural failures.
7. Run Gate-6 internal review via `templates/internal-review-prompt_v1.md` — spawn a separate Claude session as a sub-agent in v0 governance.
8. Save the Gate-6 output as `internal-review.md`; append the human counter-signature via `templates/internal-review-counter-signature_TEMPLATE.md`.
9. Commit the intake as a single coherent commit.

For an exemplar intake, see [publications/2026-05-24_personality-mixer_activation-steering-validation_v0/](../publications/2026-05-24_personality-mixer_activation-steering-validation_v0/) and the corresponding Gate-1 entry [notebooks/2026/05/2026-05-24_personality-mixer-paper-intake.md](../notebooks/2026/05/2026-05-24_personality-mixer-paper-intake.md).

## What is NOT covered by this guide

- **The manuscript content itself.** This guide is structural only.
- **Pre-registration / Exploration Plans** (Gate 3). Those live in `preregistrations/`, not in publication folders. See `templates/pre-registration_TEMPLATE.md` and `templates/exploration-plan_TEMPLATE.md`.
- **Scoping Memos** (Gate 2). Those live in the project repo or `preregistrations/<source>_scoping-memo.md`. See `templates/scoping-memo_TEMPLATE.md`.
- **Lab-notebook entries**. Those live in `notebooks/YYYY/MM/`. See `templates/lab-notebook-entry_TEMPLATE.md`.

## Evolution

This guide is updated when:
- A new compliance artifact is added to the unit's standards (e.g., a new tier checklist item).
- An intake operator finds a gap in the template inventory (file the gap, add the template, update this guide).
- The CHARTER's tier framework evolves.

Last updated: 2026-05-24 (initial version, derived from the personality-mixer intake).
