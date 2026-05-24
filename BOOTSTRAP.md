# Bootstrap — turning this scaffold into the live repo

These are the one-time steps to convert the scaffold folder into the live `mdfy-ai-research-facility` repository at `/Users/richardweakley/ai-workspace/mdfy-ai-research-facility`.

## 1. Place the scaffold

Move (or copy) the entire `mdfy-ai-research-facility/` folder to:

```
/Users/richardweakley/ai-workspace/mdfy-ai-research-facility/
```

(The folder is the repo. There is no nested wrapper directory; the scaffold's contents *are* the repo's contents at the root.)

## 2. Review and approve the charter

Open `CHARTER.md`. The v0 founding decisions are already baked in (see §18 for the historical record and `CHANGELOG.md` for the resolution summary). Read end-to-end once before committing — this is your last chance to override anything before the founding-commit tag goes on.

## 3. Initialize git

```
cd "/Users/richardweakley/ai-workspace/mdfy-ai-research-facility"
git init
# CHARTER §6/§19 require the protected branch to be named `main`. If your git
# defaults to `master` (or anything else), rename before the founding commit:
git branch -m main 2>/dev/null || true
# (Alternative: set the default once globally so you never have to think about
# this again: `git config --global init.defaultBranch main`.)
git add .
git commit -m "Founding commit: mdfy-ai-research-facility v0.0.3-charter"
git tag -a v0.0.3-charter -m "Charter v0.0.3 adoption — scaffold complete (LICENSE, CI, review prompt v1, worked-example DEMO)"
```

## 4. Decide on remote hosting

Two practical options:

- **Single private GitHub/GitLab repo** at `[your-handle]/mdfy-ai-research-facility` — simplest, matches the v0 scope.
- **GitHub organization** — create a private org now even if you're the only member, so the future scaling path (per-project repos linking back) doesn't require rearrangement later.

Either way, push the founding commit to the remote.

## 5. Connect Zenodo for DOI minting

Sign in to Zenodo with the GitHub account that owns the repo. Flip the toggle for `mdfy-ai-research-facility`. From that point, every tagged GitHub release mints a versioned DOI on Zenodo, with a concept DOI spanning all versions. The first time you do this for the founding commit itself is optional (it creates a citable DOI for the charter); afterward, every publication's reproducibility bundle gets its own DOI by way of a tagged release.

## 6. First lab notebook entry

Add `notebooks/2026/05/2026-05-24_founding-session.md` describing the founding session, using `templates/lab-notebook-entry_TEMPLATE.md`. This both bootstraps the notebook habit and provides the first entry the charter can reference.

## 7. Optional: light CI

A simple GitHub Action that validates the structure of `publications/*/` against `templates/reproducibility-bundle_CHECKLIST.md` (presence of `reproducibility-bundle/`, `ai-use-disclosure.md`, `README.md`, `internal-review.md`) is enough for v0. The CI grows later.

## 8. Cross-repo integration

For each project repo that will eventually publish into this unit, add a one-line note in its README:

> "Research from this repo publishes to `mdfy-ai-research-facility` (`/Users/richardweakley/ai-workspace/mdfy-ai-research-facility/`). See `CHARTER.md` there for standards."

When a project finishes, it hands off:
- the manuscript source,
- the reproducibility bundle (frozen at a tagged commit of the project repo),
- the AI-use record,
- the pre-registration or exploration plan (already committed at Gate 3).

The unit's repo receives this as a new folder in `publications/` per the naming convention in CHARTER §14.

---

*Bootstrap complete when: founding commit is tagged (`v0.0.3-charter`), remote is configured, Zenodo is connected, and the first lab notebook entry is in place. The charter's founding decisions are resolved as of v0.0.3 — no remaining `[ASSUMED]` items.*
