# Shares Outstanding Availability Note — 2026-06-12

## Trigger

Use this when a user asks why `Shares Outstanding` is missing or `Not available` in `!market full` / `expanded` output.

## Durable lesson

`!market` is a selected-provider, read-only market snapshot. It should not call fallback providers solely to fill non-price fields, and FMP/Finnhub selected-provider supplement responses may not provide a reliable common-shares-outstanding field for every ticker or plan.

## User-facing explanation pattern

Keep the answer short and diagnostic:

- The provider returned usable price/market data but did not return a reliable shares-outstanding value in the selected snapshot/supplement payload.
- `!market` does not infer shares outstanding from market cap divided by price unless explicitly requested, because that can mix timestamps, share classes, and diluted/basic definitions.
- Missing shares outstanding is not a quote failure and should not trigger fallback-provider calls.
- Normal full/expanded output should omit `Shares Outstanding` rather than showing a weak or derived number.

## Workflow pitfall

If the user asks only "why is it not available?" or says "do not modify files," answer from the existing helper/provider behavior and do not perform maintenance edits in that response. Skill-library maintenance is appropriate only when separately requested.
