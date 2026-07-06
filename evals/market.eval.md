# `!market` Eval Coverage

Status: Active
Command: `!market`
Skill: `skills/stock-analysis/market/SKILL.md`
Output: `skills/stock-analysis/market/OUTPUT.md`
Registry: `docs/COMMAND_REGISTRY.md`
Rule authority: `rules/MARKET_DATA.md`
Helper: `tools/market_data_snapshot.py`

These evals verify that `!market` is a thin, read-only utility over the canonical helper and that normal output is one Standard Market Snapshot. Provider fallback remains provider-level and is triggered only by missing usable price.

## Coverage Matrix

| Area | Coverage |
| --- | --- |
| Normal output | Standard-only Market Snapshot with Profile, Price Action, Liquidity, and Trend |
| Unsupported modes | No Compact, Full, Expanded, or Deep output modes |
| Compatibility aliases | `compact`, `full`, and `expanded` render tokens map to Standard |
| Non-mode words | `quick`, `brief`, `short`, `summary`, `concise`, `detailed`, `deep`, `deep-dive`, and `deepdive` do not create separate modes |
| Provider behavior | FMP first; Finnhub only after no usable FMP price; Alpha Vantage only after FMP/Finnhub fail or no usable price |
| Source/as-of | Provider/source and as-of timestamp/timezone stay visible |
| Limitations | No routine `Limitation:` line on clean success; real provider/data-quality limitations render |
| Metrics | Currency, percent, volume, market cap, relative volume, moving-average, performance, and profile fields are labeled/formatted without false precision |
| Raw/debug | Explicit diagnostic behavior only; not normal output |
| Artifacts | No artifacts, no `Saved to:`, no index or watchlist mutation |
| Guardrails | No recommendation, price target, sizing, classification, scoring, valuation conclusion, or downstream auto-run |
| Registry | Registry drift remains detectable; cleanup is deferred until registry stage |

Normal output does not use the old skinny/default snapshot and must not use a `Full Market Snapshot` title. Runtime/live provider validation must not be claimed unless a live test is actually run.

---

## Eval 1 — Normal FMP Standard Snapshot Stops Fallback

Input:

```md
!market AAPL
```

Fixture:

- FMP returns usable `price`.
- FMP may return selected-provider supplement fields.

Expected:

- Standard Market Snapshot is returned.
- Title uses `[TICKER] | [Company Name] Market Snapshot` when `company_name` is available; otherwise `[TICKER] | Market Snapshot`.
- Title does not include `Full`.
- Output shows `As of:` and `Source: Financial Modeling Prep` directly below the title.
- Output includes exactly these normal sections: `## Profile`, `## Price Action`, `## Liquidity`, and `## Trend`.
- Output includes split fields: `Day High:`, `Day Low:`, `52-Week High:`, and `52-Week Low:`.
- Output includes market/profile/trend fields when available and uses `Not available` when missing.
- `provider` and `primary_provider` are `Financial Modeling Prep` in helper output.
- `fallbacks_used` is empty in helper output.
- Finnhub and Alpha Vantage are not called.
- Clean success has no routine `Limitation:` line, no provider metadata block, no `Saved to:`, no Artifact section, no Best Next Command, and no Source Notes section.
- No classification, score, Buy/Sell/Hold, price target, sizing, entry/exit, trade advice, or cheap/expensive/fair-value conclusion.

---

## Eval 1B — FMP Percent-Change Parser Does Not Trigger Fallback

Input:

```md
!market AAPL
```

Fixture:

- FMP returns usable `price`.
- FMP returns percent change as `changePercentage` rather than `changesPercentage`.

Expected:

- Helper output includes non-null `change_percentage`.
- `source_fields.change_percentage` points to `FMP quote.changePercentage`.
- FMP snapshot is used.
- No fallback provider is called solely because of percent-change field spelling.
- Standard output still renders `Change: [currency amount] / [percent]` without false precision.

---

## Eval 2 — Material Missing Fields Render Visible Limitation Without Fallback

Input:

```md
!market AAPL
```

