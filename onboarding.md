# Onboarding

Run this the first time someone opens the project. Ask one question at a time and wait for the answer.
Keep it to about ten minutes. Use plain words.

## 1. Say hello

In three lines: this project gives a first look at a distressed name against the team's own criteria, in one page, with sources. Setup takes about ten minutes. Nothing is sent anywhere without them.

## 2. Check the setup

- Claude app: are `workflow.md`, `rules.md` and the `data/` files in the project files? If not, point them
  to step 3 of `START-HERE.md`.
- Skill: is `cited-answer` loaded, and can you run code here? If not, say that ratios will be shown as
  formulas for them to check.

## 3. Ask

1. **Your role, and one name you would like screened first.** For now it must be a public name with public filings.
2. **How long does a first look at a new name take today, and how often does a new name come in?**
3. **What makes a name a yes?** Take them through `criteria.md`: the return threshold, the hard limits (for example leverage or liquidity), and what they look for. Fill in the file as they answer. A hard limit is a number with a unit.
4. **Where should the result go?** One page for the team, a short line for Slack, or a draft in the memo template later.
5. **Who checks a screen before it counts?** Usually the trader who keeps the pipeline, or the PM.
6. **What has compliance approved for this project?** If nothing yet: public names and public filings only.

## 4. Write the setup

Write `my-setup.md` in this format. In Claude Code, save it in this folder. In the Claude app, show it
and ask them to save it as a project file named `my-setup.md`.

```
# My setup
Date:
Role:
First task:
Today it takes:         (time per item, and how often)
Criteria filled in:     yes | partly
Output wanted:          one page | Slack line | both
Who checks:
Approved by compliance: (what, by whom, when; or "examples only")
```

## 5. First try (five minutes)

Screen their public name with `workflow.md` and the filled-in `criteria.md`. Gather the latest annual
and quarterly filings they point you to (or ask them to add the files). Save the filings in `data/` and the
page in `outputs/`, in the format of `screen-format.md`, with each figure's source page, each ratio as a formula, and each quote checked
word for word against its filing. If they named a criterion you could not test, say so on the page.

Ask how long that took, against their answer about today. Then ask: was that right, and what would you
change? Put any fix in `corrections.md`.

## 6. What to ask next

End with three requests they can copy:

- "Screen <public name> against our criteria and give me the one page."
- "Add a new criterion: interest cover below 1.5 times is a red flag, and show me which names it changes."
- "Show me what you got wrong last time."
