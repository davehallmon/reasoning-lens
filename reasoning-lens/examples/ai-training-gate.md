# Example: AI Training Gate

> **Development run, not eval evidence.** Written in the same session that wrote the Skill, to show the format. Recorded eval runs live in `evals/runs/`.

## Input

Run the lenses on this: our org should require a four-hour AI literacy course before anyone gets Copilot access.

Background: about 3,000 employees. In our 200-person pilot, people who took the course rated Copilot more useful in the end-of-pilot survey.

## Output

**The idea:** Require a four-hour AI literacy course before any employee gets Copilot access. Assuming the course covers both data handling and productive use.

### Seven Lenses

**Socrates · clarify and question** — "AI literacy" is doing a lot of work here. Is the gate meant to ensure safe use, productive use, or proof of compliance? Each goal implies a different course and a different length.
Stance: **Can't judge yet** — the goal behind the gate is not stated.

**Plato · find the deeper pattern** — The gate treats course completion as if it were competence. Completion is a stand-in; what matters is judgment in daily work, and that skill tends to grow through use with feedback, not before use.
Stance: **Challenges** — it gates on the stand-in, not the skill.

**Aristotle · classify and explain** — A prerequisite is a control, not enablement. Controls fit high-risk, hard-to-reverse actions. Most Copilot drafting is low-risk and reversible; pasting sensitive data is not.
Stance: **Supports if** — the gate covers only the high-risk uses.

**Descartes · break it down and check** — The plan rests on one premise: four hours of training changes behavior. Split it into content, completion, behavior, and outcome, and only completion gets measured.
Stance: **Challenges** — no step checks that behavior changes.

**Hume · test the evidence** — The pilot shows trained users rated Copilot higher. It does not show the course caused that. People who chose the course may have been early fans, and a survey rating is not observed use.
Stance: **Challenges** — the pilot cannot carry a mandate for 3,000 people.

**Kant · examine conditions and limits** — A gate is legitimate when it applies one rule to everyone and protects something the org must protect, such as data handling and accountability. That condition holds for the data-handling part, not the productivity part.
Stance: **Supports if** — the required part is limited to what the org must enforce.

**Hegel · work the contradiction** — The idea undercuts itself: a course meant to speed adoption delays it for 3,000 people. The control side is right that untrained use carries risk; the access side is right that skill comes from use.
Stance: **Supports if** — the gate shrinks to the risk it exists to cover.

### Where They Disagree

- **Plato vs. Aristotle** — Plato says any course gate measures the wrong thing / Aristotle says a gate fits the high-risk uses. Turns on: whether a short module changes data-handling behavior or only records completion.
- **Hume vs. Kant** — Hume says the pilot cannot justify a mandate / Kant says a narrow data-handling rule needs no outcome evidence, because it is an accountability condition. Turns on: whether the requirement is a productivity bet or a governance rule.

**Where they agree:** four hours for everyone, before any access, is more than either the evidence or the risk supports.

### Two Ways Forward

**Run with it.** Replace the four-hour prerequisite with a short required module on data handling and acceptable use, then grant access. Move the rest of the course into the first weeks of real use. This takes Kant's side: the gate is a governance rule, not a productivity bet. You are wrong if incidents involving sensitive data rise in the first 60 days.

**Investigate further.** Compare usage logs, not survey ratings, for pilot users who started at the same time with and without the course. If trained users use Copilot more and better, Hume's objection weakens and a longer course has a case; if not, the course is measuring enthusiasm.

Reply with a lens name to expand it, or "investigate" to work the open question together.
