# Design requirements from the owner's comments

Comments the owner left on the published pages, as requirements for the generator. Each says what the page
must do for every name. Newest first. A page that breaks one is a bug in `scripts/build-artifacts.mjs`.
"Checked by" names the test in `scripts/build-artifacts.test.mjs`.

| # | Requirement | Where it shows | Checked by |
|---|---|---|---|
| 17 | The pages follow one template: a green header with the situation and lane chips, Facts, Debt and Lenses tabs, and the parts in [output.md](output.md). Every part fills from the folder, and a missing input hides its part | Both pages | "the facts page has a Facts tab and a Debt tab, and the lenses page links to both"; "the situation and the analyst lane show as chips in the header" |
| 16 | Results show as key figure tiles and one chart per measure with a switcher; hovering a bar fills a readout with the value, the change and the source | Facts tab | "results: key figure tiles, one chart per measure with a switcher, and a readout that names its source" |
| 15 | Quality news (going concern, material weakness, covenant, late filing, auditor change, add-backs) stands out as colored flags, each opening to the filing's own words | Facts tab | "each Accounting and controls line is a disclosure flag with its tone and the filing's own words" |
| 14 | For distressed teams: how the debt stacks up year by year, the interest paid, what was borrowed and repaid, and what falls due when; hovering a bar lists every part of it | Debt tab | "debt: three views of the stacked chart, a readout, a table by date and a maturity wall" |
| 13 | The analyst's synthesis is bullet points, with what to check first, what would move the lane and the next look; it is written by a person | Lenses page | "the analyst view shows the points, what to check first, what would move the lane and the next look" |
| 12 | Where lenses read the same source differently, their lines sit side by side, open by default | Lenses page | "the analyst view shows the points, what to check first, what would move the lane and the next look" |
| 11 | A fictional example fills every part, so the ideal output can be seen and tested | `examples/corvane/` | "the fictional example builds and says on both pages that it is fictional" |
| 1 | A short summary of the company at the very top of both pages ("In brief", from `in-brief.md`) | Top of both pages | "an in-brief file is shown at the top of both pages and is optional"; "the example has an In brief block at the top of both pages" |
| 2 | The debt chart starts at 0 and the zero line is the baseline the bars stand on | Facts, "What is owed" | "the stacked chart has a zero baseline, bar date labels and hover text on segments and rings" |
| 3 | Hovering or tapping a bar segment says what it is, the date, the source and the issue and maturity dates | Facts, every chart | "each bar segment says what it is, its date, its source and the instrument issue date"; "the single-date charts and the results chart show hover text on bars and rings, not a title"; "a tap shows the tooltip and is not undone by the mouse events that follow it" |
| 4 | Say plainly that bars are balances at a date (year ends and the latest quarter), not issue dates; label each bar with its date | Facts, debt chart | "each bar on the stacked chart is labeled with its month and year at both widths"; "total labels and date labels on the stacked chart never overlap, at both widths" |
| 5 | One chart: debt stacked by instrument over time, the total on top, with the issue and maturity rings on the same time axis | Facts, "What is owed" | "with a history file the page draws one stacked chart over time, and without one it keeps the single-date chart"; "rings on the stacked chart take the color of their instrument, as in the legend" |
| 6 | The Sources section collapses; a click on a source tag opens it and jumps to the entry | Bottom of both pages | "the sources are in a closed details element and a tag click can open it" |
| 7 | Acronyms and terms (ADMT, ABL, RCF, EBITDA, 8-K, first lien and others) show a definition on hover, tap or tab | Everywhere text is shown | "terms from the glossary get a hover definition, but source quotes and links are left alone"; "glossary definitions are plain: no definition leans on another glossary abbreviation, and each term is defined once" |
| 8 | The instrument table is a stack of cards, one per instrument, that never scrolls sideways | Facts, "What is owed" | "the instruments are a stack of cards, never a table, and nothing in them scrolls sideways" |
| 9 | Charts are full width, one above the other, never side by side | Facts | "charts are full width, one above the other, and the lens grid never forces sideways scroll" |
| 10 | Lenses are one per row or in a grid that never forces sideways scroll | Lenses | "charts are full width, one above the other, and the lens grid never forces sideways scroll"; "eight lenses build into one grid, each with a card, a jump link and a line in the differ list" |

Always true, from the same comments and the skill rules: a source tag on every fact line, no price
targets, no model recommendation, light and dark themes, phone width with no horizontal page scroll, no
long dashes, no external scripts. Dates the generator writes read one way, such as Jan 26, 2021
("dates the page shows from the files are written one way"). Before a publish, look at both pages at
1280px and 390px in both themes: no label collides, and each tooltip stays on screen.