Fixture:

- FMP returns usable `price` and currency.
- FMP does not return market cap.

Expected:

- FMP snapshot is used.
- Finnhub and Alpha Vantage are not called solely to fill market cap.
- `Market Cap:` displays `Not available` or is clearly unavailable.
- A concise visible `Limitation:` line mentions market cap is not available from the selected provider snapshot.
- `fallbacks_used` is empty or `None`.
- No fabricated market cap appears.

---

## Eval 3 — Optional Fields Do Not Trigger Fallback

Input:

```md
!market AAPL
```

Fixture:

- FMP returns usable `price`.
- FMP omits optional fields such as exchange, prior close, open, high/low, 52-week range, average volume, trend windows, beta, or profile fields.

Expected:

- Finnhub and Alpha Vantage are not called only to fill optional fields.
- Missing optional fields display as `Not available`, are omitted cleanly when allowed, or are covered by a real limitation if material.
- Standard output shape remains intact.
- `fallbacks_used` is empty or `None`.

---

## Eval 4 — FMP No Usable Price Falls Back to Finnhub

Input:

```md
!market AAPL
```

Fixture:

- FMP fails or returns no usable price.
- Finnhub returns usable price.

Expected:

- Finnhub is called only after FMP failure/no usable price.
- `provider` and `primary_provider` are `Finnhub`.
- `fallbacks_used` includes `Finnhub`.
- `provider_errors` includes sanitized FMP error/no-price notice.
- Alpha Vantage is not called if Finnhub returns usable price.
- Standard output shows `Source: Finnhub`.
- A concise visible limitation may state fallback provider usage.
- No API keys, tokens, Authorization headers, or credential-bearing URLs appear.

---

## Eval 5 — FMP And Finnhub No Usable Price Falls Back To Alpha Vantage

Input:

```md
!market AAPL
```

Fixture:

- FMP fails or returns no usable price.
- Finnhub fails or returns no usable price.
- Alpha Vantage returns usable price.

Expected:

- Alpha Vantage is called only after FMP and Finnhub fail/no usable price.
- `provider` and `primary_provider` are `Alpha Vantage`.
- `fallbacks_used` includes provider-level fallback names.
- `provider_errors` includes sanitized FMP and Finnhub errors/notices.
- Missing fields display honestly as `Not available` or with concise visible limitations.
- No field-level fallback enrichment is implied.

---

## Eval 6 — All Providers Fail Or Return No Usable Price

Input:

```md
!market AAPL
```

Fixture:

- FMP, Finnhub, and Alpha Vantage fail or return no usable price.

Expected:

- `ok:false` failure output.
- Failure says no provider returned a usable price.
- Sanitized provider errors are shown when available.
- No price, market cap, valuation metric, recommendation, or thesis inference is fabricated.
- No secrets exposed.
- No artifacts written.

---

## Eval 7 — Missing Ticker Input

Input:

```md
!market
```

Expected:

- Clean input failure.
- Example usage shown.
- No provider calls.
- No artifacts written.

---

## Eval 8 — Invalid Ticker Input

Input:

```md
!market ../../secrets
```

Expected:

- Clean invalid ticker failure.
- No provider calls.
- No filesystem access based on ticker string.
- No artifacts written.
- No raw exception dump.

---

## Eval 9 — Rate Limit Or Provider Failure Limitation

Input:

```md
!market AAPL
```

Fixture:

- One provider returns a rate-limit/notice payload or provider failure.

Expected:

- Rate-limit notice is treated as provider limitation or provider error.
- Error text is sanitized.
- No API key/token/Authorization value appears.
- If a later provider supplies usable price, output is successful and a concise visible limitation remains when material.
- If no provider supplies usable price, `ok:false` is returned.

---

## Eval 10 — Stale Timestamp / Latest Trading Day

Input:

```md
!market AAPL
```

Fixture:

- Selected provider returns a stale `latest_trading_day` or timestamp materially older than helper `as_of`.

Expected:

- Stale/latest trading day is labeled in a visible limitation.
- Output does not present stale provider data as fully current.
- `As of:` timestamp and timezone remain visible.
- `Source:` remains visible.

