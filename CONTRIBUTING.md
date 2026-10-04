# Contributing

Thanks for your interest. This project welcomes contributions.

## Ways To Contribute

- Report a bug.
- Share a run where the lenses converged, or invented a disagreement.
- Propose a change to a lens card.
- Add an eval case.
- Fix a typo.

## How To Contribute

1. Open an issue first. Describe the change and why it helps.
2. Fork the repo.
3. Make the change on a branch.
4. Open a pull request. Link the issue.
5. Wait for review.

## Style

- Use active voice.
- Use short words.
- Cut filler.
- No clichés.
- Keep `reasoning-lens/SKILL.md` under 500 lines.
- Put detail in `reasoning-lens/references/`.

## Changing a Lens

The seven lenses are fixed to the seven prompts in Harb et al. (2026). Changes must stay faithful to the source.

1. Change the profile in `docs/profiles/` first. Check it against the upstream prompt at the commit in `docs/source-registry.md`.
2. Then change the card in `reasoning-lens/references/lenses.md` to match.
3. Do not copy text from the upstream prompts. They carry no license. Restate the moves in your own words.

## New Lenses

Not for now. A philosophy-of-science set (Bacon, Peirce, Popper, Kuhn, Lakatos) was considered and deferred; see `docs/DESIGN.md` §8. Open an issue with eval evidence of a gap the seven do not cover.

## Testing

Run `python3 evals/check_rules.py reasoning-lens/examples/*.md` before opening a pull request. Changes to Skill behavior should come with a new round in `evals/`.

## Claims

Do not describe anything about the sweep as research-validated. See `docs/research-context.md`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.
