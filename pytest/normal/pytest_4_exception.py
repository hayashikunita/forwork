# test_exception.py
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)