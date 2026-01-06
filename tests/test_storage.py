from app.storage import init_db, insert_records, get_all_records, get_last_record

def test_insert_and_read():
    init_db()

    record = [{
        "ticker": "TEST",
        "timestamp": "2025-01-01T09:15:00",
        "open": 100.0,
        "high": 110.0,
        "low": 90.0,
        "close": 105.0,
        "volume": 1000,
    }]

    insert_records(record)

    all_records = get_all_records()
    last_record = get_last_record()

    assert len(all_records) >= 1
    assert last_record["ticker"] == "TEST"


def test_duplicate_insert():
    init_db()

    record = [{
        "ticker": "DUP",
        "timestamp": "2025-01-01T10:00:00",
        "open": 200.0,
        "high": 210.0,
        "low": 190.0,
        "close": 205.0,
        "volume": 500,
    }]

    insert_records(record)
    insert_records(record)  # duplicate

    all_records = get_all_records()

    # Should still be only one record for that timestamp
    filtered = [r for r in all_records if r["ticker"] == "DUP"]
    assert len(filtered) == 1
