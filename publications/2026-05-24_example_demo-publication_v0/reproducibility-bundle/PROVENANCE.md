# Provenance — DEMO

> **⚠ DEMO.** Worked example of a `PROVENANCE.md` for a Tier-M publication. Real publications trace every headline figure and table back through the named scripts to the raw inputs.

## Chain of derivation

| Manuscript artifact | Producing script | Inputs | Outputs |
|---------------------|------------------|--------|---------|
| §3 "Results" — claim that the DEMO folder passes the v0 structure check | `code/01_verify_bundle_structure.py` | The publication folder itself (file presence) | Exit code (0 = pass) printed to stdout; recorded in `replication-log.md` |
| §3 "Results" — same claim, redundantly verified at the repo level | `scripts/check-publication-structure.sh` (repo-root) | The publications/ directory (file presence) | Exit code (0 = pass); recorded in `replication-log.md` |

## Manual steps

None. Every artifact named in the manuscript is produced by one of the named scripts above. No manual coding, no expert-judgment steps, no spreadsheet operations.

## Inputs

The "inputs" to this DEMO are the files of the publication folder itself; the DEMO is self-referential by design. For real publications, this section names: raw data files (with checksums), pretrained model checkpoints (with hashes), prompt templates, external API endpoints used (with timestamps of retrieval), and any randomness sources.

## Determinism

This DEMO is fully deterministic — both verifiers depend only on file existence. No randomness. For real publications, this section documents random seeds (in `seeds.json`), GPU non-determinism mitigations, and any irreducible sources of stochasticity in the analysis.

## Tolerance

The DEMO's headline result is a single bit (pass/fail); no tolerance is needed. For real publications, this section states the numerical tolerance within which a re-run is considered to match the published numbers.

## License of artifacts

The DEMO's code is Apache-2.0 per repo `LICENSE-CODE`. Manuscript and provenance content are CC-BY-4.0 per repo `LICENSE-CONTENT`. No data is bundled.
