import pytest
import time
from src.validator import Validator

@pytest.fixture
def validator():
    return Validator()

def test_valid_amount(validator):
    time.sleep(3)
    assert validator.is_valid_amount(50)
    assert not validator.is_valid_amount(-10)

def test_valid_category(validator):
    large_data = ["x" * 2000 for _ in range(10**6)]
    assert validator.is_valid_category("Food")
    assert not validator.is_valid_category("Random")
