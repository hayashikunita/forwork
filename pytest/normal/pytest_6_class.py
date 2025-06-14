# https://qiita.com/zomaphone/items/284354fed78663a7b39d

import pytest
class TestTwo:

    @pytest.fixture
    def variable_in_c(self):
        return "hi"

    def test_01(self, variable_in_c):
        assert variable_in_c == "hi"

