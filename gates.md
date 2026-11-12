# Gates

| Gate | Fails when | Then |
|---|---|---|
| `check-facts.mjs` | A line has no tag, a tag has no source, or a figure is not in the quote | Fix or cut the line |
| `verify-quotes.mjs` | A quote is not word for word in its saved page | Fix the quote or the url |
| `instrument-card.mjs --strict` | A card lacks amount, issue date, maturity or pricing, or cites an unknown source | Find it, or keep the note and a Gaps line |
| Verifier | A line says more than its quote | Fix or cut the line |
| `lens-stale.mjs` | A part rests on a changed section or source | Rerun that part |
| `plant.mjs` | A gate misses a planted error | Fix the gate, never the folder, to pass |
| `build-artifacts.mjs` | A long dash, an email, an unknown tag, a chart figure not in its quotes, or a bad date | Fix the file it names |
