import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from pytest.db.pytest_db_3_sqlalchemy import Base # main.py からモデルのBaseをインポート

# テスト用のインメモリSQLiteデータベースエンジン
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session() -> Session:
    """
    テストごとに独立したDBセッションとトランザクションを提供するフィクスチャ
    """
    # テーブルを毎回作成・削除することでテストの独立性を保つ
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session  # テスト関数にセッションを渡す

    session.close()
    transaction.rollback() # テスト後、変更をロールバックしてDBをクリーンな状態に戻す
    connection.close()
    Base.metadata.drop_all(bind=engine)