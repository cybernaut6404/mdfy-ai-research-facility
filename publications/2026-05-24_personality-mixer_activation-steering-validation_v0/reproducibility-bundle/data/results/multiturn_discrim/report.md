# Multi-turn discriminability — rick vs warm_direct_coach

## Method
- Judge: claude-opus-4-7
- Pairs: 24
- Construct A: Direct, low-warmth, novelty-seeking, financial-risk-tolerant, ambition-pushing.
- Construct B: Warm, collaborative, depth-oriented, capital-preserving, sustainable-pace.
- Acceptance per ROADMAP §9.6: pairwise κ > 0.4 (or equivalently, decided accuracy >70%)

## Per-turn discriminability

| Turn | Correct | Wrong | Tie | Decided acc | Effective κ (ties=chance) |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 4 | 0% | +0.000 |
| 1 | 1 | 0 | 3 | 100% | +0.250 |
| 2 | 3 | 0 | 1 | 100% | +0.750 |
| 3 | 1 | 1 | 2 | 50% | +0.000 |
| 4 | 4 | 0 | 0 | 100% | +1.000 |
| 5 | 1 | 3 | 0 | 25% | -0.500 |

## Aggregate (all turns)
- Correct: 10, Wrong: 4, Tie: 10 (42%)
- Decided accuracy: 71%
- Effective κ: +0.250
- **Verdict: FAIL (overall κ +0.250 ≤ 0.4)**

## Interpretation

If discriminability rises with turn index (e.g. κ at turn 0 < κ at turn 5), the substrate works in conversation but not in single-shot. If discriminability stays flat across turns, multi-channel CAA composition does not produce persona substitution even with conversational accumulation.

## Provenance
- rick runs: experiments/d4-fader-intervention/runs/rick_multiturn
- warm_direct_coach runs: experiments/d4-fader-intervention/runs/warm_direct_coach_multiturn