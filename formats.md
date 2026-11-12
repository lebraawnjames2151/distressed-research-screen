# Name folder formats

One folder per name. Git keeps the inputs. `.cache/` (saved pages) and `out/` (built pages) stay out
of git, as in `research/`.

```text
research/names/<slug>/          or <client>/runs/<code-N>/<date>/<slug>/ for client work
  name.json                     name, as-of date, lens parts, what each part read, artifact links
  factual-summary.md            the facts, in fixed sections
  sources.json                  one entry per quote
  instruments.json              one card per debt instrument
  lens-parts/<id>.md            one file per lens part, unedited
  history.json                  balances of each instrument at past dates, and optional interest and flows per period (optional)
  in-brief.md                   5 to 6 tagged lines: what the company is and where it stands, shown as "In brief" at the top of both pages
  board.json                    the analyst's view (optional, written by a person)
  glossary.json                 hover definitions for terms of this name, added to scripts/glossary.json (optional)
  change-log.md                 newest entry first (optional)
  verify.json                   written by verify-quotes.mjs
  verification.md               written by the verifier agent
  .cache/                       saved page text, one file per url (not in git)
  out/facts.html, out/lenses.html   written by build-artifacts.mjs (not in git)
```

## name.json

| Field | Content |
|---|---|
| `name`, `ticker`, `exchange`, `slug` | The company. `slug` is the folder name |
| `as_of` | `YYYY-MM-DD`. The date of the last `new` or `refresh` |
| `chart_unit` | The unit the debt chart draws, for example `USD millions`. Cards in another unit are listed, not drawn |
| `situation` | Optional. The panel situation from [panels.md](panels.md): `in-court`, `pre-default`, `post-emergence`, `single-asset` or `going-concern`. Shown as a chip in the header |
| `fictional` | Optional. `true` only for a made-up teaching example. The pages then say so in the header |
| `parts` | `{ id, title, reads }` per lens part, printed by `panel.mjs` for the name's situation ([panels.md](panels.md)). `reads` lists `##` section names of the summary, or `["*"]` for all. The part `why-look` is the overview |
| `lens_inputs` | Written by `lens-stale.mjs --record`: per part, the date and a hash of each section it read and each source it cites. Never edit it |
| `artifacts` | `{ facts, lenses }`: the Artifact URLs once published, else `null` |

## sources.json

A list of `{ id, title, publisher, date, url, type, quote }`. `id` is `S` and a number, never reused.
`type` is `primary` or `secondary`. `quote` is word for word from the page text with tags removed;
for a table row, quote from the column headers through the row. A FRED row is its own source:
`url` is the `fredgraph.csv` link for that date, and `quote` is the CSV line, such as `2020-09-30,0.47`.

## Quote checks

`verify.json` records each source's status and `source_sha256`, a fingerprint of its URL, quote,
date and title. A partial check reuses only unchanged successful results. Changed sources and
older reports without fingerprints must be checked again; never add fingerprints by hand.

Both pages show how many quotes matched saved source copies, and each source entry shows its
status. These are text matches, not confirmation of the claim's interpretation or a search for
newer filings. An offline draft can build without a verification report, but it stays visibly
unverified. The CI table separates this source status from technical checks.

## factual-summary.md

A `#` title, an as-of line, then these `##` sections in this order. Any other `##` section is shown
after Key dates.

- **Business**: 4 to 6 tagged lines.
- **Capital structure and debt**: an optional table, then tagged lines on totals, cash, liquidity,
  covenants, defaults and grace periods. The page shows the cards from `instruments.json` instead of the table.
- **Results by year**: a line with the units (the word "thousands" makes the chart show millions),
  then one table: the first column is the period, the last column is `Source`, the columns between
  are numbers. `(1,234)` is negative, `none reported` is zero, `not stated` is left out of the chart.
