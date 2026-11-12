# Research folder

Drop analyst research, call transcripts and other material on a name here. The screen reads it at step 0 of
Job 1 (`workflow.md`). One folder per name, named by ticker: `research/public/DND/`, `research/restricted/DND/`.

## Which folder

| Folder | What goes in | Pushed to GitHub? | Used by the screen? |
|---|---|---|---|
| `public/<TICKER>/` | Material anyone can get free from the company or a public site: call transcripts and webcasts the company posts, investor decks, press releases, public news articles | Yes | Yes |
| `restricted/<TICKER>/` | Broker and sell-side research, transcripts from paid vendors, expert-network calls, rating-agency reports, your own call notes, anything licensed or internal | **No** (git-ignored, stays on this machine) | **No**, until `my-setup.md` records written compliance approval for it |

If you are not sure, put it in `restricted/`.

## File names

`YYYY-MM-DD_type_source_title.ext`, for example `2026-11-12_transcript_company_Q1-FY27-call.pdf`.
Types: `transcript`, `deck`, `broker`, `rating`, `news`, `notes`, `other`. The date is the date of the
material, not the day you saved it.

PDF, Word, text and Markdown all work. For quote checks, Claude saves a text copy in `_text/` next to the
file. It never edits or deletes what you put here.

## How the screen uses it

- **Figures come from filings only.** Leverage, cash, debt and EBITDA on a page are taken from the filings in
  `data/`. A number that appears only in research or a transcript is shown as "per <source>, not in filings".
- **Transcripts** give management's own words: guidance, refinancing plans, dates. Each quote is checked word
  for word and cited with the call date and the speaker.
- **Broker research and other restricted material** (once approved) goes in a separate "What others say"
  section, labelled with firm and date, never mixed with facts. Price targets and ratings are not copied onto
  the page.
- **Conflicts** between research and the filings are listed as flags. The filing wins until a person decides.
- Material older than the latest filing is marked stale.
