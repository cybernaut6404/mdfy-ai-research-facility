# Reproducibility Bundle — DEMO

> **⚠ DEMO.** Worked example of a Tier-M reproducibility bundle. Contains real code that runs but produces no research findings.

## How to reproduce

From this directory:

```
make replicate
```

This runs:

1. The repo-level CI guard `scripts/check-publication-structure.sh` (verifying the publication folder's structural compliance).
2. The independent Python verifier `code/01_verify_bundle_structure.py` (verifying this bundle's own required files).

Both must exit 0 for the "headline result" of the DEMO to hold.

## What's in this bundle

- `Makefile` — entry point for `make replicate`.
- `environment.yml` — minimal Python environment (3.11 + standard library; no third-party deps).
- `seeds.json` — empty seed table (no randomness in this DEMO).
- `code/01_verify_bundle_structure.py` — the verifier.
- `data/` — placeholder; the DEMO uses no data.
- `PROVENANCE.md` — chain from inputs to the headline result.
- `replication-log.md` — record of the founder's end-to-end run.

## Notes for real publications

A real Tier-M publication would replace each of these files with substantive content: real code in `code/`, real data or pointers-plus-checksums in `data/`, pinned third-party dependencies in `environment.yml`, real random seeds, and a `PROVENANCE.md` that traces actual headline figures back to raw inputs through named scripts.
