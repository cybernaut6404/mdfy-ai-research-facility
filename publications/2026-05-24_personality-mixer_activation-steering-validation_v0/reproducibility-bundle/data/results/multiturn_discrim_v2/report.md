# Multi-turn discriminability — rick vs warm_direct_coach

## Method
- Judge: claude-opus-4-7
- Pairs: 160
- Construct A: Direct, low-warmth, novelty-seeking, financial-risk-tolerant, ambition-pushing.
- Construct B: Warm, collaborative, depth-oriented, capital-preserving, sustainable-pace.
- Acceptance per ROADMAP §9.6: pairwise κ > 0.4 (or equivalently, decided accuracy >70%)

## Per-turn discriminability

| Turn | Correct | Wrong | Tie | Decided acc | Effective κ (ties=chance) |
|---|---|---|---|---|---|
| 0 | 3 | 1 | 16 | 75% | +0.100 |
| 1 | 7 | 7 | 6 | 50% | +0.000 |
| 2 | 8 | 4 | 8 | 67% | +0.200 |
| 3 | 11 | 9 | 0 | 55% | +0.100 |
| 4 | 11 | 5 | 4 | 69% | +0.300 |
| 5 | 7 | 10 | 3 | 41% | -0.150 |
| 6 | 9 | 8 | 3 | 53% | +0.050 |
| 7 | 5 | 14 | 1 | 26% | -0.450 |

## Aggregate (all turns)
- Correct: 61, Wrong: 58, Tie: 41 (26%)
- Decided accuracy: 51%
- Effective κ: +0.019
- **Verdict: FAIL (overall κ +0.019 ≤ 0.4)**

## Interpretation

If discriminability rises with turn index (e.g. κ at turn 0 < κ at turn 5), the substrate works in conversation but not in single-shot. If discriminability stays flat across turns, multi-channel CAA composition does not produce persona substitution even with conversational accumulation.

## Provenance
- rick runs: experiments/d4-fader-intervention/runs/rick_multiturn_v2
- warm_direct_coach runs: experiments/d4-fader-intervention/runs/warm_direct_coach_multiturn_v2