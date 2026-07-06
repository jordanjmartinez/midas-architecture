# Market Data Fallbacks and Theme/Subtheme Screening Notes

Use this reference when a `!gems` run needs current market cap / stock-move context or a narrow theme/subtheme screen where obvious tickers may be too crowded.

## Market data fallback pattern

1. Start with a reliable quote source for latest price, market cap, and recent performance if available.
2. If a quote API fails or returns unusable/truncated data, do not stop the screen. Retry with a different source and document the source actually used.
3. Nasdaq historical endpoints can be used as a practical fallback for recent closes and 1m / 3m / 6m / 1y / YTD performance when other quote sources are unavailable.
4. For approximate market cap, pair latest close with the most recent SEC share count. Label it approximate and note the as-of dates.
5. Do not use failed data sources in the final artifact except as an internal note if relevant. The artifact should cite the source that actually supported the figures.

## Narrow theme/subtheme screening pattern

For hype-heavy subthemes such as AI agents:

1. Build the universe from direct theme names plus enabling-layer companies.
2. Separate direct exposure from enabling exposure:
   - Direct: company sells the workflow, agent, automation product, or AI platform.
   - Enabling: company provides data, knowledge management, annotation, infrastructure, customer operations, or other inputs that make the workflow possible.
3. Prefer companies with filing-backed language that ties the product/service to commercial use, not only press-release hype.
4. Downgrade names that are already obvious, crowded, or post-rerate even if business quality is better.
5. Classify fragile enablers as watch-only / risk-first when the same technology could cannibalize the core business.

## Useful examples from prior runs

- `CXM` fit as a researchable AI-agent workflow candidate because the exposure was enterprise workflow/customer-experience automation, not just generic AI branding.
- `EGAN` fit as a researchable niche knowledge-management candidate despite subscale market cap because filings tied trusted answers to customers, employees, and AI agents.
- `TASK` fit only as watch-only / risk-first because AI-services exposure was real, but AI cannibalization risk and leverage needed a risk review first.
- `INOD` was downgraded despite strong AI-enablement exposure because it was already sharply rerated and less pre-rerate.

These examples are not permanent views on those tickers; re-check filings, market data, and price performance on every new run.
