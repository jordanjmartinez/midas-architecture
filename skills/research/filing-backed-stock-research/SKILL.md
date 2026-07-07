---
name: filing-backed-stock-research
description: SEC filing-backed public-company stock research and business/financial analysis workflows with claim-level citations.
---

# Filing-Backed Stock Research

## MIDAS Routing Note

In the MIDAS profile, `!research`, `!financials`, `!thesis`, and `!risk` are MIDAS commands owned by `skills/stock-analysis/` and registered in `docs/COMMAND_REGISTRY.md`. This skill must not handle those triggers or define their output shapes; the command references in this skill and its references folder are historical (including references to the removed `!full`). Use this skill only for general filing-backed research workflows when no MIDAS command applies.

Use this skill when the user asks for stock research, company business-model research, financial analysis, thesis-style equity research, or asks to apply their Stock Research / Business Analysis / Financials prompt to a public company.

## Core principles

1. Prioritize primary filings first.
   - Use the most recent 10-K and 10-Q unless the user specifies exact filings/accessions.
   - If the user provides filing dates or accession numbers, use those exact filings and do not substitute newer filings without asking.
   - Treat press releases, investor decks, websites, and market commentary as secondary unless the user explicitly asks for them.

2. Cite every material claim.
   - Every business-model, revenue, margin, customer, geographic, risk, balance-sheet, or growth claim needs a source citation.
   - Prefer citations to SEC filing line numbers from extracted text.
   - If a claim is an inference, label it clearly as an interpretation and cite the facts that support it.

3. Do not overstate filing language.
   - Frame management claims as management claims, e.g. “Zeta says…” or “the company states…”
   - Do not turn a company’s competitive positioning language into independently verified fact.
   - If filings do not support an answer, say so directly.

4. Respect “do not analyze yet.”
   - If the user asks only for filing dates, accessions, or source gathering and says not to analyze, provide only that information.
   - Begin analysis only after an explicit analysis request.

## Workflow

0. Interpret command scope when invoked from chat shorthand.
   - Treat `!research $TICKER` as a standard company/financials research note.
   - Treat `!risk $TICKER` as a concise risk brief with rating, market facts, main risks, upside offsets, de-risking signals, and bottom line.
   - Treat `!full $TICKER` as a fuller equity-research note with verdict, business overview, latest quarter, annuals, balance sheet, cash flow, backlog/segments if relevant, dilution, bull/bear case, risks, catalysts, and bottom line.
   - In Telegram/mobile contexts, use headings and bullets; avoid markdown tables.
   - See `references/telegram-stock-command-modes.md` for reusable mobile note shapes.

1. Identify issuer and filings.
   - Resolve ticker to company/CIK through SEC company tickers.
   - Pull company submissions and identify the requested or latest 10-K/10-Q.
   - Record form type, filing date, accession number, and local extracted text path.

2. Extract and index filing text.
   - Download the filing HTML or primary document from SEC EDGAR.
   - Convert to readable text while preserving line numbers via the file-reading tool.
   - Search for key terms before drafting: Business, Overview, Revenue, Revenue Recognition, customers, segments, geography, seasonality, competition, risks, liquidity, debt, acquisitions, MD&A, Results of Operations.

3. Gather evidence before synthesis.
   - Read the business overview, revenue recognition/disaggregation, segment/geography, customer metrics, results of operations, liquidity/debt, and risk sections.
   - Capture exact figures and line references.
   - For quarterly updates, compare 10-Q MD&A against the prior-year quarter and the annual 10-K baseline.

4. Draft in the user’s preferred research shape.
   - Plain-English summary.
   - What the company does.
   - How it makes money by product/channel/segment.
   - Customers, customer concentration, recurrence, and purchase frequency.
   - Geography.
   - Pricing power and constraints.
   - Cyclicality / recession exposure / seasonality.
   - Recent financial performance.
   - Balance sheet, liquidity, debt, and capital allocation if relevant.
   - Recent acquisitions or major developments.
   - Red flags / risks.
   - Bottom-line business quality or thesis view, explicitly labeled as filing-based.

5. Verify before final answer.
   - Check every number against the extracted filing excerpt.
   - Make sure each material statement has a citation.
   - Avoid unsupported assumptions and market claims not present in filings.

## Citation style

Use compact citations in terminal-friendly prose:

- `(10-K lines 1511-1515)`
- `(10-Q lines 4804-4838)`
- Include filing/accession in the source list at the end.

When citing an interpretation, cite the underlying facts:

> Interpretation: revenue visibility is meaningful but not pure SaaS because the company discloses recurring revenue streams, usage-based revenue, non-automatic renewals in many relationships, and remaining performance obligations. (10-K lines …; 10-Q lines …)

## Pitfalls

- Do not mistake a SPAC/shell/new ticker history for the current operating business. Verify the issuer, recent business combination, redomiciliation, reverse split, and latest operating-company filings.
- Do not use unsupported assumptions about pricing power, moat, cyclicality, or customer retention.
- Do not cite secondary sources when SEC filings contain the answer.
- When using SEC `companyfacts`, do not select facts solely by newest `filed` date: new filings often restate old comparison periods. Filter by the target `fy`/`fp`/`form` or by the latest matching `frame`/`end` period before trusting the number.
- SEC `companyfacts` concept coverage can be uneven across issuers. If a concept returns stale results or missing current-period data (for example gross profit/cost concepts), extract the actual income statement table from the latest 10-Q/10-K HTML/text and use that as the controlling source.
- If a market-data endpoint rate-limits, continue with SEC filings for fundamentals and a different current market-data source for quote/valuation context rather than asking the user to retry.
- Do not preserve SEC request User-Agent contact details or other credentials in notes; redact as `[REDACTED]`.
- Do not create a long one-off narrative as procedural memory; if a session has useful details, place them under `references/` and keep the main skill class-level.

## Support files

- `references/zeta-business-analysis-2026.md` — example evidence map from a ZETA filing-backed business analysis using specified 2026 10-K and 10-Q accessions.
- `references/telegram-stock-command-modes.md` — reusable mobile-friendly output shapes and data workflow notes for `!research`, `!risk`, and `!full` ticker commands.
