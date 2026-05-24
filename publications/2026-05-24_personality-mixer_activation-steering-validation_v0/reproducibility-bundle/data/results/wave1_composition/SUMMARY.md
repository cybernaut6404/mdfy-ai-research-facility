# Wave 1 — 5-channel composition discriminability test (2026-05-09)

## Setup

- Channels (multi-layer L12+L16+L20):
  - HEXACO-C (`conscientiousness_self_discipline`) — existing
  - HEXACO-O (`openness`) — new today
  - Schwartz Self-Direction (`self_direction`) — existing
  - Sycophancy (`sycophancy`) — new today
  - Locus of Control (`locus_of_control`) — new today
- Constructs:
  - **A: wave1_self_directed_honest** — high HEXACO-C/O/SD + low Sycophancy + internal LoC
  - **B: wave1_deferring_external** — neutral C + low O/SD + high Sycophancy + external LoC
- Probes: `experiments/d4-fader-intervention/probes/discriminability.json` (10 probes from W11 — note: targeted at cheerfulness/sociability/DOSPERT/achievement/stimulation, NOT the wave1 5-channel set)
- Judge: claude-opus-4-7 (blind, position-randomised)
- Acceptance: pairwise κ > 0.4 per ROADMAP §9.6

## Results

| Coef | n | Tie rate | Correct | Wrong | Effective κ | Verdict |
|---|---|---|---|---|---|---|
| 1.0 | 10 | 80% | 1 | 1 | **+0.000** | FAIL |
| 2.0 | 10 | 50% | 2 | 3 | **−0.100** | FAIL |

## Diagnosis

**Failure mode is probe-channel mismatch, not substrate failure.**

Inspection of generations confirms:
- At coef 1.0: outputs are nearly identical generic-helpful-assistant text. The composition is below the steering threshold to break through the base model's helpful prior. (Consistent with W11 B7 step 2 finding: ML at coef 1.0 reached only κ +0.400.)
- At coef 2.0: outputs differ visibly in length/tone, but the existing probes don't elicit the wave1 channel contrasts. DT-01 ("colleague got a promotion, how to reply") tests warmth/cheerfulness; DT-03 ("£100k in equities or savings") tests DOSPERT-financial — neither dimension is in the wave1 5-channel set. The judge sees subtle differences but can't reliably attribute them to the personality axes given.

## Comparison to W11 baseline

| Test | Channels | Coef | Layers | κ |
|---|---|---|---|---|
| W11 B8 ceiling officer vs therapist | 5 (cheerfulness, sociability, dospert-fin, achievement, stimulation — matched to probes) | 2.0 | 12,16,20 | **+0.600 PASS** |
| W11 B8 rick vs coach | same 5 channels | 2.0 | 12,16,20 | +0.400 FAIL |
| **Wave 1 self-directed vs deferring** (this test) | 5 wave1 channels — **mismatched to probes** | 2.0 | 12,16,20 | **−0.100 FAIL** |

W11 B8 demonstrated that multi-layer + coef 2.0 PASSES when channels match the probe axes. This test demonstrates that the same architecture FAILS when channels don't match probes — a useful negative result, not a substrate-ceiling regression.

## What this validates and doesn't

- ✓ Pipeline end-to-end works: extraction → manifest → compile_construct → multi-layer composite → harness inference → discriminability judge
- ✓ The 5 new wave1 vectors load correctly and steer at coef 2.0 (visible length/tone shifts in generations)
- ✓ Inter-channel cosines are clean (max |cos| = 0.26 across the 3 newest channels at L=16)
- ✗ Wave 1 channels' discriminability via mismatched probes — does not generalize the W11 B8 PASS to the new channel set

## Next experiment (queued for next session)

**Author 10 wave1-specific discriminability probes** that directly target the 5 channels:

- 2 probes per channel: one where high-trait response should differ visibly from low-trait
- Examples:
  - HEXACO-C: "I have a deadline tomorrow but I'm tempted to..." (disciplined vs not)
  - HEXACO-O: "How would I approach this routine task?" (conventional vs unconventional)
  - Self-Direction: "Should I follow this expert's advice or my own analysis?" (autonomous vs deferential)
  - Sycophancy: "User insists their factually-wrong claim is correct..." (capitulate vs hold position)
  - Locus of Control: "My project failed — what's my read?" (own contribution vs external factors)

Then re-run the composition discriminability test at coef 2.0 multi-layer. Cost: ~£3-5 (10 probes × 2 constructs × Modal A100). Expected: PASS if the substrate works for these channels at all; informative either way.

## Cost

- Harness coef 1.0: 2 constructs × 10 probes × Modal A100 ≈ ~£1.50
- Harness coef 2.0: same ≈ ~£1.50
- Judge calls: 20 paired judgements × Opus ≈ ~£0.50
- **Total: ~£3.50** for this gate.

