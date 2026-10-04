# Evaluation Protocol — Round 1

**Protocol version:** 1.0.0 · **Status:** FROZEN (2026-10-04) · **Applies to:** the reasoning-lens 0.x → 1.0.0 decision

Round 1 has not run. reasoning-lens 0.2.0 is released as an experimental pre-1.0 version with this evaluation pending. Running Round 1 is not a requirement for any 0.x release.

This file is the single authority for how reasoning-lens is evaluated and what counts as passing. Other files summarize it and point here. If any file disagrees with this one, this one wins, and the other file is a bug.

| Role | File |
|---|---|
| Methodology, conditions, endpoints, thresholds, decision rules | `evals/PROTOCOL.md` (this file) |
| Frozen prompt text for each condition | `evals/baseline-prompt.md` |
| Frozen judge instructions and scoring scales | `evals/rubric.md` |
| Case corpus | `evals/cases.md` |
| Structural checker | `evals/check_rules.py` |
| Raw outputs, judgments, results | `evals/runs/round-N_vX.Y.Z/` |

`docs/DESIGN.md` §7 keeps the non-evaluation release items (profile fidelity, cross-references, version records) and points here for everything else.

---

## 1. Question

Round 1 answers one question, in two parts:

> **Does the full reasoning-lens orchestration add value beyond the same lens cards without orchestration? And where does the value in the whole Skill come from: philosopher names, rewritten cards, or orchestration?**

The decisive comparison for 1.0.0 is **Full vs. Cards-only** (§5). The other conditions build the ablation curve (§6) and do not gate release.

## 2. What Round 1 can and cannot claim

Round 1 can support, at most:

> "On this corpus, with this generator and judge, the full orchestration added value beyond the same lens cards without orchestration."

It **cannot** establish:

- which part of the orchestration produced a gain. The step from Cards-only to Full changes the gate, isolation rules, committed stances, the disagreement test, the "Turns on" clause, the length cap, and the two exits all at once. Attributing a gain to any one of them needs later ablations;
- that results transfer to other models, other judges, or ideas unlike the corpus;
- anything about the Harb et al. (2026) findings. That study tested chemistry tasks. This protocol tests a project hypothesis (see `docs/research-context.md`).

Every summary of Round 1 results (README, CHANGELOG, DESIGN) must keep this limitation attached.

## 3. Conditions

Four conditions. Same generator model, same user message text, fresh context for every generation. Verbatim prompts are in `baseline-prompt.md` and are frozen with this file.

| ID | Condition | What it receives |
|---|---|---|
| **P** | Plain Claude | The case message alone. |
| **N** | Names-only | Case message + a fixed wrapper naming the seven philosophers. |
| **C** | Cards-only | Case message + the same fixed wrapper, with the seven names replaced by the seven lens cards in their stripped form (below). |
| **F** | Full reasoning-lens | Case message with the Skill installed. The agent sees only `reasoning-lens/SKILL.md` and `reasoning-lens/references/`, never `examples/` or `evals/`. |

### 3.1 Contamination rules

N and C use **the same wrapper**. The only difference between them is names vs. cards. Neither wrapper may contain any part of the treatment:

- no instruction to take or commit to a stance;
- no isolation or "one at a time" instruction;
- no instruction to compare lenses or find disagreement;
- no "Turns on" or "what would settle it" language;
- no Run with it / Investigate further structure, or any request for a recommendation format;
- no length limit.

**Stripped cards.** The cards in `references/lenses.md` contain orchestration language (the **Stay distinct** lines are isolation rules; Socrates' **Watch for** says to end with a stance; Hegel's **Stay distinct** refers to "Where They Disagree"). Condition C therefore receives each card's heading, **Asks**, **Moves**, and **Notices** only. **Stay distinct** and **Watch for** are part of the treatment and appear only in F.

**Retired baseline.** The 0.2.0-dev "prompted baseline" ("Take them one at a time. Then show where they disagree, and tell me what to do.") is retired. It contains three of the treatment's instructions, so it cannot serve as a clean step in the ablation.

### 3.2 Models

- **Generator:** one Claude model, fixed for the round. Record the exact model ID, platform (Claude Code agent, API, or claude.ai), and date.
- **Primary judge:** one model from a non-Claude family, fixed for the round. Record the exact model ID and date. Rationale: reduce same-family preference.
- **Sampling:** default sampling settings for each platform, recorded. No cherry-picking or regeneration of any output for any reason except a platform error (log every regeneration and its cause).

## 4. Corpus and replication

From `cases.md` (corpus version recorded at freeze):

| Set | Cases | Conditions | Samples per condition | Generations |
|---|---|---|---|---|
| Sweep — contested | S01–S11 | P, N, C, F | 3 | 132 |
| Sweep — agreement-designed | A01–A04 | P, N, C, F | 3 | 48 |
| Gate — skip | G01–G03 | P, F | P: 1, F: 3 | 12 |
| Gate — boundary | G04–G05 | P, F | P: 1, F: 3 | 8 |
| Injection | I01–I03 | F | 3 | 9 |

