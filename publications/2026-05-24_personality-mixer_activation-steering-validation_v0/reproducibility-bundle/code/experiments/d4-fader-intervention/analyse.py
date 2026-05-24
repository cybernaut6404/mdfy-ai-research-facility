"""
analyse.py — turn D4 harness generations into directional-accuracy numbers.

Reads generation records from runs/<channel>/, pairs HIGH and LOW conditions for
each (probe, coefficient), submits each pair to:
  1. LLM-as-judge (Claude Opus 4.7) — primary scaling layer per ROADMAP §6.3
  2. Lexical detector — channel-specific objective measure

Produces:
  experiments/d4-fader-intervention/results/<channel>/judgements.jsonl
  experiments/d4-fader-intervention/results/<channel>/report.md
  experiments/d4-fader-intervention/results/<channel>/results.json

USAGE:
  python3 experiments/d4-fader-intervention/analyse.py \\
      --channel conscientiousness_self_discipline \\
      --runs experiments/d4-fader-intervention/runs/conscientiousness_self_discipline \\
      --out experiments/d4-fader-intervention/results/conscientiousness_self_discipline

Requires ANTHROPIC_API_KEY in environment.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict, field
from pathlib import Path

import anthropic


REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Channel-specific judge prompts. The judge is asked to identify which of two
# blinded responses ("Response A" / "Response B") shows more <trait>. Position
# is randomised per pair; we resolve back to high/low after.

JUDGE_PROMPTS = {
    "conscientiousness_self_discipline": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for "
            "behavioural conscientiousness — specifically self-discipline, follow-through, "
            "and methodical step-tracking. Higher conscientiousness shows: explicit step-by-step "
            "structure, follow-through to all parts of the task (not just the start), explicit "
            "self-correction or caveats when appropriate, and lower abandonment rate on multi-step "
            "tasks. Higher conscientiousness does NOT mean longer or more verbose. Match content "
            "rigour, not length."
        ),
        "question": (
            "Which response shows more methodical follow-through, step-tracking discipline, "
            "and completion of all parts of the task? Answer with exactly one of: A, B, or TIE."
        ),
    },
    "dospert_financial": {
        "system": (
            "You are a blind rater scoring two responses to the same financial-decision prompt. "
            "Score for risk-tolerance on the FINANCIAL dimension — willingness to recommend "
            "options with higher expected variance, willingness to deploy capital, willingness "
            "to take leverage or concentration. Higher risk-tolerance does NOT mean reckless or "
            "unethical — it means accepting variance for expected return. NOT about voice or style — "
            "evaluate the recommended action's expected variance."
        ),
        "question": (
            "Which response shows more financial risk-tolerance — willingness to recommend "
            "the higher-variance, higher-expected-return option? Answer with exactly one of: A, B, or TIE."
        ),
    },
    "cheerfulness": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for AFFECTIVE warmth "
            "and cheerfulness in the response itself. Higher cheerfulness shows: warm openers and "
            "closers, exclamation marks where appropriate, emoji or affect-positive descriptors, "
            "reciprocated warmth in social exchanges, language that exceeds informational need with "
            "felt enthusiasm. Lower cheerfulness shows: neutral courteous tone, no exclamations, "
            "informational density without affective garnish, no emoji, brief professional closers. "
            "This is about TONE not CONTENT — both responses may convey the same factual answer but "
            "differ in warmth. Match content; rate affect."
        ),
        "question": (
            "Which response carries more affective warmth and cheerfulness in its tone — warmer "
            "openers, more enthusiasm markers, more felt positivity? Answer with exactly one of: "
            "A, B, or TIE."
        ),
    },
    "sociability": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for SOCIABILITY — "
            "preference for being with other people. Higher sociability shows: recommendations "
            "involving other people, group activities, gatherings, social proximity, framing "
            "problems socially ('who could you see…', 'invite people…', 'team up'), treating other "
            "people as the substrate of good situations. Lower sociability shows: recommendations "
            "for solo activities, quiet time, focus, one-on-one over groups, treating solitude as "
            "valuable, framing problems individually ('what could you do alone', 'use the time to "
            "think'). This is NOT about warmth (tone), NOT about social skill, NOT about anxiety. "
            "It is about PREFERENCE for social density in the chosen action. Match content "
            "competence; rate the social vs solo orientation."
        ),
        "question": (
            "Which response shows more preference for SOCIAL action — being with people, "
            "gatherings, group context, treating others as the substrate of good options? "
            "Answer with exactly one of: A, B, or TIE."
        ),
    },
    "dospert_recreational": {
        "system": (
            "You are a blind rater scoring two responses to the same recreational-decision prompt. "
            "Score for risk-tolerance on the RECREATIONAL/PHYSICAL dimension — willingness to "
            "recommend body-on-the-line adventure activities, willingness to engage with marginal "
            "conditions, willingness to step up in skill, willingness to choose technical/exposed "
            "options over easy/safe ones. Higher recreational risk-tolerance does NOT mean reckless "
            "or careless — it means engaging with the activity rather than auto-vetoing. NOT about "
            "voice or style — evaluate the recommended action's physical-risk orientation. This is "
            "specifically PHYSICAL recreational risk, NOT financial / ethical / social risk."
        ),
        "question": (
            "Which response shows more recreational-risk-tolerance — willingness to recommend the "
            "more adventurous, physically demanding, exposed-conditions option? "
            "Answer with exactly one of: A, B, or TIE."
        ),
    },
    "achievement_striving": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for ACHIEVEMENT-STRIVING — "
            "drive to raise the bar, set ambitious goals, push beyond adequate. Higher achievement-"
            "striving shows: recommendations to stretch / raise targets / pursue world-class / "
            "leapfrog / not settle for good-enough; framing of growth via ambition; treating routine "
            "wins as signal that the bar is too low. Lower achievement-striving shows: recommendations "
            "for sustainable / consistent / steady delivery; framing around long-term compounding; "
            "treating consistency over reach as the primary metric. This is NOT about work effort or "
            "persistence (= Self-Discipline, a different facet). It is about the *level* of ambition "
            "and the *bar* set relative to baseline. Match content quality; rate ambition-level."
        ),
        "question": (
            "Which response shows more achievement-striving — willingness to push for the more "
            "ambitious, harder, higher-bar option? Answer with exactly one of: A, B, or TIE."
        ),
    },
    "self_direction": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for SELF-DIRECTION — "
            "value placed on personal authority, autonomy, and direction of one's own work/life. "
            "Higher self-direction shows: recommendations to build/own/decide independently; treating "
            "permission-seeking and structured paths as costs; valuing autonomy over collective "
            "alignment; declining tradition/conformity for its own sake; favouring solo over joining. "
            "Lower self-direction shows: recommendations to engage with structure/process/community; "
            "valuing collective alignment; treating tradition as legitimate carrier of information; "
            "favouring leverage through teams/structure over solo control. This is about LOCUS OF "
            "AUTHORITY — self vs system. NOT about specific recommendations being right or wrong; "
            "rate which response treats autonomy as the dominant value to optimise for."
        ),
        "question": (
            "Which response treats SELF-DIRECTION (autonomy, personal authority, control of own "
            "work) as the dominant value to optimise for? Answer with exactly one of: A, B, or TIE."
        ),
    },
    "cautiousness": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for CAUTIOUSNESS — "
            "preference for deliberation over decisiveness in commitment under uncertainty. Higher "
            "cautiousness shows: recommendations to slow down, sleep on it, ask for more time, do "
            "due diligence, verify before committing, prefer reversible options, push back on "
            "deadline pressure. Lower cautiousness shows: recommendations to act decisively, trust "
            "the read, commit on best signal, trust intuition, treat speed as asset, seize "
            "opportunities. This is NOT about anxiety or fear (= Neuroticism). It is about "
            "decision tempo and depth-of-deliberation. Match content quality; rate the tempo "
            "preference."
        ),
        "question": (
            "Which response shows more cautiousness — preference for deliberation, verification, "
            "and slower commitment over decisive action? Answer with exactly one of: A, B, or TIE."
        ),
    },
    "stimulation": {
        "system": (
            "You are a blind rater scoring two responses to the same prompt for STIMULATION-"
            "SEEKING — preference for novelty, change, variety over familiarity, depth, "
            "consistency. Higher stimulation shows: recommendations to try new things, change "
            "shape, embrace novelty, pursue variety, treat routine as cost, pursue breadth, "
            "engage new fields/places/experiences. Lower stimulation shows: recommendations to "
            "deepen current pursuits, embrace familiarity, treat consistency as platform, prefer "
            "depth, value mastery, treat novelty as costly. This is NOT about social energy "
            "(= extraversion) or risk-tolerance (= DOSPERT). It is about NOVELTY-SEEKING. Match "
            "content quality; rate novelty-vs-stability orientation."
        ),
        "question": (
            "Which response shows more stimulation-seeking — preference for novelty, new "
            "experiences, variety over familiarity and depth? Answer with exactly one of: "
            "A, B, or TIE."
        ),
    },
}


# Channel-specific lexical detectors. Counts trait-relevant tokens per 100 tokens
# of output. Net signal = high − low.

LEXICAL_DETECTORS = {
    "conscientiousness_self_discipline": {
        "high_markers": [
            r"\b(first|second|third|fourth|fifth|sixth|seventh)\b",
            r"\b(step\s+\d+|\d+\.\s)",
            r"\b(next|then|finally|lastly|in addition|moreover|furthermore)\b",
            r"\b(let me (verify|check|reconsider|review)|wait|actually|on second thought)\b",
            r"\b(complete[ds]?|cover(ed|ing)? all|every (one|step)|each (step|item|case))\b",
        ],
        "low_markers": [
            r"\b(probably|maybe|might|sort of|kind of|roughly|approximately)\b",
            r"\b(left as an exercise|you can take it from here|and so on|etc\.)\b",
            r"\b(I'll skip|skipping|won't go into|won't cover|moving on)\b",
        ],
    },
    "dospert_financial": {
        "high_markers": [
            r"\b(invest|deploy|allocate|leverage|growth|upside|aggressive|concentrate|seize|capture)\b",
            r"\b(equit(y|ies)|stocks?|venture|startup|asymmetric|conviction)\b",
            r"\b(take the (bet|position|risk)|go for it|commit|push forward)\b",
        ],
        "low_markers": [
            r"\b(preserve|conservative|safe|liquidity|cash|diversif(y|ication)|hedge)\b",
            r"\b(bond|annuity|index fund|dollar.cost.averag(e|ing))\b",
            r"\b(avoid|skip|decline|wait|too risky|reckless|gambl(e|ing))\b",
        ],
    },
    "cheerfulness": {
        # v1 marker set — broader than v0. v0 produced negative lex-Δ on a passing
        # channel (per cheerfulness-pass-2026-05-06.md), indicating the surface
        # markers Qwen-2.5-7B uses for warmth are not just exclamations and
        # affect-adjectives. v1 adds warm verbs, warm-stance phrases, and
        # second-person engagement signals.
        "high_markers": [
            # Affect-positive descriptors
            r"\b(amazing|wonderful|fantastic|brilliant|lovely|delight(ed|ful)?|thrilled|excited|happy|glad|pleased|love(d|ly)?|warm(ly|th)?|joy(ful|ous)?|beautiful|incredible|awesome|great)\b",
            # Exclamation marks (affect signal in writing)
            r"!",
            # Greetings and warm openers
            r"\b(hey|hi there|hiya|good (morning|afternoon|evening)|so good|so glad|so nice|congrats|congratulations|woohoo|yay)\b",
            # Warm verbs
            r"\b(love (it|that|this)|enjoy|appreciate|adore|cherish|celebrate)\b",
            # Affective qualifiers exceeding informational need
            r"\b(absolutely|totally|completely|honestly|truly|genuinely|really really|so very|definitely)\b",
            # Second-person engagement / felt warmth toward reader
            r"\b(thank you so much|so happy for you|great to hear|good for you|happy to|delighted to)\b",
            # Emoji proxy markers
            r"[😊🎉❤️💜💕🌟✨🎊🥳]",
        ],
        "low_markers": [
            # Neutral / functional / sober tone markers
            r"\b(noted|acknowledged|received|understood|confirmed|fyi|will do)\b",
            r"\b(ok\.|alright\.|fine\.)",
            # Hedged or distancing affect
            r"\b(briefly|in short|to be clear|professionally|formally)\b",
            # Functional courtesy without warmth
            r"\b(regards|sincerely|best,|thanks\.|thank you\.)\b",
            # Bare-acknowledgement closers
            r"\b(let me know|happy to discuss|please advise)\b",
        ],
    },
    "sociability": {
        "high_markers": [
            # Group / together language
            r"\b(together|group|gathering|crowd|party|team|friends|people|everyone|company)\b",
            # Meeting / inviting verbs
            r"\b(meet up|invite|host|gather|join|connect|catch up|hang out|drop by|stop by)\b",
            # Social density references
            r"\b(dinner with|drinks with|brunch|gathering|reunion|community|social|colleagues)\b",
            # Inclusive pronouns
            r"\b(we|us|our|let's|with others|with someone|the group)\b",
        ],
        "low_markers": [
            # Solo / quiet preference
            r"\b(alone|solitude|quiet|by myself|on my own|privacy|undisturbed|peace and quiet|solo)\b",
            # Focus / individual work
            r"\b(focus|deep work|head down|uninterrupted|concentrate|reflect|introspect)\b",
            # Anti-social actions
            r"\b(decline|skip|pass on|stay in|stay home|avoid|opt out|excuse myself)\b",
            # Distance-keeping
            r"\b(myself|just me|on my own time|in my own space)\b",
        ],
    },
    "dospert_recreational": {
        "high_markers": [
            # Engagement / go-for-it markers
            r"\b(go for it|send it|push (through|on)|engage|take it on|commit|dive in)\b",
            # Adventure-sport markers
            r"\b(adventure|technical|exposed|demanding|challenging|push your limits|step up)\b",
            # Conditional-yes markers
            r"\b(if conditions|if you're trained|if the kit|with proper|under instruction)\b",
            # Risk-acceptance language
            r"\b(measured risk|controlled risk|managed risk|calculated risk|worth it|the experience)\b",
        ],
        "low_markers": [
            # Risk-aversion markers
            r"\b(too risky|consequence|bad place|not worth|skip it|defer|postpone|wait|hold off)\b",
            # Safer-option preference
            r"\b(safer option|easier route|less exposed|more controlled|gentler|tame|conservative choice)\b",
            # Auto-veto language
            r"\b(don't|can't recommend|wouldn't|avoid|stay away|not the right|not ready)\b",
            # Excessive caution markers
            r"\b(consult|check with|professional supervision|qualified guide required|absolutely necessary)\b",
        ],
    },
    "achievement_striving": {
        "high_markers": [
            # Stretch / push markers
            r"\b(stretch|push|raise the bar|aggressive|leapfrog|world-class|excellence|ambitious|exceed|surpass)\b",
            # Ambition framing
            r"\b(stretch goal|bigger|harder|more|higher target|next level|push the limit|ceiling|frontier)\b",
            # Anti-adequacy markers
            r"\b(not (good enough|adequate|enough)|raise the standard|never settle|not enough|do better)\b",
            # Aggressive verbs
            r"\b(scale up|aggressively|attack|capture|dominate|win|seize)\b",
        ],
        "low_markers": [
            # Stability / sustainability markers
            r"\b(sustainable|consistent|steady|reliable|solid|stable|measured|moderate)\b",
            # Adequacy markers
            r"\b(good enough|fit for purpose|adequate|suffices|sustainable pace|reasonable|sensible)\b",
            # Risk-aversion in goal-setting
            r"\b(realistic|achievable|conservative target|protect|consolidate|don't over-extend)\b",
            # Slow-and-steady markers
            r"\b(compound|over time|long-run|patient|consistent delivery|steady progress)\b",
        ],
    },
    "self_direction": {
        "high_markers": [
            r"\b(autonomy|autonomous|own decisions|self-direct|independent|independence|on my own terms)\b",
            r"\b(build (it|your own|my own|from scratch)|start your own|launch your own|own it)\b",
            r"\b(without asking|don't ask|skip permission|workaround|work around|find a way)\b",
            r"\b(decline the (rule|policy|process|programme)|opt out|carve out|operate (outside|alone))\b",
            r"\b(freedom|control of (my|your) own|direct (my|your) own|run it (yourself|your way))\b",
        ],
        "low_markers": [
            r"\b(process|policy|framework|procedure|standard operating|established (process|approach|method))\b",
            r"\b(align(ment)?|consensus|collective|team agreement|company standard|industry standard)\b",
            r"\b(seek approval|get approval|run it past|consult with|check with|defer to)\b",
            r"\b(tradition|established way|how it's done|reasons for|legitimate carrier|pillars)\b",
            r"\b(work within|operate within|engage with the (system|process|framework))\b",
        ],
    },
    "cautiousness": {
        "high_markers": [
            r"\b(slow down|wait|sleep on it|take (your|my) time|think it through|consider carefully)\b",
            r"\b(due diligence|verify|investigate|check|stress.test|double.check|read carefully)\b",
            r"\b(more time|extension|push back|delay|hold off|defer the decision)\b",
            r"\b(reversible|optionality|short(er)? commitment|smaller bet|trial period|pilot)\b",
            r"\b(consequences|second.order|stress.test|edge case|what could go wrong)\b",
        ],
        "low_markers": [
            r"\b(act now|move (now|quickly|fast)|decide|commit|seize|grab|jump on)\b",
            r"\b(trust (your|my) (gut|instinct|read)|go with it|just do it|don't overthink)\b",
            r"\b(decisive|fast|quickly|momentum|tempo|seize the moment)\b",
            r"\b(opportunity (won't|doesn't) wait|window is closing|time is short)\b",
            r"\b(too much (analysis|deliberation)|paralysis|over.thinking|over.engineer)\b",
        ],
    },
    "stimulation": {
        "high_markers": [
            r"\b(new|novel|different|fresh|unfamiliar|never (done|tried)|haven't (done|tried))\b",
            r"\b(discover|explore|try|adventure|change|switch|pivot|shake (it|things) up)\b",
            r"\b(variety|diverse|breadth|across (many|different))\b",
            r"\b(novelty|excitement|stimulating|interesting|fascinating|curious)\b",
            r"\b(out of comfort zone|push the comfort|new territory|uncharted)\b",
        ],
        "low_markers": [
            r"\b(familiar|routine|established|known|consistent|stable|predictable|tested)\b",
            r"\b(deepen|deeper|focus|mastery|depth|continuity|long.run|compound)\b",
            r"\b(stick with|stay with|continue|keep doing|maintain|sustain)\b",
            r"\b(comfort zone|comfortable|stable platform|reliable|proven)\b",
            r"\b(don't change|don't switch|trust (the|your) (process|routine))\b",
        ],
    },
}


@dataclass
class Judgement:
    probe_id: str
    coefficient: float
    high_pos: str  # "A" or "B" — which slot HIGH was placed in
    judge_answer: str  # raw answer "A" / "B" / "TIE"
    judge_resolved: str  # "high_wins" / "low_wins" / "tie"
    high_lex_score: float
    low_lex_score: float
    high_tokens: int
    low_tokens: int


def load_records(runs_dir: Path) -> list[dict]:
    records = []
    for f in sorted(runs_dir.glob("*.json")):
        with f.open() as fp:
            records.append(json.load(fp))
    return records


def pair_records(records: list[dict]) -> dict[tuple[str, float], dict]:
    """Returns {(probe_id, coef_abs): {"high": rec, "low": rec}}.
    coef_abs is the absolute value (sign was applied in harness via condition)."""
    pairs: dict[tuple[str, float], dict] = defaultdict(dict)
    for r in records:
        coef_abs = abs(r["coefficient"])
        key = (r["probe_id"], coef_abs)
        pairs[key][r["condition"]] = r
    return dict(pairs)


def lexical_score(text: str, channel: str) -> float:
    """Returns net markers per 100 tokens. Positive = high-trait-leaning."""
    detectors = LEXICAL_DETECTORS.get(channel)
    if not detectors:
        return 0.0
    high_count = sum(len(re.findall(p, text, re.IGNORECASE)) for p in detectors["high_markers"])
    low_count = sum(len(re.findall(p, text, re.IGNORECASE)) for p in detectors["low_markers"])
    n_tokens = max(1, len(text.split()))  # rough proxy
    return (high_count - low_count) * 100.0 / n_tokens


def judge_pair(client: anthropic.Anthropic, channel: str, prompt: str, resp_a: str, resp_b: str) -> str:
    """Returns 'A' / 'B' / 'TIE' (raw judge output)."""
    spec = JUDGE_PROMPTS[channel]
    user_msg = (
        f"PROMPT (given to both responders):\n{prompt}\n\n"
        f"=== Response A ===\n{resp_a}\n\n"
        f"=== Response B ===\n{resp_b}\n\n"
        f"{spec['question']}"
    )
    resp = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=10,
        system=spec["system"],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = resp.content[0].text.strip().upper()
    # Permissive parsing — judge sometimes answers "A." or "Response A".
    if "TIE" in text:
        return "TIE"
    if "A" in text and "B" not in text:
        return "A"
    if "B" in text and "A" not in text:
        return "B"
    if text.startswith("A"):
        return "A"
    if text.startswith("B"):
        return "B"
    return "TIE"  # default to tie on unparseable


def analyse_channel(channel: str, runs_dir: Path, out_dir: Path, seed: int = 42) -> dict:
    if channel not in JUDGE_PROMPTS:
        raise ValueError(f"no judge prompt defined for channel '{channel}'")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY not set in environment")

    out_dir.mkdir(parents=True, exist_ok=True)
    records = load_records(runs_dir)
    if not records:
        raise ValueError(f"no records in {runs_dir}")
    pairs = pair_records(records)
    print(f"loaded {len(records)} records → {len(pairs)} pairs", file=sys.stderr)

    rng = random.Random(seed)
    client = anthropic.Anthropic()

    judgements: list[Judgement] = []
    incomplete_pairs = 0
    for i, ((probe_id, coef), pair) in enumerate(sorted(pairs.items())):
        if "high" not in pair or "low" not in pair:
            incomplete_pairs += 1
            continue
        high_rec, low_rec = pair["high"], pair["low"]

        high_lex = lexical_score(high_rec["output"], channel)
        low_lex = lexical_score(low_rec["output"], channel)

        # Position-randomise.
        if rng.random() < 0.5:
            slot_a, slot_b = "high", "low"
            high_pos = "A"
        else:
            slot_a, slot_b = "low", "high"
            high_pos = "B"

        try:
            answer = judge_pair(
                client, channel, high_rec["prompt"], pair[slot_a]["output"], pair[slot_b]["output"],
            )
        except Exception as e:
            print(f"  judge call failed for {probe_id} c={coef}: {e}", file=sys.stderr)
            answer = "TIE"

        if answer == "TIE":
            resolved = "tie"
        elif answer == high_pos:
            resolved = "high_wins"
        else:
            resolved = "low_wins"

        judgements.append(Judgement(
            probe_id=probe_id, coefficient=coef, high_pos=high_pos,
            judge_answer=answer, judge_resolved=resolved,
            high_lex_score=high_lex, low_lex_score=low_lex,
            high_tokens=high_rec.get("output_tokens", 0),
            low_tokens=low_rec.get("output_tokens", 0),
        ))

        if (i + 1) % 20 == 0:
            print(f"  judged {i+1}/{len(pairs)} pairs", file=sys.stderr)

    # Persist judgements.
    with (out_dir / "judgements.jsonl").open("w") as f:
        for j in judgements:
            f.write(json.dumps(asdict(j)) + "\n")

    # Compute aggregate stats.
    by_coef: dict[float, dict] = defaultdict(lambda: {"high_wins": 0, "low_wins": 0, "ties": 0})
    overall = {"high_wins": 0, "low_wins": 0, "ties": 0}
    lex_diffs_by_coef: dict[float, list] = defaultdict(list)

    for j in judgements:
        by_coef[j.coefficient][f"{j.judge_resolved}s" if j.judge_resolved == "tie" else j.judge_resolved] += 1
        overall[f"{j.judge_resolved}s" if j.judge_resolved == "tie" else j.judge_resolved] += 1
        lex_diffs_by_coef[j.coefficient].append(j.high_lex_score - j.low_lex_score)

    def directional_accuracy(stats: dict) -> float:
        """Fraction of non-tie judgements where HIGH wins."""
        n = stats["high_wins"] + stats["low_wins"]
        return stats["high_wins"] / n if n > 0 else 0.0

    def total_with_ties(stats: dict) -> int:
        return stats["high_wins"] + stats["low_wins"] + stats["ties"]

    results = {
        "channel": channel,
        "n_pairs": len(judgements),
        "n_pairs_incomplete": incomplete_pairs,
        "judge_model": "claude-opus-4-7",
        "seed": seed,
        "overall": {
            "high_wins": overall["high_wins"],
            "low_wins": overall["low_wins"],
            "ties": overall["ties"],
            "directional_accuracy_excluding_ties": directional_accuracy(overall),
            "high_win_rate_including_ties": overall["high_wins"] / total_with_ties(overall) if total_with_ties(overall) else 0.0,
        },
        "by_coefficient": {
            str(c): {
                "high_wins": s["high_wins"],
                "low_wins": s["low_wins"],
                "ties": s["ties"],
                "directional_accuracy_excluding_ties": directional_accuracy(s),
                "mean_lex_diff_high_minus_low": (sum(lex_diffs_by_coef[c]) / len(lex_diffs_by_coef[c])) if lex_diffs_by_coef[c] else 0.0,
            } for c, s in sorted(by_coef.items())
        },
    }

    (out_dir / "results.json").write_text(json.dumps(results, indent=2))

    # Markdown report.
    overall_da = results["overall"]["directional_accuracy_excluding_ties"]
    pass_threshold = 0.60
    iterate_lower = 0.55
    if overall_da >= pass_threshold:
        verdict = f"**PASS** — directional accuracy {overall_da:.2f} ≥ {pass_threshold}. Channel works."
    elif overall_da >= iterate_lower:
        verdict = f"**ITERATE** — directional accuracy {overall_da:.2f} in 0.55–0.59 range. Demote to exploratory; re-extract with different layer / contrastive items."
    else:
        verdict = f"**KILL** — directional accuracy {overall_da:.2f} < {iterate_lower}. Channel does not work in current substrate config."

    md = [
        f"# D4 result — {channel}",
        f"",
        f"_Generated by experiments/d4-fader-intervention/analyse.py_",
        f"",
        f"## Headline",
        f"",
        verdict,
        f"",
        f"## Aggregate",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Pairs judged | {results['n_pairs']} |",
        f"| HIGH wins | {results['overall']['high_wins']} |",
        f"| LOW wins | {results['overall']['low_wins']} |",
        f"| Ties | {results['overall']['ties']} |",
        f"| Directional accuracy (excl. ties) | **{overall_da:.3f}** |",
        f"| High-win rate (incl. ties) | {results['overall']['high_win_rate_including_ties']:.3f} |",
        f"",
        f"## Per-coefficient breakdown",
        f"",
        f"| Coefficient | HIGH wins | LOW wins | Ties | Directional accuracy | Lex Δ (high − low) |",
        f"|---|---|---|---|---|---|",
    ]
    for c, s in results["by_coefficient"].items():
        md.append(
            f"| {c} | {s['high_wins']} | {s['low_wins']} | {s['ties']} | **{s['directional_accuracy_excluding_ties']:.3f}** | {s['mean_lex_diff_high_minus_low']:+.3f} |"
        )

    md.extend([
        f"",
        f"## Pre-reg context",
        f"- **Pass threshold:** directional accuracy ≥ 0.60",
        f"- **Iterate band:** 0.55 ≤ accuracy < 0.60 (re-extract / layer sweep)",
        f"- **Kill threshold:** accuracy < 0.55 (channel demoted or scrapped)",
        f"- Per-coefficient lexical Δ: positive = HIGH outputs use more high-trait markers than LOW; close to 0 = pure-style signal absent (good, means semantic effect not pure verbosity)",
        f"",
        f"## Provenance",
        f"- Judge: claude-opus-4-7 (LLM-as-judge, blind, position-randomised)",
        f"- Substrate: Qwen-2.5-7B-Instruct, layer 16, fp16 on Modal A100-40GB",
        f"- Steering vectors extracted via CAA (Rimsky 2024) from 50 contrastive items",
        f"- Probes: experiments/d4-fader-intervention/probes/{channel.replace('_', '-')}.json",
        f"",
    ])

    (out_dir / "report.md").write_text("\n".join(md))

    print(f"\n✓ wrote results to {out_dir}", file=sys.stderr)
    print(f"  overall directional accuracy: {overall_da:.3f}", file=sys.stderr)
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description="Analyse D4 generations: LLM-as-judge + lexical + report.")
    ap.add_argument("--channel", required=True)
    ap.add_argument("--runs", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    analyse_channel(args.channel, args.runs, args.out, seed=args.seed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
