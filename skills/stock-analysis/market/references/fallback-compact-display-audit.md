# Fallback Compact Display Audit

Use this reference when auditing or rendering a normal compact `!market [ticker]` output where the helper returns a usable price from a fallback provider.

## Trigger

The canonical helper returns:

- `ok: true`
- `provider` is a fallback provider, such as `Finnhub` or `Alpha Vantage`
- `fallbacks_used` is non-empty
- `provider_errors` includes sanitized failure/error details for an earlier provider

Example pattern from the RCAT smoke check:

- `provider: Finnhub`
- `primary_provider: Finnhub`
- `fallbacks_used: ["Finnhub"]`
- `provider_errors: [{"provider": "Financial Modeling Prep", "error": "FMP request failed: endpoint=quote, status=402"}]`

## Correct Compact Rendering

A compact successful fallback snapshot should still use the normal snapshot shape:

```md
📈 [Display Name] ($[TICKER]) | Market Snapshot
As of: [timestamp]

Price: [price]
Market Cap: [market cap or Not available]
Change: [change / percent if available]
Volume: [only if available]
Exchange: [exchange if available]
Source: [selected fallback provider]
```

## Display Rules

- It is valid to mention FMP unavailable/failed only when the fresh helper output actually shows FMP failure/no usable price and fallback use, **and** the command failed or the user explicitly asked for source/debug/raw output.
- In default compact success, do not add `Provider note:` even when a fallback provider was used; end at `Source: [selected provider]`.
- Do not dump provider metadata blocks, endpoint lists, source fields, or raw JSON in compact mode.
- Do not add the routine generic disclaimer/footer after a normal successful compact snapshot.
- Do not show `Volume` if the selected provider returned `volume: null`, unless full/expanded mode explicitly wants unavailable fields.
- Do not contaminate a primary-provider success with fallback language from another ticker or stale workspace artifact.

## Contrast With Successful FMP Snapshot

If the helper returns FMP as the selected provider with empty `fallbacks_used` and empty `provider_errors`, end after:

```md
Source: Financial Modeling Prep
```

No fallback note and no routine disclaimer/footer.
