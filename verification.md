# Verification: WD-40 Company (WDFC) factual summary

As of Nov 11, 2026. Files checked: factual-summary.md, instruments.json, and the five files in lens-parts/ (why-look, credit-downside, equity-upside, catalysts-timeline, key-risks). Each line was checked against its quotes in sources.json. No file was changed.

## Source quotes

verify.json marks all 47 sources (S1 to S47) as "found". Under the rule, no URL needed to be opened by hand, so none was.

## Failures

| # | File | Line or card | Tag | What is wrong |
|---|---|---|---|---|
| 1 | lens-parts/equity-upside.md | "The board approved a share buyback of up to $100.0 million." | S34 | **Adds a subject.** The quote starts at "approved a new share repurchase program…" and never says who approved it, so "the board" is not in the quote. The quote also gives no date, and the line puts it among fiscal 2026 facts without one. The quote says "repurchase … of its outstanding common stock"; "buyback" is fine as a paraphrase. |
| 2 | factual-summary.md | Capital structure bullet: "The $20.8 million drawn on the revolver at Aug 31, 2026 was all in euros." | S17 | **Missing tag.** S17 says $20.8 million "was classified as long-term" and was entirely in euros. It does not say this was all of the amount drawn. Only S7 (20,849 thousand outstanding) shows that, and S7 is not tagged on this line. The table row is tagged correctly. |
| 3 | instruments.json | Revolver card, `rank: "unsecured"` | none | **No tag, and wrong field.** The value has no source. "Unsecured" (S16) describes security, not rank. The quotes don't give the revolver's rank (senior or subordinated). The `security` field already holds "unsecured" with S16. |
| 4 | factual-summary.md | Capital table, revolver row, Rank column "unsecured" | S16 | **Wrong field.** Same problem as #3. S16 supports "unsecured" as a security term, not as a rank. The notes rows correctly say "not stated". |
| 5 | lens-parts/equity-upside.md | "What would change this view": "No release date has been announced." | (untagged) | **Drops a qualifier.** The facts say the date is "not announced in the sources read". The lens line states it as an absolute. |
| 6 | lens-parts/catalysts-timeline.md | Assumption: "No date is announced for the next results release (from the facts)." | (untagged) | **Drops a qualifier.** Same as #5: the "in the sources read" limit is missing. |
| 7 | lens-parts/key-risks.md | Assumption: "The filings show covenant compliance but not how much room is left (from the facts)." | (untagged) | **Overstates.** The facts say the year-end ratios were "not reported in the parts read". The line widens that to "the filings" as a whole. |

## Lines that pass (worth noting)

- **Series A spread (106 bps):** 3.39 - 2.33 = 1.06. The 100% price comes from S36. The card flags that using the 10-year rate is a judgment.
- **Series B spread (203 bps):** 2.50 - 0.47 = 2.03. The term, Sep 30, 2020 to Nov 15, 2027, is about 7.1 years. The card flags that taking the yield as the coupon is an assumption.
- **Series C spread (200 bps):** 2.69 - 0.69 = 2.00. The term is about 10.1 years. The same assumption is flagged.
- **Series A schedule:** It matches the quotes. Twelve payments of $0.4 million from Nov 2026 to May 2032 total $4.8 million, and 13.2 - 4.8 = $8.4 million, the last payment due Nov 15, 2032 (S8, S18).
- **Results by year table:** All 12 figures match S24 to S27 exactly.
- **Fourth quarter and fiscal 2027 guidance lines:** All match S28 and S31 (figures, percentages and comparison periods).
- **Nov 15, 2026 date line:** Supported by S18, S47 and S38.
- **why-look line 5:** It links the S20 ratios to both agreements. That is supported by S46 ("the same financial covenants").

## Count of lines checked

| File | Tagged lines or values checked | Failures |
|---|---|---|
| factual-summary.md | 41 (Business 6, debt table rows 4, debt bullets 11, results table rows 3, recent results and guidance 5, key dates 10, tagged gaps 2) | 2 (#2, #4) |
| instruments.json | 25 tagged card values (Revolver 6, Series A 7, Series B 6, Series C 6), plus 11 untagged rank and note fields read | 1 (#3) |
| lens-parts/why-look.md | 6 | 0 |
| lens-parts/credit-downside.md | 5 | 0 |
| lens-parts/equity-upside.md | 5, plus 1 untagged line | 2 (#1, #5) |
| lens-parts/catalysts-timeline.md | 4, plus 1 untagged line | 1 (#6) |
| lens-parts/key-risks.md | 4, plus 1 untagged line | 1 (#7) |
| **Total** | **90 tagged lines or values** | **7** (2 involve a tagged line saying more than its quote, 2 are tag or field problems, 3 untagged lines drop a qualifier) |

## Resolution (added by the author after this report)

This is the third verifier pass. The first found 27 failures and the second 25; each set was fixed
in the facts and the lenses were rerun. After this pass:

- #2: the line now cites S7 for the amount outstanding and S17 for the euro share.
- #3 and #4: `rank` was replaced by a tagged `security` field in `instruments.json`, and the table
  column is now "Security". The build now refuses `secured` or `unsecured` without a source.
- #1, #5, #6 and #7: the lens brief now says to keep limits such as "in the parts read". All five
  parts were rerun on the fixed facts and pass `check-facts.mjs`. They have not had a fourth
  verifier pass.
