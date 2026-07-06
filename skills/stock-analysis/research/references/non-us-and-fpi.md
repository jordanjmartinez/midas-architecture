# !research Non-U.S. and Foreign Private Issuer Notes

This is command-local support for `!research`. It does not replace GLOBAL.md, SOURCES.md, OUTPUT.md, METRICS.md, or ARTIFACTS.md.

Use this when the issuer is a foreign private issuer, non-U.S. company, or otherwise lacks a normal U.S. 10-K / 10-Q filing pattern.

## Primary-source equivalents

- Treat Form 20-F as the annual primary-source equivalent for many FPIs.
- Use Form 6-K and attached exhibits for interim, earnings, MD&A, operating-review, or current-event updates when they contain useful disclosure.
- For non-SEC issuers, use annual reports, interim reports, local exchange filings, regulator filings, and official company disclosures.
- Inspect exhibits and local reports; the cover filing can be thin while the useful data lives in an attachment.
- Normal Source Notes should identify source type, filing/report date, period or report date, and source basis.
- Raw URLs/accessions are optional and mostly internal unless audit/source-recovery/debug context or ambiguity requires them.

## Avoid U.S.-issuer assumptions

Do not force U.S. 10-K/10-Q concepts when the issuer does not disclose that way.

Check what the issuer actually provides for:

- segments or operating divisions;
- channel, product, geography, and customer mix;
- revenue recognition and deferred revenue;
- RPO, backlog, ARR, or contract metrics, if disclosed;
- local currency, presentation currency, FX, tax, tariff, and country risk;
- customer, supplier, distributor, or manufacturing concentration.

## Contract-heavy or reset issuers

For FPIs or non-U.S. issuers with large infrastructure, AI/GPU, capacity, or outsourcing contracts:

- Separate legacy business from reset/current business when a divestiture or reorganization changed the company.
- Extract contract mechanics, not just headline value:
  - counterparty;
  - effective date and term;
  - deployment or tranche schedule;
  - service-level or availability obligations;
  - termination rights and service credits;
  - capex, power, data-center, financing, or delivery dependencies.
- Treat contract value and deferred revenue as evidence to pressure-test, not fully de-risked revenue.
- Label recurrence conditionally when delivery or availability obligations must be met.

## Hybrid models

For non-U.S. infrastructure, cybersecurity, application-delivery, consumer, or technology issuers:

- Separate subscription, support, services, hardware/software product, professional services, and other revenue when disclosed.
- Do not call the company pure SaaS, recurring, or asset-light unless filings support it.
- Explain when a cloud/security/subscription narrative coexists with hardware cycles, channel dependence, services, or incubating-loss segments.

## Source limitations

State plainly when:

- the issuer has no latest 10-K/10-Q pair;
- interim data comes from Form 6-K exhibits or local reports;
- segment, product, geography, contract, customer, or recurrence data is not disclosed;
- predecessor/legacy results are not comparable to the current business.
