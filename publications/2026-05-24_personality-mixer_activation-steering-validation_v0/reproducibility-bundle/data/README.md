# `data/` — pointer to source repos

The data that fed the validation (contrastive items, probes, rubrics, run
artifacts, steering vectors) lives in private project repositories
controlled by the author. At the time of pack assembly (2026-05-24), it
has **not yet been mirrored into this folder**. This is a Gate-7
(reproducibility-bundle finalisation) blocker for external submission.

## Data inventory and source-of-truth locations

Within `mg-digital-twin` at commit `f492844`:

### Contrastive items (vector-extraction inputs)

- Path: `experiments/contrastive-items/<channel>/items.json`
- Format: JSON array of `{prompt, completion_low, completion_high}` triples.
- Volume: 30–50 items per channel × 24 channels = ~720–1200 items total.
- Provenance: authored by hand, drawing on the operational definitions in
  HEXACO-100, NEO-PI-R, Schwartz Human Values, DOSPERT, Dark Tetrad short
  form, ECR-R, Rotter LOC, Self-Monitoring Scale, Mach IV. All items
  reference the single human subject's psychometric battery completed
  2026-04-15.
- License: CC-BY-4.0 per the unit's defaults; contains the author's
  single-subject operationalisation of each trait but no third-party PII.

### Probe libraries

- Path: `experiments/d4-fader-intervention/probes/`
- Volume:
  - Generic: `discriminability.json` (10 scenarios)
  - Dark Tetrad: 4 × `dark-*.json` (14 directional + 2 QC each)
  - HEXACO / attachment / locus / self-construct: 11 × `new-*.json`
    (10–12 directional + 2 QC each)
  - Original 9: 9 × `<channel>.json` (substrate-paper standard 30 probes
    each: 20 directional + 8 length-controlled + 2 QC)
- Format: JSON per channel, each probe is a scenario prompt.
- License: CC-BY-4.0 per the unit's defaults.

### Blind-rater rubrics

- Path: `experiments/d4-fader-intervention/analyse.py::JUDGE_PROMPTS`
- Format: Python dict mapping channel → {system_prompt, question}
- Verbatim text reproduced in `SUPPLEMENTARY_TABLES.md` Table S6.
- License: CC-BY-4.0 per the unit's defaults.

### Run artifacts (generations from the validation runs)

- Path: `experiments/d4-fader-intervention/runs/<channel>_<config>/`
  where `<config>` ∈ {`darkv2`, `darkv3hi`, `mlretest`, `newval`, etc.}
- Format: per-probe directory containing `high.txt`, `low.txt`, and
  `metadata.json` (channel, layers, coefficient, model version, decoding
  params).
- Volume: ~21 runs × ~12–16 probes × 2 directions = ~500–700 generated
  responses total. Estimated total size: a few MB.

### Judge reports

- Path: `experiments/d4-fader-intervention/results/<channel>_<config>/`
  with `report.md` (human-readable) and `results.json` (machine-readable).
- Each `results.json` contains the per-probe rating (`A`/`B`/`TIE`),
  the high-side win count, the low-side win count, the tie count, and
  the computed κ.
- License: CC-BY-4.0.

### Steering vectors (extracted CAA vectors)

- Path:
  `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/<channel>/vector.pt`
- Format: PyTorch tensor, shape (28, 3584) — one vector per layer for
  Qwen2.5-7B-Instruct's 28 decoder layers; hidden size 3584; fp32 stored
  (cast to fp16 at inference time on Modal L4).
- Volume: 24 channels × 28 × 3584 × 4 bytes = ~10 MB total, plus
  `refusal/vector.pt` of the same shape (~0.4 MB).
- Provenance: each `vector.pt` carries a SHA-256 used as
  `steering_vector_ref` in `personality-central-db.catalog.channels`
  (e.g. row for `cheerfulness` references the SHA of the
  `cheerfulness/vector.pt` blob, or the `_ct` contrastive-template
  variant per Phase 8c-vi of the work log).
- License: CC-BY-4.0 per the unit's content license; downstream use of
  the *steered model behaviour* is bounded by the original Qwen
  open-weights license.

### Refusal direction vector

- Path: `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/_refusal/vector.pt`
- Provenance: extracted from a separate refusal/non-refusal contrastive
  set; used in the AlphaSteer refusal-cosine protocol per Table S2.

### Inter-channel cosine matrices

- Path:
  `mg-digital-twin/infra/steering-vectors/inter-channel-cosines-dark-2026-05-23.md`
- Full pairwise cosine matrix at L12, L16, L20. Selected pairs are
  reproduced in `SUPPLEMENTARY_TABLES.md` Table S3.

### Orthogonalisation report

- Path:
  `mg-digital-twin/infra/steering-vectors/orthogonalisation-report-2026-05-08.md`
- Norm-preservation ratios per channel under modified Gram-Schmidt.
  Reproduced in `SUPPLEMENTARY_TABLES.md` Table S4.

### Refusal cosine report (substrate paper era)

- Path:
  `mg-digital-twin/infra/steering-vectors/refusal-cosines-w4-2026-05-07.md`
- Refusal-direction cosine values for the 9 originally-validated channels.
  Cross-referenced in Table S2.

## Sensitivity of the contrastive items

The contrastive items are authored against the **author's own**
single-subject psychometric battery (15 instruments, completed
2026-04-15). Releasing the items implies releasing the author's
operational identification of each trait dimension (Honesty-Humility,
Dark Tetrad, attachment style, etc.). The author has elected to do this
(the manuscript is publication-intent) but reviewers should note that:

- No third-party PII is in the contrastive items.
- The author's own operationalisations of each construct are inferrable
  from the items.
- This is a personal disclosure that any single-subject methods paper
  inherently makes; the author has elected to bear it for the
  methodological value.

## License of the data artifacts

All data artifacts above are released under **CC-BY-4.0** per the unit's
content license (`../../../LICENSE-CONTENT`), with the caveats:

- The steering vectors are derivative of Qwen2.5-7B-Instruct's weights.
  Downstream USE of the steered behaviour is bounded by Qwen's open-
  weights license, even though the vectors themselves are CC-BY-4.0.
- The contrastive items reference the author's operationalisation of
  established psychometric constructs (HEXACO, Dark Tetrad, etc.). The
  underlying psychometric instruments are owned by their respective
  authors and publishers; this work reproduces no instrument verbatim.

A `data/LICENSE.md` formalising the above will be added at Gate 7. The
inheritance from the unit's `LICENSE-CONTENT` is sufficient for v0.

## Checksums for the source-repo artifacts

Where data is referenced by SHA-256 in `personality-central-db.catalog.channels`
(specifically the `steering_vector_ref` field for each channel), the
checksum chain is:

```
sha256(mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/<channel>/vector.pt)
  → catalog.channels[<channel>].steering_vector_ref
```

A future `data/checksums.txt` file will enumerate these for every
artifact. This is Gate-7 TODO.

## Access procedure

Same as `code/README.md` §"Access procedure for the current state": a
third party may request access to the source repos at the pinned SHAs
via `rick@mdfy.co.uk`. For v0 (arXiv target), this is acceptable. For
Tier 2+ submission, the data must be made public alongside the source
code.
