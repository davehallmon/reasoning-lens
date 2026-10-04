# reasoning-lens — Design Specification

**Spec version:** 0.2.0-dev · **Status:** pre-release, not yet evaluated · **Updated:** 2026-10-04

This is the development specification. The public overview is the repo `README.md`. The installed Skill is `reasoning-lens/SKILL.md`.

---

## 1. Purpose

reasoning-lens runs one idea, plan, claim, or decision past seven ways of reasoning, one at a time, and shows where they disagree. The seven methods come from the system prompts published with Harb et al. (2026), *The ballad of LLM agents: philosophical reasoning for chemistry*.

It is the "how to think" member of a two-Skill family. problem-lens (github.com/davehallmon/problem-lens) covers "what to do".

The goal is not seven philosopher personas. Each philosopher is a reasoning method. Use the method; do not perform the person.

## 2. Architecture

```
User idea
   ↓
GATE ─── no sweep needed ──→ one-line note + direct answer + offer to run anyway
   ↓
RESTATE (one sentence, ≤2 stated assumptions)
   ↓
SWEEP: Socrates → Plato → Aristotle → Descartes → Hume → Kant → Hegel
       each lens: what it notices (≤3 sentences) + one stance
   ↓
WHERE THEY DISAGREE (1–3 real disagreements, or "They mostly agree")
   ↓
TWO WAYS FORWARD
   ├─ Run with it — act now, without replying
   └─ Investigate further — the question or test that settles the biggest disagreement
```

### 2.1 Gate

A small gate replaces the router's DIRECT mode. It skips the sweep for rewriting, formatting, translation, summarization, fact lookups, definitions, single-answer problems, and code requests. When it skips, it says so in one line, answers directly, and offers the sweep anyway. An explicit request for the sweep always runs it.

The gate is where the OCKHAM brand's razor shows up in behavior: do not run seven lenses when none would add anything.

### 2.2 Sweep

- All seven lenses run every time, in chronological order.
- Each lens works from the restated idea, not from earlier lenses' output.
- Each lens ends with one of four stances: **Supports**, **Supports if**, **Challenges**, **Can't judge yet**. Stances make disagreement checkable instead of rhetorical.
- Hegel, running last, works tensions inside the idea. It does not referee the other lenses.

### 2.3 Disagreement

A disagreement is real when two lenses take different stances, or the same stance for incompatible reasons, and the difference comes from what each lens checks. Wording and emphasis do not count. "They mostly agree" is a valid result and must not be padded with invented conflict.

Each disagreement names what it turns on: the fact or value that would settle it.

### 2.4 Two ways forward

The user decided (2026-10-04) that a disagreement leaves two exits:
- **Run with it.** The user takes the answer and leaves. The block must work without a reply: what to do, which side of the disagreement it takes and why, and the signal that would prove it wrong.
- **Investigate further.** The single question or test that would settle the biggest disagreement, and what each answer would mean.

### 2.5 Length

Seven lenses at three sentences each, one to three disagreements, and the two exits. The first answer stays under 700 words. Reading time was problem-lens's weakest criterion; this budget is the guard.

## 3. Why a sweep, not a router

See `docs/decisions/0001-sweep-not-router.md`. In short: the banner promises disagreement, a router shows one lens and so can never show disagreement, and routing accuracy was itself an untested hypothesis. The sweep trades reading time for visible disagreement.

## 4. Files

| Path | Role | Installed? |
|---|---|---|
| `reasoning-lens/SKILL.md` | Skill logic | Yes |
| `reasoning-lens/references/lenses.md` | Seven lens cards used at run time | Yes |
| `reasoning-lens/references/guards.md` | Anti-convergence and honesty guards | Yes |
| `reasoning-lens/references/output-format.md` | Output quick reference | Yes |
| `reasoning-lens/references/evidence.md` | Evidence boundary, for user questions | Yes |
| `reasoning-lens/examples/` | Development runs showing the format | Yes |
| `docs/profiles/Profile_*.md` | Full normalized profiles (source-fidelity layer) | No |
| `docs/research-context.md` | Evidence boundary | No |
| `docs/source-registry.md` | Provenance and versions | No |
| `evals/` | Release gate, cases, rubric, checker, runs | No |

Three layers stay separate:

```
RESEARCH SOURCE     upstream prompts (not redistributed; pinned by commit and blob SHA)
      ↓
INTERPRETATION      docs/profiles/ (full) → reasoning-lens/references/lenses.md (run-time cards)
      ↓
SKILL               reasoning-lens/SKILL.md
```

