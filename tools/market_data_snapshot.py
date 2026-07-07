#!/usr/bin/env python3
"""Read-only Midas live market-data snapshot helper.

v1 provider policy:
1. Call FMP first.
2. If FMP returns a usable price, stop.
3. If FMP fails or returns no usable price, call Finnhub.
4. If Finnhub returns a usable price, stop.
5. If Finnhub fails or returns no usable price, call Alpha Vantage.
6. If Alpha Vantage returns a usable price, return a partial snapshot.
7. If no provider returns a usable price, return ok:false.

Fallback is provider-level only. Do not call fallback providers solely to fill
market cap, currency, volume, high/low, prior close, 52-week range, or other
non-price fields.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


FMP_API_KEY = os.getenv("FMP_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")

FMP_BASE_URL = "https://financialmodelingprep.com/stable"
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"
ALPHA_BASE_URL = "https://www.alphavantage.co/query"

DISPLAY_FIELDS = [
    "price",
    "market_cap",
    "currency",
    "change",
    "change_percentage",
    "volume",
    "exchange",
    "previous_close",
    "open",
    "day_high",
    "day_low",
    "week_52_high",
    "week_52_low",
    "shares_outstanding",
    "average_volume",
    "relative_volume",
    "beta",
    "sector",
    "industry",
    "country",
    "ipo_date",
    "issuer_flags",
    "price_avg_50",
    "price_avg_200",
    "price_vs_50d_avg_percentage",
    "price_vs_200d_avg_percentage",
    "performance_5d_percentage",
    "performance_1m_percentage",
    "performance_3m_percentage",
    "performance_6m_percentage",
    "performance_ytd_percentage",
    "performance_1y_percentage",
]

SECRET_KEY_RE = re.compile(
    r"(?i)(api[_-]?key|apikey|token|key|secret|authorization)(\s*[=:]\s*|%3[dD])([^\s,&]+)"
)
AUTH_HEADER_RE = re.compile(r"(?i)(authorization\s*:\s*)(bearer\s+)?[^\s,;]+")
URL_QUERY_RE = re.compile(r"https?://[^\s]+")


def now_et() -> str:
    return datetime.now(ZoneInfo("America/New_York")).isoformat()


def first_item(data):
    if isinstance(data, list) and data:
        item = data[0]
        return item if isinstance(item, dict) else {}
    if isinstance(data, dict):
        return data
    return {}


def safe_float(value):
    if value in (None, "", "None", "null"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def safe_int(value):
    if value in (None, "", "None", "null"):
        return None
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def first_float(mapping: dict, *keys: str):
    for key in keys:
        value = safe_float(mapping.get(key))
        if value is not None:
            return value
    return None


def first_int(mapping: dict, *keys: str):
    for key in keys:
        value = safe_int(mapping.get(key))
        if value is not None:
            return value
    return None


def relative_volume(volume, average_volume):
    volume_value = safe_float(volume)
    average_value = safe_float(average_volume)
    if volume_value is None or average_value in (None, 0):
        return None
    return volume_value / average_value


def percentage_vs_value(price, baseline):
    price_value = safe_float(price)
    baseline_value = safe_float(baseline)
    if price_value is None or baseline_value in (None, 0):
        return None
    return ((price_value - baseline_value) / baseline_value) * 100


def safe_bool(value):
    if value in (None, "", "None", "null"):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    text = str(value).strip().lower()
    if text in {"true", "yes", "1", "y"}:
        return True
    if text in {"false", "no", "0", "n"}:
        return False
    return None


def has_usable_price(context: dict | None) -> bool:
    if not context:
        return False
    price = safe_float(context.get("price"))
    return price is not None and price > 0


def strip_query_params(text: str) -> str:
    def replace_url(match):
        return match.group(0).split("?", 1)[0]

    return URL_QUERY_RE.sub(replace_url, text)


def sanitize_error(message: object) -> str:
    text = strip_query_params(str(message))
    text = SECRET_KEY_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}[REDACTED]", text)
    text = AUTH_HEADER_RE.sub(lambda m: f"{m.group(1)}[REDACTED]", text)
    return text


def clean_provider_error(provider: str, error: object) -> dict:
    return {"provider": provider, "error": sanitize_error(error)}


def source_fields(**kwargs) -> dict:
    return {field: source for field, source in kwargs.items() if source}


def fetch_fmp_json(endpoint: str, symbol: str):
    if not FMP_API_KEY:
        raise RuntimeError("Missing FMP_API_KEY environment variable")

    response = requests.get(
        f"{FMP_BASE_URL}/{endpoint.strip('/')}",
        params={"symbol": symbol, "apikey": FMP_API_KEY},
        timeout=15,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"FMP request failed: endpoint={endpoint}, status={response.status_code}")
    return response.json()


def get_fmp_profile_supplement(symbol: str) -> dict:
    return first_item(fetch_fmp_json("profile", symbol))


def get_fmp_price_change_supplement(symbol: str) -> dict:
    return first_item(fetch_fmp_json("stock-price-change", symbol))


def issuer_flags_from_fmp_profile(profile: dict) -> dict | None:
    flags = {
        "is_etf": safe_bool(profile.get("isEtf")),
        "is_adr": safe_bool(profile.get("isAdr")),
        "is_fund": safe_bool(profile.get("isFund")),
        "is_actively_trading": safe_bool(profile.get("isActivelyTrading")),
    }
    return flags if any(value is not None for value in flags.values()) else None


def get_fmp_snapshot(symbol: str) -> dict:
    quote = first_item(fetch_fmp_json("quote", symbol))
    if not quote:
        raise RuntimeError(f"No FMP quote data returned for {symbol}")

    price = safe_float(quote.get("price"))
    if price is None:
        raise RuntimeError(f"FMP returned no usable price for {symbol}")

    # Stage 3 selected-provider supplements: only after FMP quote has supplied
    # usable price. These failures must not trigger provider fallback.
    profile = {}
    price_change = {}
    supplement_limitations = []
    provider_endpoints = ["FMP: quote"]

    try:
        profile = get_fmp_profile_supplement(symbol)
        if profile:
            provider_endpoints.append("FMP: profile")
    except Exception as exc:
        supplement_limitations.append(f"FMP profile fields unavailable: {sanitize_error(exc)}")

    try:
        price_change = get_fmp_price_change_supplement(symbol)
        if price_change:
            provider_endpoints.append("FMP: stock-price-change")
    except Exception as exc:
        supplement_limitations.append(f"FMP price-performance fields unavailable: {sanitize_error(exc)}")

    market_cap = safe_int(quote.get("marketCap"))
    market_cap_source = "FMP quote.marketCap" if market_cap is not None else None
    volume = first_int(quote, "volume")
    average_volume = first_int(quote, "avgVolume", "averageVolume", "volAvg", "volumeAvg")
    average_volume_source = "FMP quote.avgVolume/averageVolume" if average_volume is not None else None
    profile_average_volume = first_int(profile, "averageVolume", "volAvg", "volumeAvg")
    if average_volume is None and profile_average_volume is not None:
        average_volume = profile_average_volume
        average_volume_source = "FMP profile.averageVolume"

    change_percentage = first_float(quote, "changePercentage", "changesPercentage")
    change_percentage_source = None
    if quote.get("changePercentage") is not None:
        change_percentage_source = "FMP quote.changePercentage"
    elif quote.get("changesPercentage") is not None:
        change_percentage_source = "FMP quote.changesPercentage"

    price_avg_50 = first_float(quote, "priceAvg50")
    price_avg_200 = first_float(quote, "priceAvg200")
    issuer_flags = issuer_flags_from_fmp_profile(profile)

    return {
        "provider": "Financial Modeling Prep",
        "provider_endpoints": provider_endpoints,
        "company_name": quote.get("name") or profile.get("companyName"),
        "exchange": quote.get("exchange") or profile.get("exchange") or profile.get("exchangeShortName"),
        "currency": quote.get("currency") or profile.get("currency") or "USD",
        "price": price,
        "market_cap": market_cap,
        "market_cap_source": market_cap_source,
        "volume": volume,
        "change": safe_float(quote.get("change")),
        "change_percentage": change_percentage,
        "previous_close": first_float(quote, "previousClose", "previous_close"),
        "open": first_float(quote, "open"),
        "day_high": first_float(quote, "dayHigh", "high"),
        "day_low": first_float(quote, "dayLow", "low"),
        "week_52_high": first_float(quote, "yearHigh", "week52High", "52WeekHigh"),
        "week_52_low": first_float(quote, "yearLow", "week52Low", "52WeekLow"),
        "shares_outstanding": first_int(quote, "sharesOutstanding", "shares_outstanding"),
        "average_volume": average_volume,
        "relative_volume": relative_volume(volume, average_volume),
        "beta": first_float(profile, "beta"),
        "sector": profile.get("sector"),
        "industry": profile.get("industry"),
        "country": profile.get("country"),
        "ipo_date": profile.get("ipoDate"),
        "issuer_flags": issuer_flags,
        "price_avg_50": price_avg_50,
        "price_avg_200": price_avg_200,
        "price_vs_50d_avg_percentage": percentage_vs_value(price, price_avg_50),
        "price_vs_200d_avg_percentage": percentage_vs_value(price, price_avg_200),
        "performance_5d_percentage": first_float(price_change, "5D"),
        "performance_1m_percentage": first_float(price_change, "1M"),
        "performance_3m_percentage": first_float(price_change, "3M"),
        "performance_6m_percentage": first_float(price_change, "6M"),
        "performance_ytd_percentage": first_float(price_change, "ytd", "YTD"),
        "performance_1y_percentage": first_float(price_change, "1Y"),
        "source_fields": source_fields(
            company_name="FMP quote.name/profile.companyName" if (quote.get("name") or profile.get("companyName")) else None,
            exchange="FMP quote.exchange/profile.exchange" if (quote.get("exchange") or profile.get("exchange") or profile.get("exchangeShortName")) else None,
            currency="FMP quote.currency/profile.currency/default_USD",
            price="FMP quote.price",
            market_cap=market_cap_source,
            volume="FMP quote.volume" if volume is not None else None,
            change="FMP quote.change" if quote.get("change") is not None else None,
            change_percentage=change_percentage_source,
            previous_close="FMP quote.previousClose" if first_float(quote, "previousClose", "previous_close") is not None else None,
            open="FMP quote.open" if first_float(quote, "open") is not None else None,
            day_high="FMP quote.dayHigh/high" if first_float(quote, "dayHigh", "high") is not None else None,
            day_low="FMP quote.dayLow/low" if first_float(quote, "dayLow", "low") is not None else None,
            week_52_high="FMP quote.yearHigh/week52High" if first_float(quote, "yearHigh", "week52High", "52WeekHigh") is not None else None,
            week_52_low="FMP quote.yearLow/week52Low" if first_float(quote, "yearLow", "week52Low", "52WeekLow") is not None else None,
            shares_outstanding="FMP quote.sharesOutstanding" if first_int(quote, "sharesOutstanding", "shares_outstanding") is not None else None,
            average_volume=average_volume_source,
            relative_volume="Midas derived: volume / average_volume" if relative_volume(volume, average_volume) is not None else None,
            beta="FMP profile.beta" if first_float(profile, "beta") is not None else None,
            sector="FMP profile.sector" if profile.get("sector") else None,
            industry="FMP profile.industry" if profile.get("industry") else None,
            country="FMP profile.country" if profile.get("country") else None,
            ipo_date="FMP profile.ipoDate" if profile.get("ipoDate") else None,
            issuer_flags="FMP profile.isEtf/isAdr/isFund/isActivelyTrading" if issuer_flags is not None else None,
            price_avg_50="FMP quote.priceAvg50" if price_avg_50 is not None else None,
            price_avg_200="FMP quote.priceAvg200" if price_avg_200 is not None else None,
            price_vs_50d_avg_percentage="Midas derived: (price - price_avg_50) / price_avg_50" if percentage_vs_value(price, price_avg_50) is not None else None,
            price_vs_200d_avg_percentage="Midas derived: (price - price_avg_200) / price_avg_200" if percentage_vs_value(price, price_avg_200) is not None else None,
            performance_5d_percentage="FMP stock-price-change.5D" if first_float(price_change, "5D") is not None else None,
            performance_1m_percentage="FMP stock-price-change.1M" if first_float(price_change, "1M") is not None else None,
            performance_3m_percentage="FMP stock-price-change.3M" if first_float(price_change, "3M") is not None else None,
            performance_6m_percentage="FMP stock-price-change.6M" if first_float(price_change, "6M") is not None else None,
            performance_ytd_percentage="FMP stock-price-change.ytd" if first_float(price_change, "ytd", "YTD") is not None else None,
            performance_1y_percentage="FMP stock-price-change.1Y" if first_float(price_change, "1Y") is not None else None,
        ),
        "provider_limitations": supplement_limitations,
    }


def fetch_finnhub_json(path: str, params: dict):
    if not FINNHUB_API_KEY:
        raise RuntimeError("Missing FINNHUB_API_KEY environment variable")

    request_params = dict(params)
    request_params["token"] = FINNHUB_API_KEY
    response = requests.get(
        f"{FINNHUB_BASE_URL}/{path.strip('/')}",
        params=request_params,
        timeout=15,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"Finnhub request failed: endpoint={path}, status={response.status_code}")

    data = response.json()
    if isinstance(data, dict) and data.get("error"):
        raise RuntimeError(f"Finnhub error: {data.get('error')}")
    return data


def get_finnhub_metric_supplement(symbol: str) -> dict:
    data = fetch_finnhub_json("stock/metric", {"symbol": symbol, "metric": "all"})
    if isinstance(data, dict) and isinstance(data.get("metric"), dict):
        return data.get("metric") or {}
    return data if isinstance(data, dict) else {}


def get_finnhub_snapshot(symbol: str) -> dict:
    quote = fetch_finnhub_json("quote", {"symbol": symbol})
    price = safe_float(quote.get("c"))
    if price is None:
        raise RuntimeError(f"Finnhub returned no usable price for {symbol}")

    # Only fetch supplements after Finnhub has established a usable price. These
    # calls do not decide provider fallback and must degrade gracefully.
    profile = {}
    metric = {}
    profile_error = None
    metric_error = None
    try:
        profile = fetch_finnhub_json("stock/profile2", {"symbol": symbol})
    except Exception as exc:
        profile_error = sanitize_error(exc)
    try:
        metric = get_finnhub_metric_supplement(symbol)
    except Exception as exc:
        metric_error = sanitize_error(exc)

    previous_close = safe_float(quote.get("pc"))
    change = None
    change_percentage = None
    if previous_close not in (None, 0):
        change = price - previous_close
        change_percentage = (change / previous_close) * 100

    market_cap_millions = safe_float(profile.get("marketCapitalization"))
    market_cap = safe_int(market_cap_millions * 1_000_000) if market_cap_millions is not None else None
    shares_outstanding_millions = safe_float(profile.get("shareOutstanding"))
    shares_outstanding = safe_int(shares_outstanding_millions * 1_000_000) if shares_outstanding_millions is not None else None
    average_volume = first_int(metric, "10DayAverageTradingVolume", "3MonthAverageTradingVolume")
    average_volume_source = None
    if metric.get("10DayAverageTradingVolume") is not None:
        average_volume_source = "Finnhub stock/metric.10DayAverageTradingVolume"
    elif metric.get("3MonthAverageTradingVolume") is not None:
        average_volume_source = "Finnhub stock/metric.3MonthAverageTradingVolume"
    price_avg_50 = first_float(metric, "50DayMovingAverage", "ma50", "priceAvg50")
    price_avg_200 = first_float(metric, "200DayMovingAverage", "ma200", "priceAvg200")
    week_52_high = first_float(metric, "52WeekHigh")
    week_52_low = first_float(metric, "52WeekLow")
    beta = first_float(metric, "beta")
    performance_5d = first_float(metric, "5DayPriceReturnDaily")
    performance_3m = first_float(metric, "13WeekPriceReturnDaily")
    performance_6m = first_float(metric, "26WeekPriceReturnDaily")
    performance_ytd = first_float(metric, "yearToDatePriceReturnDaily")
    performance_1y = first_float(metric, "52WeekPriceReturnDaily")

    limitations = []
    if profile_error:
        limitations.append(f"Finnhub profile fields unavailable: {profile_error}")
    if metric_error:
        limitations.append(f"Finnhub metric fields unavailable: {metric_error}")

    return {
        "provider": "Finnhub",
        "provider_endpoints": ["Finnhub: quote"] + (["Finnhub: stock/profile2"] if profile else []) + (["Finnhub: stock/metric"] if metric else []),
        "company_name": profile.get("name"),
        "exchange": profile.get("exchange"),
        "currency": profile.get("currency") or "USD",
        "price": price,
        "market_cap": market_cap,
        "market_cap_source": "Finnhub stock/profile2.marketCapitalization_millions" if market_cap is not None else None,
        "volume": None,
        "change": change,
        "change_percentage": change_percentage,
        "previous_close": previous_close,
        "open": safe_float(quote.get("o")),
        "day_high": safe_float(quote.get("h")),
        "day_low": safe_float(quote.get("l")),
        "week_52_high": week_52_high,
        "week_52_low": week_52_low,
        "shares_outstanding": shares_outstanding,
        "average_volume": average_volume,
        "relative_volume": None,
        "beta": beta,
        "sector": None,
        "industry": profile.get("finnhubIndustry"),
        "country": profile.get("country"),
        "ipo_date": profile.get("ipo"),
        "issuer_flags": None,
        "price_avg_50": price_avg_50,
        "price_avg_200": price_avg_200,
        "price_vs_50d_avg_percentage": percentage_vs_value(price, price_avg_50),
        "price_vs_200d_avg_percentage": percentage_vs_value(price, price_avg_200),
        "performance_5d_percentage": performance_5d,
        "performance_1m_percentage": None,
        "performance_3m_percentage": performance_3m,
        "performance_6m_percentage": performance_6m,
        "performance_ytd_percentage": performance_ytd,
        "performance_1y_percentage": performance_1y,
        "source_fields": source_fields(
            company_name="Finnhub stock/profile2.name" if profile.get("name") else None,
            exchange="Finnhub stock/profile2.exchange" if profile.get("exchange") else None,
            currency="Finnhub stock/profile2.currency/default_USD",
            price="Finnhub quote.c",
            market_cap="Finnhub stock/profile2.marketCapitalization_millions" if market_cap is not None else None,
            change="Finnhub derived: quote.c - quote.pc" if change is not None else None,
            change_percentage="Finnhub derived: (quote.c - quote.pc) / quote.pc" if change_percentage is not None else None,
            previous_close="Finnhub quote.pc" if previous_close is not None else None,
            open="Finnhub quote.o" if quote.get("o") is not None else None,
            day_high="Finnhub quote.h" if quote.get("h") is not None else None,
            day_low="Finnhub quote.l" if quote.get("l") is not None else None,
            week_52_high="Finnhub stock/metric.52WeekHigh" if week_52_high is not None else None,
            week_52_low="Finnhub stock/metric.52WeekLow" if week_52_low is not None else None,
            shares_outstanding="Finnhub stock/profile2.shareOutstanding_millions" if shares_outstanding is not None else None,
            average_volume=average_volume_source,
            beta="Finnhub stock/metric.beta" if beta is not None else None,
            industry="Finnhub stock/profile2.finnhubIndustry" if profile.get("finnhubIndustry") else None,
            country="Finnhub stock/profile2.country" if profile.get("country") else None,
            ipo_date="Finnhub stock/profile2.ipo" if profile.get("ipo") else None,
            price_avg_50="Finnhub stock/metric.50DayMovingAverage" if price_avg_50 is not None else None,
            price_avg_200="Finnhub stock/metric.200DayMovingAverage" if price_avg_200 is not None else None,
            price_vs_50d_avg_percentage="Midas derived: (price - price_avg_50) / price_avg_50" if percentage_vs_value(price, price_avg_50) is not None else None,
            price_vs_200d_avg_percentage="Midas derived: (price - price_avg_200) / price_avg_200" if percentage_vs_value(price, price_avg_200) is not None else None,
            performance_5d_percentage="Finnhub stock/metric.5DayPriceReturnDaily" if performance_5d is not None else None,
            performance_3m_percentage="Finnhub stock/metric.13WeekPriceReturnDaily" if performance_3m is not None else None,
            performance_6m_percentage="Finnhub stock/metric.26WeekPriceReturnDaily" if performance_6m is not None else None,
            performance_ytd_percentage="Finnhub stock/metric.yearToDatePriceReturnDaily" if performance_ytd is not None else None,
            performance_1y_percentage="Finnhub stock/metric.52WeekPriceReturnDaily" if performance_1y is not None else None,
        ),
        "provider_limitations": limitations,
    }


def fetch_alpha_global_quote(symbol: str):
    if not ALPHA_API_KEY:
        raise RuntimeError("Missing ALPHA_API_KEY environment variable")

    response = requests.get(
        ALPHA_BASE_URL,
        params={"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": ALPHA_API_KEY},
        timeout=15,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"Alpha Vantage request failed: endpoint=GLOBAL_QUOTE, status={response.status_code}")

    data = response.json()
    if "Note" in data:
        raise RuntimeError(f"Alpha Vantage rate limit or notice: {data['Note']}")
    if "Information" in data:
        raise RuntimeError(f"Alpha Vantage notice: {data['Information']}")
    if "Error Message" in data:
        raise RuntimeError(f"Alpha Vantage error: {data['Error Message']}")

    quote = data.get("Global Quote") or {}
    if not quote:
        raise RuntimeError(f"No Alpha Vantage quote data returned for {symbol}")
    return quote


def get_alpha_snapshot(symbol: str) -> dict:
    quote = fetch_alpha_global_quote(symbol)
    price = safe_float(quote.get("05. price"))
    if price is None:
        raise RuntimeError(f"Alpha Vantage returned no usable price for {symbol}")

    change_percentage_raw = quote.get("10. change percent")
    change_percentage = None
    if isinstance(change_percentage_raw, str):
        change_percentage = safe_float(change_percentage_raw.replace("%", ""))

    return {
        "provider": "Alpha Vantage",
        "provider_endpoints": ["Alpha Vantage: GLOBAL_QUOTE"],
        "company_name": None,
        "exchange": None,
        "currency": "USD",
        "price": price,
        "market_cap": None,
        "market_cap_source": None,
        "volume": safe_int(quote.get("06. volume")),
        "change": safe_float(quote.get("09. change")),
        "change_percentage": change_percentage,
        "previous_close": safe_float(quote.get("08. previous close")),
        "open": safe_float(quote.get("02. open")),
        "day_high": safe_float(quote.get("03. high")),
        "day_low": safe_float(quote.get("04. low")),
        "week_52_high": None,
        "week_52_low": None,
        "shares_outstanding": None,
        "average_volume": None,
        "relative_volume": None,
        "latest_trading_day": quote.get("07. latest trading day"),
        "source_fields": source_fields(
            currency="Alpha Vantage default_USD",
            price="Alpha Vantage GLOBAL_QUOTE.05 price",
            volume="Alpha Vantage GLOBAL_QUOTE.06 volume" if quote.get("06. volume") is not None else None,
            change="Alpha Vantage GLOBAL_QUOTE.09 change" if quote.get("09. change") is not None else None,
            change_percentage="Alpha Vantage GLOBAL_QUOTE.10 change percent" if quote.get("10. change percent") is not None else None,
            previous_close="Alpha Vantage GLOBAL_QUOTE.08 previous close" if quote.get("08. previous close") is not None else None,
            open="Alpha Vantage GLOBAL_QUOTE.02 open" if quote.get("02. open") is not None else None,
            day_high="Alpha Vantage GLOBAL_QUOTE.03 high" if quote.get("03. high") is not None else None,
            day_low="Alpha Vantage GLOBAL_QUOTE.04 low" if quote.get("04. low") is not None else None,
            latest_trading_day="Alpha Vantage GLOBAL_QUOTE.07 latest trading day" if quote.get("07. latest trading day") else None,
        ),
    }


def selected_provider_payload(symbol: str, snapshot: dict, fallbacks_used: list[str], provider_errors: list[dict]) -> dict:
    provider = snapshot.get("provider")
    internal_notes = [
        "Market data may be delayed, stale, plan-limited, or incomplete depending on provider coverage.",
        "Market data is Tier 2 market context, not filing-backed evidence and not investment advice.",
        "Do not use this output to create Buy/Sell/Hold calls, price targets, sizing, or trade instructions.",
    ]
    visible_limitations = list(snapshot.get("provider_limitations") or [])
    if fallbacks_used:
        visible_limitations.append(
            f"Fallback provider used after prior provider returned no usable price: {provider}."
        )
    if snapshot.get("market_cap") is None:
        visible_limitations.append("Market cap not available from selected provider snapshot.")
    if snapshot.get("currency") in (None, ""):
        visible_limitations.append("Currency not available from selected provider snapshot.")
    if snapshot.get("latest_trading_day"):
        visible_limitations.append(f"Provider latest trading day: {snapshot.get('latest_trading_day')}.")

    return {
        "ok": True,
        "ticker": symbol,
        "provider": provider,
        "primary_provider": provider,
        "fallbacks_used": fallbacks_used,
        "provider_errors": provider_errors,
        "provider_endpoints": {provider: snapshot.get("provider_endpoints", [])},
        "as_of": now_et(),
        "timezone": "America/New_York",
        "display_fields": DISPLAY_FIELDS,
        "company_name": snapshot.get("company_name"),
        "exchange": snapshot.get("exchange"),
        "currency": snapshot.get("currency"),
        "price": snapshot.get("price"),
        "market_cap": snapshot.get("market_cap"),
        "market_cap_source": snapshot.get("market_cap_source"),
        "volume": snapshot.get("volume"),
        "change": snapshot.get("change"),
        "change_percentage": snapshot.get("change_percentage"),
        "previous_close": snapshot.get("previous_close"),
        "open": snapshot.get("open"),
        "day_high": snapshot.get("day_high"),
        "day_low": snapshot.get("day_low"),
        "week_52_high": snapshot.get("week_52_high"),
        "week_52_low": snapshot.get("week_52_low"),
        "shares_outstanding": snapshot.get("shares_outstanding"),
        "average_volume": snapshot.get("average_volume"),
        "relative_volume": snapshot.get("relative_volume"),
        "beta": snapshot.get("beta"),
        "sector": snapshot.get("sector"),
        "industry": snapshot.get("industry"),
        "country": snapshot.get("country"),
        "ipo_date": snapshot.get("ipo_date"),
        "issuer_flags": snapshot.get("issuer_flags"),
        "price_avg_50": snapshot.get("price_avg_50"),
        "price_avg_200": snapshot.get("price_avg_200"),
        "price_vs_50d_avg_percentage": snapshot.get("price_vs_50d_avg_percentage"),
        "price_vs_200d_avg_percentage": snapshot.get("price_vs_200d_avg_percentage"),
        "performance_5d_percentage": snapshot.get("performance_5d_percentage"),
        "performance_1m_percentage": snapshot.get("performance_1m_percentage"),
        "performance_3m_percentage": snapshot.get("performance_3m_percentage"),
        "performance_6m_percentage": snapshot.get("performance_6m_percentage"),
        "performance_ytd_percentage": snapshot.get("performance_ytd_percentage"),
        "performance_1y_percentage": snapshot.get("performance_1y_percentage"),
        "source_fields": snapshot.get("source_fields", {}),
        "limitations": internal_notes + visible_limitations,
        "visible_limitations": visible_limitations,
    }


def failure_payload(symbol: str, provider_errors: list[dict], message: str) -> dict:
    return {
        "ok": False,
        "ticker": symbol,
        "provider": "multi-provider",
        "primary_provider": None,
        "fallbacks_used": [],
        "provider_errors": provider_errors,
        "as_of": now_et(),
        "timezone": "America/New_York",
        "error": sanitize_error(message),
        "limitations": [
            "No provider returned a usable price; no market-data values should be inferred.",
            "Provider errors are sanitized and API keys/authorization values are redacted.",
        ],
    }


def input_error_payload(message: str) -> dict:
    return {
        "ok": False,
        "provider": "multi-provider",
        "primary_provider": None,
        "fallbacks_used": [],
        "provider_errors": [],
        "as_of": now_et(),
        "timezone": "America/New_York",
        "error": sanitize_error(message),
        "limitations": ["No provider calls were made for invalid input."],
    }


def get_market_context(symbol: str) -> dict:
    symbol = symbol.upper().strip()
    if not symbol:
        return input_error_payload("Missing ticker symbol")
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9.\-]{0,14}", symbol):
        return input_error_payload("Invalid ticker symbol format")

    provider_errors = []

    try:
        fmp = get_fmp_snapshot(symbol)
        if has_usable_price(fmp):
            return selected_provider_payload(symbol, fmp, [], provider_errors)
        provider_errors.append(clean_provider_error("Financial Modeling Prep", "FMP returned no usable price"))
    except Exception as exc:
        provider_errors.append(clean_provider_error("Financial Modeling Prep", exc))

    try:
        finnhub = get_finnhub_snapshot(symbol)
        if has_usable_price(finnhub):
            return selected_provider_payload(symbol, finnhub, ["Finnhub"], provider_errors)
        provider_errors.append(clean_provider_error("Finnhub", "Finnhub returned no usable price"))
    except Exception as exc:
        provider_errors.append(clean_provider_error("Finnhub", exc))

    try:
        alpha = get_alpha_snapshot(symbol)
        if has_usable_price(alpha):
            return selected_provider_payload(symbol, alpha, ["Finnhub", "Alpha Vantage"], provider_errors)
        provider_errors.append(clean_provider_error("Alpha Vantage", "Alpha Vantage returned no usable price"))
    except Exception as exc:
        provider_errors.append(clean_provider_error("Alpha Vantage", exc))

    return failure_payload(symbol, provider_errors, "No market-data provider returned a usable price")


def format_as_of(value: str | None) -> str:
    if not value:
        return "Not available"
    try:
        parsed = datetime.fromisoformat(value)
        month = parsed.strftime("%b")
        hour = parsed.strftime("%I").lstrip("0") or "0"
        return f"{month} {parsed.day}, {parsed.year}, {hour}:{parsed.strftime('%M %p')} ET"
    except Exception:
        return value


def format_number(value, decimals: int = 2, *, suffix: str = "") -> str:
    numeric = safe_float(value)
    if numeric is None:
        return "Not available"
    return f"{numeric:,.{decimals}f}{suffix}"


def format_integer(value) -> str:
    numeric = safe_int(value)
    if numeric is None:
        return "Not available"
    return f"{numeric:,}"


def format_money(value, currency: str | None = "USD") -> str:
    numeric = safe_float(value)
    if numeric is None:
        return "Not available"
    prefix = "$" if (currency or "USD") == "USD" else f"{currency} "
    return f"{prefix}{numeric:,.2f}"


def format_market_cap(value, currency: str | None = "USD") -> str:
    numeric = safe_float(value)
    if numeric is None:
        return "Not available"
    prefix = "$" if (currency or "USD") == "USD" else f"{currency} "
    abs_value = abs(numeric)
    for divisor, label in ((1_000_000_000_000, "T"), (1_000_000_000, "B"), (1_000_000, "M")):
        if abs_value >= divisor:
            return f"{prefix}{numeric / divisor:,.2f}{label}"
    return f"{prefix}{numeric:,.0f}"


def format_percent(value) -> str:
    return format_number(value, 2, suffix="%")


def format_change(payload: dict) -> str:
    change = payload.get("change")
    change_percentage = payload.get("change_percentage")
    if change is None and change_percentage is None:
        return "Not available"
    change_text = format_money(change, payload.get("currency")) if change is not None else "Not available"
    percent_text = format_percent(change_percentage) if change_percentage is not None else "Not available"
    return f"{change_text} / {percent_text}"


def issuer_type(payload: dict) -> str:
    flags = payload.get("issuer_flags") or {}
    if flags.get("is_etf") is True:
        return "ETF"
    if flags.get("is_adr") is True:
        return "ADR"
    if flags.get("is_fund") is True:
        return "Fund"
    if flags:
        return "Common stock"
    return "Not available"


def yes_no(value) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return "Not available"


def title_for_payload(payload: dict) -> str:
    ticker = payload.get("ticker") or "UNKNOWN"
    company = payload.get("company_name")
    suffix = "Market Snapshot"
    if company:
        return f"{ticker} | {company} {suffix}"
    return f"{ticker} | {suffix}"


def render_failure(payload: dict) -> str:
    ticker = payload.get("ticker") or "UNKNOWN"
    errors = payload.get("provider_errors") or []
    error_text = "; ".join(f"{item.get('provider')}: {item.get('error')}" for item in errors) if errors else payload.get("error", "Unavailable")
    return "\n".join([
        f"!market {ticker} — Market Data Unavailable",
        f"As of: {format_as_of(payload.get('as_of'))}",
        "",
        "No provider returned a usable price.",
        f"Provider errors: {sanitize_error(error_text)}",
        "Limitations: No price, market cap, or valuation metric should be inferred from this failure.",
    ])


def render_compact_snapshot(payload: dict) -> str:
    # Compatibility wrapper only. The old skinny compact snapshot is no longer a
    # normal display path; all human-readable snapshot renders use Standard.
    return render_standard_snapshot(payload)


def render_standard_snapshot(payload: dict) -> str:
    if not payload.get("ok"):
        return render_failure(payload)
    currency = payload.get("currency")
    flags = payload.get("issuer_flags") or {}
    lines = [
        title_for_payload(payload),
        f"As of: {format_as_of(payload.get('as_of'))}",
        f"Source: {payload.get('provider')}",
        "",
        "## Profile",
        "",
        f"Sector: {payload.get('sector') or 'Not available'}",
        f"Industry: {payload.get('industry') or 'Not available'}",
        f"Country: {payload.get('country') or 'Not available'}",
        f"Exchange: {payload.get('exchange') or 'Not available'}",
        f"IPO Date: {payload.get('ipo_date') or 'Not available'}",
        f"Issuer Type: {issuer_type(payload)}",
        f"Actively Trading: {yes_no(flags.get('is_actively_trading'))}",
        "",
        "## Price Action",
        "",
        f"Market Cap: {format_market_cap(payload.get('market_cap'), currency)}",
        f"Price: {format_money(payload.get('price'), currency)}",
        f"Change: {format_change(payload)}",
        f"Previous Close: {format_money(payload.get('previous_close'), currency)}",
        f"Open: {format_money(payload.get('open'), currency)}",
        f"Day High: {format_money(payload.get('day_high'), currency)}",
        f"Day Low: {format_money(payload.get('day_low'), currency)}",
        f"52-Week High: {format_money(payload.get('week_52_high'), currency)}",
        f"52-Week Low: {format_money(payload.get('week_52_low'), currency)}",
        "",
        "## Liquidity",
        "",
        f"Volume: {format_integer(payload.get('volume'))}",
        f"Average Volume: {format_integer(payload.get('average_volume'))}",
        f"Relative Volume: {format_number(payload.get('relative_volume'), 2)}",
        "",
        "## Trend",
        "",
        f"5D Performance: {format_percent(payload.get('performance_5d_percentage'))}",
        f"1M Performance: {format_percent(payload.get('performance_1m_percentage'))}",
        f"3M Performance: {format_percent(payload.get('performance_3m_percentage'))}",
        f"6M Performance: {format_percent(payload.get('performance_6m_percentage'))}",
        f"YTD Performance: {format_percent(payload.get('performance_ytd_percentage'))}",
        f"1Y Performance: {format_percent(payload.get('performance_1y_percentage'))}",
        f"50D Avg: {format_money(payload.get('price_avg_50'), currency)}",
        f"200D Avg: {format_money(payload.get('price_avg_200'), currency)}",
        f"Price vs 50D Avg: {format_percent(payload.get('price_vs_50d_avg_percentage'))}",
        f"Price vs 200D Avg: {format_percent(payload.get('price_vs_200d_avg_percentage'))}",
        f"Beta: {format_number(payload.get('beta'), 2)}",
    ]
    limitations = payload.get("visible_limitations") or payload.get("provider_limitations") or []
    if limitations:
        lines.extend(["", f"Limitation: {sanitize_error(str(limitations[0]))}"])
    return "\n".join(lines)


def render_market_snapshot(payload: dict, mode: str = "standard") -> str:
    # Normal !market output has one Standard Market Snapshot shape. Former
    # compact/full/expanded render tokens are accepted only as compatibility
    # aliases and do not select separate display modes.
    return render_standard_snapshot(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Midas market-data snapshot helper")
    parser.add_argument("ticker", nargs="?", help="Ticker symbol")
    parser.add_argument("mode", nargs="?", choices=["standard", "compact", "full", "expanded"], help="Optional render compatibility token; all render the Standard snapshot")
    parser.add_argument("--render", choices=["standard", "compact", "full", "expanded"], help="Render human-readable Standard output instead of JSON")
    args = parser.parse_args()

    if not args.ticker:
        payload = input_error_payload("Usage: python tools/market_data_snapshot.py TICKER")
        if args.render:
            print(render_market_snapshot(payload, args.render))
        else:
            print(json.dumps(payload, indent=2))
        return 1

    payload = get_market_context(args.ticker)
    render_mode = args.render or args.mode
    if render_mode:
        print(render_market_snapshot(payload, render_mode))
    else:
        print(json.dumps(payload, indent=2))
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
