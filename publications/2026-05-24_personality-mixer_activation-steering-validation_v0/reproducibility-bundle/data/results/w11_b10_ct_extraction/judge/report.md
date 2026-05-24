# Multi-turn discriminability — cheerfulness_ct_high vs cheerfulness_ct_low

## Method
- Judge: claude-opus-4-7
- Pairs: 160
- Construct A: Upbeat, optimistic in tone. Expresses positive affect — finds the bright side, frames opportunities, leans into excitement.
- Construct B: Subdued, muted in tone. Reserved emotional expression — flags concerns, dwells on problems, doesn't flourish.
- Acceptance per ROADMAP §9.6: pairwise κ > 0.4 (or equivalently, decided accuracy >70%)

## Per-turn discriminability

| Turn | Correct | Wrong | Tie | Decided acc | Effective κ (ties=chance) |
|---|---|---|---|---|---|
| 0 | 11 | 7 | 2 | 61% | +0.200 |
| 1 | 9 | 9 | 2 | 50% | +0.000 |
| 2 | 8 | 11 | 1 | 42% | -0.150 |
| 3 | 7 | 7 | 6 | 50% | +0.000 |
| 4 | 12 | 4 | 4 | 75% | +0.400 |
| 5 | 8 | 9 | 3 | 47% | -0.050 |
| 6 | 12 | 8 | 0 | 60% | +0.200 |
| 7 | 8 | 4 | 8 | 67% | +0.200 |

## Aggregate (all turns)
- Correct: 75, Wrong: 59, Tie: 26 (16%)
- Decided accuracy: 56%
- Effective κ: +0.100
- **Verdict: FAIL (overall κ +0.100 ≤ 0.4)**

## Interpretation

If discriminability rises with turn index (e.g. κ at turn 0 < κ at turn 5), the substrate works in conversation but not in single-shot. If discriminability stays flat across turns, multi-channel CAA composition does not produce persona substitution even with conversational accumulation.

## Provenance
- cheerfulness_ct_high runs: experiments/d4-fader-intervention/runs/cheerfulness_ct_high_multiturn
- cheerfulness_ct_low runs: experiments/d4-fader-intervention/runs/cheerfulness_ct_low_multiturn