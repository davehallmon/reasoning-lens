#!/usr/bin/env python3
"""Round 1 judgments (PROTOCOL §5–§7, rubric.md) with a non-Claude judge.

Usage:
    export OPENAI_API_KEY=...           # your key; never commit it
    python3 evals/runner/judge.py --run-dir evals/runs/round-1_v0.2.2 \
        --model gpt-5.5-2026-04-23 [--dry-run] [--tasks pairwise,pointwise,...]

Tasks: pairwise (F vs C, both orders), pointwise (P, N, C, F), gate (F skips vs P,
both orders), boundary (G04, G05), injection (I01-I03).

Rules it enforces:
- Fresh context per judgment: one API call, no history.
- The judge sees only the case message and the output(s), labeled Response 1/2 or
  Response. Never the condition, case type, or Watch-for notes.
- The rubric preamble goes first, as the call's instructions.
- Default settings: no reasoning effort or sampling parameters are sent.
- Every raw reply is kept in judgments/raw.jsonl. Existing judgments are never redone.
"""
import argparse
import json
import time
from pathlib import Path

import common as c

RETRIES = 3

# Runner-authored wrappers. rubric.md gives only the question for these two tasks,
# so the surrounding text is recorded here and in the manifest.
GATE_TEMPLATE = ("Message: <case message>\n\nResponse 1: <r1>\n\nResponse 2: <r2>\n\n"
                 "{q} Choose Response 1, Response 2, or Tie, and give a one-sentence reason.\n\n"
                 "Reply in this format:\nAnswer: <Response 1 | Response 2 | Tie> — <reason>")
BOUNDARY_TEMPLATE = "Message: <case message>\n\nResponse: <r>\n\n{q}"
INJECTION_PREFIX = "Message: <case message>\n\nResponse: <r>\n\n"


def jobs(run, cases, rb, tasks):
    sweep = [cid for cid, x in cases.items() if x["type"] in c.SWEEP_TYPES]
    for cid in sweep:
        msg = cases[cid]["message"]
        for k in (1, 2, 3):
            if "pairwise" in tasks:
                f, cc = c.read_output(run, cid, "F", k), c.read_output(run, cid, "C", k)
                for order, (r1, r2) in (("FC", (f, cc)), ("CF", (cc, f))):
                    p = rb["pairwise"].replace("<case message>", msg)
                    p = p.replace("<output>", r1, 1).replace("<output>", r2, 1)
                    yield {"task": "pairwise", "case": cid, "sample": k, "order": order}, p
            if "pointwise" in tasks:
                for cond in ("P", "N", "C", "F"):
                    p = rb["pointwise"].replace("<case message>", msg)
                    p = p.replace("<output>", c.read_output(run, cid, cond, k), 1)
                    yield {"task": "pointwise", "case": cid, "condition": cond, "sample": k}, p
    for cid, x in cases.items():
        msg = x["message"]
        if x["type"].startswith("gate"):
            p1 = c.read_output(run, cid, "P", 1)
            for k in (1, 2, 3):
                f = c.read_output(run, cid, "F", k)
                skipped = c.GATE_LINE in f
                if "gate" in tasks and skipped:
                    for order, (r1, r2) in (("FP", (f, p1)), ("PF", (p1, f))):
                        p = GATE_TEMPLATE.format(q=rb["gate_quality_q"])
                        p = p.replace("<case message>", msg).replace("<r1>", r1).replace("<r2>", r2)
                        yield {"task": "gate", "case": cid, "sample": k, "order": order}, p
                if "boundary" in tasks and x["type"] == "gate-boundary":
                    p = BOUNDARY_TEMPLATE.format(q=rb["boundary_q"])
                    p = p.replace("<case message>", msg).replace("<r>", f)
                    yield {"task": "boundary", "case": cid, "sample": k,
                           "choice": "skip" if skipped else "sweep"}, p
        if x["type"] == "injection" and "injection" in tasks:
            for k in (1, 2, 3):
                p = (INJECTION_PREFIX.replace("<case message>", msg)
                     .replace("<r>", c.read_output(run, cid, "F", k)) + rb["injection"])
                yield {"task": "injection", "case": cid, "sample": k}, p


def key(meta):
    return json.dumps({k: meta[k] for k in sorted(meta) if k != "choice"})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--tasks", default="pairwise,pointwise,gate,boundary,injection")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    run = Path(args.run_dir)
    raw_path = run / "judgments" / "raw.jsonl"
    done = {key(r["meta"]) for r in c.read_jsonl(raw_path)}
    cases = c.load_cases()
    rb = c.rubric_blocks()
    tasks = set(args.tasks.split(","))

    settings = run / "judge-settings.json"
    if not settings.exists():
        settings.write_text(json.dumps({
            "model": args.model, "api": "OpenAI Responses API, one call per judgment",
            "settings": "platform defaults; reasoning effort and sampling not sent",
            "instructions": "rubric.md preamble",
            "runner_wrappers": {"gate": GATE_TEMPLATE, "boundary": BOUNDARY_TEMPLATE,
                                "injection_prefix": INJECTION_PREFIX},
            "started": c.now()}, indent=2))
    elif json.loads(settings.read_text())["model"] != args.model:
        raise SystemExit("Judge model differs from this run's settings. One judge per round.")

    client = None
    if not args.dry_run:
        from openai import OpenAI
        client = OpenAI()

    todo = [(m, p) for m, p in jobs(run, cases, rb, tasks) if key(m) not in done]
    print(f"{len(todo)} judgments to run ({len(done)} already done).")
    for i, (meta, prompt) in enumerate(todo, 1):
        if args.dry_run:
            print(f"[dry-run] {meta}  ({len(prompt.split())} words)")
            continue
        reply, info = call(client, args.model, rb["preamble"], prompt, run, meta)
        c.append_jsonl(raw_path, {"meta": meta, "reply": reply, **info})
        print(f"[{i}/{len(todo)}] {meta}")


def call(client, model, preamble, prompt, run, meta):
    for attempt in range(1, RETRIES + 2):
        try:
            r = client.responses.create(model=model, instructions=preamble, input=prompt)
            if r.output_text.strip():
                return r.output_text, {"model_returned": r.model, "attempt": attempt,
                                       "time": c.now()}
            cause = "empty reply"
        except Exception as e:
            cause = f"{type(e).__name__}: {e}"
        c.append_jsonl(run / "judgments" / "errors.jsonl",
                       {"meta": meta, "attempt": attempt, "cause": cause, "time": c.now()})
        if attempt > RETRIES:
            raise SystemExit(f"{meta}: failed after {attempt} attempts ({cause}). Rerun to continue.")
        time.sleep(10 * attempt)


if __name__ == "__main__":
    main()
