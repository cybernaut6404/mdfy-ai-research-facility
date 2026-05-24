# 2026-05-24 — Intake of the personality-mixer activation-steering validation paper into the unit

**Project:** `personality-mixer` ecosystem (originating workspace: `mg-digital-twin` + `personality-central-db` + `personality-construct-runner` + `personality-mixer-codex` + `personality-mixer-claude` + `mdfy-GSTACK`).
**Tier:** M (methods/engineering) with secondary exploratory findings — assigned by author; Gate-6 internal review will confirm or override.
**Time:** 2026-05-24 afternoon, immediately following the v0.0.4-charter amendment and during the same bootstrap session.
**AI assistance this session:** Anthropic Claude (model `claude-opus-4-7-1m`) — this session, drafting the compliance artifacts (`ai-use-disclosure.md`, `deviations.md`, `coi-disclosure_weakley.md`, `neurips-checklist.md`, full `reproducibility-bundle/` skeleton, `correspondence/README.md`) and orchestrating the Gate-6 review. The originating research and the manuscript draft were produced in a separate Cowork session by a different Claude instance (model `claude-opus-4-7-1m`, with earlier validation runs on `claude-opus-4-6`) — see `publications/2026-05-24_personality-mixer_activation-steering-validation_v0/ai-use-disclosure.md` for the full record.

This is a **publication-touching session** per CHARTER §10's transcript-mirror procedure (introduced at v0.0.4). The full prompt archive will be deposited at the publication folder's `ai-use-disclosure.md` per `AI_USE_POLICY.md` §"Archive requirements" before any external submission.

---

## What I set out to do

Bring the personality-mixer activation-steering validation pack (drafted in a separate Cowork session and pasted into this conversation by Rick) into the unit's repository under canonical naming and standards. The pack pre-dates the unit's adoption — it was assembled on 2026-05-24 before the v0.0.3-charter founding commit landed the same day — so this intake is retroactive compliance work rather than from-the-gates work.

The bar Rick set explicitly: "don't undercook it." The pack is the first real publication ingested by the unit, and the way I handle it sets the template for every subsequent project-repo handoff. Every shortcut here propagates.

## What I actually did

### Re-naming and relocation

- The original pack at the source machine was at
  `mdfy-ai-research-facility/RESEARCH-PUBLICATIONS/2026-05-24_personality-mixer_activation-steering-validation/`.
  Two non-compliance issues with that path:
  1. `RESEARCH-PUBLICATIONS/` should be `publications/` per CHARTER §6.
  2. Folder name should carry `_v0` suffix per CHARTER §14's
     `YYYY-MM-DD_source-repo_short-kebab-title_vN` convention.
- Both fixed. Canonical location is now
  `publications/2026-05-24_personality-mixer_activation-steering-validation_v0/`.

### Source-of-truth files written from the pasted .md sources

