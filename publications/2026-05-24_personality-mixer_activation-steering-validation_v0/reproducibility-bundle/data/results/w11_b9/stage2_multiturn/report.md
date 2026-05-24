# Multi-turn discriminability — orth_rick_ml vs orth_coach_ml

## Method
- Judge: claude-opus-4-7
- Pairs: 160
- Construct A: Direct, low-warmth, novelty-seeking, financial-risk-tolerant, ambition-pushing.
- Construct B: Warm, collaborative, depth-oriented, capital-preserving, sustainable-pace.
- Acceptance per ROADMAP §9.6: pairwise κ > 0.4 (or equivalently, decided accuracy >70%)

## Per-turn discriminability

| Turn | Correct | Wrong | Tie | Decided acc | Effective κ (ties=chance) |
|---|---|---|---|---|---|
| 0 | 6 | 2 | 12 | 75% | +0.200 |
| 1 | 8 | 5 | 7 | 62% | +0.150 |
| 2 | 7 | 8 | 5 | 47% | -0.050 |
| 3 | 9 | 6 | 5 | 60% | +0.150 |
| 4 | 8 | 8 | 4 | 50% | +0.000 |
| 5 | 6 | 10 | 4 | 38% | -0.200 |
| 6 | 10 | 10 | 0 | 50% | +0.000 |
| 7 | 8 | 11 | 1 | 42% | -0.150 |

## Aggregate (all turns)
- Correct: 62, Wrong: 60, Tie: 38 (24%)
- Decided accuracy: 51%
- Effective κ: +0.012
- **Verdict: FAIL (overall κ +0.012 ≤ 0.4)**

## Interpretation

If discriminability rises with turn index (e.g. κ at turn 0 < κ at turn 5), the substrate works in conversation but not in single-shot. If discriminability stays flat across turns, multi-channel CAA composition does not produce persona substitution even with conversational accumulation.

## Provenance
- orth_rick_ml runs: experiments/d4-fader-intervention/runs/orth_rick_ml_multiturn
- orth_coach_ml runs: experiments/d4-fader-intervention/runs/orth_warm_direct_coach_ml_multiturn