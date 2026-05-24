# `code/` — TEMPLATE

The code that produced the manuscript's results. At Gate-7 closure, this
directory is fully vendored or git-submodule-pinned. Until then, it can
operate in pointer-only mode (this template).

## Source-of-truth commits (pinned)

The following commit SHAs define the exact source code state that produced
every claim in the manuscript:

| Repository | Role | HEAD at pack assembly |
|---|---|---|
| `[source-repo-1]` | [Validation harness / extraction / etc.] | `[SHA]` |
| `[source-repo-2]` | [Data pipeline / models / etc.] | `[SHA]` |

All repos are at GitHub under `[ACCOUNT/ORG]/[REPO]`.

## Files specifically referenced by the manuscript

For each source file mentioned by name in the manuscript, list the path at
the pinned SHA + a one-line role description.

## Gate-7 finalisation options

Three options for closing the pointer-only state. Pick one before any external
submission:

1. **Vendor into `code/`.** Copy the named files at the pinned SHAs into
   `code/<source-repo>/<path>`. Simplest; bundle is fully self-contained;
   downside is bundle gets large and license terms must be checked for every
   third-party dependency. Recommended for the smallest-possible
   self-contained bundle for arXiv attachment.
2. **Git submodules pinned at SHAs.** Add source repos as git submodules of
   this publication folder, pinned at the listed SHAs. Bundle stays small;
   replicator runs `git submodule update --init` then `make replicate`.
   Downside: source repos must be public for a third party to clone.
3. **Pointer + access-on-request.** Leave the bundle in pointer-only state,
   document the access procedure below. Acceptable only at preprint stage
   while source repos are being prepared for public release; fails the
   unit's TOP Level-2 standard and any journal with an open-data policy.

## Access procedure (Option 3 only)

A third party wishing to verify the results can:

1. Contact the corresponding author at [EMAIL] requesting read access.
2. The author grants time-limited read access to a clone of each repo at the
   pinned SHA, with a written usage agreement bounded by the unit's
   Apache-2.0 (code) and CC-BY-4.0 (content) licenses.
3. The third party clones the repos, installs the env per `environment.yml`,
   and runs the validation harness with their own credentials.
4. The third party records their run in `../replication-log.md` and PRs the
   updated log back to this publication folder.
