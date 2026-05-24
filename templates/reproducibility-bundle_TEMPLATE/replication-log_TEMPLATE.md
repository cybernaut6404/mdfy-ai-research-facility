# Replication Log — [PUBLICATION TITLE]

This file records every end-to-end replication run of this bundle on a fresh
machine. Per the unit's reproducibility-bundle standard (CHARTER §9,
STANDARDS.md), every Tier-C/E/M publication's bundle must be end-to-end run by
the author (or, where available, an independent third party) before release,
with the recovered headline numbers within the documented tolerance of the
published numbers.

---

## Status

Choose the variant that applies at the time of writing:

**Variant A — Not yet run end-to-end (acceptable at v0; closure path required):**

> The bundle has not yet been run end-to-end on a fresh machine from this
> folder. This is a Gate-7 (reproducibility-bundle finalisation) blocker for
> any external submission. The bundle is honest about it: rather than
> fabricate a replication-log entry, this file states the gap.

**Variant B — Run by author / first party only:**

> The bundle has been run end-to-end by the author from a fresh machine /
> container as recorded in §"Replication-run records" below. An independent
> third-party run is the next closure step.

**Variant C — Run by independent third party (best state, required for Tier 2+ venues):**

> The bundle has been run end-to-end by both the author and at least one
> independent third party as recorded in §"Replication-run records" below.

## What an end-to-end run would need (Variant A only)

For a replication to count under the unit's standard, the following operations
must succeed from a clean clone of this publication folder (plus the project
repos at the pinned SHAs):

1. `conda env create -f environment.yml && conda activate [ENV_NAME]`
2. Set credentials: [list required environment variables]
3. `make replicate` from this directory, which (once finalised) will:
   - Pull / vendor the source-repo code at the pinned SHAs into `code/`
   - Run the validation harness for each condition at the pre-specified
     configurations
   - Run the analyser over the resulting outputs against the committed rubrics
   - Emit `recovered-results.json` and `recovered-results.md`
4. Compare `recovered-results.json` against `data/published-results.json`
   (pre-populated with the manuscript's reported numbers) within the
   tolerance specified in `PROVENANCE.md` §"Tolerance".

When this succeeds with zero out-of-tolerance deviations, an entry is appended
to this file using the record template below.

## What's blocking a real end-to-end run (Variant A only)

In order, by closure cost:

1. [Lift X from source repo into seeds.json. ~5 minutes.]
2. [Vendor or git-submodule the source repos at the pinned SHAs into code/. ~30 minutes.]
3. [Pre-populate data/published-results.json with the manuscript's reported numbers for delta comparison. ~30 minutes.]
4. [Implement the real `make replicate` target. ~1 hour.]
5. [Run end-to-end with a fresh environment. Estimated [X] hours of GPU time + [Y] in compute + judge calls.]

Total to clear this blocker: roughly [HALF/FULL] day of focused work plus the
real money cost of one end-to-end run.

## Replication-run records

Template for each entry:

```
### YYYY-MM-DD — replicator: NAME

- Machine: macOS / Linux / WSL2 + chip + RAM
- GPU: Modal L4 / local GPU / CPU-only
- Environment hash: SHA256 of the resolved environment lockfile
- Cloud accounts: [Modal, Anthropic, etc.]
- Run wall-clock time: HH:MM
- Run cost: $X compute + $Y judge calls
- Headline-metric deltas (recovered vs published):
  - [Metric 1]: [recovered] vs [published] → [delta] [✓ within tolerance / ❌ out of tolerance]
  - [Metric 2]: ...
- Deltas outside ±[tolerance]: [none | list]
- QC checks pass: YES / NO
- Notes: [any deviations, warnings, environment issues]

Signature: [REPLICATOR NAME]
Status: PASS / PARTIAL / FAIL
```

---

## Acknowledgement of the gap (Variant A only)

This empty log is, by the unit's standards (CHARTER §9), an honest disclosure
that the bundle is not yet fully reproducible by an independent third party.
A successful end-to-end run from this bundle, recorded here, is a hard
requirement before any preprint posting under the unit's standards.