- **Recent results**: tagged lines, grouped under short plain lines that name the period.
- **Key dates**: one line each, `- Nov 15, 2027: Series B notes mature. [S9]`. A date may be a month
  and year (`Dec 2026 (expected)`). Add `(expected)` when only the company expects it. The page shows
  every date as `Nov 15, 2027` or `Dec 2026`; a line with no leading date is shown as "no set date".
- **Debt timeline** (optional): one dated line per issue, amendment, waiver or missed payment.
- **Restructuring terms** (optional): what a plan, support agreement or offer gives each class, who
  signed, and which companies and debts are inside it.
- **Accounting and controls** (optional): one disclosure flag per line, in this form:
  `- **Going concern** (Mar 16, 2026): The fiscal 2025 10-K states substantial doubt. [S4]`.
  Cover the audit opinion and going-concern wording as written, material weaknesses, restatements,
  covenant breaches, waivers and forbearance, late filings, a change of auditor, and large non-GAAP
  add-backs. The title sets the color on the page: going concern, material weakness or restatement is
  rose; covenant, default, forbearance, waiver, grace or late filing is amber; anything else is grey.
  The page shows the quote of the line's first tag under "The filing's words". The date, like every
  figure, must be in a quote the line cites.
- **Gaps**: what was looked for and not found.
- **Checks**: the tools run. Not shown on the pages.

## in-brief.md

Five or six `- ` lines for a reader who knows nothing about the company: what it does, what happened
lately, what it owes and when, and what comes next. Each line ends with its tags and passes
`check-facts.mjs`. Plain words: write `a net loss of $269.3 million`, not `(269,322) thousand`; a
figure in millions may round a quote in thousands to one decimal. Write dates as `Jan 26, 2021`.
A folder without the file still builds, with no In brief block.

## instruments.json

A list of cards. The fields that `instrument-card.mjs` checks are `amount`, `issued`, `maturity`,
`coupon`, `pricing` and `current`, each `{ value, src }`, or `{ note }` when not found.
`--strict` requires `amount`, `issued`, `maturity` and `pricing`.

| Field | Content |
|---|---|
| `name` | Full name, for example `2.50% Series B Senior Notes due 2027` |
| `short` | Short label for the charts |
| `in_case` | `true` when the instrument is inside a court case, else `false` |
| `security` | `{ value, src }`. `value` is `secured`, `unsecured`, `not stated` or `repaid` and sets the color. `secured` and `unsecured` need a source |
| `issued_date`, `maturity_date` | `YYYY-MM-DD` for the dates chart. The year must appear in `issued.value` or `maturity.value` |
| `dates` | Optional extra chart dates: `[{ date, label, src }]`. The page puts `short` in front of a label that lacks it, so `add-on` shows as `2028 notes add-on` |
| `spreads` | Optional `[{ label, bps, formula, src }]`. The formula names the yield, the Treasury and every judgment |
| `chart` | `{ outstanding, limit, unit, as_of, src }` in `unit`, for example millions. `limit` is for a facility. The build refuses a figure that is not in the quotes of `src` as millions, thousands or units. `0` needs no quote |

## history.json

A list of `{ instrument, date, usd_thousands, basis, src }`. `instrument` is the card's `short` label, or
the name of an instrument that is already repaid and has no card. `basis` is `principal` or
`carrying amount`. With this file the facts page draws one chart: debt stacked by instrument at each
date, with the issue and maturity rings on the same time axis. The latest balance on each card is
added as a bar when no history date is within five months of it. A bar marked `*` leaves out an
instrument that existed then but has no balance in the file. Without the file the page draws the
single-date bars and the date strip. `chart_unit` in `name.json` must be in millions.

Each row may also carry flows for the period that ends on its `date`, in thousands:
`interest_paid_usd_thousands`, `borrowed_usd_thousands` and `repaid_usd_thousands` (zero or more;
leave a field out rather than guess). Each must be in a quote of the row's `src`, like the balance.
With any of them, the debt chart gets an Interest paid view, a Borrowed and repaid view, or both, and
the Debt by date table gets an interest row.

