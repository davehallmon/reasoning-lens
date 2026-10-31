#!/usr/bin/env python3
"""Blind human review packet (PROTOCOL §8).

Step 1, after score.py has picked the cases (human-review-cases.txt):
    python3 evals/runner/human_packet.py --run-dir RUN --seed N make
  Writes human-review/<case>-<k>.md (message + Response 1 + Response 2, order
  randomized) and human-review/answers.csv for you to fill with
  "Response 1", "Response 2", or "Tie" for E1 and E2. The key goes to
  human-review/.key.json. Do not open the key, the outputs folder, or
  judgments/ until you have filled every row. Read Watch-for notes in
  cases.md only after recording a preference.

Step 2, when answers.csv is complete:
    python3 evals/runner/human_packet.py --run-dir RUN --seed N finalize
  Converts your answers to F/C/Tie in judgments/human.csv. Then rerun score.py.
"""
import argparse
import csv
import json
import random
from pathlib import Path

import common as c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("step", choices=["make", "finalize"])
    args = ap.parse_args()
    run = Path(args.run_dir)
    hr = run / "human-review"
    hr.mkdir(exist_ok=True)

    if args.step == "make":
        sel = (run / "human-review-cases.txt").read_text()
        ids = [x.strip() for line in sel.splitlines()[1:] for x in line.split(":", 1)[1].split(",") if x.strip()]
        cases = c.load_cases()
        rb = c.rubric_blocks()
        rng = random.Random(args.seed)
        key, rows = {}, []
        for cid in ids:
            for k in (1, 2, 3):
                order = rng.choice(["FC", "CF"])
                outs = {"F": c.read_output(run, cid, "F", k), "C": c.read_output(run, cid, "C", k)}
                body = rb["pairwise"].replace("<case message>", cases[cid]["message"])
                body = body.replace("<output>", outs[order[0]], 1).replace("<output>", outs[order[1]], 1)
                (hr / f"{cid}-{k}.md").write_text(body + "\n")
                key[f"{cid}-{k}"] = order
                rows.append([cid, k, "", ""])
        (hr / ".key.json").write_text(json.dumps({"seed": args.seed, "order": key}, indent=2))
        c.write_csv(hr / "answers.csv", ["case", "sample", "E1", "E2"], rows)
        print(f"Wrote {len(rows)} blind pairs to {hr}. Fill answers.csv, then run finalize.")
    else:
        key = json.loads((hr / ".key.json").read_text())["order"]
        out = []
        for r in csv.DictReader(open(hr / "answers.csv")):
            order = key[f"{r['case']}-{r['sample']}"]
            conv = []
            for e in ("E1", "E2"):
                v = r[e].strip()
                if v not in ("Response 1", "Response 2", "Tie"):
                    raise SystemExit(f"{r['case']}-{r['sample']} {e}: '{v}' is not Response 1, Response 2, or Tie")
                conv.append("Tie" if v == "Tie" else (order[0] if v == "Response 1" else order[1]))
            out.append([r["case"], r["sample"], *conv])
        c.write_csv(run / "judgments" / "human.csv", ["case", "sample", "E1", "E2"], out)
        print(f"Wrote judgments/human.csv ({len(out)} rows). Rerun score.py.")


if __name__ == "__main__":
    main()
