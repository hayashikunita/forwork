import pytest

def test_sample_data(sample_data):
    sample_data_val = sample_data
    assert sample_data_val["name"] == "Alice"
    assert sample_data_val["age"] == 30
