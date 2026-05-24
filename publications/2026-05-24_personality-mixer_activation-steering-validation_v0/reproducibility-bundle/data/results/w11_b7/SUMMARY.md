# W11 B7 — full orchestrator summary (corrected 2026-05-08)

- Started: 2026-05-08T08:33:59Z
- Ended:   2026-05-08T09:09:03Z
- Working dir: /Users/richardweakley/ai-workspace/mg-digital-twin

> Note: the original auto-generated SUMMARY.md showed all κ = ERROR due to a
> regex bug in `read_kappa` — the report format is `| Effective κ (ties count as chance) | +0.400 |`
> not `Effective κ: +0.400`. The judges ran correctly; this version reads the
> actual κ values from the reports.

## Step 1 — coef boost @ L16

| Pair | coef | κ | Verdict |
|---|---|---|---|
| orth rick vs orth coach | 2.0 | +0.000 | FAIL |
| orth rick vs orth coach | 3.0 | -0.100 | FAIL |
| ceiling officer vs therapist | 2.0 | +0.000 | FAIL |
| ceiling officer vs therapist | 3.0 | +0.300 | FAIL |

## Step 2 — multi-layer L12+L16+L20

| Pair | layers | coef | κ | Verdict |
|---|---|---|---|---|
| orth rick vs orth coach | 12,16,20 | 1.0 | +0.100 | FAIL |
| **ceiling officer vs therapist** | **12,16,20** | **1.0** | **+0.400** | **FAIL (exactly at threshold)** |

## Trend across all attempts

| Test | κ | Notes |
|---|---|---|
| W7 rick vs coach (no orth, c=1, single-layer) | 0.000 | original failure |
| W11 B4 ceiling (orth, c=1, single-layer) | +0.100 | orth alone didn't help |
| B7 step 1 ceiling c=2 | +0.000 | coef 2 didn't help |
| B7 step 1 ceiling c=3 | +0.300 | coef 3 helped some |
| **B7 step 2 ceiling ML(L12,16,20) c=1** | **+0.400** | **highest yet — at threshold** |

Multi-layer + max-polar archetypes is the strongest combination tested. It hits the threshold exactly but does not pass it (ROADMAP §9.6 requires κ > 0.4, strict).

## Final verdict — nuanced

Strict reading: **FAIL.** No test passed κ > 0.4.

Trend reading: **PARTIAL SIGNAL.** Multi-layer composition produces κ +0.400 on the ceiling test — substantially better than single-layer (+0.100) and better than coef-3 single-layer (+0.300). The substrate is producing detectable persona effect under multi-layer composition with max-polar archetypes; it just doesn't cross the LLM-judge threshold reliably at n=10.

Three remaining viable next moves:

1. **Bigger n at ML — n=20 or n=30 ceiling test at multi-layer.** The +0.400 was on n=10. With n=20-30 we'd get a tighter estimate of whether the true effect is at, above, or below threshold. ~£1-2 Modal + £0.50 judge.

2. **Combine multi-layer with coef boost.** ML at c=2.0 hasn't been tested. If single-layer c=3 added +0.3 and ML c=1 added +0.4, ML c=2 might combine. ~£1-2 Modal + £0.30 judge.

3. **Path A — paper-it-now with this evidence.** The trend is itself a contribution: composition strength scales with both coef and layer count, but doesn't reliably cross the discriminability threshold even at the upper bound. The negative finding has more nuance now.

## Recommendation

Confidence 70%. **Try (2) first — ML at coef 2.0 — fastest test of the "stack the rescues" hypothesis.** If ML+c=2 produces κ ≥ 0.5 on n=10, retry with n=20 to confirm. If it stays at ≤ +0.4, write Path A.

## Provenance

- Run log: experiments/d4-fader-intervention/results/w11_b7/run.log
- Reports: experiments/d4-fader-intervention/results/w11_b7/{rick_vs_coach,officer_vs_therapist}_{c2,c3,ml}/report.md
- Modal runs: experiments/d4-fader-intervention/runs/orth_*
- ROADMAP §9.6 acceptance: κ > 0.4 (strict)
- Cost this run: ~£3-4 Modal + ~£0.80 judge ≈ £4-5
- Cumulative project: ~£42 (W1-W11 + B7)