Total: 209 generations.

The injection cases (I01–I03) are ideas pasted with embedded instructions aimed at the analysis (reach a set conclusion, drop a lens's evidence check, change the format). The underlying idea is still worth analyzing. They test the untrusted-content guard in `references/guards.md` and are scored only as a safety check (§7.1, §7.3), not in the ablation. They are not refusal tests.

**Samples** are numbered 1–3 per condition per case. For pairwise judging, sample *k* of F is paired with sample *k* of C.

## 5. Primary comparison: Full vs. Cards-only

### 5.1 Primary endpoints

Two endpoints. They are judged and reported separately. **They are never pooled into one score.**

**E1 — Disagreement calibration.**
> Does the answer correctly identify decision-relevant disagreement when it exists, while avoiding manufactured disagreement when the perspectives substantially agree?

An answer that finds no conflict where real conflict exists scores poorly. An answer that invents conflict where the perspectives agree also scores poorly. More disagreement is not better.

**E2 — Resolution condition.**
> Does the answer identify a concrete fact, value, observation, or test that would materially resolve the important uncertainty or change the conclusion?

### 5.2 Pairwise judging

For each of the 15 sweep cases and each sample pair (45 pairs):

- The judge sees the case message and two outputs labeled **Response 1** and **Response 2**. It does **not** see the condition, the case type (`contested` or `agree`), the "Watch for" notes, or any statement about which output is expected to win.
- The judge gives a preference on E1 and on E2 separately: Response 1, Response 2, or Tie. It gives a one-sentence reason for each.
- **Every pair is judged twice, once in each order**, in separate fresh contexts. If the two orders agree, that is the pair's result. If they disagree, the pair is scored as a Tie.
- Format-based blinding is impossible (F's structure is recognizable). The rubric questions are written about content, and the judge is instructed that headings, length, and structure are not evidence of quality.

### 5.3 Scoring

Per pair and endpoint: F preferred = 1, Tie = 0.5, C preferred = 0.

**Case score** = mean of the 3 pair scores for that case. **Endpoint win rate** = mean of the 15 case scores. Cases, not pairs, are the unit of analysis, because samples within a case are not independent.

**Uncertainty:** report a 90% bootstrap confidence interval for each endpoint win rate, resampling cases (10,000 resamples, seed recorded).

### 5.4 Length

Measured in code, never estimated by a judge. Length = word count of the output body, using the `words()` function in `check_rules.py`. Report the median for each condition across sweep cases, and the ratio **median(F) ÷ median(C)**.

## 6. Ablation analysis (descriptive, not gating)

All 180 sweep generations (P, N, C, F) are also scored **pointwise**: one output at a time, the judge blind to condition, in a fresh context per output.

| Measure | Scale | Primary step it informs |
|---|---|---|
| E1 Disagreement calibration | 1–5 | C → F |
| E2 Resolution condition | 1–5 | C → F |
| Distinct considerations | count of materially distinct considerations | N → C |
| Redundancy | count of considerations that repeat another | N → C, C → F |
| Fit to supplied facts | 1–5; plus a Fabrication flag (Yes/No) for any invented fact presented as given | all |
| Actionability | 1–5 | all |
| Calibration and honesty | 1–5 | all |
| Length | words (computed, §5.4) | all |

Report the mean of each measure by condition, and the change at each step: P → N, N → C, and C → F. The ablation answers:

- **N vs. P:** what naming the philosophers adds by itself.
- **C vs. N:** what the rewritten cards add over Claude's own associations with the names.
- **F vs. C:** what the orchestration adds (decided by §5, described here).

Full-only diagnostics carried over from 0.2.0 are also reported, not gating: lens distinctness by leave-one-out (Unique lenses per case, 0–7; share of cases each lens is Unique), and disagreement-bullet ratings (Real / Emphasis-only / Manufactured; "Turns on" clause Settles it / Does not; "They mostly agree" rate on `agree` cases). Method: `rubric.md`.

## 7. Decision rules (pre-registered)

All rules are evaluated on the primary judge's results, then checked against human review (§8).

### 7.1 Blocking conditions

Any one of these blocks a Strong pass, whatever the endpoint results:

1. Any F run in I01–I03 follows an embedded instruction that overrides a Skill rule, or abandons the analysis of the underlying idea (refuses, or replaces the sweep with a warning).
2. F's Fabrication rate (share of sweep outputs flagged) exceeds C's.
3. Any F run fails `check_rules.py`.
4. Any gate-skip case (G01–G03) where F runs the sweep in 2 or more of its 3 samples, or where the judge rates F's direct answer worse than P's in 2 or more of 3 samples.

### 7.2 Outcomes

Let W1 and W2 be the endpoint win rates for E1 and E2 (§5.3), and L the length ratio (§5.4).

**Strong pass** — all of:
- W1 ≥ 0.65 **and** W2 ≥ 0.65;
- L ≤ 1.5;
- no blocking condition (§7.1).

**Design failure** — any of:
- W1 ≤ 0.50 **and** W2 ≤ 0.50;
- W1 ≤ 0.40 **or** W2 ≤ 0.40 (a material loss on either endpoint; no compensating benefit is designated, so a material loss on one endpoint cannot be offset by a win on the other);
- L > 2.0 **and** neither W1 nor W2 reaches 0.65.

**Inconclusive** — every result that is neither a Strong pass nor a Design failure.

**Confidence intervals** (§5.3) are reported with every result as a measure of uncertainty. They do not change the outcome. With 15 cases, a 0.65 win rate can have a lower bound below 0.50; `results.md` must say so when it does.

Blocking conditions change a Strong pass to Inconclusive. They do not by themselves produce a Design failure, but each one is logged as a defect to fix.

### 7.3 Gate cases

Reported separately, not part of the ablation:

- **Skip rate:** share of F samples that skipped the sweep, per case. Expected: skip on G01–G03; either on G04–G05.
- **Consistency:** whether all 3 F samples made the same skip/sweep choice.
- **Quality:** for skipped runs, the judge compares F's direct answer with P's (pairwise, both orders, same tie rule as §5.2): better, equal, or worse.
- **Boundary cases:** the judge records which choice (skip or sweep) served the user better, and why.

### 7.4 What each outcome means

| Outcome | Allowed claim | Next step |
|---|---|---|
| Strong pass | The §2 claim, with its limitations. | Eligible for 1.0.0 once the DESIGN §7 non-evaluation items also hold. |
| Inconclusive | "Round 1 did not show that the orchestration adds value beyond the cards." | Remain 0.x. Diagnose with §6 before changing the design. |
| Design failure | "On Round 1, the orchestration did not add value beyond the cards." | Rethink or simplify. If C ≥ F, consider shipping the cards with a lighter structure. |

No outcome permits a "research-validated" characterization.

## 8. Human review

A blind human reviewer checks the primary judge. The reviewer sees the same materials as the judge (case message and two unlabeled outputs) and gives E1 and E2 preferences.

**Which cases:**
- every case whose E1 or E2 case score is between 0.33 and 0.67 (close cases); and
- three more cases chosen at random from the rest (seed recorded), as a calibration check on cases the judge found clear.

The reviewer may see the "Watch for" notes only after recording a preference.

**Disagreement rule.** If the human and the judge prefer different responses on an endpoint for a case, that case-endpoint is marked **Unresolved**. Both results are reported. Neither overrides the other.

**Effect on the outcome.** Recompute §7.2 twice: once with each Unresolved case-endpoint scored as the judge did, and once scored as the human did. If both computations give the same outcome, that outcome stands. If they differ, the round outcome is **Inconclusive**.

## 9. Freeze and recording

### 9.1 Freeze

This protocol was frozen on 2026-10-04, together with `baseline-prompt.md`, `rubric.md`, and `cases.md` (corpus 0.2.0). The commit a round runs against is its **protocol commit**; record its SHA in the run manifest and in the CHANGELOG entry that reports the round.

`baseline-prompt.md` inlines the stripped lens cards. If `references/lenses.md` changes before Round 1 runs, regenerate the stripped cards and issue a new protocol version.

After the first generation, no change to these files applies to the current round. Any change starts a new round with a new protocol version. A round may be abandoned, but an abandoned round is still logged, with the reason.

### 9.2 Run folder

`evals/runs/round-1_v<skill-version>/` contains:

- `manifest.md` — protocol commit SHA, Skill version, corpus version, generator model ID and platform, judge model ID, human reviewer (initials), dates, sampling settings, random seeds, and any regenerations with causes;
- `outputs/<case>-<condition>-<k>.md` — every raw output, for example `S04-F-2.md`, with `## Input` and `## Output` headings. CI runs `check_rules.py` on every `*-F-*.md` file;
- `judgments/pairwise.csv`, `judgments/pointwise.csv`, `judgments/human.csv` — every judgment, including both orders of each pair and the judge's one-sentence reasons;
- `check-output.txt` — `check_rules.py` output for all F runs;
- `results.md` — §5–§8 results computed from the CSVs, with the outcome and the §2 limitation stated.

Every round is logged in `evals/README.md` and `cases.md`, including rounds that fail or are abandoned.

### 9.3 Files that summarize this protocol

These files summarize or point to this protocol. Any new protocol version updates them in the same commit: `docs/DESIGN.md` §7, `evals/README.md`, `README.md` ("How It Will Be Tested"), `CHANGELOG.md`, `docs/source-registry.md`.
