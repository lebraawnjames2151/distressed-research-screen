# Lens panels

The panel has eight expert lenses. A name runs four to seven of them, chosen by its situation, plus
the overview part `why-look`. The table that code reads is [panels.json](panels.json); a test keeps
this page and the lens cards in step with it.

## The lenses

| Id | Expert | Question | Reads |
|---|---|---|---|
| `credit-analyst` | Distressed credit analyst | What is owed, to whom, in what order, and when? | Capital structure and debt, Debt timeline, Restructuring terms, Key dates, Gaps |
| `restructuring-counsel` | Restructuring counsel | What is the process, who is bound, which steps are open? | Capital structure and debt, Restructuring terms, Key dates, Gaps |
| `liquidity-treasury` | Liquidity and treasury | How much cash and borrowing room, and what could cut it off? | Capital structure and debt, Results by year, Recent results, Key dates, Gaps |
| `forensic-accountant` | Forensic accountant | How far can the reported figures be relied on? | Results by year, Recent results, Accounting and controls, Gaps |
| `industry-operator` | Industry operator | What drives revenue and costs, and what does the business not control? | Business, Results by year, Recent results |
| `equity-special-sits` | Equity special situations | Who ends up owning what, and what dilutes it? | Capital structure and debt, Restructuring terms, Recent results |
| `catalyst-tracker` | Catalyst tracker | What is dated ahead, and what does each date settle? | Key dates, Recent results, Restructuring terms |
| `skeptic` | Skeptic | Where are the facts thin, in conflict or missing? | all sections |

Each card is in [lens-cards/](lens-cards/). A lens may name a section the name does not have. It then
says so under Not covered, and it reruns when the section appears.

## Panels by situation

| Situation | Use when | Lenses | Often added |
|---|---|---|---|
| `in-court` | A court case is open: chapter 11, CCAA, a scheme or an administration | `credit-analyst`, `restructuring-counsel`, `liquidity-treasury`, `equity-special-sits`, `catalyst-tracker`, `skeptic` | `industry-operator` when one asset carries the value |
| `post-emergence` | The company left a court case or closed an exchange in about the last two years | `credit-analyst`, `forensic-accountant`, `industry-operator`, `equity-special-sits`, `catalyst-tracker`, `skeptic` | `liquidity-treasury` when the exit facility is drawn |
| `pre-default` | A missed payment, a grace period, a waiver, a forbearance, an exchange offer or a support agreement, with no court case | `credit-analyst`, `restructuring-counsel`, `liquidity-treasury`, `forensic-accountant`, `industry-operator`, `catalyst-tracker`, `skeptic` | `equity-special-sits` when the deal issues new equity |
| `single-asset` | One asset, project, permit or contract carries the value | `credit-analyst`, `liquidity-treasury`, `industry-operator`, `catalyst-tracker`, `skeptic` | `forensic-accountant` when going-concern doubt is stated |
| `going-concern` | An operating company that is not in court, with or without stated doubt | `credit-analyst`, `liquidity-treasury`, `forensic-accountant`, `industry-operator`, `catalyst-tracker`, `skeptic` | `equity-special-sits` when convertibles or a rights offering are in the facts |

## Pick one

1. Read the facts page first. Take the first row above that fits, from the top.
2. If a second row also fits, add its lenses as extras. Never run more than eight.
3. Print the parts and put them in `name.json` `parts`:

   ```bash
   node .claude/skills/name-brief/scripts/panel.mjs in-court industry-operator
   ```

   The output is the whole `parts` array: `why-look` first, then each lens as `{ id, title, reads }`.
4. Say in `change-log.md` which situation you chose and why, with the tag of the fact that decides it.
5. When the situation changes (a filing, an emergence), print the new parts, run the lenses that are
   new, and delete the lens parts that left the panel. A lens that stays reruns only if `lens-stale.mjs` says so.

## A new lens

Add it to `panels.json` and write its card with the same six lines (Title, Question, Reads, Look for,
Needs, Must not). Keep the panel at eight or fewer: a new lens replaces one or merges with one.
