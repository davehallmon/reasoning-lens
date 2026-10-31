#!/usr/bin/env python3
"""Round 1 generations (PROTOCOL §3–§4): 209 outputs on the Claude API.

Usage:
    export ANTHROPIC_API_KEY=...        # your key; never commit it
    python3 evals/runner/generate.py --run-dir evals/runs/round-1_v0.2.2 \
        --model claude-opus-5-5 [--dry-run] [--only S01,S02]

Rules it enforces:
- Fresh context per generation: one API call, no history.
- Default sampling: temperature and other sampling parameters are not set.
  max_tokens must be sent on this API; its value is recorded in the manifest.
- No regeneration. An output that exists on disk is never overwritten.
  Every completed response is kept, whatever it says. Only a platform error
  (an API exception or an empty response) is retried, and each one is logged
  to regenerations.jsonl with its cause.
- Refuses to start if frozen files or Skill files have uncommitted changes.
"""
import argparse
import json
import time
from pathlib import Path

import common as c

MAX_TOKENS = 8000
RETRIES = 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--only", help="comma-separated case IDs (for a smoke test)")
    ap.add_argument("--dry-run", action="store_true", help="write prompts, call nothing")
    args = ap.parse_args()

    if c.git_dirty_frozen() and not args.dry_run:
        raise SystemExit("Frozen or Skill files have uncommitted changes. Commit or revert first.")

    run = Path(args.run_dir)
    (run / "outputs").mkdir(parents=True, exist_ok=True)
    cases = c.load_cases()
    suffixes = c.condition_suffixes()
    system_f, f_files = c.skill_system_prompt()

    settings = run / "generation-settings.json"
    if not settings.exists():
        settings.write_text(json.dumps({
            "protocol_commit": c.git_sha(),
            "model": args.model,
            "platform": "Claude API (Messages), one call per generation",
            "max_tokens": MAX_TOKENS,
            "sampling": "platform defaults; temperature, top_p, top_k not sent",
            "F_condition": "SKILL.md and references/ supplied as the system prompt",
            "F_files": f_files,
            "started": c.now(),
        }, indent=2))
    else:
        prev = json.loads(settings.read_text())
        if prev["model"] != args.model or prev["protocol_commit"] != c.git_sha():
            raise SystemExit("Model or protocol commit differs from this run's settings. "
                             "A round uses one generator and one protocol commit.")

    client = None
    if not args.dry_run:
        import anthropic
        client = anthropic.Anthropic()

    only = set(args.only.split(",")) if args.only else None
    jobs = []
    for cid, case in cases.items():
        if only and cid not in only:
            continue
        for cond, n in c.PLAN[case["type"]].items():
            for k in range(1, n + 1):
                jobs.append((cid, cond, k))

    done = skipped = 0
    for cid, cond, k in jobs:
        path = c.out_path(run, cid, cond, k)
        if path.exists():
            skipped += 1
            continue
        msg = c.user_message(cases[cid]["message"], cond, suffixes)
        system = system_f if cond == "F" else None
        if args.dry_run:
            print(f"[dry-run] {path.name}: {len(msg.split())} words in message"
                  f"{', Skill system prompt' if system else ''}")
            continue
        text, meta = call(client, args.model, system, msg, run, path.name)
        path.write_text(f"# {cid}-{cond}-{k}\n\n## Input\n\n{msg}\n\n## Output\n\n{text.strip()}\n")
        c.append_jsonl(run / "generation-log.jsonl", {"file": path.name, **meta})
        done += 1
        print(f"wrote {path.name}  ({done} new, {skipped} already present, {len(jobs)} total)")
    print(f"Finished: {done} new, {skipped} already present, {len(jobs)} planned.")


def call(client, model, system, msg, run, name):
    kwargs = {"model": model, "max_tokens": MAX_TOKENS,
              "messages": [{"role": "user", "content": msg}]}
    if system:
        kwargs["system"] = system
    for attempt in range(1, RETRIES + 2):
        try:
            r = client.messages.create(**kwargs)
            text = "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
            # Any completed response is kept as-is, including a max_tokens stop
            # (recorded). Only an API error or an empty response is retried.
            if text.strip():
                return text, {"model_returned": r.model, "stop_reason": r.stop_reason,
                              "input_tokens": r.usage.input_tokens,
                              "output_tokens": r.usage.output_tokens,
                              "attempt": attempt, "time": c.now()}
            cause = f"stop_reason={r.stop_reason}, text_len={len(text)}"
        except Exception as e:  # platform error
            cause = f"{type(e).__name__}: {e}"
        c.append_jsonl(run / "regenerations.jsonl", {"file": name, "attempt": attempt,
                                                     "cause": cause, "time": c.now()})
        if attempt > RETRIES:
            raise SystemExit(f"{name}: failed after {attempt} attempts ({cause}). "
                             "Logged in regenerations.jsonl. Rerun later to continue.")
        time.sleep(10 * attempt)


if __name__ == "__main__":
    main()
