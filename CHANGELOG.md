# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning. Versions below 1.0.0 are pre-release.

## [0.2.1] — 2026-10-26

Release status: experimental pre-release; Round 1 evaluation pending.

### Changed
- Brand: suite renamed from OCCAMI NOVACULA to Organon, by Ockham. Ockham is the maker's mark; Novacula now names a separate writing suite.
- Updated the README, `index.md`, `docs/DESIGN.md` (§2.1 and §9, spec version), `docs/source-registry.md`, the repo description, and topics to match. The README opens with "Organon: thinking tools by Ockham."
- `docs/source-registry.md`: version 0.2.1. Upstream commit, blob SHAs, and license status re-verified 2026-10-26; unchanged.

### Not changed
- SKILL.md, references/, and all eval files are unchanged. evals/PROTOCOL.md v1.0.0 still applies.

### Fixed
- `docs/DESIGN.md` §6 and `docs/source-registry.md`: both said the paper PDF is not bundled, but the repo keeps a reference copy in `docs/research/` under CC BY 4.0. Both now say so. The upstream prompts are still not bundled.

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
