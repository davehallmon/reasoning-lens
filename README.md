# reasoning-lens

![reasoning-lens banner: Seven minds. One problem. See where they disagree.](assets/banner.png)

![Version](https://img.shields.io/badge/version-0.2.0-orange)
![Status](https://img.shields.io/badge/status-experimental%2C%20evaluation%20pending-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple)

A Claude Skill that runs your idea past seven philosophers' ways of reasoning, one at a time, so you see what each one notices, and where they disagree.

> **Experimental pre-release (0.2.0).** No eval rounds have run yet. See [How It Will Be Tested](#how-it-will-be-tested).

## Why

Ask for "a few perspectives" and you usually get one answer said seven ways. reasoning-lens makes each lens commit to a stance, then lists only the disagreements that come from what each lens actually checks. When the lenses agree, it says so instead of inventing conflict.

The seven reasoning methods come from a published study: Harb et al. (2026), *The ballad of LLM agents: philosophical reasoning for chemistry*. The study turned seven philosophers' methods into system prompts and tested each one alone on chemistry questions. reasoning-lens applies all seven, in sequence, to general ideas. That extension is this project's hypothesis, not the study's finding.

## What It Does

- Restates your idea in one sentence, with any assumptions stated.
- Runs seven lenses in order: Socrates, Plato, Aristotle, Descartes, Hume, Kant, Hegel. Each says what it notices in three sentences or fewer and commits to a stance: **Supports**, **Supports if**, **Challenges**, or **Can't judge yet**.
- Lists one to three real disagreements, each with the fact or value it turns on. Or says "They mostly agree."
- Gives you two ways forward:
  - **Run with it:** what to do now, which side it takes, and the signal that would prove it wrong. Usable without replying.
  - **Investigate further:** the one question or test that would settle the biggest disagreement.
- Skips the sweep for rewrites, lookups, definitions, code, and one-answer problems. It answers directly and offers the sweep anyway.

## The Lenses

| Lens | Method | Asks |
|---|---|---|
| Socrates | clarify and question | Are we examining the right idea, stated clearly? |
| Plato | find the deeper pattern | What structure lies under this, and is the visible version only a partial view? |
| Aristotle | classify and explain | What kind of thing is this, and what causes it? |
| Descartes | break it down and check | Can this be built from reliable parts, in order, and verified? |
| Hume | test the evidence | What is observed, what is inferred, and how confident should we be? |
| Kant | examine conditions and limits | What must already be true for this to work, and where does it stop applying? |
| Hegel | work the contradiction | Where does this pull against itself, and what fuller version keeps what is right on each side? |

These are reasoning methods, not characters. The Skill never writes in a philosopher's voice.

## Sample Output

See [`reasoning-lens/examples/ai-training-gate.md`](reasoning-lens/examples/ai-training-gate.md): should an org require a four-hour AI course before granting Copilot access? This is a development run written to show the format, not eval evidence.

## Install

The Skill lives in the `reasoning-lens/` folder of this repo. Install that folder, not the whole repo.

### claude.ai

1. Clone this repo.
2. From the repo root, zip the Skill folder: `zip -r reasoning-lens.zip reasoning-lens`
3. In claude.ai, turn on code execution in Settings.
4. Go to **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**. Upload `reasoning-lens.zip`.
5. Ask: "Run the lenses on this: ..."

Uploaded Skills apply to your account, not to a single Project.

### Claude Code (personal)

1. Clone this repo.
2. Copy the `reasoning-lens/` folder into `~/.claude/skills/`.
3. Restart Claude Code.
4. Ask: "Run the lenses on this: ..."

### Claude Code (project)

1. Clone this repo.
2. Copy the `reasoning-lens/` folder into `.claude/skills/` in your project repo.
3. Restart Claude Code.
4. Ask: "Run the lenses on this: ..."

## Requirements

- **Claude access** with Skills support: claude.ai with code execution on, or Claude Code.
- **An idea to examine:** a plan, claim, proposal, or decision, with some background.
- **No dependencies.** The Skill is Markdown only. The `evals/` folder holds a maintainer-only checker that is not part of the install.

## Try First

Run the lenses on this: we should replace our annual performance reviews with quarterly check-ins.

Background: 400 employees. Managers say the annual review takes too long; we have no data on whether it changes performance.

## How It Will Be Tested

Before 1.0.0, the Skill must pass a pre-registered evaluation, [`evals/PROTOCOL.md`](evals/PROTOCOL.md). The method and thresholds were fixed before any output was generated.

The key test is whether the Skill's structure earns its place. The full Skill is compared with Claude given the same seven lens cards but none of the orchestration (no committed stances, no disagreement test, no two ways forward). Plain Claude and Claude given only the philosophers' names complete the comparison, to show whether the value comes from the names, the cards, or the structure. Judges from a different model family score the outputs blind on two things:

1. **Disagreement calibration:** does it find the disagreements that matter, and avoid inventing them when the idea is sound?
2. **Resolution condition:** does it name the fact, value, or test that would settle the main uncertainty?

Length is measured, not judged, and the Skill fails the bar if it wins only by saying more. All runs, scores, and caveats will be in [`evals/`](evals/), including rounds that lose. Until then, treat the Skill as an experiment.

## Evidence

| Claim | Class |
|---|---|
| Individual philosophy-inspired prompts changed accuracy on numerical chemistry questions, and no single prompt was best everywhere. | Published finding (Harb et al., 2026) |
| The lens cards capture those prompts' reasoning moves outside chemistry. | This project's interpretation |
| Running all seven in sequence, and showing where they disagree, helps you think about an idea. | This project's hypothesis, untested |

Details: [`docs/research-context.md`](docs/research-context.md).

## When Not To Use

- You want one quick answer, not seven angles.
- The task is a rewrite, a lookup, or code.
- You need a ranked list of options and a first step. Use [problem-lens](https://github.com/davehallmon/problem-lens) for that.

## The Family

reasoning-lens is one of two Skills from OCKHAM:

| Skill | Question | Shape |
|---|---|---|
| [problem-lens](https://github.com/davehallmon/problem-lens) | What should I do? | Twelve lenses, six ranked moves, one first step |
| reasoning-lens | How should I think about this? | Seven methods, one idea, the disagreements |

## Credits

The seven reasoning methods are summarized from the system prompts published by Hassan Harb, Yunkai Sun, Mustafa Unal, Nicholas Chia, Zhenzhen Yang, Brian Ingram, and Rajeev Surendran Assary with *The ballad of LLM agents: philosophical reasoning for chemistry*, Mach. Learn.: Sci. Technol. 7, 030503 (2026), DOI [10.1088/2632-2153/ae792d](https://doi.org/10.1088/2632-2153/ae792d). Original prompts: [HassanHarb92/Sci_reasoning_LLMs](https://github.com/HassanHarb92/Sci_reasoning_LLMs).

This project is independent and not endorsed by the authors. The original prompts are not redistributed here. See [`NOTICE.md`](NOTICE.md).

## Contributing

See `CONTRIBUTING.md`. Design spec: [`docs/DESIGN.md`](docs/DESIGN.md).

## License

MIT for the original work in this repo. See `LICENSE` and `NOTICE.md`.
