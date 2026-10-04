# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning. Versions below 1.0.0 are pre-release.

## [0.2.0-dev] — 2026-10-04

First public version. Pre-release: no eval rounds run.

### Changed
- **Sweep, not router.** All seven lenses run on every non-trivial idea, one at a time, instead of routing to one primary and one optional secondary mode. See `docs/decisions/0001-sweep-not-router.md`.
- DIRECT mode became a small gate. It skips the sweep for rewrites, lookups, definitions, code, and one-answer problems, and offers the sweep anyway.
- Profiles rewritten for the sweep (v0.2). Routing sections ("Compatible Secondary Modes", "Selection Boundary", "Diagnostic Signals") replaced with "What It Notices in a Sweep", "Stay Distinct From", and "Known Risk".
- Release gate replaced. Routing accuracy and boundary-routing cases retired. New gate: lens distinctness, real disagreement, and a blind comparison with a named-philosophers prompted baseline. A ChatGPT run is now optional.
- Renamed from "Philosophical Reasoning Router" to reasoning-lens.

### Added
- `reasoning-lens/SKILL.md`: gate, restatement, seven-lens sweep with committed stances, "Where They Disagree", and two ways forward (Run with it, Investigate further).
- `references/`: lens cards, guards against convergence and manufactured disagreement, output format, evidence boundary.
- `examples/`: one sweep and one gate skip, labeled as development runs.
- `evals/`: twenty cases, rubric, baseline prompts, `check_rules.py`, and a CI workflow.
- `docs/`: design spec, decision record, research context, source registry, profiles.
- `NOTICE.md`: attribution, and why upstream prompts are not redistributed.

## [0.1.0-dev] — 2026-10-02

Private development version: the Philosophical Reasoning Router. Never released or evaluated.
