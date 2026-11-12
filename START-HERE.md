# Research Distressed Screen

Built by Otterd for the Greywolf research and credit team. Open this file first.

It gives a first look at a distressed name in one page: **yes, no or watch** against your own
criteria and return thresholds, the top three red flags, the reasons to buy, and what would change the
view, with every figure linked to its source page. You said analysts can spend hours on a deep dive
before they find a red flag such as too much leverage or weak free cash flow; this comes first, so the
hours go to the names that deserve them. The screen suggests; the analyst decides. It never changes the
pipeline spreadsheet.

This is the first version, from the on-site sessions on 10 and 12 Nov. It changes as you use it and tell us what to fix.

## Before you start

- [ ] **Compliance has said what may go into this project.** Until then: public names and public filings
      only. No pipeline names, positions, prices from the pipeline sheet or internal views.
- [ ] **Your criteria are written down** in `criteria.md` (the onboarding helps you fill it in).

## Set it up (pick one)

**In the Claude app (claude.ai or the desktop app), as a Project**

1. Create a new Project. Name it "Research Distressed Screen".
2. Open `CLAUDE.md`, copy everything in it, and paste it into the Project's **Instructions**.
3. Add every other file in this folder, and the files in `data/`, to the Project's files.
4. Go to **Settings, Capabilities, Skills** and upload `skills/cited-answer.zip` and `skills/name-brief.zip`.
   Turn on code execution if your workspace allows it, so Claude can work out ratios in code.
5. Start a chat in the Project and type **start**.

**In Claude Code or Cowork, as a folder**

1. Unzip this folder where you keep your work.
2. Open the folder in Claude Code (or `cd` into it and run `claude`), or choose it in Cowork.
3. Type **start**. `CLAUDE.md` and the skills in `.claude/skills/` load by themselves.

The first chat is a short onboarding: about ten minutes of questions, then a first try on an example.

## Name briefs and the research board

The `name-brief` skill keeps one public name current as a facts page (with a Debt tab) and a lenses
page, and the research board shows what lands next, names by lane, and if-then bets. Every figure
links to its source quote.

**See the sample:** open `sample-board/board.html` in this folder (double-click it), then click **Open
brief** on a name. Nothing to install. Corvane, and every name marked fictional, is made-up sample data;
WD-40 is a real public name.

**Make your own:** in Cowork or Claude Code, with this folder chosen, type **brief on <name>** for a
public name, or **show the research board**. Claude builds the pages and saves them in `outputs/`.

## What is in this folder

| File | What it is |
|---|---|
| `START-HERE.md` | This page |
| `CLAUDE.md` | Claude's instructions for this project |
| `onboarding.md` | The first conversation, step by step |
| `workflow.md` | The work, step by step, and what "done" means |
| `rules.md` | What Claude may and may never do here |
| `corrections.md` | Where your fixes go, so the next answer is better |
| `data/` | What Claude reads: the examples, and the files you add |
| `outputs/` | Everything Claude makes: queries, results, answers, pages, logs |
| `criteria.md` | Your screen criteria and return thresholds. You own this file |
| `screen-format.md` | The one-page format and the short line for Slack |
| `skill-cited-answer.md` | The cited-answer skill, readable as a project file |
| `skill-name-brief.md` | The name-brief skill, readable as a project file |
| `VERSIONS.md` | Which version of each skill this copy has |
| `skills/` | Skill zips for the Claude app (Claude Code uses `.claude/skills/`) |
| `sample-board/` | The sample research board and two name briefs. Open `board.html` in a browser |

## Updates

Otterd sends a new copy of this folder when a skill improves. Replace everything except your own files:
`my-setup.md`, `corrections.md`, `criteria.md`, your files in `data/`, and everything in `outputs/`. In the Claude app, upload the new skill zips again.
Questions: ask Hiro or Eric at Otterd.
