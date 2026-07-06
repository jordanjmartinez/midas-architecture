# SEC + Yahoo Sourcing Pattern for `!updates`

Use this when a public-company update scan needs current filings plus a recent price-move check.

## SEC identity and recent filings

- Resolve ticker via SEC company tickers JSON: `https://www.sec.gov/files/company_tickers.json`.
- Zero-pad CIK to 10 digits, then fetch submissions: `https://data.sec.gov/submissions/CIK##########.json`.
- Prioritize recent `8-K`, `10-Q`, `10-K`, proxy, registration, and material amendments.
- For each material filing, use the SEC archive URL built from CIK without leading zeros and accession without dashes:
  - `https://www.sec.gov/Archives/edgar/data/[cik_int]/[accession_no_dashes]/[primary_doc]`
- For earnings 8-Ks, inspect `index.json` in the filing directory to find Exhibit 99.1 if the primary 8-K only references the release.

## Price-move check

- A practical fallback market-data source is Yahoo chart JSON:
  - `https://query1.finance.yahoo.com/v8/finance/chart/[TICKER]?period1=[unix]&period2=[unix]&interval=1d&events=history`
- Use adjusted close/close for approximate recent move context.
- State dates and calculations in plain English, e.g. “closed at $X on [date] and $Y on [date], down about Z%.”
- Treat price movement as context only, not thesis proof.
- If the stock gaps after an earnings release, separate:
  - close-to-close move,
  - next-day open gap,
  - likely driver from filings/company sources.

## Output discipline

- If earnings are the main update, summarize only the earnings headline and route to `!earnings TICKER`.
- Do not expand into a full quarter review inside `!updates`.
- Save `updates.md` only after a material update is actually found and the report is complete.
