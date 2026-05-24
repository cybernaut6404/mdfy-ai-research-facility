# W11 B10 Phase 2 — chat-template re-extraction multi-turn diagnostic

- Started: 2026-05-09T05:52:01Z
- Ended:   2026-05-09T06:36:29Z
- Channel: cheerfulness (re-extracted on chat-template-wrapped items)
- Source items: infra/steering-vectors/contrastive-items/e5-cheerfulness-ct.jsonl (50 items)
- New vector: infra/steering-vectors/qwen2.5-7b-instruct/cheerfulness_ct/vector.pt
- Layer: L=16 (single-layer)
- Coef: +2.0 (high) vs -2.0 (low)

## Hypothesis tested

H1 (extraction-distribution mismatch): the original cheerfulness vector was
extracted on raw-text `context + completion` activation distribution. It
fails in multi-turn deployment (Phase 1 result). Re-extracting on chat-
template-wrapped distribution should narrow the extraction-deployment gap and
rescue multi-turn discrim, IF distribution mismatch is the bottleneck.

## Result

| Metric | κ | Verdict |
|---|---|---|
| Overall κ (160 paired comparisons) | +0.100 | FAIL |
| Best per-turn κ | 0.400 | FAIL |

**Final verdict: FAIL** (any-turn rule, gate κ > 0.4)

## Comparison

| Test | Vector source | Overall κ | Best-turn κ |
|---|---|---|---|
| Phase 1 (baseline) | cheerfulness raw-text extracted, L=16, c=±2 | [Phase 1 result] | [Phase 1 result] |
| Phase 2 (this) | cheerfulness chat-template extracted, L=16, c=±2 | +0.100 | 0.400 |

## Interpretation

**Re-extraction on chat-template distribution does NOT rescue per-channel multi-turn.** Both raw-text-extracted (Phase 1) and chat-template-extracted (Phase 2) vectors fail. Extraction-distribution mismatch at the chat-template level (H1-light) is ruled out. Two candidates remain: (a) full multi-turn extraction with paired multi-turn conversations as the source corpus may still rescue (H1-strong); (b) RLHF instruct-tuning persona-prior is dominating regardless of extraction distribution (H2), which is only testable by re-extraction on Qwen2.5-7B-Base. Substrate paper conclusion strengthens: per-channel multi-turn is bounded under additive prefill-fired steering on Qwen-Instruct regardless of single-axis extraction-distribution alignment.

## Provenance

- Wrapped contrastive items: infra/steering-vectors/contrastive-items/e5-cheerfulness-ct.jsonl
- Re-extracted vector: infra/steering-vectors/qwen2.5-7b-instruct/cheerfulness_ct/vector.pt
- Judge report: experiments/d4-fader-intervention/results/w11_b10_ct_extraction/judge/report.md
- High dialogues: experiments/d4-fader-intervention/runs/cheerfulness_ct_high_multiturn/
- Low dialogues:  experiments/d4-fader-intervention/runs/cheerfulness_ct_low_multiturn/
- Run log: experiments/d4-fader-intervention/results/w11_b10_ct_extraction/run.log

## Cost (estimated)

| Item | Modal | Anthropic |
|---|---|---|
| Stage 1: re-extraction (50 items × 2 conds × 1 layer) | ~£1.00 | — |
| Stage 2: 2 × 160 multi-turn generations | ~£7.00 | — |
| Stage 3: 160 paired comparisons (Opus judge) | — | ~£0.50 |
| **Total** | **~£8.00** | **~£0.50** |
