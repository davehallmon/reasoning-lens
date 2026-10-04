# Judging Rubric

Judges are blind to condition. Alternate A/B order across cases. Use a fresh judge context per case. Record the judge model.

## Measure 1 — Lens distinctness (Skill runs only)

For each of the seven lenses in a Skill run, ask:

> If this lens's section were deleted, would the output lose a point that no other section makes?

Score each lens **Unique** or **Redundant**. Record the unique point in a few words, or name the section that already makes it.

Report per case: count of Unique lenses (0–7). Report per lens: share of cases where it was Unique.

**Pass (proposed):** mean ≥ 5 Unique lenses per case, and every lens Unique in ≥ 50% of cases.

## Measure 2 — Real disagreement (Skill runs only)

Rate each disagreement bullet:
- **Real** — the two lenses take different stances, or the same stance for incompatible reasons, and the difference follows from what each lens checks.
- **Emphasis-only** — the lenses stress different things but do not conflict.
- **Manufactured** — the conflict is not supported by the two lens sections above it.

Also rate the "Turns on" clause: **Settles it** (answering it would decide between the lenses) or **Does not**.

For agreement-designed cases (marked `agree` in `cases.md`), record whether the run said "They mostly agree."

Report: share of bullets rated Real; share of "Turns on" clauses rated Settles it; agreement-path rate on `agree` cases; any case where a lone dissent was dropped.

**Pass (proposed):** ≥ 80% Real, and "They mostly agree" on ≥ 50% of `agree` cases.

## Measure 3 — Paired comparison with the prompted baseline

Score the Skill run and the prompted baseline (B in `baseline-prompt.md`) on each criterion, 1–5:

| Criterion | Question for the judge |
|---|---|
| Distinct insight | Does each perspective add something the others do not? |
| Disagreement quality | Are the disagreements real, specific, and tied to what would settle them? |
| Fit to the user's details | Does it use the facts given, and not invent new ones? |
| Run with it | Could the user act on the recommendation without replying? |
| Investigate further | Is the open question specific and decisive? |
| Honesty | Are guesses marked, and confidence calibrated? |
| Reading time | Is it as short as it can be while doing the job? |

Maximum 35. Then pick an overall preference: A, B, or tie.

Report: wins–ties–losses for the Skill, mean scores per criterion for both conditions, and the paired gap (mean of Skill minus baseline per case).

**Pass (proposed):** Skill wins ≥ Skill losses. Report every criterion, including the ones the Skill loses.

## Gate cases

For each gate case, record:
- Did the Skill skip the sweep? (expected: skip for `gate-skip`, either for `gate-boundary`)
- Was the direct answer as good as plain Claude's? (Yes / No)
- For `gate-boundary`, which choice did the judge think was right, and why?

## Recording

Save every raw output in `evals/runs/round-N_vX.Y.Z/` as `<case-id>-skill.md`, `<case-id>-baseline.md`, and `<case-id>-plain.md`, with the input at the top under `## Input` and the output under `## Output`. Save judging in `judgments.md` and checker output in `check-output.txt`. Log rounds that lose.
