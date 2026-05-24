# Replication Log — DEMO

> **⚠ DEMO.** Worked example. The "run" recorded here is the structural check, not real research replication.

## Run 1 — founder, fresh checkout

- **Date:** 2026-05-24
- **Operator:** Rick Weakley (founder; v0 self-check)
- **Machine:** macOS, Apple Silicon (host of the founding-session Cowork workspace)
- **Python version used:** 3.11 (standard library only; no third-party dependencies needed for the DEMO verifier)
- **Command:** `cd reproducibility-bundle && make replicate`
- **Result:** Exit code 0 from both verifiers (`scripts/check-publication-structure.sh` and `code/01_verify_bundle_structure.py`).
- **Headline numbers match published?** N/A — the DEMO's headline result is the boolean exit-code outcome; the manuscript reports "exit code 0" and the run produced exit code 0. Match.

## Notes

This DEMO's replication is trivial: no data, no randomness, no compute beyond file-existence checks. Real publications record:

- the machine class and the operating system version;
- the exact commit hash and tag the run was performed against;
- the time elapsed and any resource usage that matters;
- the recovered headline numbers, each compared to the published number within the documented tolerance;
- any deviations encountered during the run (e.g., a dependency that broke, a flaky GPU operation), with mitigation.

The bundle is considered "replicable" only after Run 1 — an end-to-end re-run on a fresh machine — passes. Subsequent runs by independent third parties (when available) are added as Run 2, Run 3, etc.
