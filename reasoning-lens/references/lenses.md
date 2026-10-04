# The Seven Lenses

Each lens is a reasoning method, not a character. The methods are summarized from the seven system prompts published with Harb et al. (2026), *The ballad of LLM agents: philosophical reasoning for chemistry*. The original prompts were written for chemistry. These cards restate their reasoning moves for general ideas. See `evidence.md` for what the study did and did not test.

Run the lenses in this order. Each card has:
- **Asks:** the core question.
- **Moves:** the reasoning operations to apply.
- **Notices:** what this lens tends to catch that others miss.
- **Stay distinct:** how to keep it from collapsing into a neighbor.
- **Watch for:** this lens's typical failure.

---

## Socrates · clarify and question

**Asks:** Are we examining the right idea, stated clearly?

**Moves:** define the key terms; cross-examine the claim for contradictions; test whether it generalizes beyond the example; list competing hypotheses and what would eliminate each; draw out what the user already knows but has not said.

**Notices:** vague terms, a solution offered before the problem is defined, confidence the idea has not earned.

**Stay distinct:** Socrates questions the claim itself. Leave framework conditions to Kant and evidence weight to Hume.

**Watch for:** returning only questions. End with a stance.

## Plato · find the deeper pattern

**Asks:** What structure lies under this case, and is the visible version only a partial view of it?

**Moves:** look for the stable pattern shared across examples; divide the concept into parts, then regroup them; ask whether the current representation (a metric, a label, a story) is a shadow of the real issue; place the local question inside the larger whole.

**Notices:** a metric mistaken for the goal, a local fix for a system-level problem, a pattern that unites scattered cases.

**Stay distinct:** Plato abstracts upward. Leave category boundaries to Aristotle and resolving conflicts to Hegel.

**Watch for:** a grand pattern the evidence cannot carry. Hume will check it.

## Aristotle · classify and explain

**Asks:** What kind of thing is this, and what causes it?

**Moves:** define by class and distinguishing feature; sort the idea into the right category; separate the causes (what it is made of, its form, what drives it, what it is for); separate what is possible from what is actual; lay out the premises that lead to the conclusion; seek the mean between two extremes.

**Notices:** category mistakes, mixed levels of explanation, a missing premise, an idea that treats a means as an end.

**Stay distinct:** Aristotle organizes the object. Leave the validity of the framework to Kant and deeper unifying patterns to Plato.

**Watch for:** tidy categories that hide a real tension.

## Descartes · break it down and check

**Asks:** Can this be built from reliable parts, in order, and verified?

**Moves:** doubt every premise that is not established; make each term clear and distinct; split the idea into parts; solve the simple parts first; rebuild in order; check each step and the final result.

**Notices:** a weak premise the plan depends on, steps in the wrong order, a step that does not follow, no way to verify success.

**Stay distinct:** Descartes checks whether the reasoning and the plan hold together. Leave whether the evidence supports it to Hume.

**Watch for:** precise steps built on an unclear goal.

## Hume · test the evidence

**Asks:** What is observed, what is inferred, and how confident should we be?

**Moves:** separate observation from inference; treat cause as an inference from repeated pattern, not a seen fact; flag extrapolation beyond the observed cases; compare other causes that fit the same evidence; calibrate confidence; keep "is" separate from "ought".

**Notices:** correlation sold as cause, a small or unrepresentative sample, a recommendation that does not follow from the facts.

**Stay distinct:** Hume weighs evidence. Leave logical order to Descartes and the conditions of validity to Kant.

**Watch for:** doubting everything without saying what evidence would be enough.

## Kant · examine conditions and limits

**Asks:** What must already be true for this idea to work, and where does it stop applying?

**Moves:** name the conditions the idea presupposes; separate the framework from the data it organizes; test what stays invariant across perspectives; separate concepts that define the thing from ideas that only guide the search; mark the limits beyond which the idea cannot support a conclusion.

**Notices:** hidden preconditions, a measure that only means something inside one framework, a conclusion stretched past its scope.

**Stay distinct:** Kant examines the framework that makes a claim valid. Leave the immediate claim to Socrates and category sorting to Aristotle.

**Watch for:** listing conditions without saying which one matters most.

## Hegel · work the contradiction

**Asks:** Where does this idea pull against itself, and what fuller version keeps what is right on each side?

**Moves:** state the idea's first, simple form; find the specific point where it undermines itself; state what the opposing view gets right; judge the idea by its own commitments; build a fuller version that keeps the valid parts and drops the rest.

**Notices:** a self-defeating goal, a false either/or, two sides that are each right about different conditions.

**Stay distinct:** Hegel works tensions inside the idea. It does not referee the other lenses; that happens in "Where They Disagree". Leave abstraction without conflict to Plato.

**Watch for:** forcing a synthesis where a plain choice is better.
