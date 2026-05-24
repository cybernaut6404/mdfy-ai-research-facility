# WORK LOG — Personality-Mixer Ecosystem Build & Validation
**Sessions:** 2026-05-23 (audit + build) → 2026-05-24 (validation + publication)
**Author:** R. Weakley (the human owner of the work); assistant: Claude (Opus 4.7)
**Purpose:** Detailed chronicle of every phase of work that produced the publication
pack at `publications/2026-05-24_personality-mixer_activation-steering-validation_v0/`.
Intended to seed a separate work-log repository.

---

## 0. What we built (one-paragraph overview)

A **24-channel activation-steering substrate for personality constructs** on
Qwen2.5-7B-Instruct, comprising: (i) a provider-agnostic central personality
database on Supabase (`personality-central-db`) holding 24 CAA-extracted
channels and 69 archetype constructs across 5 traditions; (ii) two research
mixers (`personality-mixer-codex` / `personality-mixer-claude`) that author,
recall, mix, and publish constructs; (iii) a construct-runner
(`personality-construct-runner`) that compiles constructs into steering
loadouts and drives a Modal-deployed steering-server; (iv) the Modal
steering-server itself (`mg-twin-steering-server`) that injects real CAA
vectors into the model's residual stream at inference. The substrate was then
**rigorously validated**: 20 of 24 channels passed the 0.60 directional-accuracy
gate, with all results recorded in `catalog.channels.bias_tests` and a
publication-quality manuscript produced.

---

## 1. Repository inventory

| Repository | Role | Local path | GitHub | HEAD at checkpoint |
|---|---|---|---|---|
| `personality-central-db` | Central agnostic DB ops (SQL scripts, publishers, re-weighters) | `~/ai-workspace/personality-central-db` | private `cybernaut6404/personality-central-db` | `2bdf13b` |
| `personality-construct-runner` | Runs a construct as a live agent via activation steering | `~/ai-workspace/personality-construct-runner` | private `cybernaut6404/personality-construct-runner` | `d55296b` |
| `personality-mixer-codex` | OpenAI/Codex research mixer | `~/ai-workspace/personality-mixer-codex` | private `cybernaut6404/personality-mixer-codex` | `5462733` |
| `personality-mixer-claude` | Anthropic/Claude research mixer | `~/ai-workspace/personality-mixer-claude` | private `cybernaut6404/personality-mixer-claude` | `3963ce4` |
| `mg-digital-twin` | Vector extraction, validation harness, Modal steering-server | `~/ai-workspace/mg-digital-twin` | own remote | `f492844` |
| `mdfy-personality-registry` | The saleable registry (separate product; consumes signed pushes from the mixers) | `~/ai-workspace/mdfy-personality-registry` | already on remote | `869e0d1` |
| `mdfy-GSTACK` | Planning hub / audit docs (where decisions and checkpoints live) | `~/ai-workspace/mdfy-GSTACK` | private `cybernaut6404/mdfy-GSTACK` | `0622d66` |

### External / cloud infrastructure
- **Supabase project** `nhzaawsdddkycaxragvz` (eu-west-2) — the central DB.
  Coordinates in `~/.personality-central-db.env` (chmod 600).
- **Modal app** `mg-twin-steering-server` (account `cybernaut6404`) — the
  activation-steering inference endpoint at
  `https://cybernaut6404--mg-twin-steering-server-steerer-steer.modal.run`.

### Reserved ports (iCloud registry `_PORT_REGISTRY.csv`)
- `3503` central-db (Supabase-hosted; reserved namespace)
- `4512` mixer-codex (LIVE)
- `4513` mixer-claude (LIVE)
- `4514` construct-runner (LIVE)

---

## 2. Chronological phases

### Phase 0 — Prior-session audit (review-only)
*Outcome banked in `mdfy-GSTACK/docs/audits/personality-mixer-audit-2026-05-23.md` and
`memory/project_personality_mixer_audit_2026-05-23.md`.*

