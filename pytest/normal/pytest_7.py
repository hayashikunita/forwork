# https://note.com/yukiko_python/n/ncb6aa978ec28#57bbde15-ebf8-4e0f-be7a-189f6bbf8d0e

# test_math_functions.py
import pytest
from math_functions import add, subtract, multiply, divide

@pytest.fixture
def sample_data():
    return {
        "a": 10,
        "b": 2
    }

def test_add(sample_data):
    assert add(sample_data["a"], sample_data["b"]) == 12

def test_subtract(sample_data):
    assert subtract(sample_data["a"], sample_data["b"]) == 8

def test_multiply(sample_data):
    assert multiply(sample_data["a"], sample_data["b"]) == 20

def test_divide(sample_data):
    assert divide(sample_data["a"], sample_data["b"]) == 5
    with pytest.raises(ValueError):
        divide(sample_data["a"], 0)