import pytest
import pandas as pd
from unittest.mock import patch
from app.fetcher import fetch_stock_data


@patch("app.fetcher.yf.Ticker")
def test_fetch_invalid_ticker(mock_ticker):
    # Mock empty DataFrame
    mock_ticker.return_value.history.return_value = pd.DataFrame()

    with pytest.raises(ValueError):
        fetch_stock_data("INVALID")


@patch("app.fetcher.yf.Ticker")
def test_fetch_valid_data(mock_ticker):
    # Create fake stock data
    data = {
        "Open": [100.0],
        "High": [110.0],
        "Low": [90.0],
        "Close": [105.0],
        "Volume": [1000],
    }

    index = pd.to_datetime(["2025-01-01 09:15"])
    fake_df = pd.DataFrame(data, index=index)

    mock_ticker.return_value.history.return_value = fake_df

    records = fetch_stock_data("TEST")

    assert len(records) == 1
    assert records[0]["ticker"] == "TEST"
    assert records[0]["open"] == 100.0
    assert records[0]["close"] == 105.0
