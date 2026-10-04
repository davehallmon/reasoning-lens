# Evaluations

**Status: no eval rounds run yet.** reasoning-lens has not been tested against any baseline. Until it is, treat it as an experiment.

Nothing in this folder is part of the installed Skill.

**The single authority for method and pass criteria is [`PROTOCOL.md`](PROTOCOL.md)** (v1.0.0, frozen 2026-10-04). This page summarizes it. If they disagree, `PROTOCOL.md` wins.

## What Round 1 asks

> Does the full orchestration add value beyond the same lens cards without it? And where does the Skill's value come from: philosopher names, rewritten cards, or orchestration?

Four conditions, same model, fresh context each time:

| ID | Condition |
|---|---|
| P | Plain Claude |
| N | Names-only: the seven philosophers named, nothing else |
| C | Cards-only: the seven lens cards (Asks, Moves, Notices), no orchestration |
| F | Full reasoning-lens |

The decisive comparison is **F vs. C**, judged blind and pairwise on two pre-registered endpoints: **disagreement calibration** (finds real disagreement, invents none) and **resolution condition** (names what would settle the main uncertainty). Length is measured in code and capped relative to C. The other steps (P → N, N → C) are reported to show where value comes from.

Outcomes are pre-registered: **Strong pass** (eligible for 1.0.0), **Inconclusive** (stay 0.x), or **Design failure** (rethink or simplify). Thresholds and blocking conditions are in `PROTOCOL.md` §7. Round 1 is the gate for 1.0.0, not for 0.x releases.

## Results

| Round | Skill version | Protocol | Generator | Judge | E1 win rate | E2 win rate | Length F÷C | Outcome |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | NOT_RUN |

Every round will be logged here, including rounds that fail or are abandoned.

## Known risks going in

- **Convergence.** One model running seven lenses tends toward seven framings of one answer. The Full-only diagnostics (lens distinctness, disagreement-bullet ratings) are built to show it.
- **Reading time.** Seven sections is long. problem-lens trailed plain Claude on reading time; expect the same pressure here. Length is a hard constraint on a Strong pass.
- **Blinding is partial.** The Full output's format is recognizable. Judges are never told which output is which, and the rubric scores content, not structure.
- **Small corpus.** Fifteen sweep cases. Confidence intervals are reported with every result.

## Files

- [`PROTOCOL.md`](PROTOCOL.md) — method, endpoints, thresholds, decision rules. The authority.
- [`baseline-prompt.md`](baseline-prompt.md) — exact text for each condition.
- [`rubric.md`](rubric.md) — judge instructions and scales.
- [`cases.md`](cases.md) — twenty-three cases and the run log.
- [`check_rules.py`](check_rules.py) — structural checker for Full outputs: `python3 evals/check_rules.py reasoning-lens/examples/*.md`. It does not judge reasoning quality.
- `runs/` — raw outputs, judgments, and results, one folder per round (`PROTOCOL.md` §9.2).
