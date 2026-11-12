---
name: name-brief
description: Keep one public name's research current as two pages. The facts page has the business, capital structure, one card per debt instrument, results by year, key dates, gaps and sources. The lenses page has a panel of blind expert lenses chosen by the name's situation (in court, pre-default, post-emergence, single asset, or an operating company), what would change each view, where the lenses differ, why the name is worth a look, and a slot for the analyst's own view. Mode new builds both. Mode refresh adds the filings and dated events since the as-of date, reruns only the lenses whose facts changed, and republishes to the same links. Use for "brief on <name>", "name brief", "refresh <ticker>", "what changed on <name>", "update the facts page", or to record an analyst's status on a name. Also builds the research board (countdowns to dated events, names by lane, if-then bets with first, second and third order names) for "build the board", "add a bet", "move <ticker> to watching" or "show the research board".
---

# Name brief

One public name, two pages, public sources only:

- `facts.html`: facts only. Every line has a source tag that links to its quote.
- `lenses.html`: the same facts through four to eight blind expert lenses, plus the analyst's view.

Code builds both pages from one name folder, so a refresh needs no hand edit.
The facts page has two tabs, Facts and Debt; the lenses page ends with the analyst's view.

**The ideal output is [references/output.md](references/output.md).** It lists every part of both
pages and the file that fills it. Build `examples/corvane/` (fictional, every part filled) to see it.
Aim for that page on every name. Fill each part the sources support, and leave a part out (with a
Gaps line) rather than guess.
Formats: [references/formats.md](references/formats.md). Agent briefs: [references/agents.md](references/agents.md).
Panels and lens cards: [references/panels.md](references/panels.md).
Example: [examples/wdfc/](examples/wdfc/). `$N` is `.claude/skills/name-brief/scripts`, run from the repo root.

## Try it

The scripts run from any folder. With no folder, `build-board.mjs` builds the sample board, and
`--open` opens it in the browser:

```bash
node <repo>/.claude/skills/name-brief/scripts/build-board.mjs --open
node <repo>/.claude/skills/name-brief/scripts/build-artifacts.mjs <repo>/.claude/skills/name-brief/examples/corvane
```

`<repo>` is the full path of the clone, for example `~/otterd-clients`. Each script prints the full
path of every page it writes. When you give someone a command, give the full path or a Desktop path,
never a path that only works from the repo root.

## Where the name folder goes

- A public demo: `research/names/<slug>/`.
- A client's own names or data: `<client>/runs/<code-N>/<date>/<slug>/` (`CLAUDE.md`, rules 1 and 7).
  Name the client code before you read or write.
- Never copy a fact or a file between a client folder and `research/`.

## Rules

- Public information only. Never use a fund's own positions, models, notes or logins.
- Every fact line ends with its tags, such as `[S3]`. Each figure on the line is in the quote of a
  tag on that line. A figure in millions may round a quote in thousands. A line that fails is fixed or cut.
- For a table row, quote from the column headers through the row, so the date is in the quote.
- Prefer filings, releases and dockets. Mark news `secondary`.
- Say "not found" and add a Gaps line instead of guessing.
- Plain words, short sentences, no long dashes, no email addresses. The pages refuse both.
- The system never recommends: no price target or range, no confidence score, no buy, sell or hold,
  no judging adjective. A lens
  says what would change its view. The only view on what to do is the analyst's, in `board.json`,
  written by a person. This keeps the `fund-research-pack` rule: never recommend a trade, a vote or an election.
- Never edit a page, a lens part or `lens_inputs` by hand. Fix the facts and run the step again.
- If a site asks for a login, a CAPTCHA or acceptance of terms, stop and ask.
- For EDGAR, set `PACK_USER_AGENT` (a name and contact) in the shell. Never write it into a file.
  Where the network needs a proxy, add `NODE_USE_ENV_PROXY=1`.

## The lens panel

