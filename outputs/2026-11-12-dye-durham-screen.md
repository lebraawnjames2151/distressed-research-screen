# Dye & Durham (TSX: DND)  Capital structure, all tranches  Data to 30 Sep 2026
**Result: WATCH**, tested against `criteria.md` as of 12 Nov 2026. Draft until the trader signs it off.

No hard limit fails on the figures available. Three tests could not be run: LTV, the IRR threshold and the CLO maturity wall. The public press releases give no debt terms, maturities or prices. A yes or no needs the Q1 FY2027 MD&A and financial statements from SEDAR+.

## Top three red flags
1. **Convertible debentures of $101.3m are classified as current, against $89.0m of cash** (S5, S6). That is 114% of cash (calc 12). The maturity date is not in the sources read. Loans and borrowings due within a year add $27.1m (S5).
2. **Control and filing problems.** Internal controls over financial reporting were "not effective as at June 30, 2026 due to a material weakness" (S9). Q3 FY2026 net income was restated down by $24.6m, from $66.0m to $41.4m (S10, S4, calc 14). The FY2025 annual statements were filed late, and the company needed a waiver under its senior credit agreement in December 2025 (S11).
3. **Revenue is falling, and the margin rests on cost cuts.** Q1 FY2027 revenue fell 12.4% year on year (8% excluding the Credas sale) (S1, calc 13). Operating costs fell 17% (S2). LTM interest cover was 1.73x adjusted EBITDA to March 2026 (calc 8), only just above your 1.5x red-flag line. There is no permanent CEO: the interim CEO was appointed on 31 Aug 2026 and the search continues (S12).

## Reasons to buy
- **Cash generation.** LTM operating cash flow to Sep 2026 was $144.5m (calc 9, S3, S7). Cash rose from $41.4m to $89.0m in the quarter (S5).
- **Deleveraging.** First-lien net leverage, as defined in the credit agreement, fell from about 5.52x at March 2026 to 5.17x at June 2026 (S13, S8). Finance costs, net, fell $26.3m year on year in Q1 (S2). The covenants were met at 30 Sep 2026 (S2).
- **Governance settled.** Plantro and EdgePoint, about 36% of shares, signed standstill and voting support agreements to September 2027. The litigation is to be dismissed (S14).

## What would change the view
- **The convertible maturity and how it is refinanced.** Source: the Q1 FY2027 MD&A on SEDAR+. Date not in the sources read.
- **Debt by tranche, with coupons, maturities and trading prices.** This would allow the IRR, YTW and LTV tests.
- **Capitalised development costs.** These are needed for leverage on your default EBITDA. If they are large, leverage moves up from 6.3x.
- **A permanent CEO, or an outcome from the strategic process.** The process "remains ongoing" as of 23 Jun 2026 (S15).
- **Next dated event:** none found. The Q2 FY2027 results date is not announced in the sources read. The standstill runs to September 2027 (S14).

## Criteria
| Criterion | Limit | This name | Pass? | Source |
|---|---|---|---|---|
| Net leverage (both funds) | ≤10.0x | 6.33x net debt / LTM adj EBITDA (6.40x with leases) | **Pass**, on company-adjusted EBITDA | calc 5, 6 |
| Same, on adj EBITDA less capitalised costs (default) | ≤10.0x | Not testable. Capitalised costs are not in the sources read | Not testable | |
| Liquidity runway (both funds) | ≥12 months | Cash $89.0m. LTM operating cash flow is +$144.5m, so no operating burn. Revolver size and undrawn amount not found. FCF after capex and capitalised development not found | **Pass on the evidence available**, not confirmed | S5, calc 9 |
| LTV (CLO) | ≤60% | Needs EV of at least $2,205m, or 11.3x LTM adj EBITDA, with all debt counted. Market cap and the loan's place in the stack not found | Not testable | calc 10, 11 |
| Maturity wall (CLO) | None inside 18 months without a plan | $101.3m of converts and $27.1m of loans are current. No maturity date or plan is in the sources read | Not testable. Likely a fail unless the MD&A shows a plan | S5 |
| IRR (opportunities fund) | >15% over 2 to 5 years | No instrument price | Not testable | |
| Interest cover (red flag only) | <1.5x is a flag | 1.73x (LTM to Mar 2026) | No flag, little headroom | calc 8, S11 |
| Hard assets with real value | Wanted | Goodwill $1,062m plus intangibles $541m make up 88% of the $1,819m of total assets. PP&E is $5.7m | Not met | S5 |
| Sticky recurring revenue with a moat | Wanted | The recurring share and churn are not in the sources read. Revenue fell 12.4% | Not shown | S1 |
| Sponsor adding equity | Wanted | None found. The support agreements cover governance only | Not met | S14 |
| Catalysts in 6 to 24 months | Wanted | CEO search, strategic process, standstill to Sep 2027 | Partly met, no dates | S12, S14, S15 |
| Path to positive FCF | If burning | Operating cash flow is positive. FCF is not testable | n/a | calc 9 |

