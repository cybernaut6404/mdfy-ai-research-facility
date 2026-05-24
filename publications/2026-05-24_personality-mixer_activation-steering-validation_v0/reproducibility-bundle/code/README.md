# `code/` — vendored source + bundle-local analysis tooling

This directory contains the code that produced the manuscript's results, plus
the analysis tooling that re-derives the published numbers from the vendored
judge reports.

## Bundle-local analysis tooling (added at intake)

Three Python scripts the bundle calls via `make replicate`:

- **`compute_stats.py`** — per-channel two-sided binomial tests, 95% Wilson
  score CIs, Holm-Bonferroni + BH-FDR correction across the 18-channel
  family (the 5 "from prior validation" rows in Table S1 with blank W/L/T
  are excluded from the correction family). Writes
  `../data/derived/stats.{json,md}`.
- **`figures.py`** — matplotlib-only generator for the three manuscript
  figures: κ forest plot (Figure 1), inter-channel cosine heatmap (Figure 2),
  refusal-cosine bar chart (Figure 3). Writes
  `../data/figures/fig{1,2,3}_*.png`.
- **`verify_kappa.py`** — recovers κ from each vendored `results/*/results.json`
  and compares to the manuscript's reported value within ±0.05 tolerance.
  Writes `../data/derived/replication-delta.md`. Honest about the gap: the
  4 KILL-rescued channels and the 15 new channels' results are NOT in
  the vendored data (they live on the unpushed local SHA f492844).

Run all three via `make replicate` from `../`. Requires Python 3.10+; the
bundle's `Makefile` creates a `.venv-stats/` with scipy + statsmodels +
matplotlib + numpy on first run.

## Vendored source

The code below is vendored from `cybernaut6404/mg-digital-twin` at the
remote HEAD as of 2026-05-24. The originating-session SHA `f492844` was
a local-only commit on the MacMini that was never pushed; the vendored
code corresponds to the most-recent pushed state, which contains the
9-channel substrate-paper baseline harness + judge but not the 15-new-channel
+ ML-rescue extensions that produced the manuscript's headline numbers.
See `../replication-log.md` §"Honest gap surfaced by the local replicate"
and `../data/derived/replication-delta.md` for the full disclosure.

### `experiments/d4-fader-intervention/`

- **`harness.py`** (24KB) — the validation harness. Loads
  Qwen/Qwen2.5-7B-Instruct via `AutoModelForCausalLM.from_pretrained` (no
  HF `revision=` pinned in source; defaults to HuggingFace `main` at run
  time — replicators record their effective revision in
  `../replication-log.md`). Adds forward hooks to layers 12/16/20 and
  injects `c × v_L` to the residual stream at every token position. Designed
  to run on Modal L4 (or any 24GB+ GPU). Greedy decoding (`do_sample=False`,
  `max_new_tokens=512`).
- **`analyse.py`** (32KB) — the blind-rater judge. Calls Anthropic Claude
  (model `claude-opus-4-7` per the source code; the WORK_LOG references
  `claude-opus-4-6` + `claude-opus-4-7-1m` from the original Cowork-session
  runs — see `../seeds.json` §"_note_on_work_log_inconsistency"). Per-channel
  rubrics in the `JUDGE_PROMPTS` dict. Position randomisation via fixed
  seed = 42 (default seed argument). κ aggregation +
  per-coefficient breakdown.
- **`probes/`** (~180KB across 24 channels) — the trait-eliciting D0 probe
  libraries. Each `*.json` is a list of scenario prompts.

### `infra/steering-vectors/`

- **`cosine_probe.py`** (7KB) — refusal-direction cosine probe (AlphaSteer
  protocol). Used to compute the Table S2 worst-layer |cos| values.
- **`inter_channel_cosines.py`** (7KB) — pairwise inter-channel cosine
  computation. Produces Table S3.
- **`extract_caa.py`** (18KB) — the CAA extraction script. Reads
  contrastive items, runs the model, computes mean activation difference
  at the answer-token position, L2-normalises, saves `vector.pt`.
- **`orthogonalise.py`** (10KB) — modified Gram-Schmidt orthogonalisation
  of the 9-channel validated basis. Produces Table S4.
- **`contrastive-items/`** (~384KB) — the per-channel contrastive-item
  libraries authored against the author's single-subject psychometric
  battery (15 instruments, 2026-04-15). Released under CC-BY-4.0 per the
  unit's content license; release implies disclosure of the author's
  operationalisation of each trait, which the author has elected per the
  n=1 framing of the manuscript.

## What's NOT vendored, and why

| Artifact | Why not vendored | Closure path |
|---|---|---|
| Steering vectors (`infra/steering-vectors/qwen2.5-7b-instruct/<channel>/vector.pt` × 24) | Access-on-request per the manuscript's Broader Impacts mitigation (§4.6) and the deployed runtime's access policy. Public release of the vectors would lower the bar for downstream Dark-Tetrad steering on Qwen2.5-7B; the manuscript's safety posture is to gate access by request rather than publish. | Request via `rick@mdfy.co.uk`; or wait for the v2 publication's Tier-2-readiness review of the public-release decision. |
| Raw generations (`runs/*/`, ~41MB) | Regenerable via `make replicate-full` (which calls `harness.py`). Vendoring 41MB of Dark-Tetrad-steered generations would publish content that, while sandboxed in research context, is sensitive at scale and adds disk weight without enabling any verification beyond what `make replicate-full` already provides. | Run `make replicate-full` (requires Modal + Anthropic creds). |
| 15-new-channel judge reports (`results/<new-channel>_*/results.json`) | The local commit `f492844` that produced them was never pushed to `cybernaut6404/mg-digital-twin`. | Push the local SHA from the MacMini, or selectively vendor from the MacMini clone, or `make replicate-full`. |
| Multi-layer-rescue judge reports for the 4 KILL channels (dospert_recreational, cautiousness, conscientiousness_self_discipline, self_direction at ML L12/16/20 c=2) | Same — produced on the local SHA `f492844`, not pushed. The vendored `results/` for these channels contains the *single-layer baseline* (κ ≈ 0.35-0.55), which `verify_kappa.py` correctly identifies as `OUT_OF_TOLERANCE` relative to the manuscript's headline *multi-layer rescued* κ values. | Same as above. |

## Access procedure for the not-vendored items

Contact `rick@mdfy.co.uk` requesting either:
- Read access to the relevant repos at the relevant SHAs, OR
- A copy of the unpushed-local `f492844` SHA state from the MacMini clone, OR
- Coordination on a `make replicate-full` run on Modal (requires the
  replicator's own Modal + Anthropic accounts; estimated $5–15 cost).

The author records each access grant in this folder's
`../correspondence/` directory per the unit's convention.

## License

All vendored source: Apache-2.0 (per the unit's `LICENSE-CODE`) — original
license terms inherited from `cybernaut6404/mg-digital-twin`.

All vendored content (rubrics, contrastive items, probe libraries):
CC-BY-4.0 (per the unit's `LICENSE-CONTENT`).
