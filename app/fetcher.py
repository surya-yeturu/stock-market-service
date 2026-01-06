import yfinance as yf
from typing import List, Dict
from app.config import DEFAULT_PERIOD, DEFAULT_INTERVAL


def fetch_stock_data(ticker: str) -> List[Dict]:
    """
    Fetch OHLCV stock data for a given ticker from Yahoo Finance
    """

    # Create a ticker object
    stock = yf.Ticker(ticker)

    # Fetch historical data
    df = stock.history(
        period=DEFAULT_PERIOD,
        interval=DEFAULT_INTERVAL
    )

    # Handle invalid ticker or empty data
    if df.empty:
        raise ValueError("Invalid ticker or no data available")

    records = []

    # Convert DataFrame rows into dictionaries
    for index, row in df.iterrows():
        record = {
            "ticker": ticker,
            "timestamp": index.isoformat(),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        }
        records.append(record)

    return records
