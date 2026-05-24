# `code/` — pointer to source repos

The code that produced the manuscript's results lives in private project
repositories controlled by the author. At the time of pack assembly
(2026-05-24), it has **not yet been vendored into this folder**. This is a
Gate-7 (reproducibility-bundle finalisation) blocker for external
submission.

## Source-of-truth commits (pinned)

The following commit SHAs define the exact source code state that produced
every claim in the manuscript:

| Repository | Role | HEAD at pack assembly |
|---|---|---|
| `mg-digital-twin` | Vector extraction (`extract_caa.py`), validation harness (`harness.py`), blind-rater judge (`analyse.py`), steering-server (`infra/steering-server/steering_server.py`), refusal-cosine probe, inter-channel cosine matrix, Gram-Schmidt orthogonalisation | `f492844` |
| `personality-central-db` | The 24-channel catalog (`scripts/publish_channel_set_2.py`, `scripts/publish_channel_set_2_1.py`); per-channel `bias_tests` records; the `v_channels` / `v_constructs` / `v_channel_sets` views | `2bdf13b` |
| `personality-construct-runner` | Steering-loadout compiler (`lib/steering.mjs`); construct → loadout → steering-server orchestration | `d55296b` |
| `personality-mixer-codex` | UI for authoring constructs (not needed for κ re-derivation) | `5462733` |
| `personality-mixer-claude` | UI for authoring constructs (not needed for κ re-derivation) | `3963ce4` |

All five repos are at GitHub under `cybernaut6404/<repo>` (private at the
time of writing).

## Files specifically referenced by the manuscript and supplementary tables

Within `mg-digital-twin` at `f492844`:

- `experiments/d4-fader-intervention/harness.py` — Modal-deployed
  validation runner; takes (channel, layers, coefficient, probes) →
  generated response pairs.
- `experiments/d4-fader-intervention/analyse.py` — blind-rater judge
  prompting (the `JUDGE_PROMPTS` dict named in Tables S6 of the
  supplementary tables); κ aggregation; results-report emission.
- `experiments/d4-fader-intervention/probes/*.json` — the probe libraries
  enumerated in Table S5.
- `experiments/d4-fader-intervention/runs/<channel>_<config>/` — raw
  generations from `harness.py`.
- `experiments/d4-fader-intervention/results/<channel>_<config>/report.md`
  and `results.json` — per-channel judge reports (Table S7).
- `infra/steering-vectors/cosine_probe.py` — refusal-direction cosine
  (Table S2).
- `infra/steering-vectors/inter_channel_cosines.py` — inter-channel cosine
  matrix (Table S3).
- `infra/steering-vectors/orthogonalise.py` (or equivalent) — modified
  Gram-Schmidt orthogonalisation (Table S4).
- `infra/steering-server/steering_server.py` — the Modal app serving
  steered generations to the construct-runner (manuscript §2.8).
- `infra/steering-vectors/qwen2.5-7b-instruct/<channel>/vector.pt` — the
  24 channel steering vectors (referenced by SHA-256 in
  `personality-central-db.catalog.channels.steering_vector_ref`).

Within `personality-central-db` at `2bdf13b`:

- `scripts/publish_channel_set_2.py` and `scripts/publish_channel_set_2_1.py`
  — the publishers that committed the validated 9 channels (2.0.0) and
  added the 15 unvalidated-at-publish-time channels (2.1.0).
- `scripts/reweight_baselines_v2.py` and `scripts/reweight_shadow_v3.py` —
  the baseline / shadow-archetype re-weighting against the validated
  catalog.
- `infrastructure/sql/0001-0010` — the registry schema applied to the
  central DB.

## Gate-7 finalisation options

Three options for closing this gap. To be decided by the author:

1. **Vendor into `code/`.** Copy the named files at the pinned SHAs into
   `code/<source-repo>/<path>`. Simplest; bundle is fully self-contained;
   downside is the bundle gets large (the steering vectors alone are tens
   of MB across 24 channels) and license terms must be checked for every
   third-party dependency. Recommended for the smallest-possible self-
   contained bundle for arXiv attachment.
2. **Git submodules pinned at SHAs.** Add the five source repos as git
   submodules of this publication folder, pinned at the listed SHAs.
   Bundle stays small; replicator runs `git submodule update --init` then
   `make replicate`. Downside: the source repos must be public for a
   third party to clone, which the author has elected not to do yet.
3. **Pointer + access-on-request.** Leave the bundle as-is (this current
   state), document the access procedure here, and let a Gate-6 reviewer
   accept "available on request" as the access procedure for the v0
   publication. This fails the unit's TOP Level-2 standard and any
   journal with an open-data policy; acceptable only at preprint stage
   while the source repos are being prepared for public release.

Per ROADMAP_TO_TOP_VENUES.md, Tier 1 (arXiv) tolerates option 3 with a
prominent disclosure. Tier 2+ (Psychological Bulletin, etc.) requires
option 1 or option 2.

## Access procedure for the current state

A third party wishing to verify the κ values can:

1. Contact the author at rick@mdfy.co.uk requesting read access to the
   named repos at the pinned SHAs.
2. The author will grant time-limited read access to a clone of each
   repo at the pinned SHA, with a written usage agreement bounded by the
   unit's Apache-2.0 (code) and CC-BY-4.0 (content) licenses.
3. The third party clones the repos, installs the env per `environment.yml`,
   and runs the validation harness against their own Modal + Anthropic
   credentials.
4. The third party records their run in `replication-log.md` and PRs the
   updated log back to this publication folder.

This procedure is acceptable for v0 (Tier-M methods publication, arXiv
target). It does NOT meet the standard for Tier 2+ journals; the source
repos must be made public, or the relevant code vendored into `code/`,
before any Tier-2+ submission.
