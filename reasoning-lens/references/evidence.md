# Evidence

Read this when the user asks whether the sweep works, or what it is based on. Keep the three classes of claim apart.

## Published finding

Harb et al. (2026), *The ballad of LLM agents: philosophical reasoning for chemistry*, *Machine Learning: Science and Technology* 7, 030503. DOI: 10.1088/2632-2153/ae792d.

- The study tested seven philosophy-inspired system prompts (Socrates, Plato, Aristotle, Descartes, Hume, Kant, Hegel), one at a time, on 243 open-ended numerical chemistry questions from ChemBench.
- Models: GPT-4o, GPT-5, and GPT-5.1. Single turn, no tools, no retrieval.
- Some prompts raised accuracy over the base model. At the strict 1% error threshold, the abstract reports +11.5 points for GPT-4o with Hume, +4.5 for GPT-5 with Kant, and +21.8 for GPT-5.1 with Socrates.
- No single prompt was best across all models, task types, and subdomains.
- The authors note failure modes for some prompts on this benchmark, naming Hegel and Plato as examples.

## Source-grounded interpretation

The lens cards in `lenses.md` restate the reasoning moves in those prompts for ideas outside chemistry. They are this project's reading of the prompts, not the authors' text.

## Project hypothesis (not tested by the study)

- That these reasoning methods help outside chemistry.
- That running all seven in sequence is useful.
- That the disagreements the sweep finds are informative.
- That the sweep beats asking Claude for "several philosophical perspectives" directly.

The study did not test sequences, combinations, or a sweep. The authors list agent routing and multi-agent deliberation as future work. This Skill's own evaluation status is in the repo's `evals/` folder.

If asked, say plainly: the reasoning methods come from a published study; using all seven together on general ideas is this project's untested extension.
