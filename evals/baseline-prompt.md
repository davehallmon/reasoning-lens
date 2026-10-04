# Baselines

Every case runs under three conditions. Use the same model, the same user message text, and a fresh context for each.

## A. Skill

The user message as written in `cases.md`, with the reasoning-lens Skill installed. The agent sees only `reasoning-lens/SKILL.md` and `reasoning-lens/references/`, never `examples/` or `evals/`.

## B. Prompted baseline (primary comparison)

No Skill. The case's user message, followed by this text:

```
Look at this through the reasoning of seven philosophers: Socrates, Plato,
Aristotle, Descartes, Hume, Kant, and Hegel. Take them one at a time. Then
show where they disagree, and tell me what to do.
```

This is the cheap alternative a user could type without installing anything. If the Skill cannot beat it, the profiles, stances, and guards are not earning their place.

For gate cases, use the user message alone, with no added text. The Skill's gate is compared against plain Claude doing the task.

## C. Plain Claude (context only)

No Skill, the case's user message alone. Reported for context. Not part of the pass/fail gate.
