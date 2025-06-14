# https://qiita.com/zomaphone/items/284354fed78663a7b39d
import pytest

@pytest.fixture
def variable():
    return "hi"

class TestOne:
    def test_00(self, variable):
        assert variable == "hi"
