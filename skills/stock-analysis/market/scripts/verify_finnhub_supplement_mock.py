#!/usr/bin/env python3
"""Mock verifier for `!market` Finnhub selected-provider supplements.

Run from the Midas profile root:

    python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py

This script performs no network calls. It monkeypatches the canonical helper so that:
- FMP fails/no usable price.
- Finnhub quote succeeds and selects Finnhub.
- Finnhub stock/profile2 and stock/metric supplement behavior is tested.
- Alpha Vantage raises if accidentally called.

It verifies the durable Stage 5 contract: Finnhub stock/metric is selected-provider-only,
non-fatal on failure, and compact render remains lean.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

PROFILE_ROOT = Path(__file__).resolve().parents[4]
HELPER_PATH = PROFILE_ROOT / "tools" / "market_data_snapshot.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("market_data_snapshot", HELPER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load helper from {HELPER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def install_common_mocks(module):
    def fake_fmp(symbol: str):
        raise RuntimeError("FMP forced failure apiKey=SHOULD_REDACT")

    def fake_alpha(symbol: str):
        raise AssertionError("Alpha Vantage should not be called after Finnhub quote succeeds")

    module.get_fmp_snapshot = fake_fmp
    module.get_alpha_snapshot = fake_alpha


def verify_metric_success():
    module = load_helper()
    install_common_mocks(module)

    def fake_finnhub_json(path: str, params: dict):
        if path == "quote":
            return {"c": 100.0, "pc": 95.0, "o": 96.0, "h": 101.0, "l": 94.0}
        if path == "stock/profile2":
            return {
                "name": "Test Corp",
                "exchange": "NASDAQ",
                "currency": "USD",
                "marketCapitalization": 1234.5,
                "shareOutstanding": 12.3,
                "finnhubIndustry": "Software",
                "country": "US",
                "ipo": "2020-01-02",
            }
        if path == "stock/metric":
            return {
                "metric": {
                    "52WeekHigh": 120,
                    "52WeekLow": 80,
                    "10DayAverageTradingVolume": 1234567,
                    "beta": 1.23,
                    "13WeekPriceReturnDaily": 10.5,
                    "26WeekPriceReturnDaily": 20.5,
                    "52WeekPriceReturnDaily": 30.5,
                    "yearToDatePriceReturnDaily": 15.5,
                    "50DayMovingAverage": 98,
                    "200DayMovingAverage": 90,
                }
            }
        raise AssertionError(f"Unexpected Finnhub endpoint: {path}")

    module.fetch_finnhub_json = fake_finnhub_json
    payload = module.get_market_context("TEST")
    assert payload["ok"] is True, payload
    assert payload["provider"] == "Finnhub", payload
    assert payload["fallbacks_used"] == ["Finnhub"], payload
    assert "Finnhub: stock/metric" in payload["provider_endpoints"]["Finnhub"], payload["provider_endpoints"]
    assert payload["week_52_high"] == 120
    assert payload["average_volume"] == 1234567
    assert payload["beta"] == 1.23

    full = module.render_market_snapshot(payload, "full")
    compact = module.render_market_snapshot(payload, "compact")
    assert "## Trend" in full and "## Profile" in full, full
    assert "## Quote" not in full and "## Market Size" not in full and "Shares Outstanding:" not in full, full
    assert full.index("## Profile") < full.index("## Price Action") < full.index("Market Cap:") < full.index("Price:") < full.index("## Liquidity") < full.index("## Trend"), full
    assert "52-Week High / Low: $120.00 / $80.00" in full, full
    assert "Average Volume: 1,234,567" in full, full
    assert "Beta: 1.23" in full, full
    assert "Fallbacks Used:" not in full, full
    assert "## Source / Limitations" not in full, full
    assert "## Trend" not in compact and "## Profile" not in compact, compact
    compact_lines = compact.splitlines()
    assert compact_lines[1].startswith("As of: "), compact
    assert compact_lines[2] == "Source: Finnhub", compact
    assert compact_lines[3] == "", compact
    assert "SHOULD_REDACT" not in full and "SHOULD_REDACT" not in compact


def verify_metric_failure_nonfatal():
    module = load_helper()
    install_common_mocks(module)

    def fake_finnhub_json(path: str, params: dict):
        if path == "quote":
            return {"c": 100.0, "pc": 95.0}
        if path == "stock/profile2":
            return {"name": "Test Corp", "currency": "USD"}
        if path == "stock/metric":
            raise RuntimeError("metric failed token=SECRET")
        raise AssertionError(f"Unexpected Finnhub endpoint: {path}")

    module.fetch_finnhub_json = fake_finnhub_json
    payload = module.get_market_context("TEST")
    assert payload["ok"] is True, payload
    assert payload["provider"] == "Finnhub", payload
    assert payload["fallbacks_used"] == ["Finnhub"], payload
    assert payload["week_52_high"] is None

    full = module.render_market_snapshot(payload, "full")
    compact = module.render_market_snapshot(payload, "compact")
    compact_lines = compact.splitlines()
    assert compact_lines[1].startswith("As of: "), compact
    assert compact_lines[2] == "Source: Finnhub", compact
    assert compact_lines[3] == "", compact
    assert "SECRET" not in json.dumps(payload) and "SECRET" not in full
    assert "metric fields unavailable" in json.dumps(payload).lower(), payload


def main() -> int:
    verify_metric_success()
    verify_metric_failure_nonfatal()
    print("PASS: Finnhub selected-provider supplement mock contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
