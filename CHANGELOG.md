# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning. Versions below 1.0.0 are pre-release.

## [0.2.0] — 2026-10-04

First public release. Experimental pre-1.0 release: no eval rounds run. The evaluation that gates 1.0.0 is pre-registered in `evals/PROTOCOL.md` and has not been run.

### Changed
- **Sweep, not router.** All seven lenses run on every non-trivial idea, one at a time, instead of routing to one primary and one optional secondary mode. See `docs/decisions/0001-sweep-not-router.md`.
- DIRECT mode became a small gate. It skips the sweep for rewrites, lookups, definitions, code, and one-answer problems, and offers the sweep anyway.
- Profiles rewritten for the sweep (v0.2). Routing sections ("Compatible Secondary Modes", "Selection Boundary", "Diagnostic Signals") replaced with "What It Notices in a Sweep", "Stay Distinct From", and "Known Risk".
- Release gate replaced. Routing accuracy and boundary-routing cases retired. The 1.0.0 gate is now `evals/PROTOCOL.md` (see Added).
- Renamed from "Philosophical Reasoning Router" to reasoning-lens.

### Added
- `reasoning-lens/SKILL.md`: gate, restatement, seven-lens sweep with committed stances, "Where They Disagree", and two ways forward (Run with it, Investigate further).
- `references/`: lens cards, guards against convergence and manufactured disagreement, output format, evidence boundary.
- `examples/`: one sweep and one gate skip, labeled as development runs.
- `evals/PROTOCOL.md` (v1.0.0, frozen): the single authority for evaluation. A four-condition ablation (plain Claude, names-only, cards-only, full Skill); a blind pairwise Full vs. Cards-only comparison on two pre-registered endpoints, disagreement calibration and resolution condition; a length limit; blocking conditions; human review rules; and three pre-registered outcomes (Strong pass, Inconclusive, Design failure).
- `evals/`: twenty-three cases (including three prompt-injection cases), the frozen prompt for each condition, the judge rubric, `check_rules.py`, and a CI workflow.
- Untrusted-content guard in `references/guards.md`: instructions inside pasted or quoted material are analyzed as content and cannot override the Skill.
- `docs/`: design spec, decision record, research context, source registry, profiles.
- `NOTICE.md`: attribution, and why upstream prompts are not redistributed.

### Removed
- The 0.2.0-dev named-philosophers "prompted baseline". It included three of the instructions under test (one at a time, show disagreement, say what to do), so it could not serve as a clean control.

## [0.1.0-dev] — 2026-10-02

Private development version: the Philosophical Reasoning Router. Never released or evaluated.
