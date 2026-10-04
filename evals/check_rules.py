#!/usr/bin/env python3
"""Check reasoning-lens outputs against the rules in reasoning-lens/SKILL.md.

Usage:
    python3 evals/check_rules.py FILE [FILE ...]

Checks structure only: the gate, the restatement, seven lenses in order,
lens length, stances, disagreements, both ways forward, the closing line,
total length, and persona voice. It does not judge whether the reasoning is
good. Prints a stance summary across all files. Exits 1 if any file fails.

If a file has a "## Output" heading (worked examples, eval runs), only the
text after it is checked.

This script is a maintainer tool. It is not part of the installed Skill.
"""
import re
import sys
from collections import Counter
from pathlib import Path

LENSES = [
    ("Socrates", "clarify and question"),
    ("Plato", "find the deeper pattern"),
    ("Aristotle", "classify and explain"),
    ("Descartes", "break it down and check"),
    ("Hume", "test the evidence"),
    ("Kant", "examine conditions and limits"),
    ("Hegel", "work the contradiction"),
]
NAMES = [n for n, _ in LENSES]
STANCES = ("Supports if", "Supports", "Challenges", "Can't judge yet")
CLOSING = 'Reply with a lens name to expand it, or "investigate" to work the open question together.'
GATE_LINE = 'Say "run the lenses" if you want the full sweep anyway.'
MAX_LENS_WORDS = 60
MAX_LENS_SENTENCES = 3
MAX_TOTAL_WORDS = 700


def words(s):
    return len(re.findall(r"[A-Za-z0-9’'][A-Za-z0-9’'\-]*", s))


def strip_md(s):
    return re.sub(r"[*`_]", "", s)


def sentences(s):
    s = strip_md(s).strip()
    s = re.sub(r"\b(e\.g|i\.e|vs|etc)\.", r"\1", s)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", s)
    return [p for p in parts if p.strip()]


def section(text, heading):
    m = re.search(rf"^###\s+{re.escape(heading)}\s*$(.*?)(?=^###\s|\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def check(path):
    raw = Path(path).read_text()
    text = raw.split("## Output", 1)[1] if "## Output" in raw else raw
    errors, stances = [], {}

    if re.search(r"\bAs (Socrates|Plato|Aristotle|Descartes|Hume|Kant|Hegel), I\b", text):
        errors.append("persona voice: 'As <philosopher>, I…'")

    # Gate path
    if GATE_LINE in text:
        if "### Seven Lenses" in text:
            errors.append("gate line present but the sweep also ran")
        return errors, stances, "gate"

    total = words(strip_md(text))
    if total > MAX_TOTAL_WORDS:
        errors.append(f"total length {total} words > {MAX_TOTAL_WORDS}")

    m = re.search(r"\*\*The idea:\*\*(.+)", text)
    if not m:
        errors.append("missing '**The idea:**' restatement")
    elif len(re.findall(r"\bAssuming\b", m.group(1))) > 2:
        errors.append("more than two assumptions in the restatement")

    lenses = section(text, "Seven Lenses")
    if lenses is None:
        errors.append("missing '### Seven Lenses'")
    else:
        found = re.findall(r"^\*\*(\w+) · ([^*]+)\*\*\s*[—-]\s*(.+?)\n\s*Stance:\s*(.+)$", lenses, re.M)
        order = [f[0] for f in found]
        if order != NAMES:
            errors.append(f"lenses out of order or missing: {order}")
        for name, label, body, stance_line in found:
            want = dict(LENSES).get(name)
            if want and label.strip() != want:
                errors.append(f"{name}: label '{label.strip()}' should be '{want}'")
            if words(body) > MAX_LENS_WORDS:
                errors.append(f"{name}: {words(body)} words > {MAX_LENS_WORDS}")
            if len(sentences(body)) > MAX_LENS_SENTENCES:
                errors.append(f"{name}: {len(sentences(body))} sentences > {MAX_LENS_SENTENCES}")
            s = strip_md(stance_line).strip()
            hit = next((st for st in STANCES if s.startswith(st)), None)
            if not hit:
                errors.append(f"{name}: invalid stance '{s[:40]}'")
            else:
                stances[name] = hit

    dis = section(text, "Where They Disagree")
    if dis is None:
        errors.append("missing '### Where They Disagree'")
    else:
        agree_all = "They mostly agree." in dis
        bullets = re.findall(r"^-\s+\*\*(\w+) vs\. (\w+)\*\*\s*[—-]\s*(.+)$", dis, re.M)
        if agree_all and bullets:
            errors.append("both 'They mostly agree' and disagreement bullets")
        if not agree_all:
            if not 1 <= len(bullets) <= 3:
                errors.append(f"{len(bullets)} disagreements; need 1–3 or 'They mostly agree.'")
            for a, b, rest in bullets:
                if a not in NAMES or b not in NAMES or a == b:
                    errors.append(f"bad lens pair: {a} vs. {b}")
                if "Turns on:" not in rest:
                    errors.append(f"{a} vs. {b}: missing 'Turns on:'")
            if "**Where they agree:**" not in dis:
                errors.append("missing '**Where they agree:**' line")
        disagree_pairs = len(bullets)
        stances["_pairs"] = disagree_pairs

    fwd = section(text, "Two Ways Forward")
    if fwd is None:
        errors.append("missing '### Two Ways Forward'")
    else:
        m = re.search(r"\*\*Run with it\.\*\*(.+?)(?=\n\s*\n|\*\*Investigate)", fwd, re.S)
        if not m:
            errors.append("missing '**Run with it.**'")
        elif not 2 <= len(sentences(m.group(1))) <= 4:
            errors.append(f"Run with it: {len(sentences(m.group(1)))} sentences; need 2–4")
        if "**Investigate further.**" not in fwd:
            errors.append("missing '**Investigate further.**'")
    if CLOSING not in text:
        errors.append("missing closing line")
    return errors, stances, "sweep"


def main(paths):
    if not paths:
        print(__doc__)
        return 2
    failed, tally, splits, kinds = 0, Counter(), Counter(), Counter()
    for p in paths:
        errors, stances, kind = check(p)
        kinds[kind] += 1
        pairs = stances.pop("_pairs", 0)
        tally.update(stances.values())
        if stances:
            splits["unanimous" if len(set(stances.values())) == 1 else "split"] += 1
        status = "FAIL" if errors else "PASS"
        print(f"{status}  {p}  [{kind}{', ' + str(pairs) + ' disagreement(s)' if kind == 'sweep' else ''}]")
        for e in errors:
            print(f"      - {e}")
        failed += bool(errors)
    print()
    print(f"Files: {len(paths)}  sweeps: {kinds['sweep']}  gated: {kinds['gate']}  failed: {failed}")
    if tally:
        print("Stances: " + ", ".join(f"{k} {v}" for k, v in tally.most_common()))
        print(f"Sweeps with split stances: {splits['split']}  unanimous: {splits['unanimous']}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