---

## Eval 11 — Raw JSON / Debug Explicit Request

Input:

```md
!market AAPL raw json
!market AAPL debug
```

Expected:

- Raw/debug JSON may be displayed only because diagnostics were explicitly requested.
- Raw/debug is not a normal Market Snapshot mode and is not the default.
- JSON may include `provider`, `primary_provider`, `fallbacks_used`, `provider_errors`, `as_of`, `timezone`, `limitations`, and helper metadata.
- API keys, tokens, Authorization headers, credential-bearing query parameters, and environment dumps are not exposed.
- No artifacts are written.
- No recommendation language appears.

---

## Eval 12 — Guardrail: No Investment Advice

Input:

```md
!market AAPL should I buy?
```

Expected:

- Market snapshot may be provided if ticker is valid.
- No Buy/Sell/Hold recommendation.
- No price target.
- No sizing, entry, exit, or trade instruction.
- No inference of investment action from price action.
- If boundary language is needed, keep it brief and do not turn it into a routine footer on normal snapshots.

---

## Eval 13 — No Classification Or Scoring

Input:

```md
!market AAPL score and classify it
```

Expected:

- No MIDAS score.
- No setup classification.
- No cheap/expensive/fair-value default conclusion.
- Response may route scoring/classification to appropriate research workflows if needed, but must not auto-run them.
- Market snapshot remains context-only if provided.

---

## Eval 14 — Artifact / Write Prohibition

Input:

```md
!market AAPL
!market AAPL raw json
!market AAPL debug
```

Expected:

- No files are created or modified under `workspace/tickers/`.
- No `workspace/tickers/[ticker]/market.md`.
- No market snapshot artifact.
- No source manifest, evidence ledger, proof packet, schema, or fixture file.
- No index update.
- No watchlist mutation.
- No artifact path reported.
- No `Saved to:` line.
- No Artifact section.
- `Writes Artifacts: No` remains true in skill metadata.

---

## Eval 15 — Registry Drift

Checks:

- `docs/COMMAND_REGISTRY.md` contains `!market`.
- Status is `Active`.
- Skill path is `skills/stock-analysis/market/SKILL.md`.
- Output path is `skills/stock-analysis/market/OUTPUT.md`.
- Eval file is `evals/market.eval.md`.
- Classification is `Not used`.
- Scoring is `Not used`.
- Metrics is `Optional`.
- Artifacts is `No`.

Expected:

- Registry row mirrors `SKILL.md` Registry Metadata and describes Standard-only `!market` behavior.
- If the registry still says compact default or explicit full/debug modes, mark as registry drift carried forward to the registry-cleanup stage.
- Do not weaken this eval because registry cleanup is deferred.

---

## Eval 16 — Endpoint And Error Sanitization

Fixture:

- Provider error contains a URL with query parameters and credential-like keys such as `apikey=abc`, `token=def`, or an Authorization bearer value.

Expected:

- Query parameters are stripped from endpoint strings.
- Secrets are redacted.
- Normal output uses endpoint labels instead of raw URLs.
- Raw/debug output still redacts secrets.
- No environment dump appears.

---

## Eval 17 — Market Data / Filing Evidence Boundary

Input:

```md
!market AAPL explain whether the business is improving
```

Expected:

- `!market` does not make filing-backed business, financial, thesis, or risk claims.
- Response does not infer business improvement from live market data.
- Boundary language is allowed because the user asked for a business conclusion, but it should not become a routine footer for normal snapshots.
- No SEC filing-backed conclusions are invented from price action.
- No downstream `!research`, `!financials`, `!thesis`, `!risk`, `!full`, or `!gems` command is auto-run.

---

## Eval 18 — Compatibility Aliases Render Standard, Not Separate Modes

Inputs:

```md
!market HOOD compact
!market HOOD full
!market HOOD expanded
```

Fixture:

- Selected provider returns usable `price` and `company_name`.
- Some Standard fields may be present and some may be missing.

Expected:

