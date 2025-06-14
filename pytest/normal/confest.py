# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser():
    """
    テストセッション全体で一度だけWebブラウザを起動し、終了するフィクスチャ。
    実際のテストではSelenium WebDriverなどの初期化・終了処理が入る。
    """
    print("\n--- ブラウザを起動しました ---")
    # ここで実際のWebDriver (例: selenium.webdriver.Chrome()) を初期化
    _browser_instance = "Simulated Chrome Browser"
    yield _browser_instance  # テストにブラウザインスタンスを渡す
    print("--- ブラウザを閉じました ---")

@pytest.fixture(scope="function")
def logged_in_user(browser):
    """
    各テスト関数でログイン状態のユーザーを作成するフィクスチャ。
    'browser' フィクスチャに依存しているため、browserが先に実行される。
    """
    print("--- ユーザーがログインしました ---")
    user_session_data = f"User logged into {browser}"
    yield user_session_data
    print("--- ユーザーがログアウトしました ---")