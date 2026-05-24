# `data/` — TEMPLATE

The data that fed the validation: raw inputs, processed intermediates, run
artifacts, and (where applicable) trained model checkpoints / extracted
vectors. At Gate-7 closure, this directory contains all data (or
cryptographically-verifiable pointers to data) needed to re-derive the
manuscript's headline results.

## Data inventory and source-of-truth locations

### Raw inputs

For each raw input source, document:
- What it is.
- Where it lives (path in this bundle if vendored; URL + SHA-256 + access
  procedure if not).
- Volume.
- Provenance (how it was authored / collected).
- License.

### Processed intermediates

If the pipeline produces intermediate artifacts (extracted vectors,
preprocessed data, computed indices), document each:
- Path.
- Producing script + commit SHA (cross-reference `../PROVENANCE.md`).
- SHA-256 checksum (for vendored artifacts).
- Format.

### Run artifacts

The actual outputs of the evaluation runs (generations, scores, judge
reports). Document each subdirectory:
- `runs/<condition>/` — raw outputs.
- `results/<condition>/` — per-condition reports + machine-readable scores.

### Released model / vector artifacts (if applicable)

If the publication releases any model checkpoint, steering vector, fine-tune
LoRA, etc., document:
- Path.
- Format (PyTorch tensor, safetensors, etc.).
- Source (extracted from which base model, trained with which procedure).
- License (downstream USE may be bounded by the base model's original license).
- Model Card location (per Mitchell et al. 2019; required for any released
  model).

## Sensitivity of the data artifacts

For each data category, document any PII / privacy / consent / dual-use
considerations. Common patterns:

- **No PII** — declare explicitly.
- **Author self-experimentation** — declare prominently; per CHARTER §11, this
  is permitted under the unit's standards with disclosure.
- **Third-party personal data** — must have IRB / consent documentation in
  this folder; un-consented third-party PII is a disqualifying defect.
- **Dual-use surface** — if the artifact materially lowers the bar for
  malicious actor uplift, document the Responsible-Release Review per
  CHARTER §11.

## License of the data artifacts

Default per the unit's content license: CC-BY-4.0 (via `../../../LICENSE-CONTENT`).

Exceptions:
- Derivative artifacts from external models inherit downstream-USE constraints
  from the base model's license.
- Data with restrictive original licenses honour the more restrictive terms.

A `LICENSE.md` file in this directory formalising the above is required at
Gate-7.

## Checksums

For every vendored artifact, compute and commit a SHA-256 checksum. A
`checksums.txt` file in this directory is the canonical record. Replicators
verify checksums on download.

## Access procedure (pointer-only mode)

If artifacts are not vendored, document the access procedure here. Same
template as `../code/README.md` §"Access procedure". Pointer-only state is
acceptable for arXiv preprint posting but fails Tier-2+ open-data
requirements.
