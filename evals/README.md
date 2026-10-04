# Evaluations

**Status: no eval rounds run yet.** reasoning-lens has not been tested against any baseline. Until it is, treat it as an experiment.

Nothing in this folder is part of the installed Skill.

## What the release gate measures

The sweep makes one promise: seven lenses that see different things, and an honest account of where they disagree. The gate tests that promise directly.

1. **Lens distinctness.** Delete one lens's section. Does the output lose a point no other lens makes?
2. **Real disagreement.** Is each listed disagreement real, or only a difference in emphasis, or made up? Does the Skill say "They mostly agree" when they do?
3. **Prompted baseline.** Does the Skill beat Claude simply asked to look at the idea through the same seven philosophers? This is the cheap alternative any user could type. Plain Claude is also run, for context.

Details: `rubric.md`. Baseline text: `baseline-prompt.md`. Cases: `cases.md`. Thresholds and the full gate: `docs/DESIGN.md` §7.

## Method

- **Skill runs:** fresh agents see only `reasoning-lens/SKILL.md` and `references/`, never `examples/` or `evals/`.
- **Baselines:** same model, same user message, fresh context. See `baseline-prompt.md`.
- **Judging:** one blind judge per case, A/B order alternated. Record the judge model.
- **Rule checks:** `check_rules.py` tests structure only. It does not judge whether the reasoning is good.

## Results

| Round | Version | Cases | Distinct lenses (mean of 7) | Real disagreements | Skill vs. prompted baseline (W–T–L) | Paired gap (of 35) |
|---|---|---|---|---|---|---|
| — | — | 0 | — | — | — | — |

Every round will be logged here, including rounds that lose.

## Known risks going in

- **Convergence.** One model running seven lenses tends toward seven framings of one answer. Measure 2 is built to catch it.
- **Reading time.** Seven sections is long. problem-lens trailed plain Claude on reading time; expect the same pressure here.
- **Same model family.** Generator, baselines, and judges will likely be the same model family.

## Files

- `cases.md` — twenty cases and the run log.
- `rubric.md` — how each measure is judged.
- `baseline-prompt.md` — the three conditions.
- `check_rules.py` — run `python3 evals/check_rules.py reasoning-lens/examples/*.md`.
- `runs/` — raw outputs and judgments, one folder per round.
