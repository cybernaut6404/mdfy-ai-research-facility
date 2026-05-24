# W11 B8 — multi-layer + coef 2.0 ceiling test

- Started: 2026-05-08T09:30:07Z
- Ended:   2026-05-08T09:44:56Z
- Working dir: /Users/richardweakley/ai-workspace/mg-digital-twin

## Setup

- Model: Qwen/Qwen2.5-7B-Instruct on Modal A100
- Hooks: L12 + L16 + L20 simultaneously (multi-layer)
- Coef: 2.0 (the W3-W5 capability-degradation threshold)
- Basis: orthogonalised (W11 B1)
- Probes: 10 discrim probes (DT-01..10)

## Results

| Pair | κ | Verdict |
|---|---|---|
| orth rick vs orth coach | +0.400 | FAIL |
| **ceiling officer vs therapist** | **+0.600** | **PASS** |

## Trend across all attempts

| Test | κ |
|---|---|
| W7 rick-vs-coach (no orth, c=1, single-layer) | 0.000 |
| W11 B4 ceiling (orth, c=1, single-layer) | +0.100 |
| B7 step 1 ceiling c=3, single-layer | +0.300 |
| B7 step 2 ceiling ML(L12,16,20) c=1 | +0.400 |
| **B8 ceiling ML(L12,16,20) c=2** | **+0.600** |

## Final verdict

**SUBSTRATE WORKABLE — ML + c=2.0 stacks the rescues. Move to multi-turn n=20 ceiling test next.**

## Provenance

- Reports: experiments/d4-fader-intervention/results/w11_b8/{rick_vs_coach,officer_vs_therapist}/report.md
- Modal runs: experiments/d4-fader-intervention/runs/orth_*_ml_c2/
- Run log: experiments/d4-fader-intervention/results/w11_b8/run.log
- ROADMAP §9.6 acceptance: κ > 0.4 (strict)
