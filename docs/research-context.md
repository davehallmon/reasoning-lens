# Research Context

This file is the evidence boundary for every claim in this repo about published validation.

## Source

Hassan Harb, Yunkai Sun, Mustafa Unal, Nicholas Chia, Zhenzhen Yang, Brian Ingram, and Rajeev Surendran Assary (2026). *The ballad of LLM agents: philosophical reasoning for chemistry.* Machine Learning: Science and Technology 7, 030503. DOI: [10.1088/2632-2153/ae792d](https://doi.org/10.1088/2632-2153/ae792d). Open access, CC BY 4.0.

Prompts and data: [github.com/HassanHarb92/Sci_reasoning_LLMs](https://github.com/HassanHarb92/Sci_reasoning_LLMs).

## What the study tested

- Seven philosophy-inspired fixed system prompts: Socrates, Plato, Aristotle, Descartes, Hume, Kant, Hegel.
- GPT-4o, GPT-5, and GPT-5.1.
- 243 open-ended numerical ChemBench questions.
- Single-turn runs, no retrieval, no external tools, no persistent memory.
- Each prompt alone. No routing, no combinations.

## What the study found

- Different prompts produced different performance patterns depending on model, task type, and chemistry subdomain.
- The abstract reports, at the strict 1% error threshold and relative to each base model: +11.5 points for GPT-4o with Hume, +4.5 for GPT-5 with Kant, and +21.8 for GPT-5.1 with Socrates.
- No single prompt dominated every condition.
- The authors note failure modes for some prompts on this benchmark, naming Hegel and Plato.
- The repository also includes a generic scientific-reasoning control, a chemistry-expert control, and prompt-rephrasing robustness tests, reported in the paper's Supporting Information.

## What the authors list as future work

- Adaptive agent selection (routing) and multi-agent deliberation.
- Combining agents when a question needs mixed reasoning styles.
- Ablations testing whether results depend on philosopher names, coherent principles, or structure in general.
- Domains and benchmarks beyond ChemBench.

## What the study did not test

- Use outside chemistry, including workplace, writing, strategy, management, education, or software decisions.
- Running all seven prompts on one input.
- Sequences or combinations of prompts.
- A gate that decides when no prompt is needed.
- Disagreement among prompts as an output.
- Comparison with a named-philosophers prompt like reasoning-lens's baseline.

## Evidence boundary for this project

The study supports claims about individual philosophy-inspired prompts under its chemistry benchmark conditions.

The sweep, the gate, the stances, the disagreement step, the two ways forward, the lens cards, and general-domain use are this project's hypotheses. Do not describe them as research-validated unless this repo's own evals support the specific claim. Current eval status: see `evals/README.md`.
