# The ideal output

This page is the target for every name brief. `scripts/build-artifacts.mjs` is the template: it fills
each part below from the name folder. Fill the folder as fully as the public sources allow, and the
page fills itself. A part whose input is missing is left out. It is never filled with a guess.

See it built. `examples/corvane/` is a fictional name that fills every part:

```bash
node .claude/skills/name-brief/scripts/build-artifacts.mjs .claude/skills/name-brief/examples/corvane
# open .claude/skills/name-brief/examples/corvane/out/facts.html and out/lenses.html
```

`examples/wdfc/` is a real public name with fewer inputs. It shows how the same template looks when
some parts are missing.

## Every page

| Part | What it shows | Filled from |
|---|---|---|
| Header | The name, exchange and ticker, and the as-of date. The draft mark (and a fictional mark when `fictional` is true). Chips for the situation and the analyst's lane. Tabs: Facts, Debt, Lenses and analyst view | `name.json` (`situation`, `fictional`), `board.json` `status` |
| In brief | Five or six plain tagged lines, at the top of both pages | `in-brief.md` |
| Source checks | How many quotes matched a saved copy of their page, and a link to the sources | `verify.json` |
| Source tags | Every fact ends with tags such as `S4`. A click opens the closed Sources list and jumps to that quote | `[S#]` in any text file, `sources.json` |
| Hover text | Every bar, ring and maturity block says what it is, its date and its source on hover, tap or tab. Dotted terms show a plain definition | the data itself, `scripts/glossary.json` and the folder's `glossary.json` |
| Sources | A closed list at the end: title with link, date, check status and the word-for-word quote | `sources.json` |

## Facts tab (`facts.html`)

| Part | What it shows | Filled from |
|---|---|---|
| Last change | The newest change-log entry | `change-log.md` |
| Key figures | One tile per results measure (up to four) for the latest period, with the change from the period before. Then the next dated event | `## Results by year` table, `## Key dates` |
| Business | Tagged lines | `## Business` |
| Results by year | A switcher with one bar chart per measure. A readout shows the value, the change and the source of the bar under the pointer. Below it is the full table | `## Results by year` |
| Recent results | Tagged lines | `## Recent results` |
| Disclosure flags | One card per line: going concern, material weakness, restatement, covenant breach or forbearance, late filing, auditor change, non-GAAP add-backs. Rose is audit or controls, amber is a covenant or deadline, grey is context. Each card opens to the filing's own words | `## Accounting and controls`, one `- **Title** (Mon D, YYYY): text [S#]` line per flag |
| Key dates | Every dated line. Dates on or after the as-of date are marked ahead | `## Key dates` |
| Gaps | What the sources did not answer | `## Gaps` |
| Change log | Every entry | `change-log.md` |

## Debt tab (`facts.html#debt-tab`)

| Part | What it shows | Filled from |
|---|---|---|
| Debt figures | Total debt, the total by security (secured, unsecured, not stated) and the next maturity | `instruments.json` (`chart`, `security`, `maturity_date`) |
| What is owed | With history: one chart of debt stacked by instrument at each balance date, with issue and maturity rings. Its views switch between Outstanding, Interest paid and Borrowed and repaid. A readout lists every instrument in the bar under the pointer. Without history: debt by instrument at one date, plus the dates strip | `history.json`. The interest and flow views need `interest_paid_usd_thousands`, `borrowed_usd_thousands` and `repaid_usd_thousands` |
| Instrument cards | One card per instrument: security, amount, issued, maturity, coupon, pricing at issue and now | `instruments.json` |
| Capital structure lines | Totals, cash, liquidity, covenants, defaults and grace periods | `## Capital structure and debt` |
| Debt by date | Each balance at each date, the total, and the interest paid in each period | `history.json` |
| Maturity wall | Principal due by year, from the latest balance on each card | `instruments.json` (`maturity_date`, `chart`) |
| Debt timeline, Restructuring terms | Tagged lines | the sections of the same names |

## Lenses page (`lenses.html`)

| Part | What it shows | Filled from |
|---|---|---|
| Why it is worth a look | The numbered overview | `lens-parts/why-look.md` |
| How this page works | Fixed text: the lenses were written blind and do not vote; a person decides | the builder |
| Where the lenses differ | Lines a lens marked "(assumed)", then each source more than one lens cites, with their lines side by side. Nothing is weighed | `lens-parts/*.md`, worked out by code |
| What would change these views | One line per lens | each part's "What would change this view" |
| The lenses | One card per lens, with a filter by the sections it reads | `lens-parts/<id>.md`, `name.json` `parts` |
| Analyst's view | The status and lane, a note, the synthesis points, what to check first, what would move the lane, and the next look, with the author and date | `board.json`, written by a person |

## Rules the page keeps

- Facts only on the Facts and Debt tabs. No price target, no recommendation, no confidence score.
- Lenses never vote. The lane and the synthesis come only from a person, through `board.json`.
- Every figure the page draws is in a quote of a source it cites. The build refuses one that is not.
- Light and dark themes, and no sideways scroll at 390px. Charts never sit side by side; a readout may
  sit beside its chart on a wide screen. With scripts off, every tab and view is shown in turn.

## Research board (`board.html`)

| Part | What it shows | Filled from |
|---|---|---|
| Coming up | A card per dated event in the next `horizon_days`, with a live countdown (red under a day, amber under three), what to check, its tickers and a link to the brief | `research-board.json` `events`, and each linked name's Key dates |
| Names by lane | New names, Worth checking, Watching, Not worth checking. Each card: situation, note, next dated event with countdown, the number of bets, and Open brief | `names`, and each linked folder's `board.json` |
| If-then bets | Each condition, its window and status, and the names by first, second and third order, each with why. Filter by status; click a ticker to focus the whole board on it | `bets` |
| Add a bet, copy out | A form for new bets, "Copy bets as sheet rows" (paste into a spreadsheet) and "Copy the board file" (for the skill to save) | the browser; nothing is saved until the file is |

Build it from any folder: `node <repo>/.claude/skills/name-brief/scripts/build-board.mjs --open` (no folder builds the sample).
