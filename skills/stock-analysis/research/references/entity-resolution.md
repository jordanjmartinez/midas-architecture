# !research Entity Resolution

This is command-local support for `!research`. It does not replace GLOBAL.md, SOURCES.md, OUTPUT.md, METRICS.md, or ARTIFACTS.md.

Use this when ticker/company identity, issuer status, or predecessor/successor filings could affect the research target.

## Identity checks

Before analysis, resolve:

- legal issuer name
- ticker and exchange, when available
- SEC CIK or non-U.S. filing identifier, when applicable
- SEC filer / foreign private issuer / non-SEC issuer status
- latest primary-source filing set available for that issuer

Proceed with a stated identity assumption only when the match is clear enough that ambiguity would not change the company being researched.

## Ambiguous or unresolved inputs

Ask for clarification when:

- the ticker cannot be verified from checked issuer sources;
- the input plausibly maps to multiple public companies;
- a likely typo candidate exists but the user has not confirmed it;
- tentative evidence was gathered for a candidate before identity was confirmed.

Safe behavior:

- Offer possible matches as options, not substitutions.
- Do not save a final artifact for an unconfirmed likely candidate.
- Do not say the user clarified unless they actually did in the active conversation.
- If the user issues a new command before clarifying, abandon the unresolved prior ticker unless the new command resolves it.

## Successor / redomiciled / renamed issuers

Use extra care when:

- the current ticker maps to a recently renamed, redomiciled, merged, SPAC-successor, parent-reorganization, or successor issuer;
- the latest annual or quarterly filing appears under a predecessor or legacy operating-company name;
- a recent 8-K, plan of arrangement, merger filing, or exchange listing notice explains a legal transition.

Workflow:

- Resolve the current issuer identity first.
- Identify the predecessor operating entity and the filing that explains the transition.
- Use predecessor filings only when the issuer relationship is verified.
- Explain why predecessor filings are relevant to the current ticker.
- Separate current operating evidence from future target-model or transaction narrative.
- Use transition filings for identity/mechanics unless they also contain material operating disclosure.

## Source-limitation language

When needed, state:

- which legal entity filed the operating evidence;
- which current issuer/ticker the analysis applies to;
- what transition filing connects them;
- which business-model facts remain not disclosed in reviewed filings.
