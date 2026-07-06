#!/usr/bin/env python3
"""Stage 6 mock validation harness for MIDAS !market helper.

This harness is intentionally offline: it monkeypatches provider functions in
``tools/market_data_snapshot.py`` and verifies provider policy, rendering
contracts, graceful supplement failure, failure behavior, and secret sanitizing.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HELPER_PATH = ROOT / "tools" / "market_data_snapshot.py"

FORBIDDEN_OUTPUT_TERMS = [
    "Buy",
    "Sell",
    "Hold",
    "price target",
    "sizing",
    "entry",
    "exit",
    "trade advice",
    "Global Research Score",
    "setup classification",
]


def load_helper() -> Any:
    spec = importlib.util.spec_from_file_location("market_data_snapshot_stage6", HELPER_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Unable to load helper from {HELPER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_no_forbidden_language(text: str) -> None:
    lowered = text.lower()
    for term in FORBIDDEN_OUTPUT_TERMS:
        assert term.lower() not in lowered, f"forbidden term in output: {term!r}\n{text}"


def assert_no_secrets(text: str) -> None:
    forbidden = ["SHOULD_REDACT", "SECRET_TOKEN", "SECRET_KEY", "Bearer abc123"]
    for token in forbidden:
        assert token not in text, f"secret leaked: {token}"


def assert_compact_contract(module: Any, payload: dict, provider: str) -> str:
    compact = module.render_market_snapshot(payload, "compact")
    lines = compact.splitlines()
    assert len(lines) >= 4, compact
    assert lines[1].startswith("As of: "), compact
    assert lines[2] == f"Source: {provider}", compact
    assert lines[3] == "", compact
    assert "## Trend" not in compact, compact
    assert "## Profile" not in compact, compact
    assert "Provider endpoints" not in compact, compact
    assert_no_forbidden_language(compact)
    assert_no_secrets(compact)
    return compact


def assert_full_contract(module: Any, payload: dict) -> str:
    full = module.render_market_snapshot(payload, "full")
    lines = full.splitlines()
    assert len(lines) >= 4, full
    assert lines[1].startswith("As of: "), full
    assert lines[2] == f"Source: {payload['provider']}", full
    assert lines[3] == "", full
    assert "## Profile" in full and "## Price Action" in full and "## Trend" in full, full
    assert "## Quote" not in full and "## Market Size" not in full and "Shares Outstanding:" not in full, full
    assert full.index("## Profile") < full.index("## Price Action") < full.index("Market Cap:") < full.index("Price:") < full.index("## Liquidity") < full.index("## Trend"), full
    assert "## Source / Limitations" not in full, full
    assert "Fallbacks Used:" not in full, full
    assert "Limitations:" not in full, full
    assert_no_forbidden_language(full)
    assert_no_secrets(full)
    return full


def assert_json_default_safe(payload: dict) -> None:
    # Structured JSON may carry guardrail limitation text such as
    # "Do not create Buy/Sell/Hold calls". That is allowed; this check is about
    # secret hygiene for raw/debug-safe payloads.
    serialized = json.dumps(payload, sort_keys=True)
    assert_no_secrets(serialized)


def case_fmp_success() -> None:
    module = load_helper()
    calls: list[str] = []

    def fake_fmp_json(endpoint: str, symbol: str):
        calls.append(f"FMP:{endpoint}")
        if endpoint == "quote":
            return [{
                "name": "Mock FMP Co",
                "exchange": "NASDAQ",
                "currency": "USD",
                "price": 100,
                "marketCap": 1_000_000_000,
                "volume": 2_000_000,
                "avgVolume": 1_000_000,
                "change": 2,
                "changePercentage": 2.04,
                "previousClose": 98,
                "open": 99,
                "dayHigh": 101,
                "dayLow": 97,
                "yearHigh": 120,
                "yearLow": 80,
                "sharesOutstanding": 10_000_000,
                "priceAvg50": 95,
                "priceAvg200": 90,
            }]
        if endpoint == "profile":
            return [{
                "companyName": "Mock FMP Co",
                "beta": 1.1,
                "sector": "Technology",
                "industry": "Software",
                "country": "US",
                "ipoDate": "2020-01-02",
                "isActivelyTrading": True,
                "isEtf": False,
                "isAdr": False,
                "isFund": False,
            }]
        if endpoint == "stock-price-change":
            return [{"5D": 1, "1M": 2, "3M": 3, "6M": 4, "ytd": 5, "1Y": 6}]
        raise AssertionError(endpoint)

    def fail_finnhub(*args, **kwargs):  # pragma: no cover - should never run
        raise AssertionError("Finnhub should not be called when FMP quote is usable")

    module.fetch_fmp_json = fake_fmp_json
    module.fetch_finnhub_json = fail_finnhub
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is True
    assert payload["provider"] == "Financial Modeling Prep"
    assert payload["fallbacks_used"] == []
    assert "FMP:quote" in calls
    assert "FMP:profile" in calls
    assert "FMP:stock-price-change" in calls
    assert_compact_contract(module, payload, "Financial Modeling Prep")
    full = assert_full_contract(module, payload)
    assert "Relative Volume: 2.00" in full, full
    assert "Beta: 1.10" in full, full
    assert_json_default_safe(payload)


def case_fmp_supplement_failure() -> None:
    module = load_helper()

    def fake_fmp_json(endpoint: str, symbol: str):
        if endpoint == "quote":
            return [{"name": "Mock FMP Co", "price": 100, "currency": "USD"}]
        if endpoint in {"profile", "stock-price-change"}:
            raise RuntimeError("supplement failed token=SECRET_TOKEN")
        raise AssertionError(endpoint)

    def fail_finnhub(*args, **kwargs):
        raise AssertionError("Finnhub should not be called for FMP supplement failure")

    module.fetch_fmp_json = fake_fmp_json
    module.fetch_finnhub_json = fail_finnhub
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is True
    assert payload["provider"] == "Financial Modeling Prep"
    assert payload["fallbacks_used"] == []
    assert payload["beta"] is None
    compact = assert_compact_contract(module, payload, "Financial Modeling Prep")
    full = assert_full_contract(module, payload)
    assert "SECRET_TOKEN" not in json.dumps(payload)
    assert "SECRET_TOKEN" not in compact + full
    assert "[REDACTED]" in json.dumps(payload)


def case_finnhub_metric_success() -> None:
    module = load_helper()
    calls: list[str] = []

    def fake_fmp(symbol: str):
        calls.append("FMP:snapshot")
        raise RuntimeError("FMP failed apikey=SHOULD_REDACT")

    def fake_finnhub_json(path: str, params: dict):
        calls.append(f"Finnhub:{path}")
        if path == "quote":
            return {"c": 50, "pc": 40, "o": 42, "h": 51, "l": 39}
        if path == "stock/profile2":
            return {
                "name": "Mock Finnhub Co",
                "exchange": "NYSE",
                "currency": "USD",
                "marketCapitalization": 500,
                "shareOutstanding": 25,
                "finnhubIndustry": "Industrials",
                "country": "US",
                "ipo": "2019-05-01",
            }
        if path == "stock/metric":
            return {"metric": {
                "52WeekHigh": 60,
                "52WeekLow": 20,
                "10DayAverageTradingVolume": 123456,
                "beta": 1.25,
                "50DayMovingAverage": 45,
                "200DayMovingAverage": 35,
                "5DayPriceReturnDaily": 7,
                "13WeekPriceReturnDaily": 8,
                "26WeekPriceReturnDaily": 9,
                "yearToDatePriceReturnDaily": 10,
                "52WeekPriceReturnDaily": 11,
            }}
        raise AssertionError(path)

    def fail_alpha(symbol: str):
        raise AssertionError("Alpha should not be called after Finnhub usable quote")

    module.get_fmp_snapshot = fake_fmp
    module.fetch_finnhub_json = fake_finnhub_json
    module.get_alpha_snapshot = fail_alpha
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is True
    assert payload["provider"] == "Finnhub"
    assert payload["fallbacks_used"] == ["Finnhub"]
    assert "Finnhub:stock/metric" in calls
    compact = assert_compact_contract(module, payload, "Finnhub")
    full = assert_full_contract(module, payload)
    assert "52-Week High / Low: $60.00 / $20.00" in full, full
    assert "Average Volume: 123,456" in full, full
    assert "Beta: 1.25" in full, full
    assert "[REDACTED]" in json.dumps(payload), payload
    assert_json_default_safe(payload)
    assert_no_secrets(compact + full)


def case_finnhub_metric_failure() -> None:
    module = load_helper()

    def fake_fmp(symbol: str):
        raise RuntimeError("FMP failed")

    def fake_finnhub_json(path: str, params: dict):
        if path == "quote":
            return {"c": 50, "pc": 40}
        if path == "stock/profile2":
            return {"name": "Mock Finnhub Co", "currency": "USD"}
        if path == "stock/metric":
            raise RuntimeError("metric failed token=SECRET_TOKEN")
        raise AssertionError(path)

    def fail_alpha(symbol: str):
        raise AssertionError("Alpha should not be called for Finnhub metric failure")

    module.get_fmp_snapshot = fake_fmp
    module.fetch_finnhub_json = fake_finnhub_json
    module.get_alpha_snapshot = fail_alpha
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is True
    assert payload["provider"] == "Finnhub"
    assert payload["fallbacks_used"] == ["Finnhub"]
    assert payload["week_52_high"] is None
    assert "metric fields unavailable" in json.dumps(payload).lower()
    assert_compact_contract(module, payload, "Finnhub")
    assert_full_contract(module, payload)
    assert "SECRET_TOKEN" not in json.dumps(payload)


def case_alpha_success() -> None:
    module = load_helper()
    calls: list[str] = []

    def fake_fmp(symbol: str):
        calls.append("FMP")
        raise RuntimeError("FMP failed")

    def fake_finnhub(symbol: str):
        calls.append("Finnhub")
        raise RuntimeError("Finnhub failed")

    def fake_alpha(symbol: str):
        calls.append("Alpha")
        return {
            "provider": "Alpha Vantage",
            "provider_endpoints": ["Alpha Vantage: GLOBAL_QUOTE"],
            "company_name": None,
            "exchange": None,
            "currency": "USD",
            "price": 25,
            "market_cap": None,
            "market_cap_source": None,
            "volume": 1000,
            "change": 1,
            "change_percentage": 4,
            "previous_close": 24,
            "open": 24.5,
            "day_high": 26,
            "day_low": 24,
            "week_52_high": None,
            "week_52_low": None,
            "shares_outstanding": None,
            "average_volume": None,
            "relative_volume": None,
            "source_fields": {"price": "Alpha Vantage GLOBAL_QUOTE.05 price"},
        }

    module.get_fmp_snapshot = fake_fmp
    module.get_finnhub_snapshot = fake_finnhub
    module.get_alpha_snapshot = fake_alpha
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is True
    assert payload["provider"] == "Alpha Vantage"
    assert payload["fallbacks_used"] == ["Finnhub", "Alpha Vantage"]
    assert calls == ["FMP", "Finnhub", "Alpha"]
    assert_compact_contract(module, payload, "Alpha Vantage")
    assert_full_contract(module, payload)
    assert_json_default_safe(payload)


def case_all_providers_fail() -> None:
    module = load_helper()

    def fail_provider(name: str):
        def inner(symbol: str):
            raise RuntimeError("provider failed apiKey=SHOULD_REDACT")
        return inner

    module.get_fmp_snapshot = fail_provider("FMP")
    module.get_finnhub_snapshot = fail_provider("Finnhub")
    module.get_alpha_snapshot = fail_provider("Alpha")
    payload = module.get_market_context("MOCK")
    assert payload["ok"] is False
    rendered = module.render_market_snapshot(payload, "compact")
    assert "Market Data Unavailable" in rendered
    assert "[REDACTED]" in json.dumps(payload) + rendered
    assert_no_secrets(json.dumps(payload) + rendered)
    assert_no_forbidden_language(rendered)


def main() -> int:
    cases = [
        case_fmp_success,
        case_fmp_supplement_failure,
        case_finnhub_metric_success,
        case_finnhub_metric_failure,
        case_alpha_success,
        case_all_providers_fail,
    ]
    for case in cases:
        case()
        print(f"PASS {case.__name__}")
    print(f"PASS {len(cases)} Stage 6 mock validation cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
