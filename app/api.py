from fastapi import APIRouter, Query, HTTPException
from app.fetcher import fetch_stock_data
from app.storage import insert_records, get_last_record, get_all_records

router = APIRouter()


@router.post("/fetch")
def fetch(ticker: str = Query(..., description="Stock ticker symbol")):
    try:
        records = fetch_stock_data(ticker)
        insert_records(records)
        return {
            "message": "Data fetched and stored successfully",
            "records_fetched": len(records)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/last")
def last():
    record = get_last_record()
    if record is None:
        raise HTTPException(status_code=404, detail="No data available")
    return record


@router.get("/history")
def history():
    return get_all_records()
