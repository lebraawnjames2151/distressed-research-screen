---
name: cited-answer
description: Answer a question only from a given set of documents (fund agreements, side letters, NDAs, filings, program documents), quoting the exact words with the file and page, and check every quote with code. Says "not found" rather than guess. Use for term questions ("what is the fee for fund X", "does any side letter give MFN rights"), for listing mismatches between two documents, and for any fact that must be traced to its page.
---

# Cited answer

Every answer comes from the documents you were given, and every claim carries an exact quote that code
can find in the file you cite. "Not found in these documents" is a correct answer; a guess is not.

This skill is self-contained: it ships inside client project kits, so it links to nothing outside this folder.
The check is `scripts/check_quotes.py` (Python 3, standard library only). In a client project kit it is
also at the top of the folder as `check_quotes.py`; use whichever path exists.

## Before the first answer

1. **Which documents.** Get the list of files and, for each, which fund, entity or counterparty it
   belongs to and its date or version. A side letter changes its fund's agreement only for its investor.
2. **Which version wins.** If there are drafts and finals, or an amendment, ask which governs. Use only
   that one unless asked to compare.
3. **What may be shared.** Confidential documents stay where the person's rules say. Ask if unsure.

## Each answer

1. **Restate the question** in one line: which fund or entity, which term, as of which date.
2. **Find every relevant passage,** in every document that could govern: the main agreement, each
   amendment and each side letter for that fund. Note the page or section of each.
3. **Answer in one or two sentences,** then give each supporting quote in this exact form:

   ```
   Quote: "the exact words, copied, not paraphrased"
   From: <file name>, <page or section>
   ```

   Copy the words exactly. Keep a quote to one or two sentences. Never join two passages into one quote.
   For a figure in a table, quote from the column header (the date or period) through the row, so
   the figure is tied to its period. If other rows sit between them, give the header and the row as
   two quotes from the same page.
4. **Say what could change the answer:** a later amendment, a side letter you were not given, a
   defined term defined elsewhere.
5. **Check the quotes.** Save the answer as `answer.md` and run
   `python3 scripts/check_quotes.py answer.md <folder with the documents as .txt, .md or .docx>`.
   Every quote must be FOUND. WRONG FILE means you cited the wrong fund or letter: fix the From line or
   the answer. NOT FOUND means the words are not in the document: fix the quote. If you cannot run
   code here, say so and ask the person to run the check.
6. **If nothing supports an answer,** say "Not found in these documents", list what you searched, and
   suggest where it might be.

## Comparing two documents

To list mismatches (an agreement against a form, a draft against a final), go term by term. For each,
give the quote from each side in the format above, then one line: same, different (how), or missing.
Do not resolve a mismatch yourself; the document's owner decides.

## Rules that do not bend

- Only the documents given. No outside knowledge presented as a term.
- Every claim has a quote that the check finds in the cited file.
- No arithmetic on terms in the chat for anything that will be relied on; do it in code and show it.
- You draft. A person approves the answer before anyone relies on it, and a person sends it.
