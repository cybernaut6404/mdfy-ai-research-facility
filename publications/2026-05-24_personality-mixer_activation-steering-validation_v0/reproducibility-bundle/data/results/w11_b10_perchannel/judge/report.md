# Multi-turn discriminability — cheerfulness_high vs cheerfulness_low

## Method
- Judge: claude-opus-4-7
- Pairs: 160
- Construct A: Upbeat, optimistic in tone. Expresses positive affect — finds the bright side, frames opportunities, leans into excitement.
- Construct B: Subdued, muted in tone. Reserved emotional expression — flags concerns, dwells on problems, doesn't flourish.
- Acceptance per ROADMAP §9.6: pairwise κ > 0.4 (or equivalently, decided accuracy >70%)

## Per-turn discriminability

| Turn | Correct | Wrong | Tie | Decided acc | Effective κ (ties=chance) |
|---|---|---|---|---|---|
| 0 | 14 | 4 | 2 | 78% | +0.500 |
| 1 | 7 | 9 | 4 | 44% | -0.100 |
| 2 | 11 | 6 | 3 | 65% | +0.250 |
| 3 | 9 | 10 | 1 | 47% | -0.050 |
| 4 | 13 | 5 | 2 | 72% | +0.400 |
| 5 | 7 | 7 | 6 | 50% | +0.000 |
| 6 | 13 | 7 | 0 | 65% | +0.300 |
| 7 | 6 | 8 | 6 | 43% | -0.100 |

## Aggregate (all turns)
- Correct: 80, Wrong: 56, Tie: 24 (15%)
- Decided accuracy: 59%
- Effective κ: +0.150
- **Verdict: FAIL (overall κ +0.150 ≤ 0.4)**

## Interpretation

If discriminability rises with turn index (e.g. κ at turn 0 < κ at turn 5), the substrate works in conversation but not in single-shot. If discriminability stays flat across turns, multi-channel CAA composition does not produce persona substitution even with conversational accumulation.

## Provenance
- cheerfulness_high runs: experiments/d4-fader-intervention/runs/cheerfulness_high_multiturn
- cheerfulness_low runs: experiments/d4-fader-intervention/runs/cheerfulness_low_multiturn