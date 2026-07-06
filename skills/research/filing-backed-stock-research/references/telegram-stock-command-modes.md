# Telegram stock command modes

Use these lightweight output modes when the user invokes ticker commands in Telegram-style shorthand. Keep the response readable on mobile: bullets, short sections, no markdown tables.

## Command interpretations

- `!research $TICKER` — company + financials research. Cover identity, business model, market snapshot, latest quarter, annual financials, balance sheet, operating metrics, strategic pivot/catalysts, bull/bear case, and bottom line.
- `!risk $TICKER` — risk brief only. Start with a risk rating, then market facts, main risks, what could go right, what would reduce risk, and bottom line.
- `!full $TICKER` — fuller equity-research note. Cover quick verdict, market snapshot, business overview, latest quarter, annual financials, balance sheet, cash flow, backlog/segments if relevant, dilution, bull/bear case, risks, catalysts, what would make the view more constructive, and bottom line.

## Mobile formatting

- Prefer headings plus bullets over tables; Telegram table rendering is poor.
- Put the verdict/risk rating near the top.
- Show units consistently: `$M`, `$B`, `%`, `x` multiples.
- Label interpretations clearly: “My read,” “Bull case,” “Bear case,” “Bottom line.”
- Include “Not financial advice” or equivalent for full notes.

## Data workflow notes

- Primary source: SEC company tickers → submissions → latest 10-K/10-Q → companyfacts XBRL → filing HTML/MD&A excerpts.
- Secondary source for current quote/market cap/valuation snapshot: StockAnalysis or another current market-data source when available.
- If Yahoo endpoints rate-limit, do not stall; use SEC for filing facts and a secondary market-data site for snapshot data.
- For SEC `companyfacts`, do not blindly pick the most recently filed fact for a concept. A new 10-K/10-Q can include many old comparison periods. Prefer the desired `fy`/`fp`/`form` or the latest period `frame`/`end` that matches the requested quarter/year.
- Verify ticker identity and issuer history, especially for renamed/redomiciled companies, reverse splits, SPACs, or successor issuers.
