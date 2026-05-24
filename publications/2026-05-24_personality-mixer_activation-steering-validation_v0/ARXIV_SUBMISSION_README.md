# arXiv submission guide

Step-by-step procedure for posting this paper as an arXiv preprint. This
file is committed alongside the publication; the `make arxiv` target also
includes a copy of it inside the submission tarball.

## Before you submit

Confirm all six items below. Each is either ✅ done as of the v1 revision
commit or ⏳ pending Rick's manual action.

| # | Item | Status as of v1 revision |
|---|---|---|
| 1 | Gate-6 internal review with PROCEED disposition | ✅ counter-signed PROCEED WITH REVISIONS; v1 revisions land the categories 1/4/5 fixes |
| 2 | v1 manuscript revisions landed (calibration, Broader Impacts, §8 reconciliations) | ✅ |
| 3 | Statistical significance + figures | ✅ added in §3.1.1 + Figures 1–3 |
| 4 | Bibliography (`.bib`) | ✅ `references.bib` committed; pandoc Makefile wires citeproc when bib present |
| 5 | Reproducibility-bundle stub state acceptable for arXiv | ✅ `make replicate` runs locally; gap to ML-rescue + 15-new-channel data documented in `data/derived/replication-delta.md` |
| 6 | Prompt-archive deposition | ⏳ Cowork transcripts not yet exported — see `COWORK_TRANSCRIPT_EXPORT.md` |

Item 6 is the only ⏳ that strictly blocks per AI_USE_POLICY.md §"Archive
requirements". The fastest closure: export the Cowork session(s) that
produced this manuscript and drop the export into `prompts/` in this
folder. See `COWORK_TRANSCRIPT_EXPORT.md` for the procedure.

## Build the submission package

From this directory:

```
make arxiv
```

This regenerates `MANUSCRIPT.tex` and `SUPPLEMENTARY_TABLES.tex` via
pandoc + citeproc (requires `pandoc` ≥ 3.0 — `brew install pandoc` on
macOS), copies the three figures from
`reproducibility-bundle/data/figures/`, rewrites the figure-path
references in the LaTeX to match the arXiv flat layout, and bundles
everything into `arxiv-submission.tar.gz`.

Inspect the contents before submitting:

```
ls arxiv-submission/
```

You should see:
- `main.tex` — manuscript LaTeX source
- `supplementary.tex` — supplementary tables LaTeX source
- `references.bib` — bibliography
- `figures/fig1_kappa_forest.png`
- `figures/fig2_cosine_heatmap_L16.png`
- `figures/fig3_refusal_cosine.png`
- `README.md` — a copy of this guide

## arXiv browser flow

arXiv submission cannot be done via CLI. From the moment you have
`arxiv-submission.tar.gz`:

1. **Go to** https://arxiv.org/submit/ and sign in (or register at
   https://arxiv.org/user/register if you don't have an arXiv account).
   If you have an ORCID (you do: `0009-0004-0799-1756`), link it during
   registration for cleaner author resolution.

2. **Click "Start a new submission"** and choose **License**: CC-BY 4.0
   (matches the unit's `LICENSE-CONTENT`).

3. **Primary subject classification**:
   - Primary: `cs.CL` (Computation and Language)
   - Cross-list (optional): `cs.AI` (Artificial Intelligence), `cs.LG`
     (Machine Learning)

4. **Metadata**:
   - **Title**: "A 24-Channel Activation-Steering Substrate for Personality
     Constructs in a Large Language Model: Single-Subject Validation,
     Methodological Findings, and a Roadmap to Multi-Subject Replication"
   - **Author**: Rick Weakley
   - **Author ORCID**: `0009-0004-0799-1756`
   - **Affiliation**: independent researcher (or whatever you prefer to use)
   - **Abstract**: copy from `MANUSCRIPT.md` §Abstract (the four paragraphs:
     Background, Methods, Results, Conclusions, Limitations).
   - **Comments** (the visible "comments" field): "v0; pre-TMLR. See
     `internal-review.md` Gate-6 review (PROCEED WITH REVISIONS) and
     `ROADMAP_TO_TOP_VENUES.md` in the GitHub repo for the path to higher-
     tier venues. Source + reproducibility bundle:
     https://github.com/cybernaut6404/mdfy-ai-research-facility/tree/main/publications/2026-05-24_personality-mixer_activation-steering-validation_v0"

5. **Upload**: choose `arxiv-submission.tar.gz` from this directory.

6. **arXiv compiles your LaTeX**. Wait for the compile result. If errors,
   read the log carefully — common issues are missing packages or figure
   path mismatches; the Makefile rewrites paths to `figures/` so they
   should resolve correctly.

7. **Preview the rendered PDF**. Make sure figures appear at the right
   places, references are formatted correctly, and Greek symbols (κ, etc.)
   render properly. If anything is broken, fix locally, re-run `make arxiv`,
   and re-upload.

8. **Submit**. After submission, arXiv usually publishes within 24 hours
   on weekdays.

9. **Update CITATION.cff after publication**: once arXiv assigns the paper
   ID (e.g. `arXiv:2605.12345`), add it as an identifier in
   `CITATION.cff` at the repo root.

10. **Notify Zenodo**: arXiv DOIs are separate from Zenodo concept DOIs;
    the unit's CITATION already points at the Zenodo concept DOI for the
    *charter*. After arXiv publication, this *publication's* own DOI (from
    arXiv) lives in the publication folder's README.

## Per-version bumps

When you revise the paper (post Gate-7 closure, post stats expansion, etc.),
arXiv supports versioned replacements. Use **"Replace"** on the existing
submission (don't create a new submission); arXiv tags it `v2`, `v3`, etc.

The unit's CHARTER §15 says preprint-first is the default disposition. A
post-revisions v2 / v3 / vN on arXiv lands before any journal submission.

## If submission stalls

If arXiv holds the submission for moderator review (usually because cross-
listing flags or unusual metadata), respond promptly to any arXiv emails.
arXiv typically resolves moderator holds within 1–3 business days.
