---
type: contrastive items library
status: v0 draft, AI-authored, awaiting Rick review
date: 2026-05-08
---

# Contrastive items — CAA extraction inputs

One JSONL file per channel. Each line is one `ContrastiveItem` (see `infra/steering-vectors/extract_caa.py` schema):

```json
{
  "item_id": "C5-001",
  "context": "When facing a long, multi-step project, I usually",
  "completion_high": "break it into discrete steps and track each one to completion.",
  "completion_low": "feel overwhelmed and put it off until the deadline forces me to start.",
  "notes": "Adapted from IPIP-NEO C5 facet item; tests follow-through behaviour."
}
```

The CAA extraction (`extract_caa.py`) concatenates `context + completion`, runs a forward pass, captures the residual-stream activation at the last-token position, then computes:

```
v_layer = mean(activations_high) − mean(activations_low)
```

That difference vector is the steering vector for the channel.

## Design principles

1. **Differ only on the target trait.** A pair where `high` is also longer than `low`, or has different vocabulary register, contaminates the vector with verbosity / formality directions.
2. **Plausible natural completions.** Not Likert items ("I tend to..." 1-5 scale). Scenario-completion pairs that read as natural language.
3. **Mixed contexts.** Work, decisions, social, personal, professional — so the vector isn't anchored to one domain.
4. **Length-balanced.** High and low completions roughly equal in token count (within ±20%).
5. **No leakage of related traits.** For C5, don't bake in cheerfulness/anxiety/ambition signals.

## Files

| Channel | File | N pairs |
|---|---|---|
| Conscientiousness/Self-Discipline | `c5-self-discipline.jsonl` | 50 |
| DOSPERT-Financial | `dospert-financial.jsonl` | 50 |

## Provenance

v0 drafted by Claude Opus 4.7 on 2026-05-08, anchored against:
- IPIP-NEO-300 C5 facet items (Johnson 2014)
- DOSPERT-30 financial subscale (Blais & Weber 2006)
- ROADMAP §2.2 worked examples

**Awaiting Rick review.** Any pair Rick rejects gets pulled before extraction. Per the project's principle (Rick = the principal), Rick's judgment on what "high-self-discipline Rick output" looks like is the ground truth. v0 is scaffolding; v1 is post-review.

## How to review

Recommended approach: skim each file, mark pairs that read as wrong/misleading/leaky in a comment column or by deletion. Re-run `extract_caa.py --dry-run --contrastive-items <file>` to confirm valid count after edits.

If many pairs need rework, switch to option (b) — author 5 gold-standard pairs per channel; AI expands.
