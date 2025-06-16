from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# データベースエンジンの作成 (ここではインメモリのSQLiteを使用)
engine = create_engine('sqlite:///:memory:')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ユーザーモデルの定義
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# データベースにテーブルを作成
Base.metadata.create_all(bind=engine)

def get_db():
    """データベースセッションを取得する"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(db_session, name: str, email: str) -> User:
    """ユーザーを作成してデータベースに追加する"""
    new_user = User(name=name, email=email)
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user

def get_user_by_name(db_session, name: str) -> User | None:
    """名前でユーザーを検索する"""
    return db_session.query(User).filter(User.name == name).first()