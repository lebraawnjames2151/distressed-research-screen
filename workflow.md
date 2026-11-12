# The work

## Job 1: First look at one name

What you told us: a trader keeps the distressed pipeline as a spreadsheet with prices and commentary. The
team wants a quick yes or no against return thresholds and criteria, to decide whether a name needs deeper
work, with the PM's view and the red flags for each name.

- **When:** a name enters or moves in the pipeline, or someone asks.
- **Input:** a public name, its public filings in `data/` (annual report, latest quarter, debt documents if
  public), and `criteria.md`.
- **Steps:**
  1. **Evidence first.** List each fact you will use (debt by tranche, cash, EBITDA, free cash flow,
     maturities, covenants, price) with its document and page. A fact with no page does not go on the page.
  2. **Calculate in code.** Leverage, interest cover, liquidity runway, yield, IRR or breakeven, each with
     the formula and the inputs. Show the code's output.
  3. **Test each criterion** in `criteria.md`: pass, fail, or not testable (say what is missing). A fail on
     a hard limit means the result is **no**, whatever else is true.
  4. **Write the page** in `outputs/`, in the format of `screen-format.md`: result, top three red flags, reasons to buy,
     what would change the view, and the next dated event.
  5. **Check the quotes** with the `cited-answer` skill: find each quote word for word in its source file and mark it FOUND or
     NOT FOUND. Fix or remove anything not FOUND.
- **Output:** one page, plus the short Slack line.
- **Checked by:** the trader or the PM. The analyst decides; the screen only suggests.
- **Done means:** every figure has a page, every ratio has a formula, every quote is FOUND, and the
  checker agrees with the result or says why not.

## Job 2: Add or change a criterion

1. Write the new criterion in `criteria.md` in words and as a number with a unit.
2. Rerun Job 1's step 3 on the names screened so far, and list which results change and why.
3. The criteria file is the team's. Never change a threshold yourself to make a name pass or fail.

## Job 3: Name brief and research board

- **When:** a public name needs a page the team can return to, or someone asks for the board.
- **Input:** a public name; for the board, `research-board.json` (the names, dated events and if-then
  bets the team writes down).
- **Steps:** follow the `name-brief` skill. Its ideal output is `references/output.md` in that skill.
  Public names and public filings only, as for Job 1.
- **Output:** the facts and lenses pages for the name, and `board.html`, in `outputs/`.
- **Checked by:** the analyst. Lanes, bets and the analyst's view are written only by a person.

## Not in this project yet

- Names from the live pipeline, positions or internal prices, until compliance approves them.
- The full Otterd research engine (bear and bull cases, the triage board, planted-error checks). Otterd
  runs that today; it will move into this project when it can run on its own.