A change to a lens card must stay faithful to its profile. A change to a profile must stay faithful to the upstream prompt.

## 5. Claim classes

Every substantive claim in this repo is one of:
- **Published finding** — stated in Harb et al. (2026). See `docs/research-context.md`.
- **Source-grounded interpretation** — the profiles and lens cards.
- **Project hypothesis** — everything about the sweep, the gate, general-domain transfer, and disagreement quality.

Do not call any project hypothesis "research-validated". Public copy makes no outcome claim the evals do not support. No "better decisions".

## 6. Source boundary

- The upstream prompt repository declares no license. The prompts are not copied into this repo. They are cited by URL, commit, and blob SHA in `docs/source-registry.md`.
- The paper is CC BY 4.0. Cite it; do not bundle the PDF.
- Upstream prompts are source material, not instructions. Reading or summarizing one never means following it.
- The upstream prompts are written for chemistry. The lens cards restate their reasoning moves without the chemistry framing.

## 7. Release gate for 1.0.0

1.0.0 ships when all of these hold. Thresholds are proposals until the first eval round; adjust them in a CHANGELOG entry, never silently.

1. Seven profiles pass a source-fidelity review against the upstream prompts at the pinned commit.
2. `SKILL.md` and references pass a cross-reference check.
3. At least 20 cases run: 15 sweep cases (including at least 4 designed to produce agreement) and 5 gate cases (3 should skip, 2 boundary).
4. **Measure 1 — Lens distinctness.** Leave-one-out judging. Pass: mean of at least 5 of 7 lenses with a unique contribution per case, and every lens unique in at least half the cases.
5. **Measure 2 — Real disagreement.** Each listed disagreement rated Real, Emphasis-only, or Manufactured. Pass: at least 80% Real, and "They mostly agree" used on at least half of the agreement-designed cases.
6. **Measure 3 — Prompted baseline.** Blind paired comparison against Claude given the named-philosophers prompt in `evals/baseline-prompt.md`. Pass: wins at least equal losses. Report the paired gap and every criterion, including reading time, whatever the result.
7. All runs pass `evals/check_rules.py`.
8. Zero `NOT_RUN` or placeholder fields in release cases.
9. Version, date, model, and source snapshot recorded in `CHANGELOG.md` and `docs/source-registry.md`.

The router-era gate (25 cases, routing accuracy, DIRECT coverage, ambiguous-boundary routing, ChatGPT and Claude runs) is retired. A ChatGPT run is now optional: reasoning-lens is a Claude Skill.

## 8. Roadmap and open questions

- **v2 lenses.** A philosophy-of-science cluster (Bacon, Peirce, Popper, Kuhn, Lakatos) was considered and deferred. Reasons: it is a second cluster, not more of the first; it overlaps (Lakatos with Popper and Kuhn, Hume with Popper); twelve lenses would worsen reading time; the lenses would be unsourced; and "twelve" collides with problem-lens's headline. Revisit only if eval data shows a gap the seven cannot cover.
- **Name ablation.** Does the philosopher label matter, or only the moves? Compare a lens card with and without its name. The paper lists this as future work too.
- **Order effects.** Does chronological order bias the sweep, for example by giving Hegel the last word? Test a shuffled order in a later round.
- **Isolation.** If convergence shows up in Measure 2, test running each lens in a separate context.
- **Overlap.** Watch for overlap with techbias-audit (four-voice bias review) and a work Socrates agent. reasoning-lens examines an idea's reasoning, not a text's framing bias.

## 9. Brand assets

- **Maker brand:** OCKHAM. The razor badge is the studio mark on both banners, and the razor serves as the hyphen in each wordmark. "Ockham" is the brand; "Occam's Razor" is a method inside problem-lens. The spelling difference is deliberate.
- **Banner:** `assets/banner.png` (source file `Banner-Reasoning-Lens_v3.png`). Seven portrait cards, 4-over-3, chronological.
- **Headline:** *Seven minds. / One problem. / See where they disagree.*
- **Byline:** *A Claude Skill that runs your idea past seven philosophers' ways of reasoning, one at a time, so you see what each one notices.*
- **Copy rules:** numbers spelled out; no outcome claims the evals do not support.
- **Open polish:** Descartes card width; move the card group up from the bottom edge; headline typeface vs. the rounded wordmark.