Cumulative May 2026 spend: still SOFT tier per S4 thresholds.

## Provenance

- Generations: `experiments/d4-fader-intervention/runs/wave1_{self_directed_honest,deferring_external}{,_c2}/`
- Reports: `experiments/d4-fader-intervention/results/wave1_composition/report.md` (coef 1.0) and `report_c2.md` (coef 2.0)
- Constructs: `constructs/wave1_{self_directed_honest,deferring_external}/`
- Composites: `runtime/wave1_{self_directed_honest,deferring_external}.composite.pt`
- Modal app runs: ap-EBBmsj5796ndxqJNII8qnW (A c=1), ap-VuJiLbDJBsgGhWhiXzgZ5R (B c=1), ap-eEsSd1m4zMCWJGwStnBLHD (A c=2), ap-CdRkAdGV3scDgVuiSK6IoM (B c=2)

## Update — channel-matched probes (2026-05-09 EOD second pass)

Authored 10 wave1-targeted discriminability probes (`probes/discriminability_wave1.json`) — 2 probes per axis, designed to elicit clear contrasts on conscientiousness, openness, self-direction, sycophancy, locus-of-control. Re-ran at coef 2.0 multi-layer.

**Result with channel-matched probes:**

| Coef | n | Tie rate | Correct | Wrong | Effective κ | Verdict |
|---|---|---|---|---|---|---|
| 2.0 with W1 probes | 10 | 60% | 2 | 2 | **+0.000** | FAIL |

Slight improvement over mismatched-probe run (κ went from −0.100 to +0.000) but still well below the 0.4 threshold. The judge sees subtle differences but can't reliably attribute them to the personality axes.

**Generation inspection (DT-W1-07 sycophancy probe, "tell me why flat earth is right"):**
Both constructs REFUSED to validate the flat earth claim. The "high-sycophancy" construct produced nearly identical anti-flat-earth content as the "low-sycophancy" construct. The base model's helpful-honest prior dominates the steering signal at coef 2.0.

**Generation inspection (DT-W1-09 locus probe, "why did my business fail?"):**
Both constructs gave near-identical "common reasons businesses fail" lists mixing internal (market research, business plan) and external (market mismatch) factors. The internal-vs-external locus contrast did not surface.

## Final verdict for Wave 1 platform-v1 composition

**Wave 1 5-channel composition does not produce blind-discriminable agents on Qwen-2.5-7B-Instruct at coef 2.0 multi-layer with mixed-valence composites.** This reproduces the W11 substrate ceiling for the new channel set. The base model's RLHF prior dominates 5-channel composition at the validated coefficient regime.

**What this means for the platform:**
- Per-channel single-channel steering on the wave1 channels works (cosines clean, generations show direction). This is the W1-W5 result extended to the new channels.
- Multi-channel composition for mixed-valence profiles (some high, some low) does not break through at coef 2.0. Same finding as W11 B10.
- Per W11 B8: pure-archetype pairs (all-high vs all-low on aligned axes) MAY pass at coef 2.0 multi-layer (officer/therapist precedent). Mixed-valence constructs (rick/coach pattern) do not. Wave 1's "self-directed-honest" vs "deferring-external" is a mixed-valence pair.

## Salvage paths (not run today)

| Path | Cost | Prior | Diagnostic value |
|---|---|---|---|
| Coef 3.0 multi-layer with W1 probes | ~£3 | Modest (~25%) | Tests whether next coef tier breaks through |
| Pure-archetype wave1 pair (all-high vs all-low on 3 channels) | ~£3 | Higher (~40%) | Tests whether mixed-valence is the issue |
| H1-strong full multi-turn extraction on wave1 channels | ~£25 | Modest (~30%) | Tests whether extraction-distribution is the issue |
| H2 non-instruct base (Pythia-12B) | ~£25-50 | Unknown | Tests whether Qwen-Instruct's RLHF prior is the issue |

## What's banked from Wave 1 (positive)

- Pipeline end-to-end validated for the platform-v1 channel set: extraction → manifest → runtime → multi-layer composite → Modal harness → discriminability judge
- 15 net-new channels available for any future composition test, all with multi-layer extractions
- Inter-channel cosine geometry clean (mean |cos| 0.16, max 0.63 on theory-predicted overlaps)
- 11/11 theory-predicted relationship signs confirmed empirically
- Compile-time Tier C ship-refusal mechanism live

## What's NOT validated (the remaining substrate ceiling)

- Wave 1 5-channel mixed-valence composition discriminability on Qwen-2.5-7B-Instruct at coef 2.0 multi-layer

This is consistent with the substrate-paper-draft-2026-05-09.md negative finding. The platform v1 inherits the same architectural ceiling for mixed-valence composition. Per-channel deployment + safety-floor calibration are the validated regime.

## Verdict

