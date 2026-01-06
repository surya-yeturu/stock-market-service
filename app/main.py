from fastapi import FastAPI
from app.api import router
from app.storage import init_db

app = FastAPI(title="Stock Market Data Service")

# Initialize DB on startup
init_db()

# Register API routes
app.include_router(router)
