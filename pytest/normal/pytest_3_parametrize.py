# test_math.py
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),      # 1 + 2 = 3
    (0, 0, 0),      # 0 + 0 = 0
    (-1, 1, 0),     # -1 + 1 = 0
    (100, 200, 300) # 100 + 200 = 300
])
def test_addition_multiple_cases(a, b, expected):
    """
    複数の入力値で足し算をテストする
    """
    assert a + b == expected

@pytest.mark.parametrize("input_string, expected_length", [
    ("hello", 5),
    ("", 0),
    ("日本語", 3)
])
def test_string_length(input_string, expected_length):
    """
    文字列の長さをテストする
    """
    assert len(input_string) == expected_length