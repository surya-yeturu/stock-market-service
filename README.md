# Stock Market Data Service

A Python-based service that fetches stock market data from Yahoo Finance, stores it locally, and exposes it via a REST API.

This project was built as a take-home assignment to demonstrate clean code structure, separation of concerns, API usage, local persistence, and basic testing practices.

---

## Objective

Build a small Python service that:
- Fetches OHLCV (Open, High, Low, Close, Volume) stock data
- Stores the data locally
- Exposes the data through HTTP endpoints
- Is easy to maintain, test, and extend

---

## Features

- Fetch stock data using Yahoo Finance (`yfinance`)
- Store data locally using SQLite
- Prevent duplicate records using database constraints
- REST API built with FastAPI
- Configurable behavior using environment variables
- Unit tests with pytest and mocked external API calls

---

## Tech Stack

- Python 3.13
- FastAPI
- yfinance
- SQLite
- pytest

---

## Project Structure
stock_services/
│
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── api.py # API route definitions
│ ├── fetcher.py # Yahoo Finance data fetching logic
│ ├── storage.py # SQLite database logic
│ ├── config.py # Environment-based configuration
│
├── data/
│ ├── stocks.db # Production database
│ └── test_stocks.db # Test database (used during tests)
│
├── tests/
│ ├── test_fetcher.py
│ └── test_storage.py
│
├── conftest.py # Pytest configuration
├── .env # Environment variables
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd stock_services

2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root:

DB_PATH=data/stocks.db
DEFAULT_PERIOD=1d
DEFAULT_INTERVAL=1m

Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

API Endpoints
POST /fetch

Fetches stock data from Yahoo Finance and stores it locally.

Example:

POST /fetch?ticker=TSLA


Response:

{
  "message": "Data fetched and stored successfully",
  "records_fetched": 390
}

GET /last

Returns the most recent stored stock data point.

GET /history

Returns all stored stock data.

Database Design

Table: stocks

Column	Type
id	INTEGER (Primary Key)
ticker	TEXT
timestamp	TEXT
open	REAL
high	REAL
low	REAL
close	REAL
volume	INTEGER

Constraint:

UNIQUE(ticker, timestamp)


This ensures duplicate records are not stored.

Testing

Run tests using:

pytest

Testing Approach

External API calls are mocked

Tests use a separate SQLite database

Environment variables are overridden during tests

Focused on core logic and edge cases

Design Decisions & Trade-offs

SQLite chosen for simplicity and local persistence

FastAPI used for clean API design and automatic JSON responses

Environment variables used to avoid hardcoding configuration

Database constraints used for duplicate handling instead of manual checks

# stock-market-service