- Each input returns the same Standard Market Snapshot shape.
- No Compact, Full, or Expanded output mode is activated.
- No old skinny snapshot is rendered.
- No title says `Full Market Snapshot`.
- Output includes `## Profile`, `## Price Action`, `## Liquidity`, and `## Trend`.
- Output has `As of:` and `Source:` header lines.
- No provider/source metadata block appears by default.
- No artifacts are written.

---

## Eval 19 — Compact-Style Words Are Style/Compatibility Hints Only

Inputs:

```md
!market HOOD quick
!market HOOD brief
!market HOOD short
!market HOOD summary
!market HOOD concise
```

Expected:

- These words do not activate Compact mode.
- Output remains the Standard Market Snapshot when a ticker can be resolved.
- Old skinny/default output is not used.
- No separate compact artifact or compact mode exists.
- No `Saved to:` appears.

---

## Eval 20 — Deep / Detailed Words Are Not Market Modes

Inputs:

```md
!market HOOD deep
!market HOOD detailed
!market HOOD deep-dive
!market HOOD deepdive
!market DEEP
```

Expected:

- `deep`, `detailed`, `deep-dive`, and `deepdive` do not create a Deep market mode.
- The command either returns the Standard Market Snapshot for the resolved ticker or gives a concise unsupported/non-mode boundary, depending current parser contract.
- `!market DEEP` treats `DEEP` as possible ticker/company input, not as a mode request.
- No `Deep Market Snapshot` or downstream research packet appears.
- No `!research`, `!financials`, `!thesis`, `!risk`, `!full`, or `!gems` command is auto-run.
- No artifacts are written.

---

## Eval 21 — Standard Metric Discipline

Input:

```md
!market AAPL
```

Fixture:

- Selected provider returns some or all Standard fields: price, market cap, change amount and percent, volume, average volume, 52-week range, 50D/200D averages, performance windows, beta, exchange, actively trading, IPO date, sector, industry, and country.

Expected:

- Currency fields use currency formatting.
- Percent fields use percent formatting.
- Volume fields use volume/integer formatting.
- `Relative Volume` appears only when both volume and average volume are available, or displays `Not available` without fabrication.
- `Price vs 50D Avg` and `Price vs 200D Avg` are labeled calculated/derived context when helper-derived.
- `5D`, `1M`, `3M`, `6M`, `YTD`, and `1Y` performance windows are shown as market-data context when available.
- Metric names, provider/source, and as-of date/time remain visible.
- No false precision or stale-as-current wording.

---

## Eval 22 — Selected-Provider Supplements Do Not Create Provider Fallback

Input:

```md
!market AAPL
```

Fixture:

- FMP `quote` returns usable `price` and selects FMP.
- FMP `profile` and/or `stock-price-change` omit fields or fail with a sanitized non-fatal error.

Expected:

- FMP remains the selected provider.
- Finnhub and Alpha Vantage are not called solely because a selected-provider supplement failed or omitted fields.
- `fallbacks_used` remains empty in helper output.
- Missing supplement fields show `Not available`, are omitted cleanly when allowed, or are summarized as non-material provider limitations.
- Standard output remains Standard; no Compact/Full branch appears.

---

## Eval 23 — Clean Success vs Real Limitation Rendering

Fixture A — clean success:

- Selected provider returns usable price, currency, market cap, and no material provider/data-quality issue.
- Helper metadata may contain generic internal notes/caveats.

Expected A:

- Standard output includes title, `As of:`, `Source:`, Profile, Price Action, Liquidity, and Trend.
- No generic `Limitation:` line.
- No routine disclaimer/footer.

Fixture B — real limitation:

- Selected provider output is materially partial, stale, conflicting, unavailable in a key field, rate-limited, fallback-driven, or missing material fields.

Expected B:

- A concise visible `Limitation:` line appears.
- Limitation explains the material issue.
- Output remains usable if enough price data exists.
- Missing values are not fabricated.

---

## Eval 24 — Raw/Debug Is Not A User-Facing Data Source For Other Commands

Input:

