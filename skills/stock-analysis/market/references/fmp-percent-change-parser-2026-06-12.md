# FMP Percent-Change Parser Compatibility — 2026-06-12

## Context

During `!market HOOD` validation, the canonical helper was returning a usable Financial Modeling Prep quote, but the live FMP quote payload used the field name `changePercentage` for percent change. The helper previously looked only for `changesPercentage`, which could make percent change appear unavailable even when the selected FMP quote had it.

This is a provider-field compatibility issue, not a fallback-policy issue.

## Durable Lesson

For FMP quote percent change, parse both field spellings:

- preferred live field: `changePercentage`
- compatibility fallback: `changesPercentage`

The helper should record the exact field used in `source_fields.change_percentage`, e.g.:

- `FMP quote.changePercentage`
- `FMP quote.changesPercentage`

## Guardrails

- Do not call fallback providers solely because FMP percent change is missing or field-spelled differently if FMP returned a usable price.
- Do not add endpoints for this compatibility fix.
- Do not change compact output shape for this fix.
- Compact success still ends at `Source: [provider]`.
- Do not print API keys or raw credential-bearing URLs during live verification.

## Verification Pattern

Use three checks:

1. AST/syntax parse of `tools/market_data_snapshot.py`.
2. Mock parser coverage for both `changePercentage` and `changesPercentage`.
3. Live helper smoke test using sanitized output only; confirm selected provider, fallback list, percent value, and source field.

Expected live-success shape for FMP when `changePercentage` is present:

```json
{
  "ok": true,
  "provider": "Financial Modeling Prep",
  "fallbacks_used": [],
  "change_percentage": "non-null number",
  "source_fields.change_percentage": "FMP quote.changePercentage"
}
```

## Eval Hook

`evals/market.eval.md` should include an eval covering FMP `changePercentage` parsing so future parser edits do not regress to the legacy-only `changesPercentage` lookup.