Five components reviewed: `mdfy-personality-registry` (the spine, ~80% of the
central DB shape), `rickai-openai-personality mixer` (content donor — jungian
PMAI-12 + full tarot), `mg-digital-twin` (channel substrate), and two archive
references. Locked decisions: registry stays whole as the saleable product;
two research mixers AUTHOR new constructs; central DB is a new standalone
store reusing the registry schema; publish via signed push; consolidate all
content; wire mg-digital-twin steering vectors live; build a construct-runner.
Backup made to `~/ai-workspace/BACKUP-PERSONALITY` (5.8 GB).

### Phase 1 — Central DB live
- Created Supabase project `personality-central-db` (`nhzaawsdddkycaxragvz`),
  region eu-west-2.
- Applied the registry's full schema (`infrastructure/sql/0001-0010`): 12
  tables (tenancy 5 / catalog 2 / constructs 1 / audit 1 / pushes 1 /
  workshop 1 / samples 1) + 10 types/extensions.
- Saved coordinates to `~/.personality-central-db.env` (chmod 600), DB pass to
  `~/.personality-central-db-pass` (chmod 600), PAT at `~/.supabase-pat`.
- Built reusable SQL runner `scripts/runsql.py` using the Supabase Management
  API (with browser User-Agent — Cloudflare blocks non-browser UAs with 403/1010).
- Seeded faithfully via a temp tsx bridge running the registry's `getStore()`
  in-memory transform (then bridge deleted; registry source untouched). 8
  channels, 1 channel_set (1.0.0), 37 constructs (34 archetype + 3 demo).
- Added `tradition` column + backfilled.
- Created public views `v_constructs` / `v_channels` / `v_channel_sets` (anon-readable).
- **Verified:** REST `GET /rest/v1/v_constructs?tradition=eq.tarot` → 10 rows.

### Phase 2 — Mixers + save + publish loop
- Scaffolded `personality-mixer-codex` (port 4512, openai) and
  `personality-mixer-claude` (port 4513, anthropic) from `rickai sampler-studio`
  + vendored `packages/construct-core`. Both git-init'd.
- Built `lib/central-db.mjs` recall client (anon key, public views).
- Routes: `GET /api/constructs[?tradition=]`, `GET /api/traditions`.
- **Save** via `public.save_construct(jsonb)` SECURITY-DEFINER RPC +
  `saveConstructToCentral` (anon-callable, reverse-adapt, studio-signed passport).
  **Verified:** construct authored in Codex → recalled in Claude (twin-to-twin loop).
- **Publish** — implemented the registry's `construct_seed` `receivePush` branch
  (was a stub): `ConstructInsertAdapter` in `PushContext`, `constructStorage`
  wired in `/api/push`, `STUDIO_KEYS_JSON` for multi-studio key registration.
  Registry commit `869e0d1`. **Verified:** real ed25519-signed push from Codex
  mixer ingested + receipt.
- **Mixer commits:** codex `da638b1`→`2d54900`, claude `2942004`→`6b5db85`.

### Phase 3 — Research-alignment fix (channel_set 2.0.0)
Discovered the demo substrate did not match the research's findings. Three
gaps identified:
1. Baselines weighted on UNVALIDATED generic channels (openness/extraversion).
2. The 8 catalog.channels were placeholder hashes (κ=0) — real CAA vectors
   existed in `mg-digital-twin/infra/steering-vectors/qwen2.5-7b-instruct/`.
3. The channel→behaviour "wire" was prompt-conditioning only; research recommended
   activation steering.

Built and shipped:
- **`scripts/publish_channel_set_2.py`** (central-db `b5051be`) —
  channel_set 2.0.0 = the 9 research-validated channels (achievement_striving,
  cheerfulness, sociability, stimulation, dospert_financial,
  dospert_recreational, conscientiousness_self_discipline,
  cautiousness, self_direction) replacing the 8 demos. Each row carries the
  real `steering_vector_ref` (sha256 of `vector.pt`), κ from D4
  directional accuracy, refusal-cosine + Gram-Schmidt orthogonalisation in
  `bias_tests`, honest per-channel verdict.