Eight expert lenses, each with a card in [references/lens-cards/](references/lens-cards/): distressed
credit analyst, restructuring counsel, liquidity and treasury, forensic accountant, industry operator,
equity special situations, catalyst tracker and skeptic. A name runs four to seven of them, by its
situation ([references/panels.md](references/panels.md)), plus the overview part `why-look`.

- `node $N/panel.mjs <situation> [extra lens ids]` prints the `parts` array for `name.json`. Each
  part is `{ id, title, reads }`. `reads` names the sections the lens rests on; `lens-stale.mjs` uses it.
- Each lens runs in a fresh context with only `factual-summary.md`, `sources.json`, its card and the
  shared form ([agents.md](references/agents.md)). It sees no other lens.
- Code lists where the lenses differ: each line a lens marked "(assumed)", and each source that more
  than one lens cites, with every lens's line on it. Nothing is weighed, scored or debated. A person
  combines the lenses and writes the view.

## Mode `new`

1. **Folder.** Make the name folder. Copy `examples/wdfc/name.json`, then set the name, ticker,
   exchange, slug, `as_of` (today) and `chart_unit`. Clear `lens_inputs` and `artifacts`.
   Never copy `fictional` from the Corvane example.
2. **Facts.** Start the fact writer ([agents.md](references/agents.md)). Result: `sources.json`,
   `factual-summary.md` (with its Accounting and controls flags), `instruments.json`, `in-brief.md`
   and, when the filings give past balances, `history.json` with interest and flows.
3. **Debt detail.** For each instrument, run `node $N/cap-structure-scan.mjs <filing file or URL>`
   on the whole filing. It lists each term with its sentence, and what is missing. Its sentences
   can be quotes.
4. **Spreads.** Spread at issue is the yield at issue minus a FRED Treasury yield of the same date
   and the nearest term (`DGS2`, `DGS3`, `DGS5`, `DGS7`, `DGS10`). Cite the FRED row as its own
   source. Write the formula and every judgment (term, coupon used as the yield) on the card.
   Current prices come from FINRA TRACE or a data vendor; when none was reached, say so.
5. **Checks.** Run, and fix until each passes:

   ```bash
   node $N/check-facts.mjs <dir>/factual-summary.md <dir>/sources.json
   node $N/check-facts.mjs <dir>/in-brief.md <dir>/sources.json
   node $N/verify-quotes.mjs <dir>
   node $N/instrument-card.mjs <dir>/instruments.json <dir>/sources.json --strict
   ```

   `--strict` fails on any missing card value. A value that cannot be found keeps its `note` and a
   Gaps line; report it rather than invent one.
6. **Verify.** Start the verifier ([agents.md](references/agents.md)), never the author. It writes
   `verification.md`. Fix or cut every failed line, then rerun step 5.
7. **Lenses.** Pick the situation from the verified facts ([panels.md](references/panels.md)), set
   `name.json` `situation`, put the output of `node $N/panel.mjs <situation>` in `name.json` `parts`,
   and note the choice in the change log. Start every part in one message, in parallel: each lens with its card and the shared
   form, the overview with its brief. Save each output unedited as `lens-parts/<id>.md`. Run
   `check-facts.mjs` on each. A part that fails, or runs over 200 words (`wc -w`), is run again in a
   fresh context, never edited. Then record what each read: `node $N/lens-stale.mjs <dir> --record`.
8. **Build.** `node $N/plant.mjs <dir>` must catch every planted error. Then
   `node $N/build-artifacts.mjs <dir>` writes `out/facts.html` and `out/lenses.html`.
9. **Log and publish.** Add a dated entry to `change-log.md`, then publish (below).

## Mode `refresh`

Give it the name folder and today's date. The steps follow `screen-refresh`.

1. **Find what is new.** Read `name.json` `as_of`. List every filing since then (EDGAR: 10-K,
   10-Q, 8-K, 424B, court dockets) and every Key dates line between `as_of` and today.
2. **Add facts.** Start the fact writer with the folder and the list. It adds new sources with the
   next free ids (never reuse an id), adds or changes fact lines, moves passed dates from "expected"
   to what happened, and updates the cards and `in-brief.md`. Keep a superseded fact only as dated history.
