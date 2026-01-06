import sqlite3
from typing import List, Dict
from app.config import get_db_path


def init_db():
    """
    Initialize the SQLite database and create table if not exists
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER,
        UNIQUE(ticker, timestamp)
    )
    """)

    conn.commit()
    conn.close()


def insert_records(records: List[Dict]):
    """
    Insert multiple stock records into the database
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    for r in records:
        try:
            cursor.execute("""
            INSERT INTO stocks
            (ticker, timestamp, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                r["ticker"],
                r["timestamp"],
                r["open"],
                r["high"],
                r["low"],
                r["close"],
                r["volume"]
            ))
        except sqlite3.IntegrityError:
            # Duplicate record (same ticker + timestamp)
            pass

    conn.commit()
    conn.close()


def get_last_record():
    """
    Get the most recent stock record from the database
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ticker, timestamp, open, high, low, close, volume
    FROM stocks
    ORDER BY timestamp DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    keys = ["ticker", "timestamp", "open", "high", "low", "close", "volume"]
    return dict(zip(keys, row))


def get_all_records():
    """
    Get all stock records from the database
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ticker, timestamp, open, high, low, close, volume
    FROM stocks
    ORDER BY timestamp
    """)

    rows = cursor.fetchall()
    conn.close()

    keys = ["ticker", "timestamp", "open", "high", "low", "close", "volume"]
    return [dict(zip(keys, row)) for row in rows]