- `MANUSCRIPT.md` (~4,700 words; structure preserved verbatim, mojibake cleaned to proper UTF-8 at write time — em-dashes, ×, κ, ≥, ≤, →, ↔, ≈, − all corrected; original mojibake patterns were `â`, `Ã`, `Îº`, `â¥`, `â¤`, `â`, `Â§`, etc.)
- `SUPPLEMENTARY_TABLES.md` (S1–S7 + compute/cost provenance; UTF-8 cleaned)
- `ROADMAP_TO_TOP_VENUES.md` (4-tier venue path; UTF-8 cleaned)
- `README.md` (the publication folder's README; rewritten to reference the canonical unit-compliant path and to include a "Unit-compliance status" section documenting the gaps against v0.0.4 standards)
- `WORK_LOG.md` (the chronological build-and-validation log; UTF-8 cleaned, path references corrected)
- `Makefile` (manuscript-render Makefile; cleaned of the `sed`-based mojibake substitutions that the original needed but the cleaned UTF-8 sources don't)

### New compliance artifacts created from scratch under v0.0.4 standards

- `ai-use-disclosure.md` — full Tier 3 + Tier 4 disclosure. Critical: under v0.0.4's sharpened direction-of-intellectual-origin test (AI_USE_POLICY.md), Claude's contributions to this paper are **partly Tier 4**, not pure Tier 3. The three "methodological findings" framings (§4.1 probe-instrument-is-decisive, §4.2 multi-layer-rescues-single-layer, §4.3 vector-basis-is-psychometrically-coherent) were originated by the drafting Claude and accepted by Rick — those are Tier 4 elements per the new boundary. So are the "RLHF-floor" framing of sadism and the 4-tier ROADMAP structure. Per-element accountability table written in `ai-use-disclosure.md` §2.3.
- `deviations.md` — formal disclosure of the pre-registration gap. The H1–H3 in MANUSCRIPT §1.2 read "pre-specified" but the build notes are not externally time-stamped, so the framing is post-hoc per the drafting LLM's own self-critique. Recommended revision tracked.
- `coi-disclosure_weakley.md` — ICMJE per-publication disclosure. The interesting items: Anthropic is both manuscript drafter AND blind-rater judge (one-vendor dual role; load-bearing methodological caveat); the author operates a commercial product (`mdfy-personality-registry`) that depends on this substrate (intellectual / commercial COI disclosed); the single subject is the author.
- `reproducibility-bundle/README.md` — bundle README with a honest per-item compliance status table.
- `reproducibility-bundle/PROVENANCE.md` — chain of derivation from raw inputs to every headline claim. Names every input with source-repo + pinned SHA. Tolerance for replication: κ ±0.05.
- `reproducibility-bundle/environment.yml` — conda env spec, top-level deps pinned; transitive lockfile is Gate-7 TODO.
- `reproducibility-bundle/seeds.json` — decoding params and randomisation seeds; multiple TODOs marked where the original code's exact values need to be lifted from the source repo.
- `reproducibility-bundle/replication-log.md` — honest disclosure that the bundle has NOT been run end-to-end. Documents what closure looks like and what's blocking.
- `reproducibility-bundle/Makefile` — stub Makefile that walks the operator through the manual steps until Gate-7 vendors the source code.
- `reproducibility-bundle/code/README.md` — pointer to the five source repos at pinned SHAs (mg-digital-twin@f492844, personality-central-db@2bdf13b, personality-construct-runner@d55296b, mixers@5462733 / 3963ce4), with three options for closure (vendor / submodule / access-on-request).
- `reproducibility-bundle/data/README.md` — pointer to the contrastive items, probes, rubrics, run artifacts, and steering vectors.
- `neurips-checklist.md` — completed against the NeurIPS Paper Checklist Guidelines (required by STANDARDS Tier-M for ML work). Identifies item 7 (statistical significance — no CIs, no binomial tests, no FDR correction) as the load-bearing TODO. 11 items satisfied; 5 partial / TODO; 4 N/A.
- `correspondence/README.md` — empty placeholder with naming convention for future submission correspondence.

### Gate-6 internal review

- Spawned a separate Claude session (general-purpose agent) running the v1 internal-review prompt against the manuscript + all the compliance artifacts above. The agent has the full v1 prompt, the manuscript, the deviations doc, the AI-use disclosure, the PROVENANCE, the supplementary tables, the roadmap, the NeurIPS checklist, and the bundle README as inputs. Per CHARTER §16 the output will be saved as `internal-review.md` and counter-signed by Rick.
- Running in the background as of this notebook entry; result will land in a subsequent commit.

## What worked

- The mojibake cleanup at write time was the right call. Writing the pasted text verbatim would have committed corrupted Unicode to the canonical source. Reverse-decoding `text.encode('latin-1').decode('utf-8')` patterns in my head and emitting proper Unicode (κ, ×, ≥, →, ↔, ≈, −, em-dash) on the way to disk produced clean files that don't need a separate fix-up pass.
- Treating every missing artifact as a real first-class file (not a stub or TODO) forced me to engage seriously with each one. The `deviations.md` writeup of the pre-reg gap is more useful than the same content as a footnote in the manuscript; the `ai-use-disclosure.md` Tier 4 per-element accountability table is more useful than a single inline disclosure paragraph.
- The honest-state disclosures throughout the bundle (`replication-log.md`'s "not yet run" entry; `code/README.md`'s "three options for closure"; the NeurIPS-checklist item 7 "load-bearing TODO") avoid the trap of pretending the bundle is more reproducible than it is. A Gate-6 reviewer or external replicator can see exactly what's missing and what closing the gap looks like.

## What didn't

- I cannot yet end-to-end-run the bundle from this MacBook — the source repos live on the MacMini and the steering-server lives on Modal. Closing the `replication-log.md` entry requires either (a) Tailscale + remote run, or (b) waiting for the Gate-7 vendor-into-`code/` pass.
- The contrastive items + probe libraries + judge rubrics live in the source repo and I have not mirrored them into `data/`. The data/README documents the access procedure but the artifacts themselves are still pointer-only.
- The full prompt archive from the original drafting session (the Cowork session on the MacMini that produced the manuscript) has not yet been deposited at the publication folder's `prompts/` subdirectory. This is required before arXiv preprint posting per AI_USE_POLICY.md §"Archive requirements" and is flagged in `ai-use-disclosure.md` §2.4.

## What I learned

- The v0.0.4 direction-of-intellectual-origin test for Tier 3/4 boundary really does cut differently than the old "size of contribution" reading. The manuscript's central framings (the three methodological findings, the RLHF-floor interpretation, the 4-tier roadmap) were not specified by Rick in advance — they emerged from Claude's reading of the data and were accepted by Rick. That's Tier 4 per the new boundary, even though each contribution is bounded (one paragraph, one verb, one structure). A pre-v0.0.4 reading of the same work would have called this Tier 3.
- The unit's compliance framework imposes real cost on retroactive pack ingestion. The pack came with manuscript + supplementary + roadmap + README + work log — five files. The unit's standards added 11 more files (ai-use-disclosure, deviations, coi, neurips-checklist, bundle README + PROVENANCE + env.yml + seeds.json + replication-log + bundle Makefile + code/README + data/README + correspondence/README). That's ~3× the file count and substantially more author-decision content per file. The cost is justified — each artifact carries information a reviewer or replicator needs — but it's a real cost. Future project-repo handoffs to the unit should ideally produce most of these artifacts AT the project repo before handoff, rather than be retrofitted at intake.
- The drafting LLM's self-critique (attached by Rick at the start of this session) was load-bearing. It pre-flagged exactly the items that Gate 6 will land hardest on: pre-registration gap, "overturns" calibration, no figures, no real bibliography, no statistical analysis beyond directional accuracy, single-subject / single-model / single-judge. Treating the self-critique as a pre-Gate-6 input let me build artifacts that engage seriously with those weaknesses (e.g., `deviations.md` explicitly addresses the pre-reg framing problem; `neurips-checklist.md` calls out item 7 statistical significance as load-bearing TODO).

## Decisions taken

1. **Folder name** — `2026-05-24_personality-mixer_activation-steering-validation_v0/` (added `_v0` suffix per CHARTER §14).
2. **Folder parent** — `publications/` (lowercased per CHARTER §6, replacing the pre-adoption `RESEARCH-PUBLICATIONS/`).
3. **Source-repo slug** — `personality-mixer` (covering the whole ecosystem of source repos; the validation-specific code is in `mg-digital-twin` but the wider system is the personality-mixer ecosystem).
4. **Tier assignment** — Tier M (methods/engineering) with secondary exploratory findings. The contribution is the validation methodology + three methodological findings + the substrate; H1–H3 results are exploratory secondary findings. Tier C is structurally inaccessible (no Gate-3 pre-reg); Tier E doesn't quite fit because the substantive contribution is methodological rather than hypothesis-generating. Gate-6 will confirm or override.
5. **AI-use tier classification** — Tier 3 + Tier 4 hybrid per the v0.0.4 direction-of-intellectual-origin test. Per-element accountability table in `ai-use-disclosure.md` §2.3.
6. **Bundle code/data state** — pointer-only at v0 (access-on-request); Gate-7 finalisation TODO with three options documented (vendor / submodule / access-on-request).
7. **Manuscript revisions** — NOT done in this intake. The calibration fixes (e.g. "overturns" → "challenges"; H1–H3 reframed) are tracked as Gate-6 findings and will land in a subsequent revision commit, separate from the intake commit, so the intake state preserves what was actually drafted.
8. **Spawned Gate 6 sub-agent in background** rather than running it inline, to maintain some review independence between the drafting Claude (Cowork session) and the reviewing Claude (sub-agent under the v1 prompt with the structured inputs only).
9. **Transcript-mirror category** — this session is publication-touching per the new CHARTER §10 procedure. The prompt archive will be deposited at the publication's `ai-use-disclosure.md` archive before submission; no separate `notebooks/2026/05/_transcripts/` mirror is required.

## Open threads

- **Gate-6 internal-review.md** — sub-agent is running in the background; result will land in a subsequent commit alongside Rick's counter-signature.
- **Manuscript calibration revisions** (per the self-critique and Gate-6 expected findings) — "overturns" → "challenges"; H1–H3 reframed in §1.2; possibly add the "Broader impacts" subsection per the NeurIPS checklist item 10. These should land as a revision commit, not as edits to v0.
- **Gate-7 reproducibility-bundle finalisation** — vendor the source code into `code/`; vendor the data into `data/`; lift the exact HuggingFace revision SHA, judge temperature, and position-randomisation seed into `seeds.json`; run the bundle end-to-end on a fresh machine and record in `replication-log.md`.
- **Prompt archive deposition** — the full Cowork-session transcript that produced the manuscript needs to be deposited at the publication folder's `prompts/` subdirectory before any arXiv preprint posting.
- **Manuscript figures** — per the self-critique, real top-tier work would have: (i) a κ-distribution forest plot; (ii) an inter-channel cosine heatmap; (iii) a refusal-cosine scatter with the FLAG threshold. ~2 hours with matplotlib. Should land before TMLR submission.
- **Manuscript statistics** — per the self-critique and the NeurIPS-checklist item 7, real top-tier work would have: per-channel binomial tests vs chance, Bonferroni or BH-FDR correction across 24 channels, 95% CIs on κ, Cohen's h effect sizes. ~half day with scipy.stats. Load-bearing TODO before TMLR.
- **Real bibliography** — the manuscript references list is currently illustrative (no DOIs, no .bib). ~3 hours to assemble. Required before any external submission.
- **Unit-level template emerging from this intake** — the artifact set I built for this paper (the 11 added files beyond the original 5 the project-repo provided) is the de facto template for future project-repo handoffs. Worth formalising as `templates/publication-folder_TEMPLATE/` so the next project doesn't need to retrofit at intake. Tracked as a future unit-tooling task.

## AI session notes

Session was a Claude Code session on the MacBook (this conversation). Prompting strategy: Rick set the bar ("don't undercook it"; "we are building a stand-alone specialist repo"; "significant project that will become a serious knowledge base for AI produced research") and then let me make decisions about the specific artifacts and content. Each artifact was drafted in one pass; iterative revision would happen during Gate-6 counter-signature review.

The Cowork-session transcript that originally drafted the manuscript on the MacMini is referenced from `ai-use-disclosure.md` §2.4 but is not yet deposited at the publication folder. That deposition is a hard requirement before arXiv preprint posting per AI_USE_POLICY.md.

This notebook entry is itself a charter/standards-touching session under CHARTER §10's categorisation — it shapes how the unit handles project-repo handoffs going forward — but the decisions recorded here are publication-specific rather than unit-level policy. Borderline category. Per §10's "when in doubt, mirror" rule, the prompt archive for this session should be considered for mirror to `notebooks/2026/05/_transcripts/` even though the primary archive home is `ai-use-disclosure.md`.

---

*This entry is a permanent record. Corrections are made by adding a follow-up entry that cites this one, not by editing this entry.*