The 88% asset figure: (1,062,401 + 540,764) / 1,819,246 = 0.881. This one was checked by hand, not in code.

## Calculations
Script: `outputs/2026-11-12-dnd-calcs.py`. Output: `outputs/2026-11-12-dnd-calcs-output.txt`. All figures are C$ thousands.

| # | Item | Formula | Result |
|---|---|---|---|
| 1 | Gross debt (carrying value) | 27,108 + 1,194,785 + 101,330 | 1,323,223 |
| 2 | Net debt | 1,323,223 − 88,951 | 1,234,272 |
| 3 | Net debt incl. leases | 1,234,272 + 4,620 + 9,078 | 1,247,970 |
| 4 | LTM Sep-26 adj EBITDA | 50,352 + 42,867 + 55,099 + 46,559 | 194,877 |
| 5 | Net leverage | 1,234,272 / 194,877 | 6.33x |
| 6 | Net leverage incl. leases | 1,247,970 / 194,877 | 6.40x |
| 7 | LTM Mar-26 adj EBITDA | 47,744 + 50,435 + 50,352 + 42,867 | 191,398 |
| 8 | Interest cover | 191,398 / 110,600 | 1.73x |
| 9 | LTM Sep-26 operating cash flow | 153,432 + 31,316 − 40,217 | 144,531 |
| 10 | Minimum EV for 60% LTV | 1,323,223 / 0.60 | 2,205,372 |
| 11 | As a multiple | 2,205,372 / 194,877 | 11.32x |
| 12 | Converts / cash | 101,330 / 88,951 | 114% |
| 13 | Q1 revenue change | 94,866 / 108,302 − 1 | −12.4% |
| 14 | Q3 FY26 net income restatement | 41,406 − 66,001 | −24,595 |

**Assumptions.**
- Debt is at **carrying value**, not face. The convertible is carried at fair value, and the releases say finance costs include "changes in fair value of convertible debt" (S16). Face value may differ.
- Leverage uses the company's adjusted EBITDA, because capitalised costs are not disclosed in the releases.
- Interest cover uses LTM to March 2026, the latest period with a disclosed LTM net interest figure. Q1 FY2027 finance costs, net, of $19.6m include fair-value items, so they are not annualised here.

## Sources
The sources are company press releases saved as text in `data/`. Press releases have no page numbers, so each citation names the release and the section. **This does not meet the "every figure has a page" rule.** It should be replaced with page references to the MD&A and financial statements once those are in `data/`.

- Q1 = `data/dye-durham-reports-first-quarter-fiscal-2027-financial-results.txt` (12 Nov 2026)
- FY26 = `data/dye-durham-reports-fourth-quarter-and-year-end-fiscal-2026-financial-results.txt` (29 Sep 2026)
- Q3 = `data/dye-durham-reports-third-quarter-fiscal-2026-financial-results.txt` (19 May 2026)
- SA = `data/dye-durham-announces-support-agreements-with-plantro-and-edgepoint-strengthening-governance-with-new-appointments.txt` (5 Nov 2026)
- TC = `data/dye-durham-announces-conclusion-of-transformation-committee-and-announces-appointment-of-interim-ceo-and-new-board-chair.txt` (31 Aug 2026)
- CEO = `data/dye-durham-announces-ceo-transition.txt` (23 Jun 2026)

