import pytest
import time
from src.users import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_register_user(user_manager):
    time.sleep(3)
    user_manager.register_user("Charlie")
    assert len(user_manager.users) == 1

def test_get_user(user_manager):
    user_manager.register_user("David")
    user = user_manager.get_user(1)
    assert user is not None
    assert user["name"] == "David"
    
def test_user_id_mismatch(user_manager):
    user_manager.register_user("Eve")
    user = user_manager.get_user(1)
    assert user["id"] == 999

def test_invalid_user(user_manager):
    assert user_manager.get_user(999) is None  