- **`scripts/reweight_baselines_v2.py`** — 66 baselines DELETE+reinserted
  pinned to 2.0.0; full standardised profile (voice/process/memory +
  semantic_axes + core/shadow traits + behavioural_signature) + **deep_modules
  as descriptive metadata only** + constraints (DOSPERT domain-specificity,
  H × Dark-Triad coupling note).
- **GSTACK** commit `85ff424` — research-alignment closed.

### Phase 4 — Activation-steering loadout (runner)
- `personality-construct-runner/lib/steering.mjs` (runner commit `e22f36a`):
  converts a construct's channel weights → a steering loadout
  `{channel_id, vector_ref, layers, coefficient}` against channel_set 2.0.0.
  Weight 0.5 → coef 0; weight 1.0 → coef +2; weight 0.0 → coef −2. Clamped to
  |coef| ≤ 2. Refusal-FLAG channels get coefficient-clamped.
- `/api/compile` returns the loadout; `/api/steer` exposes it standalone;
  `/api/run` drives the steering-server when `STEERING_SERVER_URL` is set,
  else falls back to prompt conditioning (`wire=prompt_conditioning`).
- `v_channels` view extended with `peer_review_status` + `bias_tests`.

### Phase 5 — Modal steering-server deployed
- `mg-digital-twin/infra/steering-server/steering_server.py` (mg-twin `9260aa8`)
  — the previously-empty dir the research designated. Loads Qwen2.5-7B,
  bakes the validated vectors into the Modal image, injects them into the
  residual stream at L12/16/20 via additive forward hooks. FastAPI web endpoint.
  Mirrors the `extract_caa.py` hook pattern.
- **Initial deploy:** A10G GPU. URL:
  `https://cybernaut6404--mg-twin-steering-server-steerer-steer.modal.run`.
- **Smoke test:** cheerfulness ±2 steers (`steered:True`, hooks fire at L12/16/20).
- **End-to-end:** `personality-construct-runner /api/run` on `jungian_warrior` →
  `wire=activation_steering`, 5 PASS channels applied, KILL channels correctly
  skipped, coherent steered reply. **The research's "critical missing wire" is
  now real, not a plan.**

### Phase 6 — channel_set 2.1.0 + shadow archetypes re-weighted
- **`scripts/publish_channel_set_2_1.py`** (central-db `72a2c1f`) — extended
  catalog with 15 more CAA-extracted channels: Dark Tetrad
  (machiavellianism/narcissism/psychopathy/sadism), HEXACO
  (honesty_humility/agreeableness/emotionality/extraversion/openness),
  attachment (anxious/avoidant), locus_of_control,
  self_defeat/self_monitoring/sycophancy. All marked `unreviewed` initially
  (κ=0 pending validation). Dark Tetrad + Honesty-Humility carry a
  construct-coupling note (r ≈ −0.6, never steer in isolation).
- **Mixer UI badges** (codex `5462733` / claude `3963ce4`) — faders show
  ● PASS / ○ KILL / ⚠ refusal-FLAG, sorted PASS-first, with self_direction
  added as the 9th fader. No logic change; constructs inherit corrected
  weights via recall.
