# Midas Metrics Standards

## Purpose

METRICS.md defines how Midas should calculate, label, interpret, and display financial metrics across research commands.

The goal is to prevent inconsistent calculations, stale data, false precision, bad peer comparisons, and misuse of financial ratios.

Metrics should support disciplined research.

Metrics are not investment recommendations.

This file applies across commands such as:

- `!financials`
- `!research`
- `!gems`
- `!track`
- `!thesis`
- `!risk`
- `!earnings`
- `!updates`

METRICS.md does not replace:

- `rules/GLOBAL.md`
- `rules/SOURCES.md`
- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/OUTPUT.md`

---

# Core Principle

Every financial metric should be:

- Defined
- Sourced
- Period-labeled
- Unit-labeled
- As-of dated when time-sensitive
- Matched to the right business model
- Compared only to relevant peers or history
- Separated into reported, adjusted, estimated, guided, or inferred

Midas should not use a metric if it cannot tell what the metric means.

---

# Metric Labeling Standard

When displaying a metric, preserve:

- Metric name
- Formula or source definition when needed
- Period
- Currency
- Unit
- GAAP vs non-GAAP
- Reported vs adjusted
- Actual vs estimated
- Latest filing or market-data date when relevant

Good examples:

```md
Revenue Growth: +12% YoY, latest 10-Q period
```

```md
Free Cash Flow: CFO minus capex, TTM, company filings
```

```md
EV/EBITDA: 8.4x, TTM adjusted EBITDA, market data as of latest available price
```

```md
Net Debt / EBITDA: 2.1x, using filing debt/cash and TTM adjusted EBITDA
```

Bad examples:

```md
Cheap at 8x.
```

```md
Margins improved.
```

```md
FCF is strong.
```

```md
EV is $2B.
```

These are incomplete because they lack period, denominator, source, or context.

---

# Source Priority for Metrics

Follow:

`rules/SOURCES.md`

Use this priority:

1. SEC filings and company financial statements
2. Earnings release tables
3. Company reconciliations
4. Investor presentations
5. Earnings call transcripts for explanations
6. Current market data providers
7. Peer/valuation databases
8. Secondary research only for context

For financial metrics, prefer filing tables and company reconciliations over narrative commentary.

For valuation metrics, combine:

- Market data for price and market cap
- Filing data for share count, cash, debt, preferred stock, minority interest, and financial statements
- Company guidance only when explicitly disclosed
- Peer data only when comparable

For current price, market cap, volume, and market-data snapshot freshness rules, follow `rules/MARKET_DATA.md`.

---

# As-Of Date Rule for Metrics

Time-sensitive metrics need an as-of date or source period.

Always preserve timing for:

- Share price
- Market cap
- Enterprise value
- Price performance
- Volume
- Short interest
- Share count
- Cash
- Debt
- Net debt
- Ownership data
- Insider transactions
- 13F positions
- Valuation multiples
- Consensus estimates
- Guidance
- Backlog

Do not mix stale filing data with current market data without noting the timing difference.

Example:

```md
Enterprise Value uses latest available market cap plus cash/debt from the latest 10-Q, so the balance-sheet inputs may lag the current share price.
```

---

# GAAP / Non-GAAP Discipline

Midas must distinguish GAAP from non-GAAP metrics.

Common non-GAAP or adjusted metrics include:

- Adjusted EBITDA
- Adjusted EBIT
- Adjusted EPS
- Adjusted net income
- Adjusted operating income
- Free cash flow, depending on definition
- Organic revenue
- Constant-currency revenue
- Pro forma revenue
- Run-rate revenue
- Core earnings
- Normalized margin
- Funds from operations
- Adjusted funds from operations
- Distributable cash flow

Rules:

- Do not treat non-GAAP metrics as equivalent to GAAP metrics.
- Check company reconciliations when available.
- Identify whether the metric is reported, adjusted, estimated, guided, or inferred.
- Watch for recurring “one-time” adjustments.
- Watch for stock-based compensation exclusions.
- Watch for acquisition-related add-backs.
- Watch for restructuring charges that recur.
- Watch for changes in definitions across periods.
- Do not compare two companies’ adjusted metrics unless their definitions are reasonably comparable.

If non-GAAP adjustments are aggressive, central to the thesis, or poorly reconciled, flag it as a risk or evidence-quality issue.

---

# Period Conventions

Use the correct period for each metric.

Common periods:

- Quarterly
- Year-to-date
- Trailing twelve months / TTM / LTM
- Annual
- Fiscal year
- Calendar year
- Forward next twelve months / NTM
- Guidance period
- Run-rate

Rules:

- Do not mix quarterly, annual, TTM, and forward metrics without labeling them.
- Do not annualize one quarter unless the business is stable and seasonality is low.
- If annualizing a quarter, label it clearly as a run-rate or estimate.
- Do not compare TTM metrics with forward peer multiples without saying so.
- For cyclical businesses, show mid-cycle or normalized metrics when possible.
- For seasonal businesses, compare year-over-year rather than sequentially unless sequential comparison is meaningful.

---

# Unit and Currency Rules

Always preserve units.

Examples:

- Dollars
- Millions
- Billions
- Basis points
- Shares
- Percent
- Multiples
- Per-share values

If a company reports in non-USD currency, preserve the reported currency unless conversion is necessary.

If converting currencies:

- State the exchange-rate basis.
- Label converted numbers as approximate.
- Avoid false precision.

---

# Share Count Rules

Share count matters for market cap, EPS, per-share value, dilution, and valuation.

Use:

- Basic shares for simple ownership context
- Diluted shares for EPS and fully diluted valuation
- Weighted-average shares for period metrics
- End-of-period shares for market cap when appropriate
- Fully diluted shares when options, warrants, converts, RSUs, or preferred stock materially affect ownership

Rules:

- Prefer diluted share count for per-share valuation when dilution is material.
- If dilution is meaningful, show both basic and diluted context.
- Check for recent offerings, buybacks, warrants, converts, preferred stock, options, RSUs, and ATM programs.
- Do not use stale share count after major issuance or buyback.
- Do not ignore in-the-money warrants or convertibles if they materially affect valuation.
- For microcaps and speculative companies, dilution risk should be treated as a major metric issue.

---

# Market Capitalization

## Formula

```md
Market Cap = Share Price × Shares Outstanding
```

Preferred convention:

```md
Market Cap = Latest share price × latest diluted or end-of-period shares, depending on use case
```

Rules:

- Use current market data for price.
- Use the latest reliable share count.
- State whether basic, diluted, or fully diluted share count is used when material.
- For companies with major recent issuance, adjust share count if possible.
- For dual-class shares, include all economic share classes if they represent ownership.
- For ADRs, confirm ADR ratio before calculating per-share or market cap values.

Use market cap for equity-value metrics such as:

- P/E
- P/S
- P/B
- P/FCF
- Dividend yield
- Buyback yield
- Earnings yield

---

# Enterprise Value

## Formula

```md
Enterprise Value = Market Cap + Total Debt + Preferred Stock + Minority Interest - Cash and Cash Equivalents
```

When available, include:

- Short-term debt
- Long-term debt
- Finance leases
- Preferred equity
- Minority interest
- Pension deficits when material
- Other debt-like obligations when material
- Cash and cash equivalents
- Marketable securities when clearly excess and available

Rules:

- Use EV for metrics where the denominator belongs to all capital providers.
- Do not use EV blindly for banks, insurers, or financial firms.
- Check whether cash is excess cash or operating cash.
- For net-cash companies, EV can be very low or even negative; explain the implication.
- For highly leveraged companies, EV-based multiples are usually more informative than equity-only multiples.
- For acquisition-heavy companies, check whether debt, earnouts, leases, and minority interests are fully captured.
- For companies with significant leases, decide whether lease liabilities should be treated as debt and be consistent.

Use enterprise value for:

- EV/Revenue
- EV/Gross Profit
- EV/EBITDA
- EV/EBIT
- EV/FCF
- EV/FCFF
- EV/Backlog when appropriate
- EV/Reserves or EV/Production for resource companies when appropriate

---

# Net Debt / Net Cash

## Formula

```md
Net Debt = Total Debt - Cash and Cash Equivalents
```

```md
Net Cash = Cash and Cash Equivalents - Total Debt
```

When relevant, include:

- Short-term debt
- Long-term debt
- Finance leases
- Preferred stock
- Restricted cash only when clearly usable
- Marketable securities only when liquid and available

Rules:

- Do not assume all cash is excess cash.
- For companies with restricted cash, separate restricted and unrestricted cash if disclosed.
- For banks and insurers, do not use industrial net debt logic.
- For distressed companies, check maturity schedule, covenants, interest expense, and liquidity.
- For acquisition-heavy companies, consider contingent consideration and earnouts.

---

# Revenue

Revenue should be measured and interpreted carefully.

Common metrics:

```md
Revenue Growth = (Current Period Revenue - Prior Period Revenue) / Prior Period Revenue
```

```md
Organic Revenue Growth = Revenue Growth excluding acquisitions, divestitures, currency, and other disclosed adjustments
```

Rules:

- Use reported revenue from filings or earnings releases.
- Label quarterly, annual, YTD, TTM, or forward revenue.
- Separate reported growth from organic growth.
- Separate constant-currency growth from reported growth.
- Watch for acquisitions driving revenue growth.
- Watch for one-time revenue or pull-forward.
- Watch for customer concentration.
- Watch for backlog conversion into revenue.
- Watch for revenue growth without cash conversion.
- For software or subscription businesses, ARR/MRR may be more useful than GAAP revenue, but definitions must be company-disclosed.

---

# Gross Profit and Gross Margin

## Formula

```md
Gross Profit = Revenue - Cost of Goods Sold / Cost of Revenue
```

```md
Gross Margin = Gross Profit / Revenue
```

Rules:

- Use company-reported gross profit when available.
- If cost of revenue is not disclosed clearly, say so.
- Compare gross margin to company history and peers.
- Watch for mix shift, pricing, input costs, utilization, freight, labor, and product/service mix.
- For software, gross margin can indicate scalability.
- For manufacturing, gross margin may be driven by raw materials, utilization, and pricing.
- For retailers, gross margin should be analyzed with inventory and markdowns.
- For service companies, gross margin definitions can vary.

---

# Operating Income and Operating Margin

## Formula

```md
Operating Margin = Operating Income / Revenue
```

Rules:

- Prefer GAAP operating income unless adjusted operating income is clearly reconciled.
- Separate GAAP operating margin from adjusted operating margin.
- Watch for restructuring add-backs.
- Watch for stock-based compensation exclusions.
- Watch for acquisition-related amortization.
- Operating margin expansion is stronger when paired with revenue growth and cash conversion.
- Margin expansion from cost cuts alone may not be durable.

---

# EBITDA and Adjusted EBITDA

## Basic Formula

```md
EBITDA = Net Income + Interest + Taxes + Depreciation + Amortization
```

or:

```md
EBITDA = EBIT + Depreciation + Amortization
```

Rules:

- EBITDA is not free cash flow.
- EBITDA ignores capital expenditures.
- EBITDA ignores working capital needs.
- EBITDA ignores taxes and interest.
- EBITDA can overstate economics for capital-intensive companies.
- Use adjusted EBITDA only if reconciled.
- Check whether adjustments are recurring.
- For highly acquisitive companies, adjusted EBITDA may exclude costs that are economically real.
- For software companies, adjusted EBITDA may exclude stock-based compensation; flag if material.
- For industrials, utilities, telecom, energy, and transportation, EBITDA should be paired with capex and free cash flow.

Preferred use:

- Capital-structure-neutral comparison
- Debt capacity analysis
- Peer valuation
- Covenant context when disclosed

Avoid using EBITDA as the only profitability metric.

---

# EBIT and NOPAT

## EBIT

```md
EBIT = Earnings Before Interest and Taxes
```

## NOPAT

```md
NOPAT = EBIT × (1 - Tax Rate)
```

Rules:

- EBIT is useful for comparing operating profit before financing.
- NOPAT is useful for ROIC and enterprise valuation.
- Use normalized tax rate when appropriate.
- For companies with volatile or unusual tax rates, explain the assumption.
- For loss-making companies, NOPAT may not be meaningful.

---

# Free Cash Flow

Free cash flow must be defined every time it is material.

## Common Simple Formula

```md
Free Cash Flow = Cash Flow from Operations - Capital Expenditures
```

## FCFF Formula

```md
FCFF = CFO + Interest × (1 - Tax Rate) - Capital Expenditures
```

## FCFE Formula

```md
FCFE = CFO - Capital Expenditures + Net Borrowing
```

Rules:

- FCF is not uniformly defined across companies.
- Always state how FCF is calculated.
- Separate CFO from FCF.
- Separate FCFF from FCFE.
- Separate maintenance capex from growth capex when possible.
- If maintenance capex is not disclosed, say it must be estimated.
- Watch for working-capital timing benefits.
- Watch for factoring, receivables growth, inventory build, and deferred revenue changes.
- Watch for capex being temporarily depressed.
- Watch for acquisition spending excluded from FCF.
- Do not treat one strong FCF quarter as durable without checking seasonality and working capital.

Preferred use:

- Cash conversion
- Balance-sheet durability
- Valuation support
- Capital allocation capacity
- Buyback/dividend sustainability

---

# Owner Earnings

Owner earnings approximates the cash a business can generate for owners after required reinvestment.

## Conceptual Formula

```md
Owner Earnings = Reported Earnings + Depreciation / Amortization and Other Non-Cash Charges - Maintenance Capex - Required Working Capital Investment
```

Rules:

- Owner earnings requires judgment.
- Maintenance capex is often an estimate.
- Do not present owner earnings with false precision.
- Use owner earnings mainly for mature businesses with understandable reinvestment needs.
- For capital-intensive businesses, owner earnings may be far lower than EBITDA.
- For high-growth companies, distinguish maintenance investment from growth investment.
- If maintenance capex is not disclosed, label the estimate clearly.

Owner earnings is useful because it focuses on economic cash generation, not just accounting earnings.

---

# Cash Conversion

Cash conversion tests whether earnings turn into cash.

Useful formulas:

```md
FCF Conversion = Free Cash Flow / Net Income
```

```md
FCF Conversion = Free Cash Flow / Adjusted Net Income
```

```md
CFO Conversion = Cash Flow from Operations / Net Income
```

```md
EBITDA-to-FCF Conversion = Free Cash Flow / EBITDA
```

Rules:

- Use the denominator that matches the question.
- If net income is negative, conversion ratios may be meaningless.
- Weak cash conversion can signal poor earnings quality.
- Strong cash conversion from working-capital release may not be durable.
- Compare cash conversion across multiple periods.
- For software, deferred revenue can boost CFO; check billings and revenue recognition.
- For manufacturing/retail, inventory and receivables can distort cash conversion.

---

# Return on Equity

## Formula

```md
ROE = Net Income / Average Shareholders' Equity
```

Rules:

- Use average equity, not just ending equity, when possible.
- ROE can be inflated by leverage.
- ROE can be distorted by buybacks, write-downs, negative equity, and financial leverage.
- For banks, insurers, and asset-light financials, ROE is often central.
- For non-financial companies, ROIC is often more informative than ROE.
- Compare ROE with leverage and earnings variability.

---

# Return on Invested Capital

ROIC measures returns generated on operating capital.

## Common Formula

```md
ROIC = NOPAT / Average Invested Capital
```

## Common Invested Capital Definition

```md
Invested Capital = Total Debt + Shareholders' Equity + Preferred Stock + Minority Interest - Cash and Non-Operating Assets
```

Alternative operating approach:

```md
Invested Capital = Net Working Capital + Net PP&E + Operating Intangibles + Other Operating Assets - Operating Liabilities
```

Rules:

- Use average invested capital when possible.
- Define invested capital clearly.
- Use NOPAT rather than net income.
- Compare ROIC to WACC when possible.
- Sustained ROIC above WACC suggests value creation.
- ROIC can be distorted by goodwill, acquisitions, write-downs, leases, and capital-light models.
- For acquisitive companies, show ROIC including and excluding goodwill when useful.
- For banks and insurers, ROIC is usually not the right metric.
- For asset-light companies, very high ROIC may be real but should be checked against reinvestment runway and competitive advantage.

---

# Return on Capital Employed

ROCE is another operating return metric.

## Common Formula

```md
ROCE = EBIT / Capital Employed
```

```md
Capital Employed = Total Assets - Current Liabilities
```

or:

```md
Capital Employed = Equity + Debt - Cash
```

Rules:

- Define the denominator because ROCE definitions vary.
- Use ROCE when it better matches the company or source material.
- ROCE is useful for industrials, consumer businesses, and asset-heavy businesses.
- Compare to company history and peers.

---

# Earnings Per Share

## Formula

```md
EPS = Net Income Available to Common Shareholders / Weighted-Average Shares
```

Rules:

- Separate basic EPS from diluted EPS.
- Separate GAAP EPS from adjusted EPS.
- Watch for buybacks masking flat net income.
- Watch for dilution masking revenue or earnings growth.
- Watch for one-time gains or losses.
- For cyclical businesses, normalized EPS may be more useful than TTM EPS.
- For loss-making companies, P/E is not meaningful.

---

# P/E Ratio

## Formula

```md
P/E = Share Price / Earnings Per Share
```

or:

```md
P/E = Market Cap / Net Income
```

Types:

- Trailing P/E
- Forward P/E
- Normalized P/E
- Cyclically adjusted P/E when appropriate

Rules:

- Use P/E for profitable companies with meaningful earnings.
- Do not use P/E for companies with negative or temporarily distorted earnings.
- Check whether EPS is GAAP or adjusted.
- Check whether forward EPS is consensus, company guidance, or Midas estimate.
- P/E is affected by leverage because earnings are after interest.
- For capital-intensive or highly leveraged companies, EV-based multiples may be more useful.
- For cyclical companies, use normalized or mid-cycle earnings.

---

# Earnings Yield

## Formula

```md
Earnings Yield = EPS / Share Price
```

or:

```md
Earnings Yield = Net Income / Market Cap
```

Rules:

- Earnings yield is the inverse of P/E.
- Use it to compare earnings power against alternative returns only when earnings are durable.
- Do not use unadjusted earnings yield when earnings are cyclical, temporarily depressed, or inflated.

---

# Price to Sales

## Formula

```md
P/S = Market Cap / Revenue
```

Rules:

- P/S is an equity-value multiple.
- P/S ignores debt and cash.
- P/S ignores profitability.
- Use only when earnings are negative or margins are not yet mature.
- For leveraged companies, prefer EV/Revenue.
- A low P/S is not automatically cheap if margins are poor or debt is high.
- A high P/S may be reasonable only when growth, margins, retention, and reinvestment economics support it.

---

# EV / Revenue

## Formula

```md
EV/Revenue = Enterprise Value / Revenue
```

Rules:

- EV/Revenue is more capital-structure-neutral than P/S.
- Useful for early-stage, low-margin, or temporarily unprofitable businesses.
- Dangerous if used without margin context.
- Always pair with gross margin, operating margin, growth, and cash burn.
- Do not compare companies with very different margin structures using EV/Revenue alone.

---

# EV / Gross Profit

## Formula

```md
EV/Gross Profit = Enterprise Value / Gross Profit
```

Rules:

- Useful when revenue quality differs due to gross margin differences.
- Helpful for software, marketplaces, distributors, retailers, and businesses with pass-through revenue.
- Still does not capture operating expenses, capex, or cash flow.
- Pair with operating margin and FCF.

---

# EV / EBITDA

## Formula

```md
EV/EBITDA = Enterprise Value / EBITDA
```

Rules:

- Useful for comparing operating businesses with different capital structures.
- Less useful when capex is heavy or depreciation is economically real.
- Less useful when EBITDA is negative or heavily adjusted.
- Pair with capex, FCF, leverage, and business quality.
- Do not treat low EV/EBITDA as cheap without checking debt, cyclicality, maintenance capex, and earnings quality.
- For financial institutions, EV/EBITDA is usually inappropriate.

---

# EV / EBIT

## Formula

```md
EV/EBIT = Enterprise Value / EBIT
```

Rules:

- Often better than EV/EBITDA when depreciation and amortization are economically meaningful.
- Useful for capital-intensive businesses.
- Still requires normalization if earnings are cyclical.
- Pair with ROIC and FCF conversion.

---

# EV / Free Cash Flow

## Formula

```md
EV/FCF = Enterprise Value / Free Cash Flow
```

or:

```md
Unlevered FCF Yield = FCFF / Enterprise Value
```

Rules:

- Use FCFF for enterprise-value comparisons.
- Use FCFE or simple FCF carefully for equity-owner cash flow.
- Make sure FCF definition is clear.
- Negative or volatile FCF makes this metric less useful.
- Do not use one-year FCF if working capital or capex is abnormal.
- For capital-intensive companies, this may be more useful than EV/EBITDA.

---

# Price / Free Cash Flow

## Formula

```md
P/FCF = Market Cap / Free Cash Flow to Equity
```

or:

```md
FCF Yield = Free Cash Flow / Market Cap
```

Rules:

- Use equity free cash flow if comparing to market cap.
- State whether FCF is CFO minus capex, FCFE, or another company-defined metric.
- Check whether debt issuance is funding shareholder returns.
- Check whether FCF covers dividends and buybacks.
- For net-cash companies, also consider EV/FCF.

---

# Price / Book

## Formula

```md
P/B = Market Cap / Common Shareholders' Equity
```

or:

```md
P/B = Share Price / Book Value Per Share
```

Rules:

- Useful for banks, insurers, asset-heavy businesses, holding companies, and deep value situations.
- Less useful for asset-light companies where book value does not capture intangible value.
- Negative book value makes P/B meaningless.
- Pair P/B with ROE.
- A low P/B is not automatically cheap if ROE is weak, assets are impaired, or losses are ongoing.
- For financial firms, book value quality matters.

---

# Net Debt / EBITDA

## Formula

```md
Net Debt / EBITDA = Net Debt / EBITDA
```

Rules:

- Use TTM EBITDA unless stated otherwise.
- Use adjusted EBITDA only if reconciled.
- For cyclical companies, use mid-cycle EBITDA when possible.
- If EBITDA is negative or temporarily inflated, ratio may be meaningless.
- Debt maturity schedule matters more than the headline ratio in stressed situations.
- Pair with interest coverage, FCF, liquidity, and covenant risk.
- For banks and insurers, do not use industrial leverage ratios.

---

# Interest Coverage

## Formula

```md
Interest Coverage = EBIT / Interest Expense
```

or:

```md
Interest Coverage = EBITDA / Interest Expense
```

Rules:

- EBIT coverage is stricter than EBITDA coverage.
- Use cash interest when available.
- Watch for floating-rate debt.
- Watch for capitalized interest.
- Watch for PIK interest.
- Watch for refinancing risk and maturities.
- Weak interest coverage should affect risk scoring.

---

# Debt Maturity and Liquidity

Important metrics:

```md
Liquidity = Cash + Available Revolver Capacity + Other Available Funding
```

```md
Near-Term Debt Burden = Debt Due Within 12–24 Months
```

Rules:

- For fragile companies, maturity schedule matters more than total debt alone.
- Check revolver availability and covenants.
- Check whether cash is restricted.
- Check whether debt is secured or unsecured.
- Check whether refinancing depends on capital markets.
- Check whether the company is free cash flow positive.
- Liquidity stress should affect Setup Classification, Risk, and Scoring.

---

# Dilution Metrics

Important metrics:

```md
Share Count Growth = Current Shares / Prior Shares - 1
```

```md
Market Cap Growth vs Per-Share Value Growth
```

```md
Stock-Based Compensation / Revenue
```

```md
Stock-Based Compensation / Gross Profit
```

```md
Stock-Based Compensation / Operating Cash Flow
```

Rules:

- Track diluted share count over time.
- Watch for ATM programs, warrants, converts, preferred stock, RSUs, and options.
- Revenue growth can be less attractive if per-share value is diluted.
- Stock-based compensation is economically real even if excluded from adjusted earnings.
- For small caps and speculative companies, dilution can be thesis-breaking.

---

# Buyback Yield and Dividend Yield

## Formulas

```md
Dividend Yield = Annual Dividends Per Share / Share Price
```

```md
Net Buyback Yield = Net Share Repurchases / Market Cap
```

```md
Shareholder Yield = Dividend Yield + Net Buyback Yield
```

Rules:

- Buybacks are value-accretive only if done below intrinsic value.
- Buybacks funded with debt or dilution elsewhere require scrutiny.
- Dividend yield must be checked against FCF coverage.
- High dividend yield can signal distress.
- For cyclical companies, payout sustainability should be tested through the cycle.

---

# Backlog and Book-to-Bill

## Formulas

```md
Book-to-Bill = Orders / Revenue
```

```md
Backlog Growth = Current Backlog / Prior Backlog - 1
```

```md
Backlog Coverage = Backlog / Revenue
```

Rules:

- Use company definitions.
- Check whether backlog is firm, cancellable, funded, awarded, or only pipeline.
- Backlog is not revenue until delivered.
- Watch for margin quality of backlog.
- Watch for customer concentration.
- Watch for backlog growth without revenue or cash conversion.
- For contractors and project businesses, backlog conversion and margin are critical.

---

# Working Capital Metrics

Important metrics:

```md
Days Sales Outstanding = Accounts Receivable / Revenue × Days
```

```md
Days Inventory Outstanding = Inventory / Cost of Goods Sold × Days
```

```md
Days Payable Outstanding = Accounts Payable / Cost of Goods Sold × Days
```

```md
Cash Conversion Cycle = DSO + DIO - DPO
```

Rules:

- Rising receivables faster than revenue can signal collection risk.
- Rising inventory can signal demand problems or supply-chain build.
- Rising payables can temporarily boost cash flow.
- Working-capital release may not be durable.
- For retailers, distributors, manufacturers, and hardware companies, working capital is central.
- For software, deferred revenue and billings are important.

---

# Inventory Metrics

Important metrics:

```md
Inventory Turnover = Cost of Goods Sold / Average Inventory
```

```md
Days Inventory = Average Inventory / Cost of Goods Sold × Days
```

Rules:

- Watch for inventory growing faster than revenue.
- Watch for write-downs.
- Watch for obsolete inventory.
- Watch for channel stuffing.
- Inventory build may be bullish if demand is confirmed, but risky if revenue does not follow.

---

# Customer Concentration Metrics

Important metrics:

```md
Largest Customer % of Revenue
```

```md
Top 5 / Top 10 Customers % of Revenue
```

```md
Customer Concentration Change Over Time
```

Rules:

- Use filing disclosures when available.
- If a customer is unnamed, say so.
- If customer revenue is not quantified, say so.
- High customer concentration increases fragility.
- For small caps, one customer can define the thesis.
- Customer concentration should affect risk, score caps, and Setup Classification.

---

# Segment Metrics

Segment metrics should be used when the company has multiple businesses with different economics.

Important metrics:

- Segment revenue
- Segment operating income
- Segment EBITDA if disclosed
- Segment margin
- Segment growth
- Segment assets
- Segment backlog
- Segment capex
- Segment customer exposure

Rules:

- Use company-disclosed segment definitions.
- Do not invent segment economics.
- Segment profit measures may differ from GAAP operating income.
- If the company changes segment reporting, note the change.
- Sum-of-the-parts valuation may be appropriate when segments have materially different growth, margin, or capital intensity.

---

# Guidance and Estimate Metrics

Guidance metrics may include:

- Revenue guidance
- EBITDA guidance
- EPS guidance
- FCF guidance
- Margin guidance
- Capex guidance
- Backlog or bookings guidance
- Production or volume guidance

Rules:

- Label guidance as company guidance.
- Preserve the guidance period.
- Preserve whether guidance is a range or point estimate.
- Do not treat guidance as fact.
- Compare guidance to prior guidance and actual results.
- If guidance is withdrawn, reduced, or made more uncertain, flag it.
- Consensus estimates are market expectations, not company facts.
- When using estimates, state whether they are consensus, company guidance, or Midas estimates.

---

# Valuation Multiple Rules

Multiples are shortcuts, not full valuation.

Rules:

- Match numerator and denominator.
- Use market cap with equity metrics.
- Use enterprise value with pre-debt operating metrics.
- Use current price/market cap with latest available balance sheet data.
- Use peer multiples only with relevant peers.
- Compare to company history when useful.
- Normalize cyclical earnings.
- Avoid single-multiple conclusions.
- Explain why the chosen multiple is appropriate.
- Do not call a stock cheap based on one multiple alone.

Correct pairings:

```md
Market Cap / Net Income
Market Cap / Free Cash Flow to Equity
Market Cap / Book Value
Enterprise Value / Revenue
Enterprise Value / Gross Profit
Enterprise Value / EBITDA
Enterprise Value / EBIT
Enterprise Value / FCFF
```

Bad pairings:

```md
Market Cap / EBITDA
Enterprise Value / Net Income
Market Cap / EBIT
Enterprise Value / EPS
```

These are usually mismatched because the numerator and denominator belong to different capital providers.

---

# Intrinsic Value and Margin of Safety

Metrics should support, not replace, intrinsic-value work.

Useful methods:

- Discounted cash flow
- Free cash flow to firm
- Free cash flow to equity
- Owner earnings
- Sum-of-the-parts
- Asset value / NAV
- Liquidation value
- Replacement value
- Residual income for financial firms
- Peer multiples as a cross-check

Margin of safety should be based on:

```md
Margin of Safety = Estimated Intrinsic Value - Current Market Price
```

or:

```md
Discount to Intrinsic Value = (Estimated Intrinsic Value - Market Price) / Estimated Intrinsic Value
```

Rules:

- Intrinsic value estimates are assumptions, not facts.
- Use ranges instead of false precision.
- Wider uncertainty requires a larger margin of safety.
- For fragile companies, demand more valuation support.
- For high-quality compounders, lower headline cheapness may be acceptable only if durability and reinvestment runway are strong.
- For speculative companies, valuation should be framed cautiously.

---

# Peer Comparison Rules

Peer comparisons should be relevant.

Good peers share:

- Similar business model
- Similar margins
- Similar growth profile
- Similar capital intensity
- Similar cyclicality
- Similar leverage
- Similar geography
- Similar end markets
- Similar accounting treatment
- Similar scale when possible

Rules:

- Do not compare a software company to hardware peers using EV/Sales without margin context.
- Do not compare banks to industrials using EV/EBITDA.
- Do not compare cyclical peak earnings to peer trough earnings.
- Do not compare adjusted metrics unless definitions are comparable.
- If peers are imperfect, say so.

---

# Sector-Specific Metric Rules

## Banks and Financial Institutions

Do not use industrial EV/EBITDA logic for banks.

Important metrics:

- Price / tangible book value
- Price / book value
- ROE
- ROTCE
- Net interest margin
- Efficiency ratio
- Loan growth
- Deposit growth
- Credit losses
- Nonperforming loans
- Charge-offs
- CET1 ratio
- Tier 1 capital ratio
- Liquidity coverage
- Tangible common equity
- Deposit beta
- Funding cost

Rules:

- Book value and capital ratios matter.
- Credit quality matters.
- Funding stability matters.
- Net interest margin matters.
- For banks, leverage is the business model, not the same as industrial debt.
- Do not calculate EV for banks unless a specialized financial-institution framework requires it.

## Insurance Companies

Important metrics:

- Price / book
- Price / tangible book
- ROE
- Combined ratio
- Loss ratio
- Expense ratio
- Float
- Investment income
- Reserve development
- Book value growth
- Premium growth
- Capital adequacy
- Underwriting profitability

Rules:

- For P&C insurers, combined ratio below 100% generally indicates underwriting profit.
- Investment income and underwriting quality both matter.
- Reserve adequacy is critical.
- Book value quality matters.
- Do not use simple industrial EV/EBITDA for insurers.

## REITs

Important metrics:

- Funds from operations / FFO
- Adjusted funds from operations / AFFO
- Net operating income / NOI
- Same-store NOI
- Occupancy
- Leasing spreads
- Cap rate
- Net asset value / NAV
- Debt / EBITDAre
- Interest coverage
- Dividend payout / AFFO
- Price / FFO
- Price / AFFO

Rules:

- FFO starts with GAAP net income and adjusts for real-estate depreciation/amortization and gains/losses from certain real estate asset sales.
- AFFO definitions vary by company.
- Do not use P/E as the primary REIT valuation metric.
- NAV and cap rates matter.
- Debt maturity schedule and interest-rate exposure matter.

## Energy and Natural Resources

Important metrics:

- Production volumes
- Realized price
- Lifting cost
- Reserve life
- Proved reserves
- Finding and development cost
- Recycle ratio
- Net debt / EBITDAX
- Free cash flow
- Maintenance capex
- Hedging position
- EV / reserves
- EV / production
- NAV

Rules:

- Commodity price assumptions drive valuation.
- Hedge books matter.
- Maintenance capex and decline rates matter.
- Reserve quality matters.
- Use normalized or mid-cycle pricing when appropriate.

## Utilities and Infrastructure

Important metrics:

- Rate base
- Allowed ROE
- Capex plan
- Regulatory lag
- Funds from operations / debt
- Interest coverage
- Dividend payout
- Debt / capitalization
- Customer growth
- Project backlog

Rules:

- Regulation drives economics.
- Capex can create value if added to rate base at attractive allowed returns.
- Balance sheet and credit metrics matter.
- Dividend safety depends on cash flow, capex, and regulatory recovery.

## SaaS / Software

Important metrics:

- ARR
- MRR
- Net revenue retention
- Gross retention
- Churn
- Gross margin
- CAC payback
- LTV/CAC
- Rule of 40
- Revenue growth
- FCF margin
- Stock-based compensation / revenue
- RPO / cRPO
- Billings
- Deferred revenue

Rules:

- Use company definitions for ARR, NRR, RPO, and billings.
- Watch for growth without FCF.
- Watch for stock-based compensation dilution.
- Gross retention is often more important than headline ARR growth.
- Rule of 40 should not replace unit economics.
- Deferred revenue and billings can distort CFO.

## Retail and Consumer

Important metrics:

- Same-store sales
- Traffic
- Ticket
- Gross margin
- Inventory turnover
- Markdown rate
- Operating margin
- Store count
- Sales per square foot
- E-commerce mix
- Loyalty/customer metrics
- Working capital
- Lease liabilities

Rules:

- Inventory quality matters.
- Same-store sales quality matters.
- Gross margin and inventory must be read together.
- Lease liabilities can be debt-like.
- Promotions can inflate sales while hurting margin.

## Industrial / Manufacturing

Important metrics:

- Orders
- Backlog
- Book-to-bill
- Capacity utilization
- Gross margin
- Operating margin
- Working capital
- Capex
- FCF conversion
- ROIC
- Net debt / EBITDA
- Customer concentration
- Input-cost exposure

Rules:

- Backlog margin matters as much as backlog size.
- Working capital swings can distort cash flow.
- Cyclicality and operating leverage matter.
- Capex and maintenance needs must be checked.

## Biotech / Pre-Revenue

Important metrics:

- Cash runway
- Cash burn
- Trial stage
- Pipeline breadth
- Probability-adjusted milestone value
- Regulatory timeline
- Partnerships
- Royalty economics
- Dilution risk
- Market opportunity
- Clinical data quality

Rules:

- Revenue multiples often do not apply.
- Valuation is highly assumption-driven.
- Cash runway and dilution are central.
- Do not treat trial success as certain.
- Use speculative classification when evidence is early-stage.

---

# Red Flags in Metrics

Midas should flag:

- Revenue growth without cash conversion
- Adjusted EBITDA growth while GAAP losses widen
- FCF improvement driven only by working-capital release
- Rising receivables faster than revenue
- Rising inventory faster than revenue
- Backlog growth without revenue conversion
- Gross margin pressure despite revenue growth
- Non-GAAP adjustments growing faster than revenue
- Repeated “one-time” charges
- Stock-based compensation materially diluting shareholders
- Buybacks while balance sheet deteriorates
- Dividend not covered by FCF
- Debt maturities approaching with weak liquidity
- Customer concentration not quantified
- Segment changes obscuring trends
- Guidance lowered while narrative remains bullish
- Share count rising materially
- EV distorted by stale cash/debt data
- Peer comparisons with non-comparable businesses

---

# Metric Quality Grades

Midas may grade metric quality when useful.

Use:

- **High** — Filing-backed, clearly defined, current, comparable, and relevant
- **Medium** — Source-backed but adjusted, estimated, partially comparable, or requires interpretation
- **Low** — Stale, loosely defined, non-GAAP without full reconciliation, inference-heavy, or weakly comparable
- **Not Useful** — Misleading, mismatched, unavailable, or inappropriate for the business model

Example:

```md
Metric Quality: Medium — EV/EBITDA is useful for peer context, but adjusted EBITDA excludes recurring restructuring costs.
```

---

# Output Format for Metrics

Compact format:

```md
Key Metrics:
- Revenue Growth: X% YoY, latest quarter
- Gross Margin: X%, latest quarter
- FCF: $X, TTM, CFO minus capex
- Net Debt / EBITDA: X.x, TTM
- Valuation: X.x EV/EBITDA, latest market data
```

Standard format:

```md
## Metrics Snapshot

