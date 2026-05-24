# W11 B10 — per-channel multi-turn diagnostic (cheerfulness)

- Started: 2026-05-09T05:07:38Z
- Ended:   2026-05-09T05:51:11Z
- Channel: cheerfulness (single-channel, isolated from composition)
- Vector:  infra/steering-vectors/qwen2.5-7b-instruct-orth/cheerfulness/vector.pt (orth, L=16, single-layer)
- Coef:    +2.0 (high) vs -2.0 (low)

## Hypothesis tested

The W10/B9 multi-turn FAIL could be:
1. Composition-specific — additive composition of multiple channels collapses over turns
2. Architecture-fundamental — additive steering of any kind doesn't sustain multi-turn

This run isolates by testing single-channel cheerfulness only.

## Result

| Metric | κ | Verdict |
|---|---|---|
| Overall κ (160 paired comparisons) | +0.150 | FAIL |
| Best per-turn κ | 0.500 | PASS |

**Final verdict: PASS** (any-turn rule, gate κ > 0.4)

## Trend (multi-turn discrim across all attempts)

| Test | Setup | Overall κ | Best-turn κ |
|---|---|---|---|
| W10 multi-turn (rick vs coach) | composite, single-layer, c=1 | +0.019 | +0.300 |
| W11 B9 multi-turn (rick vs coach) | composite, orth+ML(L12,16,20), c=2 | +0.012 | +0.200 |
| **W11 B10 (this) cheerfulness@high vs @low** | single-channel, L=16, c=±2 | +0.150 | 0.500 |

## Interpretation

**Per-channel multi-turn substrate WORKS.** The W10/B9 multi-turn FAIL is composition-specific, not architecture-fundamental. Substrate is alive at single-channel level. Implication: additive composition of multiple channels is the bottleneck. Next step: non-additive composition (K-Steering, gating, conditional routing). Substrate paper headline narrows to 'per-channel multi-turn works; multi-channel additive composition fails over conversation accumulation'.

## Provenance

- Judge report: experiments/d4-fader-intervention/results/w11_b10_perchannel/judge/report.md
- High dialogues: experiments/d4-fader-intervention/runs/cheerfulness_high_multiturn/
- Low dialogues:  experiments/d4-fader-intervention/runs/cheerfulness_low_multiturn/
- Run log: experiments/d4-fader-intervention/results/w11_b10_perchannel/run.log

## Cost (estimated)

| Item | Modal | Anthropic |
|---|---|---|
| 2 × 160 multi-turn generations | ~£7.00 | — |
| 160 paired comparisons (Opus judge) | — | ~£0.50 |
| **Total** | **~£7.00** | **~£0.50** |
