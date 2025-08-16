# test_example.py
import pytest

def test_addition():
    """
    足し算のテスト
    """
    assert 1 + 1 == 2

def test_greeting():
    """
    あいさつ文のテスト
    """
    name = "Alice"
    assert f"Hello, {name}!" == "Hello, Alice!"

def test_list_length():
    """
    リストの長さのテスト
    """
    my_list = [1, 2, 3]
    assert len(my_list) == 3
