import sys
import os
import pytest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(autouse=True)
def use_test_db(monkeypatch):
    """
    Force all tests to use a separate test database
    """
    test_db_path = "data/test_stocks.db"

    # Override DB_PATH for tests
    monkeypatch.setenv("DB_PATH", test_db_path)

    # Remove old test DB if exists
    if os.path.exists(test_db_path):
        os.remove(test_db_path)
