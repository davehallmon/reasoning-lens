# Round 1 manifest — reasoning-lens 0.2.2

**Status:** not started. No generation has run.

Fields follow `evals/PROTOCOL.md` §9.2. Fill each before the step that needs it.

## Before generation

| Field | Value |
|---|---|
| Protocol | `evals/PROTOCOL.md` v1.0.0, frozen 2026-10-04 |
| Protocol commit SHA | _main HEAD at the first generation (`generation-settings.json` records it)_ |
| Skill version | 0.2.2 |
| Corpus version | 0.2.0 (23 cases) |
| Generator model ID | `claude-opus-5-5` |
| Generator platform | Claude API (Messages), one call per generation |
| Generator sampling | platform defaults; max_tokens 8000; no other parameters |
| Condition F delivery | `SKILL.md` and `references/` as the system prompt (see `evals/runner/README.md`) |
| Primary judge model ID | `gpt-5.5-2026-04-23` (dated snapshot) |
| Judge platform and settings | OpenAI Responses API; default reasoning effort; rubric preamble as instructions |
| Human reviewer | DH (also the Skill's author; reviews before seeing judge results) |
| Bootstrap seed | _choose before scoring_ |
| Human-review sampling seed | _bootstrap seed + 1, set by score.py_ |
| Human-review packet seed | _choose before making the packet_ |

## Dates

| Step | Date |
|---|---|
| First generation | |
| Last generation | |
| Judging | |
| Human review | |
| Results | |

## Regenerations

Copied from `regenerations.jsonl` at the end of generation: file, attempt, cause.

| File | Attempt | Cause |
|---|---|---|

## Deviations

Any departure from `PROTOCOL.md`, with the reason. None so far.
