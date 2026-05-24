# 2026-05-24 — Founding session: v0.0.1 → v0.0.3 in one day

**Project:** founding-session (unit-level, no project slug)
**Tier (if applicable):** n/a (charter/scaffold work, not a research output)
**Time:** session window 2026-05-24 morning through midday (Cowork) + bootstrap
session same afternoon
**AI assistance this session:** Anthropic Claude (Cowork) — scaffold drafting;
this notebook entry written by a separate Claude bootstrap session per the
adoption procedure in `BOOTSTRAP.md`.

---

## What I set out to do

Stand up `mdfy-ai-research-facility` as a real, version-controlled research
unit: a charter strong enough to bind my own behavior, a scaffold complete
enough to publish from, and a founding-commit tag (`v0.0.3-charter`) such
that nothing produced under the unit's name can predate adoption. The
explicit goal for the day was "ready for first research project," not
"first research project shipped."

## What I actually did

Worked in a single Cowork founding session against the canonical path
`/Users/richardweakley/ai-workspace/mdfy-ai-research-facility/`. Walked the
charter from a blank page through three versioned passes:

- **v0.0.1-charter** — initial draft of `CHARTER.md`, `STANDARDS.md`,
  `AI_USE_POLICY.md`, README, CITATION.cff, the full templates set, and the
  annotated reference list. Nine items left as `[ASSUMED — confirm]` in
  §18, awaiting deliberate resolution.
- **v0.0.2-charter** — walked through the seven founding decisions from
  v0.0.1 §18 and baked each into the body of the charter. Added the v0 CI
  guard (`scripts/check-publication-structure.sh`), the COI template, the
  annual-disclosure directory, and the README dependencies/tooling block.
  Two items left for v1: the hardened Gate-6 prompt and CI-progression
  triggers.
- **v0.0.3-charter** — closed the Gate-6 prompt question by committing
  `templates/internal-review-prompt_v1.md` (ten-question schema,
  mandatory output structure, counter-signature block). Added the LICENSE
  files (`LICENSE-CODE` Apache-2.0; `LICENSE-CONTENT` CC-BY-4.0), the
  GitHub Actions workflow `.github/workflows/structure-check.yml`, and a
  fully-populated Tier-M worked-example DEMO at
  `publications/2026-05-24_example_demo-publication_v0/`. Ran both
  structural verifiers against the DEMO and recorded the 0/0 exit codes in
  the DEMO's `replication-log.md` before tagging.

Afternoon bootstrap session (this entry):

- Re-read all five mandatory files (CHARTER, BOOTSTRAP, STANDARDS,
  AI_USE_POLICY, CHANGELOG) in order before touching git.
- Re-ran both verifiers against the now-on-disk scaffold:
  `scripts/check-publication-structure.sh` → exit 0; the Python bundle
  verifier `01_verify_bundle_structure.py` → exit 0.
