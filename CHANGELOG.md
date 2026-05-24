# Changelog

All notable changes to the `mdfy-ai-research-facility` charter, standards, and policies are recorded here.

## [v0.0.3-charter] — 2026-05-24

### Scaffold completion

The v0.0.2 charter shipped with two open questions deferred to v1. The first of those — the hardened Gate-6 internal-review prompt — is closed at v0.0.3. The remaining open question (CI maturity progression triggers) stays open for the v1 charter review. The repository scaffold is now complete enough for first adoption.

### Added

- **`LICENSE-CODE`** — full Apache License 2.0 text with copyright assigned to Rick Weakley / `mdfy-ai-research-facility`. Charter §13.
- **`LICENSE-CONTENT`** — Creative Commons Attribution 4.0 International reference, attribution language, and pointer to the canonical legal text. Charter §13.
- **`.github/workflows/structure-check.yml`** — GitHub Actions workflow that runs the v0 CI guard (`scripts/check-publication-structure.sh`) on every push to `main` and every pull request touching `publications/`. Charter §6.
- **`.gitignore`** — macOS / Windows / Linux / IDE / Python / Node / data-file conventions, with explicit instructions to keep lockfiles committed for reproducibility.
- **`.gitattributes`** — LF line-ending normalization, binary-format marking, Git-LFS hint patterns (commented), GitHub Linguist hints.
- **`.editorconfig`** — UTF-8 / LF / 2-space indent baseline, with per-format overrides (Python 4-space, Makefile tabs, Markdown trailing-whitespace preservation).
- **`templates/internal-review-prompt_v1.md`** — hardened Gate-6 review prompt: ten-question schema covering tier compliance, claim-evidence calibration, pre-registration adherence, AI-use completeness, reproducibility-bundle spot check, ethics, COI, internal consistency, reservations, and recommendation; mandatory output structure; counter-signature block. Closes one of the two v0.0.2 open questions.
- **`publications/2026-05-24_example_demo-publication_v0/`** — fully-populated worked example of a Tier-M-compliant publication. Includes README, manuscript, AI-use disclosure, internal review (produced under the v1 prompt), deviations, per-publication COI, and a complete reproducibility bundle (Makefile, environment.yml, seeds.json, PROVENANCE.md, replication-log.md, working Python verifier). The DEMO's headline result — "exit code 0 from both verifiers" — was actually run and recorded in `replication-log.md`. Every file is prominently marked as a DEMO.

### Changed

- **CHARTER.md** — front matter bumped to v0.0.3. §0 updated to note that one of the two original v1 open questions is now closed. §6 (Repository structure) updated to reflect the new files and directories. §18 (Open questions) rewritten: Gate-6 prompt moved to the "resolved" list; CI maturity progression remains as the single genuine open question. §19 (Adoption) updated with the v0.0.3 commit tag and a reference to the worked-example DEMO.
- **CITATION.cff** — version bumped to 0.0.3-charter.

### Verified

- Both structural verifiers (`scripts/check-publication-structure.sh` and `publications/2026-05-24_example_demo-publication_v0/reproducibility-bundle/code/01_verify_bundle_structure.py`) executed successfully against the worked-example DEMO. Exit codes recorded in the DEMO's `replication-log.md`.

### Remaining open for v1

- CI maturity progression triggers (when to upgrade from Light to Medium/Heavy CI).

## [v0.0.2-charter] — 2026-05-24

### Founding decisions resolved
The seven deferred items from v0.0.1 §18 were walked through in the founding session and baked into the charter body. Specifically:

- **Default licenses (§13):** Apache-2.0 (code) + CC-BY-4.0 (content) confirmed. Rationale: explicit patent grant on code; maximum-reuse content license.
- **IRB posture (§11):** v0 scope explicitly limited to founder self-experimentation, computational studies, and analyses of public data. IRB partnership deferred to v1, identified at scope expansion.
- **CI scope (§6):** Light tier — shell-script structure check. Implementation added at `scripts/check-publication-structure.sh`. Medium and Heavy tiers reviewed at v1.
- **COI cadence (§12):** Per-publication ICMJE disclosure + annual snapshot at `coi/YYYY_founder-disclosure.md`. Template added at `templates/coi-disclosure_TEMPLATE.md`.
- **Null and negative findings (§15):** Charter-level equal-effort publication commitment. Promoted from §18 (open question) to §15 (substantive policy).
- **AI-provider disclosure (§12, README):** Standing "Dependencies & tooling" block added to README; restated in each publication's Methods.
- **Dual-use posture (§11):** Case-by-case at the Scoping Memo gate, with Responsible-Release Review triggered when risk is non-trivial.
- **External advisor (§16):** Sought when the first non-founder collaborator joins, paired with the human-review transition. Not sought before that point.

### Added
- `scripts/check-publication-structure.sh` — v0 CI guard.
- `templates/coi-disclosure_TEMPLATE.md` — ICMJE-style disclosure template.
- `coi/` — directory for annual disclosure snapshots.
- README "Dependencies & tooling disclosure" section.

### Changed
- CHARTER.md §0 front matter bumped to v0.0.2; status updated.
- CHARTER.md §18 rewrote from a deferred-items list to a short genuine-open-questions list, with historical record of resolved items.
- CHARTER.md §16 specifies the joint trigger for human-review transition and external-advisor recruitment.
- CITATION.cff bumped to 0.0.2.

### Remaining open for v1
- Hardened structured prompt for Gate 6 internal review (working draft in STANDARDS.md).
- CI maturity progression triggers (when to upgrade from Light to Medium/Heavy).

## [v0.0.1-charter] — 2026-05-24

### Added
- Founding Charter & Operating Manual (CHARTER.md)
- Tier standards and review checklists (STANDARDS.md)
- AI Use and Disclosure Policy (AI_USE_POLICY.md)
- README, CITATION.cff
- Templates: pre-registration, exploration plan, scoping memo, reproducibility bundle checklist, AI-use disclosure paragraph, lab notebook entry, paper README
- Annotated reference list (references/references_v0.md)
- Repository skeleton (publications/, preregistrations/, notebooks/, templates/, references/)

### Known limitations
- Single-human-reviewer governance; Gate 6 internal review performed by Claude under structured prompt and counter-signed by founder.
- Several `[ASSUMED — confirm]` decision points in CHARTER.md §18 deferred to v1.
- US dual-use research policy in transitional state; v0 defers to NIH guidance by analogy.
- Lab-manual benchmarks (Lakens, Hutter) are de facto rather than canonical published artifacts.

### Authoring note
This v0 was prepared in a founding-session Cowork session by Rick Weakley with assistance from Anthropic's Claude. Per `AI_USE_POLICY.md` Tier 2: Claude drafted the initial structure and language; Rick directed the scope, decisions, and final approval.
