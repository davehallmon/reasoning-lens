# 0001 — Sweep, Not Router

**Date:** 2026-10-04 · **Status:** accepted · **Supersedes:** router design, project version 0.1.0-dev

## Context

Version 0.1.0-dev (private, "Philosophy-Guided Reasoning Router") classified each task's dominant reasoning need and routed it to one primary philosopher mode, plus at most one secondary mode run in sequence. A DIRECT mode skipped specialized reasoning for routine work. Running all seven modes at once was prohibited.

Its release gate required 25 or more cases with routing accuracy, coverage of all seven modes plus DIRECT, ambiguous-boundary cases (Socrates ↔ Kant, Socrates ↔ Descartes, Aristotle ↔ Kant, Aristotle ↔ Plato, Descartes ↔ Hume, Hume ↔ Kant, Hegel ↔ Plato), a generic-reasoning baseline, and recorded ChatGPT and Claude runs. No cases were run.

## Decision

Run all seven lenses on every non-trivial request, one at a time, each attributed to its philosopher. Show where they disagree. Keep a small gate in place of DIRECT. End with two exits: Run with it, or Investigate further.

## Reasons

- **The product is disagreement.** A router shows one lens, so it can never show where lenses disagree. The banner promises exactly that.
- **Routing accuracy was untested too.** Harb et al. tested each prompt alone on chemistry questions. They list routing as future work. A router would have stacked two hypotheses (transfer, and correct selection); the sweep drops the second.
- **Users learn the lenses.** Seeing all seven on one idea teaches what each notices. A hidden router teaches nothing.

## Costs

- **Reading time.** Seven sections is long. problem-lens's weakest criterion was reading time. Mitigation: three sentences per lens and a 700-word cap.
- **Convergence.** One model running seven lenses on one prompt tends toward seven framings of one answer, then adds tension to fit the format. Mitigation: committed stances, independence and anti-manufacture guards, and Measure 2 in the release gate.
- **Fidelity drift.** The paper's evidence is per-prompt. Any benefit of the sweep is a project hypothesis and must be described that way.

## What carried over

- The seven methods and the profiles (rewritten for the sweep: routing sections replaced by "What It Notices", "Stay Distinct From", and "Known Risk").
- The boundary pairs, now used to keep lenses distinct rather than to choose between them.
- The claim-class discipline and the evidence boundary.
- DIRECT, as the gate.

## Router-era SKILL logic, for the record

Stage 1: select DIRECT for rewriting, formatting, translation, extraction, straightforward summarization, deterministic conversion, or simple lookup. Stage 2: select one primary mode by dominant reasoning operation (Socrates: clarify; Aristotle: classify; Descartes: decompose; Hegel: reconcile; Hume: test evidence; Plato: abstract; Kant: conditions and limits). Stage 3: optionally add one secondary mode with a distinct function, applied in sequence (preferred: Socrates → Descartes, Socrates → Hume, Aristotle → Kant, Hume → Plato, Socrates → Hegel). Route by reasoning operation, never by topic or keyword. Keep routing internal except in diagnostics.
