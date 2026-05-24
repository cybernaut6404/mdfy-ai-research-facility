# Provenance — [PUBLICATION TITLE]

The chain of derivation from raw inputs to every headline claim in the
manuscript. Cross-references use the commit SHAs of the source project repos
as of pack assembly.

## Headline claims and their derivation

| Manuscript artifact | Producing script | Inputs | Outputs |
|---|---|---|---|
| [§X claim 1] | [path/to/script.py at SHA] | [input paths + checksums] | [output paths + locations] |
| [§Y figure 1] | [path/to/figure_script.py at SHA] | [...] | [...] |
| [Table SX] | [path/to/table_script.py at SHA] | [...] | [...] |

## Manual steps

Document every manual step in the pipeline. If the pipeline is fully scripted,
state so explicitly:

> No manual steps. Every artifact named in the manuscript is produced by one of
> the scripts above. No manual coding, no expert-judgment steps, no spreadsheet
> operations.

If manual steps exist (manual coding, expert judgment, spreadsheet operations),
document each one with:
- What was done.
- Who did it.
- When (with timestamp).
- Why it was not scriptable.

## Inputs

The inputs to this study are:

1. **[Base model / dataset / API endpoint]** — at the pinned version /
   revision SHA. Source: [Hugging Face revision, dataset DOI, API timestamp].
2. **[Contrastive items / probe sets / prompts]** — at the source repo + commit SHA.
3. **[Raw measurements / extracted vectors / pretrained weights]** — at the
   source repo + commit SHA, with SHA-256 checksums committed in the bundle.
4. **[Configuration files / hyperparameters]** — at the source repo + commit SHA.

## Determinism

- **Decoding:** [greedy / temperature / top-p / top-k]; see `seeds.json` for the
  exact decoding parameters.
- **Position randomisation (if applicable):** see `seeds.json` for the seed used.
- **GPU non-determinism:** [documented if relevant; note that bitwise determinism
  may not hold across runs due to floating-point reduction order in CUDA kernels.]

## Tolerance

For a re-run, the documented tolerance is:

- **[Headline metric 1]:** ±[tolerance] at the reported precision.
- **[Headline metric 2]:** ±[tolerance].

State the tolerance the author would accept as a successful replication. Larger
deviations indicate either environment drift or a real change in the underlying
behaviour that warrants investigation.

## License of artifacts

Code: [LICENSE — typically Apache-2.0 per the unit's defaults].
Content (manuscript, provenance, tables): [LICENSE — typically CC-BY-4.0].
Data: [LICENSE — typically CC-BY-4.0 unless data has restrictive original license; honour the more restrictive terms].
Derivative artifacts (vectors, embeddings, fine-tuned models): [LICENSE; note that downstream USE may be bounded by the original model / dataset license].