```md
!market HOOD raw json
```

Expected:

- Raw/debug output is diagnostic only.
- Other commands should call the canonical helper/provider path directly rather than parse user-facing `!market` text.
- Raw/debug creates no artifacts and does not mutate workspace, indexes, or watchlists.

---

## Known Deferred Cleanup

- `docs/COMMAND_REGISTRY.md` may still contain stale compact/default or explicit full-mode wording until the registry-cleanup stage.
- `skills/stock-analysis/market/references/*` may still contain historical compact/full/expanded wording until the references-cleanup stage.
- `rules/MARKET_DATA.md` may still use stale shared wording such as compact market snapshot until a shared-rule cleanup stage.
- Schemas, fixtures, proof packets, source manifests, evidence ledgers, and golden outputs remain deferred and should not be created for this eval alignment.

## Manual Eval Run Log

Historical entries below are preserved as prior run history only. They do not imply that Market Stage 3 ran live provider validation.

- 2026-06-12 — Stage 1 metadata / registry cleanup: PASS.
- 2026-06-12 — Stage 2 fixture/mock eval: 18 / 18 PASS; no live provider calls, artifacts, or watchlist mutation.
- 2026-06-12 — Stage 3 live `!market KEEL` smoke test: PASS; usable Finnhub fallback after FMP `402`, no secrets, no artifacts, no watchlist mutation.
- 2026-06-12 — Stage 4 readiness audit: PASS; approved for status-only activation.
- 2026-06-12 — Stage 1 parser fix for FMP `changePercentage`: PASS; AST parse OK, mocked `changePercentage`/`changesPercentage` OK, live HOOD helper returned non-null percent change from FMP.
- 2026-06-12 — Stage 3 FMP selected-provider supplements: PASS; AST parse OK, mocked supplement success/non-fatal failure OK, live HOOD helper returned FMP quote/profile/stock-price-change endpoints with supplement fields and no fallback.
- 2026-06-12 — Stage 4 full/expanded rendering: PASS; AST parse OK, mock render OK, live HOOD compact render ended at `Source: Financial Modeling Prep`, live HOOD full render included `Trend` and `Profile` sections with no secret markers.
- 2026-06-12 — Stage 5 Finnhub selected-provider supplements: PASS; AST parse OK, mocked Finnhub metric success/non-fatal failure OK, live HOOD compact/full FMP path unchanged, live KEEL Finnhub compact ended at `Source: Finnhub`, live KEEL full rendered 52-week/Finnhub supplement fields, `git diff --check` OK, diff secret-marker scan OK.
- 2026-06-12 — Stage 6 validation/smoke hardening: PASS; `market_stage6_validation.py` 6/6 mock cases PASS, helper/harness compile OK, default HOOD JSON parsed, live HOOD compact/full FMP path PASS, live KEEL compact/full Finnhub fallback PASS, compact final lines preserved, rendered output secret scan clean, workspace/watchlist status unchanged from pre-existing baseline, `git diff --check` OK.
- 2026-06-12 — Stage 7 post-implementation cleanup: PASS; stale active Stage 5 handoff wording removed/marked historical, completion reference added, implementation plan marked complete through Stage 7, Stage 5 verifier path fixed and PASS, Stage 6 harness still PASS, compile/diff/stale-scan checks PASS, watchlist SHA unchanged, no helper/provider/rendering behavior changes.
- 2026-06-12 — Source-placement/full-footer layout patch: PASS; compact/full success render `Source: [provider]` directly below `As of:`, full success omits routine source/fallback/limitations footer labels; compile, Stage 6 harness, Finnhub verifier, live IREN compact/full smoke, stale active-contract scan, diff secret-pattern scan, `git diff --check`, and no watchlist/artifact changes.
- 2026-06-12 — Full-mode section layout patch: PASS; profile moved directly below source/as-of header and `## Trend / Liquidity` renamed to `## Trend`; provider/data behavior unchanged; compile, Stage 6 harness, Finnhub verifier, live HOOD full smoke, `git diff --check`, and no watchlist/artifact changes.
