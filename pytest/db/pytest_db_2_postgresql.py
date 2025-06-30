import pytest
import psycopg2

@pytest.fixture(scope='function')
def db_connection(postgresql_db):
    """
    テスト用のデータベース接続とテーブル作成を行うフィクスチャ
    - postgresql_db: pytest-postgresqlが提供するフィクスチャ
    """
    # pytest-postgresqlが作成したDBへの接続情報を取得
    conn_info = postgresql_db.get_connection_info()
    conn_str = " ".join(f"{k}={v}" for k, v in conn_info.items())

    try:
        # データベースに接続
        conn = psycopg2.connect(conn_str)
        cursor = conn.cursor()

        # テスト用のテーブルを作成
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100)
            );
        """)
        conn.commit()

        # 接続オブジェクトをテスト関数に渡す
        yield conn

    finally:
        # テスト終了後に接続を閉じる
        if 'conn' in locals() and not conn.closed:
            conn.close()


def test_insert_and_select_user(db_connection):
    """
    usersテーブルへのデータ挿入と取得をテストする
    """
    # conftest.pyで定義したdb_connectionフィクスチャを受け取る
    assert db_connection is not None, "データベース接続に失敗しました"

    try:
        with db_connection.cursor() as cursor:
            # データの挿入
            user_name = "Taro Yamada"
            user_email = "taro.yamada@example.com"
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
                (user_name, user_email)
            )
            user_id = cursor.fetchone()[0]
            db_connection.commit()

            assert user_id is not None

            # データの取得と検証
            cursor.execute("SELECT name, email FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()

            assert result is not None
            assert result[0] == user_name
            assert result[1] == user_email

    except psycopg2.Error as e:
        pytest.fail(f"データベース操作中にエラーが発生しました: {e}")

def test_connection_is_clean(db_connection):
    """
    各テストが独立したDBで実行されていることを確認する
    """
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        # 前のテストで挿入したデータが存在しないことを確認
        assert count == 0