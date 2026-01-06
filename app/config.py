import os
from dotenv import load_dotenv

# Load values from .env into environment
load_dotenv()

def get_db_path():
    return os.getenv("DB_PATH", "data/stocks.db")

DEFAULT_PERIOD = os.getenv("DEFAULT_PERIOD", "1d")
DEFAULT_INTERVAL = os.getenv("DEFAULT_INTERVAL", "1m")