- `git init` defaulted to `master`; renamed to `main` before the first
  commit because CHARTER §6 and §19 require `main` for adoption. (Noted
  here in case anyone wonders why the initial branch is `main` rather
  than git's current default.)
- Staged 42 files (no `.DS_Store` — `.gitignore` worked). Created the
  founding commit and annotated tag `v0.0.3-charter`.
- Did **not** push, did **not** add a remote, did **not** connect Zenodo.
  Remote hosting and DOI minting are deliberately deferred per
  BOOTSTRAP §4–§5 and will be done in a separate, explicit session.

## What worked

Sequencing the three charter passes as separate versions (v0.0.1 draft →
v0.0.2 decisions baked in → v0.0.3 scaffold finalized) kept each step
reviewable: the CHANGELOG is now a clean record of what was open vs.
resolved at each point, which is exactly the kind of history I'd want
anyone (including future me) to be able to audit.

Building the worked-example DEMO before tagging caught one structural
mistake I would otherwise have shipped: a publication folder is required
to contain `internal-review.md`, and writing a real one against the v1
review prompt forced the prompt itself through a dogfooding pass.

The bootstrap procedure in `BOOTSTRAP.md §3` was exact enough to follow
literally. Worth re-checking the next time a similar adoption is needed.

## What didn't

Nothing failed outright in this session, which itself is mildly suspect
for a brand-new procedure — the next adoption (e.g., when v1 lands)
should treat that as a flag and re-verify more aggressively rather than
assume the procedure is silently correct.

One real friction: git's initial-branch default is still `master` on
this machine, even though CHARTER §6/§19 specify `main`. A future
amendment to BOOTSTRAP §3 should either (a) tell the operator to run
`git config --global init.defaultBranch main` once, or (b) include the
`git branch -m master main` step inline so no one has to notice it.

## What I learned

- A research-unit charter is more useful as an enforcement document than
  as a vision document. The parts that bind my future behavior are §4
  (tier checklists), §5 (gates 1–9), §7 (AI use), §15 (null-results
  commitment), and §16 (governance). The vision parts could mostly be
  cut. Worth remembering when the v1 review tempts me to add prose.
- The single highest-leverage standard in v0 is the equal-effort
  null/negative-finding commitment in §15. Everything else in the
  charter is table stakes for credibility; that one is the part that
  actually changes incentives.
- The Gate-6 AI-as-reviewer arrangement is the weakest link by design.
  The v1 prompt mitigates it but does not fix it. The fix is human
  reviewers + an external advisor (§16), and the trigger for that fix is
  named: "first non-founder collaborator joins." Until then, every paper
  this arrangement touches carries the §16 disclosure.

## Decisions taken

All nine charter `[ASSUMED]` items from v0.0.1 §18 were resolved during
this session and baked into the charter body. Recorded in CHANGELOG
v0.0.2 and v0.0.3; restated here for the notebook record:

1. **Default licenses** (CHARTER §13): Apache-2.0 for code, CC-BY-4.0
   for content. Rationale: explicit patent grant on code; maximum-reuse
   content license. LICENSE-CODE and LICENSE-CONTENT files committed at
   v0.0.3.
2. **IRB posture in v0** (§11): self-experimentation, computational
   studies, and public-data analyses only. IRB partner identified at v1
   if scope expands.
3. **CI scope in v0** (§6): Light tier — shell-script structure check
   plus GitHub Actions workflow. Medium and Heavy tiers reviewed at v1
   (see open thread below).
4. **COI cadence** (§12): per-publication ICMJE disclosure + annual
   snapshot at `coi/YYYY_founder-disclosure.md`.
5. **Null and negative findings** (§15): charter-level equal-effort
   publication commitment, promoted from open question to substantive
   policy.
6. **AI-provider disclosure** (§12, README): standing "Dependencies &
   tooling" block in README; restated in each publication's Methods.
7. **Dual-use posture** (§11): case-by-case at the Scoping Memo gate,
   with Responsible-Release Review triggered when risk is non-trivial.
8. **External advisor** (§16): sought when the first non-founder
   collaborator joins, paired with the human-review transition. Not
   sought before that point.
9. **Gate-6 review prompt** (closed at v0.0.3): hardened ten-question
   schema committed as `templates/internal-review-prompt_v1.md`.

Operational decisions taken this afternoon (bootstrap):

10. **Branch name `main`** (not `master`) — required by CHARTER §6/§19.
    Renamed before founding commit.
11. **No remote, no Zenodo yet.** Per BOOTSTRAP §4–§5, those are
    explicit, separate steps; doing them silently here would defeat the
    point of staging adoption.

## Open threads

- **CI maturity progression (the one remaining v1 open question per
  CHARTER §18).** v0 ships Light CI (structure check). When is the
  upgrade to Medium (link/DOI validation, lockfile integrity) earned,
  and when to Heavy (on-tag end-to-end reproducibility runs)? Proposed
  triggers handed back to Rick in the bootstrap report; awaiting
  decision before §18 amendment.
- **Remote hosting choice** (BOOTSTRAP §4): private repo under personal
  GitHub vs. private org. Deferred to the next session.
- **Zenodo connection** (BOOTSTRAP §5): deferred until the first real
  publication's reproducibility bundle is ready to mint a DOI; the
  charter itself does not need a DOI in v0.
- **Source-repo handoff pattern** (BOOTSTRAP §8): each project repo
  that will publish into the unit needs the one-line pointer in its
  README. Pick this up when the first project hands off.

## AI session notes (if AI-assisted)

Two distinct AI-assisted sessions on 2026-05-24:

- **Morning (Cowork founding session)** — Anthropic Claude drafted the
  charter, standards, policy, templates, references, CI guard, LICENSE
  files, GitHub Actions workflow, Gate-6 review prompt v1, and the
  worked-example DEMO across the v0.0.1 → v0.0.2 → v0.0.3 progression.
  Rick directed scope, made every founding decision, and approved the
  full scaffold before tagging. This is Tier 2 AI use under
  `AI_USE_POLICY.md` (drafting assistance: AI generated draft text;
  human author reviewed, revised, and approved each section). No
  analysis, no data, no figures generated by AI — this session produced
  governance and scaffolding only.
- **Afternoon (this bootstrap session)** — Anthropic Claude executed
  the BOOTSTRAP procedure: read the five mandatory files in order, ran
  both structural verifiers, performed `git init` / branch-rename /
  stage / founding commit / tag, drafted this notebook entry against
  the lab-notebook template. Rick supplied the procedure prompt and
  will review this entry before the second commit lands. Same Tier 2
  classification.

The transcript of both sessions is the conversation that produced this
repo's commit history; the prompts driving them are recorded in the
respective Cowork session logs (Cowork-side artifact, not yet
mirrored into the repo — captured here so the link can be added in a
follow-up entry once the mirror procedure is decided).

---

*This entry is a permanent record. Corrections are made by adding a
follow-up entry that cites this one, not by editing this entry.*
