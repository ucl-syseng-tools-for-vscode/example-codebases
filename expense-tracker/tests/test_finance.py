import pytest
from src.finance import apply_discount, calculate_tax, split_bill

def test_apply_discount_basic():
    assert apply_discount(100, 10) == 90  
    assert apply_discount(200, 20) == 160  

def test_calculate_tax_basic():
    assert calculate_tax(100) == 5  
    assert calculate_tax(200, 0.1) == 20 

def test_split_bill_normal():
    assert split_bill(100, 2) == 50 
    assert split_bill(75, 3) == 25 