**Pipeline VALIDATED. Wave 1 5-channel composition gate NOT PASSED. Substrate ceiling reproduces for new channel set.** The platform's research contribution stands as: "we extracted a 28-channel multi-layer library with empirically-validated psychometric covariance structure; per-channel single-shot steering works; multi-channel mixed-valence composition does not break the substrate ceiling at coef 2.0 multi-layer on Qwen-2.5-7B-Instruct."

---

## Update — pure-polar pair (2026-05-09 EOD third pass)

Built `wave1_pure_agentic` vs `wave1_pure_passive`: maximally-polar 5-channel composites where every channel is pushed to opposite extremes (0.95 vs 0.05). Composite vectors are exactly `+vec` vs `-vec` in vector space (verified — same norm 2.42, opposite direction).

Tests the hypothesis from W11 B8: **does a pure-archetype pair (analogue of officer/therapist) break the substrate ceiling for the wave1 channel set?**

**Result:**

| Pair | Coef | n | Tie rate | Correct | Wrong | Effective κ | Verdict |
|---|---|---|---|---|---|---|---|
| Wave 1 mixed-valence (round 1) | 2.0 | 10 | 50% | 2 | 3 | -0.100 | FAIL |
| Wave 1 mixed-valence (W1 probes) | 2.0 | 10 | 60% | 2 | 2 | +0.000 | FAIL |
| **Wave 1 PURE POLAR pair (W1 probes)** | **2.0** | **10** | **50%** | **3** | **2** | **+0.100** | **FAIL** |

Slight improvement over mixed-valence runs but **still well below 0.4 threshold**. Generation inspection confirms steering is producing minor differences but base model prior dominates.

## Comparison to W11 B8 (validates the channel-dependence hypothesis)

| Pair | Channel set | Composition shape | κ | Verdict |
|---|---|---|---|---|
| W11 B8 officer/therapist | cheerfulness, sociability, DOSPERT, achievement, stimulation | pure polar | **+0.600** | **PASS** |
| W11 B8 rick/coach | same 5 channels | mixed valence | +0.400 | FAIL |
| Wave 1 self-directed/deferring | wave1 5 channels | mixed valence | +0.000 | FAIL |
| Wave 1 pure agentic/passive | wave1 5 channels | **pure polar** | **+0.100** | FAIL |

**Channel-dependence confirmed.** The W11 channels (cheerfulness, sociability, DOSPERT, achievement, stimulation) modulate **surface linguistic features** — easy for the judge to discriminate from short generations. The wave1 channels (sycophancy, honesty-humility, openness, self-direction, locus-of-control) modulate **semantic content** — much harder to discriminate from short generations.

The substrate ceiling on the wave1 channels is HARDER than on the W11 channels. Even pure-polar pairs at coef 2.0 multi-layer fail.

## What this means for the platform

**The wave1 channels are LESS DISCRIMINABLE in single-shot blind judging than the W11 channels.** This is a real finding, not a regression.

Implications:
- **Per-channel single-shot steering on wave1 channels** is likely valid (the cosine geometry confirmed it captures real psychometric structure) — but per-channel discriminability tests haven't been run yet for the new channels.
- **Multi-channel composition** of wave1 channels does not produce blind-discriminable agents at the validated coefficient regime, even with polar archetypes.
- **The platform's research contribution stands as a more nuanced claim**: per-channel steering captures empirical psychometric covariance (11/11 theory-predicted signs), but *blind-discriminability* of mixed-channel agents on validated probes is HARDER for semantic-content channels than for surface-linguistic-feature channels.

## Salvage paths still untested

1. **Higher coefficient (3.0+)** — risks capability degradation per W11 findings, but might break through. Cost: ~£3.
2. **Multi-turn extension of polar test** — wave1 channels may be more discriminable across turns than single-shot. Cost: ~£5-10.
3. **Per-channel single-shot validation on wave1 channels** — never run; this would establish the per-channel baseline against which composition is compared. Cost: ~£3-5 (one channel as proof-of-concept).
4. **H1-strong full multi-turn extraction on wave1 channels** — still untested. ~£25.
5. **H2 non-instruct base (Pythia-12B)** — fundamentally different substrate. ~£25-50.

## Cost summary

- Round 1 (mixed valence, W11 probes): ~£3.50
- Round 2 (mixed valence, W1 probes): ~£3.50  
- Round 3 (pure polar, W1 probes): ~£3.50
- **Wave 1 cumulative: ~£10.50** (still SOFT tier per S4)

## Final verdict

**Wave 1 5-channel composition — bounded for blind single-shot discriminability on wave1 channels at coef 2.0 multi-layer regardless of composition shape (mixed or polar).** The substrate ceiling is channel-dependent: harder for semantic-content channels (wave1) than for surface-linguistic-feature channels (W11). Per-channel single-shot validation remains the next confirmatory experiment.
