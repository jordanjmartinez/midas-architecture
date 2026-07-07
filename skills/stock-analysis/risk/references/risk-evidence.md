# !risk Evidence Judgment

This is command-local support for !risk. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, or SCORING.md.

Use this when deciding which risks are material enough for a company risk assessment. OUTPUT.md owns section order and display. SOURCES.md owns source hierarchy. This file only supports risk-evidence judgment and recurring evidence pitfalls.

## Evidence boundaries

Separate risk claims into clear evidence levels:

- Disclosed risk: directly supported by filings, official disclosures, contracts, legal/regulatory documents, or company-reported metrics.
- Inferred risk: a reasonable analytical conclusion from disclosed facts, labeled as inference rather than fact.
- Possible risk: plausible but not verified or not specifically disclosed; use only when it matters to the diligence gap.
- Unsupported risk: do not present it as company-specific risk.

Use plain labels such as `not disclosed`, `not verified`, `possible but not verified`, `source limitation`, or `could not verify` when evidence is incomplete.

## Materiality and thesis-breaker discipline

- Rank risks by materiality and thesis-breaking potential, not by filing order or boilerplate length.
- A standard risk factor is not thesis-breaking unless company-specific facts make it material.
- Concentration, covenant, liquidity, legal/regulatory, customer-retention, credit, dilution, execution, or product-dependence risks can outrank broader macro risks when filings show direct exposure.
- Include disconfirming evidence when useful, especially evidence that reduces the severity or immediacy of a risk.
- Do not exaggerate low-probability risks for drama.
- Do not invent failure points to fill a section.

## Risk category boundaries

- Balance-sheet and liquidity risk should tie to cash, debt, maturities, covenants, financing needs, dilution, regulatory capital, collateral, or similar source-backed evidence.
- Cash-flow risk should tie to CFO/FCF quality, cash burn, working capital, capex, margin pressure, profitability, or cash-conversion evidence.
- Concentration risk should tie to disclosed or materially inferable customer, revenue, product, segment, geography, supplier, counterparty, platform, or channel dependence.
- Regulatory/legal risk should tie to actual regulatory regimes, proceedings, investigations, licensing, litigation, compliance, product restrictions, or policy exposure.
- Execution risk should tie to strategy, integration, operational capacity, management execution, restructuring, product launches, manufacturing, go-to-market, or control quality.

## Evidence discipline

- Treat prior Midas artifacts as secondary synthesis inputs, not primary proof.
- Treat management optimism as a claim to test, not risk reduction by itself.
- Treat social, promotional, or sentiment sources as discovery/context only, not proof of company-specific risk.
- Separate risk evidence from recommendation framing. Overall Risk Level is a research label, not buy/sell/hold guidance.
- Do not create Evidence Ledger or Risk Heat Map requirements in normal output; they are not active normal-output expectations for !risk.
