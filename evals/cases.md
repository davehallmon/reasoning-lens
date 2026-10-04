# Eval Cases

**Corpus version:** 0.2.0 · **Status:** no rounds run yet

Twenty cases: 11 contested sweep cases, 4 agreement-designed sweep cases, 3 gate-skip cases, and 2 gate-boundary cases. Several carry over themes from the router-era corpus (noted as "from R-0xx").

"Watch for" notes guide judges. They are not answer keys. A run that finds something better than the note is fine.

Types:
- `contested` — the lenses should split.
- `agree` — a sound idea; most lenses should support it. Tests that the Skill does not invent conflict.
- `gate-skip` — the Skill should skip the sweep.
- `gate-boundary` — either choice is defensible; the judge records which was better.

---

## Contested

### S01 · readiness score · `contested` (from R-009)
**Message:** Run the lenses on this: our L&D team wants to use the new "AI readiness score," a 10-question self-assessment, to decide who gets advanced AI training first.
**Watch for:** "readiness" undefined (Socrates); self-report as a proxy (Plato, Hume); what the score can validly support (Kant).

### S02 · vague training request · `contested` (from R-002)
**Message:** Run the lenses on this: a VP asked me for "AI training" for her 40-person team by next month. I'm planning to build a two-hour Copilot prompting workshop.
**Watch for:** solution chosen before the problem is defined; whether a workshop fits the kind of need.

### S03 · central vs. departmental AI · `contested` (from R-005)
**Message:** Run the lenses on this: one team wants a central AI center of excellence that approves every use case; another wants each department to own its own AI tools. I'm leaning toward the central model.
**Watch for:** a real tension (Hegel); risk categories that might split the decision (Aristotle).

### S04 · four-hour ticket rule · `contested` (from R-014)
**Message:** Run the lenses on this: a study of our help desk found tickets closed in under four hours have 30% higher satisfaction (n = 5,000). Leadership wants a rule that every ticket must close within four hours.
**Watch for:** correlation vs. cause, easy tickets close fast (Hume); a target that corrupts the measure (Plato, Kant).

### S05 · firewall rollback · `contested` (from R-013)
**Message:** Run the lenses on this: our nightly data load started failing the day after IT changed the firewall rules. I want to ask IT to roll back the firewall change.
**Watch for:** timing as evidence of cause (Hume); a cheaper check before rollback (Descartes).

### S06 · customer-data risk split · `contested` (from R-011)
**Message:** Run the lenses on this: I want to classify all our AI use cases as "low risk" (auto-approved) or "high risk" (review board) based only on whether they touch customer data.
**Watch for:** a single criterion for a multi-factor category (Aristotle); what the binary misses (Kant).

### S07 · executive sponsor framework · `contested` (from R-006)
**Message:** Run the lenses on this: all five of our successful AI pilots had an executive sponsor. I'm writing a framework that makes executive sponsorship the first requirement for any pilot.
**Watch for:** five successes and no failures examined (Hume); pattern vs. survivorship (Plato vs. Hume).

### S08 · ADKAR vs. retrospectives · `contested` (from R-015)
**Message:** Run the lenses on this: our change team uses ADKAR; our engineers use agile retrospectives. I'm proposing we standardize on ADKAR for the AI rollout.
**Watch for:** whether the two models conflict or answer different questions (Hegel vs. Plato).

### S09 · hours-saved metric · `contested` (from R-007)
**Message:** Run the lenses on this: we'll report "hours saved by Copilot" to the board, calculated as self-reported minutes saved per week × active users × 52.
**Watch for:** what the number can legitimately claim (Kant); self-report and extrapolation (Hume).

### S10 · career move · `contested`
**Message:** Run the lenses on this: I'm thinking of leaving a stable corporate job to teach full time at a community college, because students rate my evening courses highly.
**Watch for:** ratings as evidence of fit for full-time teaching (Hume); what "stable" and "fit" mean to the user (Socrates).

### S11 · degrees obsolete · `contested`
**Message:** Run the lenses on this: my op-ed argues AI will make college degrees obsolete within ten years, because employers are dropping degree requirements.
**Watch for:** the causal link from AI to dropped requirements (Hume); "obsolete" undefined (Socrates); degrees serve several functions (Aristotle).

## Agreement-designed

### A01 · backup before migration · `agree`
**Message:** Run the lenses on this: before migrating our team's shared drive to SharePoint, we'll back it up to a second location and test a restore.
**Watch for:** "They mostly agree." Minor conditions are fine; invented conflict is a failure.

### A02 · pilot before rollout · `agree`
**Message:** Run the lenses on this: I'm going to pilot the new onboarding checklist with one team for a month before rolling it out to all twelve.
**Watch for:** agreement, possibly "Supports if" on how success is measured.

### A03 · legal review of AI contract · `agree`
**Message:** Run the lenses on this: before our vendor signs, I want our legal team to review the data-processing terms in the AI contract.
**Watch for:** agreement. Conflict here is almost certainly manufactured.

### A04 · password file scan · `agree`
**Message:** Run the lenses on this: our policy says passwords belong in the password manager, not spreadsheets. I want to enforce it by scanning shared drives for files with "password" in the name.
**Watch for:** agreement on a challenge: the method misses most cases. Most lenses should land on "Challenges" or "Supports if". A split here would need a strong reason.

## Gate

### G01 · rewrite · `gate-skip`
**Message:** Make this shorter: "I wanted to reach out to let you know that we will be moving the meeting that was originally scheduled for Tuesday to Thursday instead."
**Watch for:** skip, one-line note, good rewrite.

### G02 · definition · `gate-skip`
**Message:** What's the difference between a mean and a median?
**Watch for:** skip and a correct answer.

### G03 · code · `gate-skip`
**Message:** Write a Python function that removes duplicates from a list but keeps the original order.
**Watch for:** skip and working code.

### G04 · summarize and find gaps · `gate-boundary`
**Message:** Summarize this policy and tell me if it has gaps: "Employees may work remotely up to three days per week with manager approval. Managers must respond to requests within five business days."
**Watch for:** either a direct answer that finds the gaps, or a sweep that justifies its length.

### G05 · chart choice · `gate-boundary`
**Message:** Should I use a bar chart or a line chart for monthly sales over two years?
**Watch for:** likely a skip; a sweep would need to add something real.

---

## Run log

| Round | Version | Date | Model | Cases run | Result |
|---|---|---|---|---|---|
| — | — | — | — | 0 | NOT_RUN |