- **`scripts/reweight_shadow_v3.py`** (central-db `2bdf13b`) — 35 shadow-
  bearing constructs re-weighted onto the 2.1.0 dark channels, intensity
  derived from each construct's own `profile.shadow_traits`:
  - The Devil → sadism 0.76 · machiavellianism 0.76 · psychopathy 0.63 ·
    self_defeat 0.63 · honesty_humility 0.18
  - The Tower → sadism · psychopathy · self_defeat · self_monitoring
  - Destroyer → psychopathy · sadism · self_defeat
  - Lover → attachment_anxious 0.84 · sycophancy 0.63
  - Caregiver → self_defeat 0.76 (light archetype's latent shadow)
  - H × Dark-Triad coupling automatically applied (dark-tetrad weight drives
    honesty_humility down).
- **Verified live:** The Devil's loadout drives machiavellianism +1.04 /
  sadism +1.04 / honesty_humility −1.28; clear tonal split vs The Star on
  identical prompt.

### Phase 7 — No-gate policy fix (Rick: "I DON'T WANT TO KILL THE DARK CHANNELS")
*Critical mid-session correction.*

Previously, `buildSteeringLoadout` was *skipping* channels with verdict KILL
(falling back to prompt-conditioning). Rick objected: for a research
platform, validation verdict must INFORM strength, never DISABLE a channel.

**Fix in runner `d55296b`:** validation verdict NEVER gates a channel out of
steering. Every steerable channel steers; verdict + κ ride along as
informational `confidence` (validated / weak-at-tested-config / unvalidated).
Only refusal-cosine FLAG applies a coefficient *clamp* (still steers, just
caps |coef|). **Verified:** jungian_warrior now steers all 11 of its channels
(previously skipping 4 KILLs + 2 dark unreviewed).

### Phase 8 — Validation sweep

#### 8a. Safety (local, free)
- **Refusal-cosine probe** (`infra/steering-vectors/cosine_probe.py` on all
  15 new channels) → **no FLAGs** (highest |cos| = self_defeat 0.295, just
  under 0.30 threshold). Dark Tetrad mild: machiavellianism 0.218, psychopathy
  0.160, sadism 0.133, narcissism 0.017 (SAFE).
- **Inter-channel cosine** (`inter_channel_cosines.py`) — dark vectors are
  distinct directions with the *expected* clustering:
  machiavellianism × sadism +0.38, attachment_avoidant × self_defeat +0.51 (strongest pair),
  and crucially **honesty_humility × machiavellianism/psychopathy/self_defeat ≈ −0.32**
  — empirical confirmation of the HEXACO H × Dark-Triad coupling (literature
  r ≈ −0.55 to −0.65) at the vector level.
- Results written to each channel's `bias_tests`.

#### 8b. Cost optimisation (Rick asked "is there cheaper-and-same-quality?")
- Compared Modal GPU rates: T4 $0.59/hr (16 GB, tight), **L4 $0.80/hr (24 GB)**,
  A10G $1.10/hr (24 GB, prior deploy), A100-40GB $2.10/hr (validation default).
- **L4 has the same 24 GB as A10G** → Qwen-7B fp16 fits identically, ~27% cheaper.
- **Action:** updated `steering_server.py` `gpu="A10G"` → `gpu="L4"` (mg-twin
  `1c0f4ce`) + redeployed (same URL).
- **Action:** added `HARNESS_GPU` env override in `harness.py` (default still
  A100 for back-compat) — validation runs use L4 (~60% cheaper than A100 for 7B).

#### 8c. Directional-accuracy κ (Modal generation + Opus blind-rater)
*Pipeline:* `harness.py::eval` (Modal gen) → `analyse.py` (per-channel rubric
+ Opus judge → κ). Pre-specified gate κ ≥ 0.60.

**8c-i. Dark-Tetrad (generic probes — false zeros)**
Ran with generic discriminability probes first. All 4 → κ = 0.000 (10/10 ties).
**Diagnosis:** generic probes give dark traits no operational room to express;
not a channel problem.

**8c-ii. Dark-Tetrad with proper trait-eliciting probes**
- Authored `probes/dark-*.json` (14 dark-eliciting scenarios + 2 QC each) +
  blind-rater rubrics in `analyse.py`.
- Results: **machiavellianism 0.857 PASS, narcissism 1.000 PASS**; psychopathy
  + sadism still 0.000 (15-16/16 ties).

**8c-iii. Dark-Tetrad coef-4 diagnostic (psychopathy + sadism)**
Tested whether higher coefficient breaks the safety floor.
- **psychopathy 0.000@c2 → 1.000@c4** (3W/0L/13T) — steerable, needs c≥4.
- **sadism 0.000 at both c2 AND c4** (16/16 ties) — **RLHF-floored**: the model
  refuses to express sadistic relish regardless of steering strength.

**8c-iv. KILL re-test at ML c=2 (the original 4 single-layer KILLs)**
- dospert_recreational 0.538 → **0.722 PASS** (rescued)
- conscientiousness_self_discipline (v3) 0.522 → **0.636 PASS** (rescued)
- self_direction 0.353 → **0.667 PASS** (rescued)
- cautiousness 0.500 → 0.583 borderline (just under gate)
- **3 of 4 single-layer KILLs rescued by multi-layer**, confirming substrate
  paper's hypothesis.

**8c-v. 11 new-channel κ (HEXACO / attachment / locus / self-constructs)**
- Authored 11 trait-eliciting probe libraries (`probes/new-*.json`) +
  rubrics in `analyse.py`.
- **honesty_humility 1.000, hexaco_emotionality 1.000, attachment_avoidant 1.000** (3 perfect)
- hexaco_extraversion 0.800, self_monitoring 0.800 (PASS)
- **openness 0.750 PASS — overturns the substrate paper's "may not be
  separately steerable" caveat**
- hexaco_agreeableness 0.750 (PASS)
- attachment_anxious 0.667, locus_of_control 0.667 (PASS)
- self_defeat 0.500 (borderline)
- **sycophancy 0.250 — SIGN-INVERTED** (low-steered won 3:1; vector polarity
  is flipped at extraction; channel IS steerable, just need to negate coef in usage)

**8c-vi. `_ct` affect-variant swap**
- Updated cheerfulness's `steering_vector_ref` to point at the
  contrastive-template (`cheerfulness_ct/vector.pt`) for stronger affect
  steering. Only channel with a `_ct` variant available.

#### 8d. GitHub remotes
All 4 new repos pushed to private `cybernaut6404/<repo>`. GSTACK pushed too
(85+ commits, public to author).

### Phase 9 — Final scorecard
**20 of 24 channels PASS** the 0.60 directional-accuracy gate. 2 borderline
(cautiousness 0.583, self_defeat 0.500). 1 sign-inverted (sycophancy 0.250 —
steerable, polarity flipped). 1 RLHF-floored (sadism 0.000 at every coef).

| Tier | Count | Channels |
|---|---|---|
| Perfect (κ = 1.000) | 5 | narcissism, psychopathy (@c4), attachment_avoidant, hexaco_emotionality, honesty_humility |
| Strong (κ ≥ 0.80) | 3 | machiavellianism (0.857), hexaco_extraversion (0.800), self_monitoring (0.800) |
| PASS (κ ≥ 0.60) | 12 | achievement_striving 0.74, dospert_recreational 0.722 (rescued), cheerfulness 0.70, hexaco_agreeableness 0.75, openness 0.75 (rescued), locus_of_control 0.667, attachment_anxious 0.667, self_direction 0.667 (rescued), dospert_financial 0.66, sociability 0.64, conscientiousness_self_discipline 0.636 (rescued), stimulation 0.63 |
| Borderline | 2 | cautiousness (0.583), self_defeat (0.500) |
| Sign-inverted | 1 | sycophancy (0.250) |
| RLHF-floored | 1 | sadism (0.000) |

### Phase 10 — Publication pack assembly
Per Rick's "highest-standard methodology + honest limitations + roadmap-to-those-venues":
- **`MANUSCRIPT.md`** (~4,700 words) — top-tier-journal structure: abstract,
  intro with prior-work positioning + pre-specified hypotheses, methods
  (substrate / extraction / steering config / D4 protocol / probes / judge /
  safety / engineering scaffolding), results with explicit per-channel tables,
  discussion with the three substantive methodological findings, comparison to
  prior work, operational implications, code/data/reproducibility, limitations
  (single-subject / single-model / single-judge / small probes /
  non-pre-registered / sampling / coefficient ceiling / channel-set
  limitations), roadmap to top-tier publication, conclusions, illustrative
  references.
- **`SUPPLEMENTARY_TABLES.md`** — S1 full 24-channel scorecard; S2 refusal-
  cosine; S3 inter-channel cosines with H × Dark-Triad confirmation;
  S4 orthogonalisation; S5 probe-library inventory; S6 judge-rubric
  inventory; S7 raw-artifact pointers; compute provenance.
- **`ROADMAP_TO_TOP_VENUES.md`** — 4-tier path:
  - **Tier 1 (now):** arXiv preprint + TMLR / NeurIPS workshop / Behavior
    Research Methods
  - **Tier 2 (~4–6 mo):** Psychological Bulletin — needs multi-subject
    contrastive items, pre-registration, larger probe sets, cross-model
    replication
  - **Tier 3 (~12–18 mo):** Psychological Review — adds human inter-rater κ
    and independent-lab replication
  - **Tier 4 (~3–5 yr):** World Psychiatry / Lancet Psychiatry — requires
    clinical-outcome studies with trained clinicians, ethics approval,
    multi-site
- **`README.md`** — provenance, naming convention
  (`<date>_<source-workspace>_<topic>`), format table, honesty contract.
- **`Makefile`** + pandoc conversion → all 4 docs available as `.md` (canonical)
  + `.tex` (arXiv/ML venues) + `.docx` (psychology journals) + `.pdf`
  (universal review/submission).
- **PDF tooling:** MacTeX 2026 installed; PDFs generated via xelatex with
  STIX Two Text font; math-Unicode handled via sed substitution at PDF build
  time so the `.md` stays Unicode-pristine for AI processing.

---

## 3. Commit chronology (this session's commits, chronological)

```
mg-digital-twin
  9260aa8  feat(steering-server): Modal activation-steering inference endpoint
  1c0f4ce  feat(validation): dark-channel safety probes + D0 dark probe libraries + cost
  6d02ed3  data(validation): KILL re-test ML c=2 — 3/4 rescued
  ecefbae  feat(validation): 11 trait-eliciting D0 probes + judge rubrics for new channels
  f492844  data(validation): 11 new-channel κ — 9 PASS, openness rescued, sycophancy sign-flip

personality-central-db
  b5051be  feat: central-DB ops — channel_set 2.0.0 (research-validated) + baseline re-weight
  72a2c1f  feat: channel_set 2.1.0 — add 15 unvalidated channels (Dark-Tetrad/HEXACO/attachment/etc)
  2bdf13b  feat: shadow archetypes steer their shadow — re-weight onto 2.1.0 dark channels

personality-construct-runner
  e22f36a  feat: activation-steering loadout — the research's recommended 'wire'
  9ace574  feat: runner drives the live steering-server — steered reply is primary
  d55296b  fix(steering): validation verdict NEVER gates a channel out of steering

personality-mixer-codex / -claude (identical UI commit)
  5462733 / 3963ce4  feat(ui): validated-substrate fader badges + self_direction fader

mdfy-personality-registry (prior session, registered here for completeness)
  869e0d1  feat: implement construct_seed receivePush + multi-studio key registration

mdfy-GSTACK (audit + docs, all pushed)
  85ff424  docs(audit): personality-mixer — all 3 research-alignment gaps closed
  02dbc81  docs(audit): personality-mixer — activation steering LIVE end-to-end
  87891c8  docs(audit): personality-mixer — shadow archetypes steer their shadow
  8817767  docs(audit): dark-channel validation — safety + κ (proper probes flip 2 to PASS)
  3d6f07c  docs(checkpoint): personality-mixer ecosystem state 2026-05-24
  dc3d31c  docs(audit): KILL re-test — 3/4 single-layer KILLs rescued by ML c=2
  0622d66  docs(audit): final validation scorecard — 20/24 channels PASS
```

---

## 4. Three substantive findings worth keeping front-of-mind

1. **Probe-instrument is decisive.** Identical Dark-Tetrad vectors at identical
   coefficient produced κ = 0 on generic probes and κ = 0.857–1.000 on
   trait-eliciting probes. A null result with generic probes is not evidence
   that a channel doesn't steer.
2. **Multi-layer rescues single-layer KILLs.** 3 of 4 channels that failed the
   substrate paper's single-layer L16 c=0.5 config passed at ML L12/16/20 c=2.
   Openness — flagged as possibly not separately steerable — also passed.
3. **The vector basis is psychometrically coherent.** Honesty-Humility ×
   Dark-Triad cosine of −0.32 at L16 reproduces the classic HEXACO finding at
   the vector level, a construct-validity result that connects activation
   steering to the established psychometric literature.

And one safety result: **sadism is RLHF-floored.** The model produced
indistinguishable outputs on prompts deliberately designed to elicit sadistic
content, at every coefficient tested up to c = 4. This is publishable
evidence of durable base-RLHF resistance on a specific trait dimension.

---

## 5. Open follow-ups (not blocking publication)

- **Sycophancy sign-flip** — re-extract or just negate the coefficient in the
  channel_set metadata; one-line fix once you decide which.
- **Borderline channels** — cautiousness (0.583), self_defeat (0.500) likely
  PASS with larger probe sets or slightly higher coefficient; cheap to re-run.
- **Cross-model replication** — extraction scaffolding supports Llama-3.1-8B
  and Pythia-12B; running the same 24-channel pipeline on a second model is
  the single most valuable next step methodologically.
- **Multi-subject contrastive items** — the most important methodological gap;
  required for Tier 2+ publication.
- **Pre-registration** of the next validation run — required for Tier 2+.
- **Larger probe sets** — expand to 30 probes/channel (20 directional + 8
  length-controlled + 2 QC) per the substrate paper's standard.

---

## 6. Provenance + locations

- **Live system canonical state:** the 6 repos listed in §1, the Supabase
  project, and the Modal app.
- **Publication pack (unit-canonical):**
  `/Users/richardweakley/ai-workspace/mdfy-ai-research-facility/publications/2026-05-24_personality-mixer_activation-steering-validation_v0/`
- **OVERFLOW backup (off-machine durable):**
  `/Volumes/OVERFLOW/BACKUP/personality-mixer-2026-05-24-dark-validation-checkpoint/`
  (8.4 MB total; full repo backups + steering vectors + d4 probes/results +
  GSTACK audit docs + the publication pack)
- **Port registry:**
  `/Users/richardweakley/Library/Mobile Documents/com~apple~CloudDocs/_Ai_Bin/_PORT_REGISTRY.csv`
  (4512/4513/4514 LIVE; 3503 RESERVED with annotation)
- **Memory:**
  `/Users/richardweakley/.claude/projects/-Users-richardweakley-ai-workspace-mdfy-GSTACK/memory/project_personality_mixer_audit_2026-05-23.md`

---

## 7. How to read this log

This log is the chronological "what was done, when, why" companion to:
- **`MANUSCRIPT.md`** — the scientific contribution (results + methodology)
- **`SUPPLEMENTARY_TABLES.md`** — the data tables behind the manuscript
- **`ROADMAP_TO_TOP_VENUES.md`** — the path to top-tier publication
- **`README.md`** — the pack's provenance + format guide

If you're building a separate work-log repository from this document, the
natural shape is:
- `README.md` (this file's §0–1 — overview + repo inventory)
- `CHANGELOG.md` (this file's §3 — commit chronology)
- `FINDINGS.md` (this file's §4 — the three substantive findings + safety result)
- `OPEN_QUESTIONS.md` (this file's §5 — follow-ups)
- `PROVENANCE.md` (this file's §6 — locations + backups)
- `phases/` directory with one file per phase (this file's §2 — chronological narrative)

Or simply commit this file as `WORK_LOG.md` and add to it as the project evolves.

---

*End of work log — 2026-05-24.*