| Tag | File, section | Quote |
|---|---|---|
| S1 | Q1, highlights | "Revenue was $94.9 million, representing a decrease of $13.4 million, or 12.4% (8% excluding Credas), from Q1 FY2026" |
| S2 | Q1, highlights | "a decrease of $9.6 million, or 17%, from Q1 FY2026" / "primarily reflecting a $26.3 million decrease in finance costs, net, to $19.6 million" / "The Company was in compliance with the financial maintenance covenants under its senior credit agreement as of September 30, 2026." |
| S3 | Q1, selected key metrics | "Cash flow provided by operating activities 31,316 40,217" |
| S4 | Q1, summary of quarterly results | "Adjusted EBITDA (2) 46,559 55,099 42,867 50,352" / "Net income (loss) (1) (11,076) (19,862) 41,406 (21,790)" / "Adjusted EBITDA (2) 50,435 47,744 52,862 64,652" |
| S5 | Q1, statement of financial position | "Cash and cash equivalents 88,951 41,432" / "Loans and borrowings, current 27,108 12,435 Convertible debentures 101,330 104,396" / "Loans and borrowings 1,194,785 1,167,014" / "Goodwill 1,062,401 1,061,531 Total assets 1,819,246 1,795,488" / "Intangible assets, net 540,764 568,856" / "Property and equipment, net 5,728 6,305" / "Lease liabilities, current 4,620 4,868" / "Lease liabilities 9,078 8,895" |
| S6 | Q1, statement of financial position | "Current liabilities:" |
| S7 | FY26, selected key metrics | "Cash flow provided by operating activities 65,175 56,815 153,432 148,200" |
| S8 | FY26, Q4 highlights | "the Consolidated First Lien Net Leverage (as such term is defined in the senior credit agreement) ratio was approximately 5.17x" |
| S9 | FY26, Q3 2026 adjustments | "the Company's internal controls over financial reporting were not effective as at June 30, 2026 due to a material weakness" |
| S10 | Q3, selected key metrics | "Net income (loss) 66,001 (23,449)" |
| S11 | Q3, update on forward-looking information | "costs related to the delayed filing of the audited consolidated financial statements for the year ended June 30, 2025" / "the waiver the Company received under its senior credit agreement in December 2025" / "Net interest for LTM March 2026 is $110.6 million" |
| S12 | TC | "Mr. Schulte has been appointed as the Company's interim CEO effective immediately, while the Board search for a permanent CEO remains ongoing." |
| S13 | Q3, highlights | "the Consolidated First Lien Net Leverage Ratio (as such term is defined in the senior credit agreement) was approximately 5.52x" |
| S14 | SA | "representing approximately 36% of shares outstanding" / "customary standstill and voting support agreements with the Company until September 2027" / "The litigation between Plantro and the Company will be dismissed as part of these agreements." |
| S15 | CEO | "The Company's previously announced strategic process remains ongoing." |
| S16 | Q1, Adjusted EBITDA notes | "changes in fair value of convertible debt and derivatives" |

**Checks.** Every quote was checked word for word against its file in code (`outputs/2026-11-12-dnd-quote-check.txt`). The check ignores table separators ("|"), extra spaces and curly versus straight quote marks. All ratios were run in code, except the 88% asset share, which was checked by hand. SEDAR+ blocked automated download, and the company's report pages are password-protected. So the MD&A, the financial statement notes and the debt documents were **not read**.

## Slack line
Dye & Durham: WATCH. 6.3x leverage passes. $101m current converts vs $89m cash, maturity terms unread. Next: Q1 MD&A from SEDAR+.
