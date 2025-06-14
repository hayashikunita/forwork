import pytest

@pytest.fixture
def sample_data():
    dict_sample = {"name": "Alice", "age": 30}
    return dict_sample