| Metric | Value | Period | Source/Definition | Note |
|---|---:|---|---|---|
| Revenue Growth | X% | Latest quarter | 10-Q / earnings release | Reported |
| Gross Margin | X% | Latest quarter | Revenue less cost of revenue | Mix shift |
| FCF | $X | TTM | CFO - capex | Working capital helped |
| Net Debt / EBITDA | X.x | TTM | Filing debt/cash + adjusted EBITDA | Reconciled |
| EV/EBITDA | X.x | TTM | Market data + filing inputs | Peer context needed |
```

Full output may include:

```md
Metric Notes:
- GAAP vs non-GAAP:
- As-of date:
- Share count used:
- Cash/debt source:
- Adjustments:
- Red flags:
- Peer-comparison limitation:
```

---

# Relationship to SCORING.md

Metrics should feed scoring but not mechanically determine scoring.

Use:

`rules/SCORING.md`

Examples:

- Strong ROIC, FCF, margins, and low debt support Business Quality and Financial Strength.
- High valuation with weak FCF support should reduce Valuation / Margin of Safety.
- Rising dilution or weak liquidity should reduce Risk / Fragility.
- Strong backlog with poor conversion should reduce Information Gap confidence.
- Strong metrics with weak source quality should trigger score caps.

---

# Relationship to CLASSIFICATIONS.md

Metrics should support Setup Classification.

Use:

`rules/CLASSIFICATIONS.md`

Examples:

- High ROIC, durable margins, FCF, and reinvestment runway may support Quality Compounder.
- Low valuation, asset support, and survivable balance sheet may support Deep Value / Mispricing Candidate.
- Improving revenue, margin, FCF, and balance sheet may support Turnaround / Inflection Candidate.
- Weak liquidity, dilution, and customer concentration may support Speculative / High-Fragility Candidate.
- Overextended valuation metrics may support Watchlist / Awaiting Better Setup.

---

# Relationship to OUTPUT.md

Metrics should be displayed according to:

`rules/OUTPUT.md`

Rules:

- Keep metric output concise unless a full financial review is requested.
- Do not create giant tables unless they improve readability.
- Show as-of dates for time-sensitive metrics.
- State source limitations.
- Highlight red flags clearly.
- Avoid false precision.

---

# Final Metric Checklist

Before using a financial metric, Midas should ask:

- What is the exact formula?
- What is the source?
- What period does it cover?
- What unit is it in?
- Is it GAAP or non-GAAP?
- Is it reported, adjusted, estimated, guided, or inferred?
- Is the share count current?
- Is the balance sheet current?
- Is the market data current?
- Is this metric appropriate for the business model?
- Is the peer comparison valid?
- Does the metric hide dilution, leverage, capex, working capital, or cyclicality?
- Does this metric support or weaken the thesis?
- Does this metric affect score, classification, or risk?

## Final Rule

Metrics should clarify the business, not decorate the output.

If a metric is stale, mismatched, poorly defined, or misleading, Midas should say so or avoid using it.
