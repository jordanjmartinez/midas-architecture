# FMP Selected-Provider Supplements — Stage 3 Implementation Notes (2026-06-12)

Use this reference when maintaining or extending `tools/market_data_snapshot.py` for `!market full` / `expanded` data enrichment.

## Scope

Stage 3 implemented FMP-only selected-provider supplements. These enrich helper JSON after FMP quote has already returned a usable price.

Approved FMP supplement endpoint labels:

- `FMP: profile`
- `FMP: stock-price-change`

## Durable implementation pattern

1. Call `FMP: quote` first.
2. Verify usable price before any supplement call.
3. Only then call FMP-side supplements.
4. If a supplement fails, keep the FMP quote usable.
5. Do not call Finnhub or Alpha Vantage because a supplement failed or omitted fields.
6. Store endpoint metadata as labels only, never raw URLs or credential-bearing params.
7. Keep compact output frozen; Stage 3 changes helper JSON only, not rendering.

## Helper fields added for full/expanded rendering

- `beta`
- `sector`
- `industry`
- `country`
- `ipo_date`
- `issuer_flags`
- `price_avg_50`
- `price_avg_200`
- `price_vs_50d_avg_percentage`
- `price_vs_200d_avg_percentage`
- `performance_5d_percentage`
- `performance_1m_percentage`
- `performance_3m_percentage`
- `performance_6m_percentage`
- `performance_ytd_percentage`
- `performance_1y_percentage`

Also extend `display_fields`, `source_fields`, and selected-provider payload propagation when adding helper fields.

## Non-fatal supplement failure pattern

Supplement failures should be captured as sanitized `provider_limitations`, e.g.:

```text
FMP profile fields unavailable: [sanitized error]
FMP price-performance fields unavailable: [sanitized error]
```

Do not add these failures to provider-level `provider_errors` unless the selected quote itself failed. They are limitations on enrichment, not provider-selection failures.

## Verification pattern

Run all of the following before reporting completion:

1. AST syntax parse for `tools/market_data_snapshot.py`.
2. Mock success test proving:
   - `FMP: quote`, `FMP: profile`, and `FMP: stock-price-change` are called in that order.
   - supplement fields populate.
   - Finnhub and Alpha Vantage are not called.
3. Mock supplement-failure test proving:
   - payload remains `ok: true` with FMP selected.
   - `fallbacks_used` remains empty.
   - sanitized limitation text does not expose secrets.
4. One scoped live helper smoke test with sanitized summary only.
5. `git diff --check` on changed files.

## Pitfalls

- Do not let supplement failures become fallback triggers.
- Do not move supplement fields into compact output before the explicit full/expanded rendering stage.
- Do not print raw helper JSON in final reports if it may include verbose provider limitations; summarize secret-safe fields only.
- Do not call non-selected providers for enrichment; selected-provider-only means no field-level fallback engine.