3. **Check.** Run step 5 of `new`, with `verify-quotes.mjs <dir> --only S47,S48` for the new
   sources. Run `cap-structure-scan.mjs` on any filing that changes the debt.
4. **Verify.** Run the verifier on the changed lines only, and fix what fails.
5. **Change log.** Add an entry at the top of `change-log.md`: the date, each new fact with its tag,
   each date that passed, and what the verifier changed.
6. **Set the date.** Set `as_of` in `name.json` to today.
7. **Rerun only stale lenses.** If the new facts change the situation (a filing, an emergence),
   print the new parts first and delete the lens parts that left the panel. `node $N/lens-stale.mjs <dir>`
   prints RERUN for each part that is new or whose read sections or cited sources changed. Run only
   those parts, in fresh contexts, check them, then `node $N/lens-stale.mjs <dir> --record <ids>`.
   Name in the change log which parts reran. A folder with the four older lenses moves to a panel here.
8. **Build and publish.** Run step 8 of `new`, then republish both pages to their saved links.
9. **Report.** What changed, which lenses reran and why, and what still needs a person.

## Subagents: best and targeted

- Use the most capable model you have for steps that judge or that a person will rely on: the fact
  writer's hard calls, the verifier, every lens, the skeptic. Use a smaller, faster model only for
  mechanical steps (fetching a page, extracting a table, formatting). Use no model for what code does.
- Target each subagent: one job, only the files it needs, a fresh context, a named output file.
- Run independent subagents in parallel, in one message (the lenses). The author never verifies.
- In the report, say which model each step used and which steps ran without a subagent.

## Gates

Every step ends with a code gate: `check-facts.mjs`, `verify-quotes.mjs`, `instrument-card.mjs --strict`,
`lens-stale.mjs` and `plant.mjs`, plus the verifier agent. What each fails on, and what to do:
[references/gates.md](references/gates.md).

## Publish and update

Publish each page once as a private Artifact, save both URLs in `name.json` `artifacts`, and from then
on republish to the same URLs. Steps and comment handling: [formats.md](references/formats.md).

## The research board

One `research-board.json` per board ([formats.md](references/formats.md)) lists the names, the dated
events to watch and the if-then bets. A name with a `folder` takes its lane from the analyst's view
in that folder's `board.json`, and its future Key dates join the countdowns, so the board never
disagrees with the brief. Build it with `node $N/build-board.mjs <board-folder> [--out <dir>]`. It
writes `board.html` and builds each linked brief under `out/names/<slug>/`.

- **Add a bet or an event**: edit `research-board.json` and build again. Each bet has an `if`, a window,
  a status (`open`, `triggered`, `lapsed`) and up to three orders of names, each with a why.
- **From the page**: a person can move lanes, mark bets and add bets in the browser, then press
  "Copy the board file". When they paste it back, save it as `research-board.json`. If it moves a name
  that has a brief, record the move in that folder's `board.json` (below), only because the person asked.
- **Share**: publish `out/artifact/board.html` as the page, with every file under `out/names/` as
  files at the same paths, in one private Artifact.
- Bets and lanes are a person's calls. Never add a bet, move a lane or mark a bet triggered on your own.

## Record the analyst's view

When a person marks a name ("watching", "passed"), write it to `board.json` and republish the lenses
page ([formats.md](references/formats.md)). Never write it yourself.

## Done when

- `check-facts.mjs` passes on the summary and on each lens part.
- `verify-quotes.mjs` finds every quote, and the verifier's failures are fixed.
- `lens-stale.mjs` prints no RERUN, and `plant.mjs` catches every planted error.
- Both pages build and match [output.md](references/output.md) as far as the sources allow. Each
  opens at phone and desktop width, light and dark, with no sideways scroll, no colliding labels and
  every tooltip on screen ([design-feedback.md](references/design-feedback.md)).
- `name.json` holds both artifact links, and the user has the change log entry.
