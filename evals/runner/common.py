"""Shared helpers for the Round 1 runner.

Reads the frozen files (cases.md, baseline-prompt.md, rubric.md) at run time
and never edits them. See evals/PROTOCOL.md for every rule this code follows.
"""
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALS = ROOT / "evals"
SKILL_DIR = ROOT / "reasoning-lens"

sys.path.insert(0, str(EVALS))
from check_rules import words, strip_md  # noqa: E402  (frozen length function, PROTOCOL §5.4)

GATE_LINE = 'Say "run the lenses" if you want the full sweep anyway.'

# PROTOCOL §4: which conditions and how many samples per case type.
PLAN = {
    "contested": {"P": 3, "N": 3, "C": 3, "F": 3},
    "agree": {"P": 3, "N": 3, "C": 3, "F": 3},
    "gate-skip": {"P": 1, "F": 3},
    "gate-boundary": {"P": 1, "F": 3},
    "injection": {"F": 3},
}
SWEEP_TYPES = ("contested", "agree")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_sha():
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def git_dirty_frozen():
    """True if any frozen file or Skill file differs from HEAD."""
    paths = ["evals/PROTOCOL.md", "evals/baseline-prompt.md", "evals/rubric.md",
             "evals/cases.md", "evals/check_rules.py", "reasoning-lens/SKILL.md",
             "reasoning-lens/references"]
    out = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain", "--", *paths],
                         capture_output=True, text=True).stdout
    return bool(out.strip())


def load_cases():
    """Parse cases.md into {id: {"type", "title", "message"}}. Watch-for notes are not kept."""
    text = (EVALS / "cases.md").read_text()
    cases = {}
    blocks = re.split(r"^### ", text, flags=re.M)[1:]
    for b in blocks:
        head = b.splitlines()[0]
        m = re.match(r"(\w\d\d) · (.+?) · `([\w-]+)`", head)
        if not m:
            continue
        cid, title, ctype = m.groups()
        body = b.split("\n", 1)[1]
        msg = re.search(r"\*\*Message:\*\*\s*(.*?)(?=\n\*\*Watch for:\*\*)", body, re.S)
        if not msg:
            raise SystemExit(f"cannot parse message for {cid}")
        cases[cid] = {"type": ctype, "title": title, "message": msg.group(1).strip()}
    if len(cases) != 23:
        raise SystemExit(f"expected 23 cases, parsed {len(cases)}")
    return cases


def _fenced_blocks(text):
    return re.findall(r"^```(?:text)?\n(.*?)^```", text, re.S | re.M)


def condition_suffixes():
    """Exact added text for N and C from baseline-prompt.md."""
    text = (EVALS / "baseline-prompt.md").read_text()
    n_sec = text.split("## N — Names-only", 1)[1].split("## C — Cards-only", 1)[0]
    c_sec = text.split("## C — Cards-only", 1)[1].split("## F — Full", 1)[0]
    n = _fenced_blocks(n_sec)[0].rstrip("\n")
    c = _fenced_blocks(c_sec)[0].rstrip("\n")
    return {"N": n, "C": c}


def user_message(case_msg, condition, suffixes):
    """baseline-prompt.md: the case message first; added text after one blank line."""
    if condition in ("N", "C"):
        return f"{case_msg}\n\n{suffixes[condition]}"
    return case_msg


def skill_system_prompt():
    """Condition F: SKILL.md and every file in references/, nothing else (PROTOCOL §3)."""
    parts = ["The reasoning-lens Skill is installed. Its files follow. Follow SKILL.md; "
             "the files under references/ are the files it tells you to read.\n"]
    files = [SKILL_DIR / "SKILL.md"] + sorted((SKILL_DIR / "references").glob("*.md"))
    for f in files:
        rel = f.relative_to(SKILL_DIR)
        parts.append(f'<file path="{rel}">\n{f.read_text().rstrip()}\n</file>\n')
    return "\n".join(parts), [str(f.relative_to(ROOT)) for f in files]


def rubric_blocks():
    """Frozen judge text from rubric.md, by role."""
    text = (EVALS / "rubric.md").read_text()
    blocks = _fenced_blocks(text)
    preamble, pairwise, pointwise = blocks[0], blocks[1], blocks[2]
    injection = _fenced_blocks(text.split("## 5. Injection cases", 1)[1])[0]
    gate = text.split("## 4. Gate cases", 1)[1].split("## 5.", 1)[0]
    gate_quality_q = re.search(r"Question: \*(.+?)\*", gate).group(1)
    boundary_q = re.search(r"answers: \*(.+?)\*", gate, re.S).group(1)
    return {
        "preamble": preamble.strip(),
        "pairwise": pairwise.strip(),
        "pointwise": pointwise.strip(),
        "injection": injection.strip(),
        "gate_quality_q": " ".join(gate_quality_q.split()),
        "boundary_q": " ".join(boundary_q.split()),
    }


def fill(template, message, **responses):
    out = template.replace("<case message>", message)
    for label, text in responses.items():
        out = out.replace(f"<{label}>", text, 1)
    return out


def out_path(run_dir, cid, cond, k):
    return Path(run_dir) / "outputs" / f"{cid}-{cond}-{k}.md"


def read_output(run_dir, cid, cond, k):
    raw = out_path(run_dir, cid, cond, k).read_text()
    return raw.split("## Output", 1)[1].strip()


def append_jsonl(path, row):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(row) + "\n")


def read_jsonl(path):
    if not Path(path).exists():
        return []
    return [json.loads(l) for l in Path(path).read_text().splitlines() if l.strip()]


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def output_words(text):
    return words(strip_md(text))
