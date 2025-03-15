import pytest
import json
import os
import time
from src.file_handler import FileHandler

TEST_FILE_PATH = "data/test_expenses.json"

@pytest.fixture
def file_handler():
    """Fixture to use a test file instead of the actual expenses.json file."""
    handler = FileHandler()
    handler.FILE_PATH = TEST_FILE_PATH  # Redirect to test file
    yield handler
    if os.path.exists(TEST_FILE_PATH):  # Cleanup after test
        os.remove(TEST_FILE_PATH)

def test_save_and_load_data(file_handler):
    """Test saving and loading expense data."""
    sample_data = [
        {"id": 1, "amount": 50.0, "category": "Food", "description": "Lunch"},
        {"id": 2, "amount": 20.0, "category": "Transport", "description": "Bus ticket"}
    ]
    
    file_handler.save_data(sample_data)
    loaded_data = file_handler.load_data()

    assert loaded_data == sample_data  # Ensure data is saved and loaded correctly

def test_load_empty_file(file_handler):
    """Test loading an empty file (should return an empty list)."""
    time.sleep(1)
    assert file_handler.load_data() == []

def test_save_creates_file(file_handler):
    """Test that saving data creates a file."""
    sample_data = [{"id": 1, "amount": 100.0, "category": "Bills", "description": "Electricity"}]
    file_handler.save_data(sample_data)

    assert os.path.exists(TEST_FILE_PATH)  # File should exist
    with open(TEST_FILE_PATH, "r") as f:
        data = json.load(f)
        assert data == sample_data  # File content should match saved data
