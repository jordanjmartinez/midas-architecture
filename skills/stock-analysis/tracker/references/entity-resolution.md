# Tracker Entity Resolution

This is command-local support for !track. It does not replace GLOBAL.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, or tracker contracts.

## Purpose

Use this note when a tracker result depends on correctly resolving a person, fund, filer, issuer, security, ticker, or related disclosure. Disclosed ticker/company mapping is part of evidence quality, not a separate thesis.

## Person, fund, and filer identity

- Resolve the user input to a verified canonical person or fund before analyzing or saving anything.
- Distinguish the individual, advisory firm, reporting fund, SEC filer, account, issuer, and disclosed security.
- Do not treat a fund name, manager name, CIK, issuer name, or security title as a public-company ticker without verification.
- For fund-manager runs, confirm the SEC filer / CIK and that the filing belongs to the relevant manager, firm, fund, or related account.
- For politician/public-official runs, confirm the public role and disclosure source before treating rows as that person's reportable activity.

## Filing and accession identity

- When filing identity matters, keep the filing type, filing date, report/as-of period, accession, amendment status, and filer identity straight.
- Do not compare a current filing to an unrelated prior filing just because names look similar.
- If multiple filer accounts or related entities exist, state the identity assumption or limit conclusions to the verified filer.

## Issuer, security, and ticker mapping

- Resolve disclosed securities before presenting company-level research leads.
- Verify current public tickers when 13F issuer names, security titles, CUSIPs, or prior tickers appear stale.
- Watch for renamed companies, redomiciliations, mergers, spin-offs, relistings, reorganizations, exchanged shares, CUSIP changes, and class changes.
- Use issuer names, prior/current ticker evidence, CUSIP/security-title continuity, SEC/company filings, exchange notices, and official company releases when mapping old securities to current tickers.
- If mapping is plausible but not verified, label it as `Ticker mapping needs verification` and do not silently merge old and current securities.
- If mapping is not verified, keep the source security name and avoid presenting a confident company-level ticker lead.

## Avoid common identity errors

- Do not mix 13F holdings with 13D/G/Form 4 evidence without source-type labeling.
- Do not infer that the manager currently owns a disclosed position after the filing period unless a current source supports it.
- Do not convert broad ETFs, index options, baskets, or ambiguous derivatives into company-level leads.
- Do not bury a relevant security only because its ticker changed; investigate mapping when the change could affect ranking.
- Do not present a company as a lead if the disclosed instrument is only an ambiguous option, hedge, fund, or non-company exposure unless the caveat is clear.

## Ambiguity handling

- If identity ambiguity materially changes the tracker result, ask for clarification or state the identity assumption.
- Use `Unknown` when a field cannot be verified.
- If a related expected name is missing from the reviewed disclosure table, check or caveat related-disclosure sources before concluding there is no tracker signal.
- Identity uncertainty should lower evidence quality and may block Best Stock Leads promotion under the active mode contract.
