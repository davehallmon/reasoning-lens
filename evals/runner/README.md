# Round 1 runner

Scripts that carry out [`../PROTOCOL.md`](../PROTOCOL.md) v1.0.0. They read the frozen files (`cases.md`, `baseline-prompt.md`, `rubric.md`, `check_rules.py`) at run time and never change them. If this page and `PROTOCOL.md` disagree, `PROTOCOL.md` wins.

Nothing here is part of the installed Skill.

## Setup

Run on your own computer, from the repo root, on a clean checkout of `main`.

```bash
python3 -m pip install -r evals/runner/requirements.txt
export ANTHROPIC_API_KEY=...   # generator
export OPENAI_API_KEY=...      # judge
```

Keys stay in your shell. Never put them in a file in this repo.

## Steps

`RUN=evals/runs/round-1_v0.2.2`

1. **Fill the manifest** (`$RUN/manifest.md`) up to "Generation". Commit it.
2. **Smoke test, no API calls:** `python3 evals/runner/generate.py --run-dir $RUN --model claude-opus-5-5 --dry-run`. It should list 209 planned outputs.
3. **Generate:** same command without `--dry-run`. The first real call is the round's first generation: from then on, the frozen files cannot change for this round (§9.1). The script refuses to start if frozen or Skill files have uncommitted changes. It can be stopped and restarted; it never overwrites an output.
4. **Check F outputs:** `python3 evals/check_rules.py $RUN/outputs/*-F-*.md`.
5. **Judge:** `python3 evals/runner/judge.py --run-dir $RUN --model gpt-5.5-2026-04-23`. About 300 calls. Restartable.
6. **Score:** `python3 evals/runner/score.py --run-dir $RUN --seed <seed>`. Pick the seed before you run it and record it in the manifest. Resolve anything in `judgments/parse-issues.csv` through `judgments/manual.csv`, then rerun.
7. **Human review (§8):** `python3 evals/runner/human_packet.py --run-dir $RUN --seed <seed2> make`. Fill `human-review/answers.csv` before you open `results.md`, `judgments/`, `outputs/`, or the hidden key. Then run `finalize` and rerun `score.py`.
8. **Record:** complete the manifest; log the round in `evals/README.md` and `cases.md`; report it in `CHANGELOG.md` with the protocol commit SHA. Log the round even if it fails or is abandoned.

## Choices this runner makes

`PROTOCOL.md` leaves these to the runner. Each is recorded in the run folder.

- **Condition F on the API.** The Skill is supplied as the system prompt: `SKILL.md` and every file in `references/`, nothing else. This stands in for "installed" on a platform without Skill loading.
- **max_tokens = 8000** for every generation. The Messages API requires a value. Sampling parameters are not sent.
- **Platform errors.** Only an API error or an empty response is retried, and each one is logged in `regenerations.jsonl`. Every completed response is kept as-is.
- **Judge settings.** The rubric preamble is sent as the call's instructions; reasoning effort and sampling are left at the platform defaults.
- **Two judge prompts are wrapped by the runner.** `rubric.md` gives only the question for gate quality and gate boundary judgments. The surrounding text is in `judge.py` and is copied to `judge-settings.json`.
- **Close cases (§8)** include case scores of exactly 1/3 and 2/3.
- **Human vs. judge (§8).** A case-endpoint is Unresolved when the human's case score and the judge's fall on different sides of 0.5 (F preferred, C preferred, or even).
- **Not automated:** the Full-only diagnostics in `rubric.md` §3 (descriptive, not gating).
