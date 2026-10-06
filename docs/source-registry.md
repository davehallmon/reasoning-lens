# Source Registry

## Release metadata

| Field | Value |
|---|---|
| Project | reasoning-lens (formerly "Philosophical Reasoning Router") |
| Version | 0.2.0 |
| Release status | experimental pre-release; Round 1 evaluation pending |
| Architecture | sweep (see `docs/decisions/0001-sweep-not-router.md`) |
| Public repo | github.com/davehallmon/reasoning-lens |
| Last verification | 2026-10-04 |
| Evaluation protocol | `evals/PROTOCOL.md` v1.0.0, frozen 2026-10-04 |
| Production validation | not run; 1.0.0 requires a Round 1 Strong pass (`evals/PROTOCOL.md`) |

## Research source

- **Paper:** Harb et al. (2026), *The ballad of LLM agents: philosophical reasoning for chemistry*, Mach. Learn.: Sci. Technol. 7, 030503.
- **DOI:** 10.1088/2632-2153/ae792d
- **License:** CC BY 4.0. A reference copy of the paper is kept in `docs/research/` with attribution (see `docs/research/README.md`). The upstream prompts are cited, not bundled.

## Upstream prompt snapshot

| Field | Value |
|---|---|
| Repository | HassanHarb92/Sci_reasoning_LLMs |
| URL | https://github.com/HassanHarb92/Sci_reasoning_LLMs |
| Branch | main |
| Commit | `0682e819a19e3371c8f9d5c3ecd308a9cd0ea1cb` |
| First retrieved | 2026-10-01 |
| Verified | 2026-10-04 (rechecked at release: commit is still `main` HEAD, all blob SHAs below match, no license file) |
| License | none declared as of 2026-10-04 |

Because no license is declared, the prompts are **not redistributed** in this repo. The private development workspace keeps local copies (`.txt` renamed to `.md`, content unchanged) for source-fidelity review only.

| Lens | Upstream path | Blob SHA |
|---|---|---|
| Socrates | `sys_prompts/socrates.txt` | `fc61c1ef5aed21547ca1c0744a40db366308b7fb` |
| Plato | `sys_prompts/plato.txt` | `2c07d0f50dc3b7ce04d4dc63057c0ce462dd98a2` |
| Aristotle | `sys_prompts/aristotle.txt` | `74d1b3ba21a51ad3a2b42e9b24adbbeb3dfb4b77` |
| Descartes | `sys_prompts/descartes.txt` | `ccd51cfe441b958c701ce4224f47a87069dbb043` |
| Hume | `sys_prompts/hume.txt` | `ba98156b48c959ea382f2b0d20f69213a27548b8` |
| Kant | `sys_prompts/kant.txt` | `41299b56e120cce2fb146ff4a70c8bcacf390298` |
| Hegel | `sys_prompts/hegel.txt` | `9f9394a395050bd98a3c78deaa4ded16fd9a6678` |

## Derived files

| File | What it is | Derived from |
|---|---|---|
| `docs/profiles/Profile_*.md` (v0.2) | Full normalized profiles, sweep model | Upstream prompts; router-era profiles v0.1 |
| `reasoning-lens/references/lenses.md` | Run-time lens cards | Profiles v0.2 |
| `reasoning-lens/SKILL.md` | Skill logic | `docs/DESIGN.md` |
| `evals/cases.md` | Eval corpus 0.2.0 (23 cases) | Router-era `Router_Evaluation_Cases.md` themes, rewritten; injection cases new |
| `evals/baseline-prompt.md` (Cards-only block) | Stripped lens cards: Asks, Moves, Notices | `reasoning-lens/references/lenses.md` at 0.2.0 |

Derived files are project interpretation. They do not replace the upstream prompts.

## Superseded

| File | Superseded by | Note |
|---|---|---|
| `Router_Evaluation_Cases.md` (workspace only) | `evals/cases.md` | Routing cases; never run |
| Router-era `SKILL.md`, `README.md`, `PROJECT_INSTRUCTIONS.md`, profiles v0.1 | Sweep versions | Summary in `docs/decisions/0001-sweep-not-router.md` |

## Brand assets

| File | Source | Note |
|---|---|---|
| `assets/banner.png` | `Banner-Reasoning-Lens_v3.png` | OCCAMI NOVACULA suite mark; see `docs/DESIGN.md` §9 |
| `assets/social-preview.png` | Banner padded to 1280×640 | Upload in Settings → General → Social preview |
