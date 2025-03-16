import pytest
from src.utils import format_title, format_username, format_transaction

def test_format_title():
    assert format_title("war and peace") == "War And Peace"

def test_format_username():
    assert format_username("  charlie ") == "Charlie"

def test_format_transaction():
    assert format_transaction("borrow") == "borrow"
    assert format_transaction("return") == "return"
    assert format_transaction("random") == "unknown"