## lens-parts/<id>.md

Exactly the form in [lens-cards/_form.md](lens-cards/_form.md): `### Title`, then `**Assumptions**`,
`**What the facts show through this lens**`, `**What would change this view**`, `**Not covered**`.
`why-look.md` is `### Why it is worth a look` and a numbered list.

## board.json

The entry has the same fields as the triage board's `board.json` in `screen-refresh`. The board nests entries under `"names"`; a name folder keys them by ticker at the top level:

```json
{ "version": 1, "WDFC": { "status": "watching", "note": "...", "by": "analyst", "date": "2026-11-11" } }
```

Optional fields, each written by the person: `points` (the synthesis, a list of lines), `check_first`
(a list), `moves` (what would move the lane, a list) and `next` (when to look again, one line).

`status` is `working`, `watching`, `passed` or `none`; the page shows it with the board lane Worth
checking, Watching, Not worth checking or No lane set. A person writes it. The page shows it as the
analyst's view, not checked against the facts.

## change-log.md

`# Change log`, then one `## YYYY-MM-DD: <what>` entry per run, newest first. A line that states a
new fact carries its tag. The facts page shows the newest entry at the top and the whole log at the end.

## research-board.json (one per board, not per name)

```json
{ "version": 1, "title": "Research board", "as_of": "2026-11-12", "horizon_days": 90,
  "names": [ { "ticker": "CRVN", "folder": "../names/corvane" },
             { "ticker": "BWRG", "name": "Brightwell Retail Group", "situation": "in-court", "lane": "check", "note": "..." } ],
  "events": [ { "kind": "Court", "at": "2026-11-18T15:00:00Z", "title": "...", "check": "what to read when it lands", "tickers": ["BWRG"] } ],
  "bets": [ { "id": "b1", "if": "If ...", "window": "Grace ends Dec 15", "status": "open", "updated": "Nov 11, 2026", "by": "analyst",
              "orders": [ [ { "ticker": "CRVN", "why": "..." } ], [ ... ], [ ... ] ] } ] }
```

- `names`: `folder` is a name folder, relative to this file. With it, the name, situation and lane come
  from the folder (`name.json`, and `board.json` status: working is Worth checking, watching is
  Watching, passed is Not worth checking), and its Key dates on or after `as_of` join the countdowns.
  Without it, give `name`, `lane` (`new`, `check`, `watch` or `pass`), and optionally `situation`,
  `note` and `fictional`.
- `events`: `at` is a date (`2026-12-09`) or a time with its zone (`2026-12-09T19:00:00Z`). The strip
  shows the next `horizon_days`.
- `bets`: at most three orders of effect. A ticker named in a bet or an event but not in `names` gets a
  card in New names.
- No long dashes and no email addresses. The build refuses either.

## What the pages show

The target layout of both pages, part by part, and the file that fills each part:
[output.md](output.md).

## Publish and update

1. On the first publish, publish `out/artifact/facts.html` and `out/artifact/lenses.html` (the build
   writes these without a page wrapper, as the Artifact tool needs) as two private Artifacts, in one message.
2. Save both URLs in `name.json` `artifacts`, build again so the pages link to each other, and
   republish each to its URL.
3. On every refresh, republish each page to its saved URL. Never publish a new link for a name that
   has one.
4. Read and answer comments with the `ArtifactComments` tool. A comment that corrects a fact is a
   refresh: fix, rebuild, republish, and reply with what changed. A view goes into `board.json` only
   if a person asks.

## Recording the analyst's view

When a person says "mark WDFC as watching" or "we passed on it":

1. Open `board.json` in the name folder (create it with `"version": 1`).
2. Under the ticker, set `status` (`working`, `watching`, `passed` or `none`), `note` in the person's
   words, `by` (a role or initials, never a client person's name in `research/`) and `date`.
3. Build and republish the lenses page.
