# Successful FMP Snapshot Display Audit

Use this reference when auditing a `!market` output that incorrectly mentions FMP unavailability, fallback behavior, provider errors, or routine limitation/footer text after a successful primary-provider snapshot.

## Trigger

A normal `!market [ticker]` response includes language such as:

- `FMP unavailable`
- `Financial Modeling Prep was unavailable`
- `FMP returned a provider limitation`
- fallback/provider-error notes despite `fallbacks_used: []`
- routine footer/disclaimer after `Source: [provider]`

## Audit Pattern

1. Compare the rendered output against the canonical helper JSON for the same ticker.
2. Treat these helper fields as decisive for default compact rendering:
   - `ok: true`
   - `provider`
   - `primary_provider`
   - `fallbacks_used`
   - `provider_errors`
3. If `provider` and `primary_provider` are `Financial Modeling Prep`, `fallbacks_used` is empty, and `provider_errors` is empty, do not mention FMP unavailability or fallback behavior.
4. Check `skills/stock-analysis/market/OUTPUT.md` before blaming provider behavior. The compact contract requires ending after `Source: [provider]` unless a specific/material provider limitation needs display.
5. Do not use stale workspace artifacts, pastes, or other commands' market-context wording as evidence for the current `!market` rendering. They may reflect prior fallback cases and should not contaminate a fresh successful primary-provider snapshot.

## Correct Compact Ending For Successful FMP Snapshot

```md
Source: Financial Modeling Prep
```

Then stop. No routine disclaimer/footer. No fallback note. No provider-error note.

## Pitfall

The helper may include generic `limitations` metadata in JSON even on success. For normal compact `!market`, those generic limitations are not automatically rendered. Render limitations only when they are specific/material to the returned snapshot, such as actual provider failure, fallback behavior that needs explanation, stale/as-of uncertainty, rate-limit notices, or missing required fields in failure/debug contexts.
