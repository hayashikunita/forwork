import pytest

class User:
    def __init__(self, name,age):
        self.name = "test"
    def __init__(self, name, age):
        self.name = name
        self.age = age  # 属性の定義


# Fixture: テスト用のユーザーインスタンスを作成
@pytest.fixture
def sample_user():
    return User(name="Alice", age=25)

# テスト: ユーザーの名前が正しく設定されているか
def test_user_name(sample_user):
    assert sample_user.name == "Alice"

# テスト: ユーザーの年齢が正しく設定されているか
def test_user_age(sample_user):
    assert sample_user.age == 25

# テスト: `greet()` メソッドの動作確認
def test_user_greet(sample_user):
    assert sample_user.greet() == "Hello, my name is Alice."

# テスト: `is_adult()` メソッドの動作確認
def test_user_is_adult(sample_user):
    assert sample_user.is_adult() is True

# Fixtureを使って異なるユーザーを作成
@pytest.fixture
def underage_user():
    return User(name="Bob", age=16)

# 未成年ユーザーの `is_adult()` のテスト
def test_underage_user_is_adult(underage_user):
    assert underage_user.is_adult() is False
