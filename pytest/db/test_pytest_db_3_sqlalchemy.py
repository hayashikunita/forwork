from pytest.db.pytest_db_3_sqlalchemy import create_user, get_user_by_name

def test_create_and_get_user(db_session):
    """
    ユーザーの作成と取得が正しく行えるかをテストする
    """
    # ユーザーを作成
    user_name = "Taro Yamada"
    user_email = "taro.yamada@example.com"
    created_user = create_user(db_session, name=user_name, email=user_email)

    # アサーション: 作成されたユーザーがNoneでなく、IDが割り当てられていることを確認
    assert created_user is not None
    assert created_user.id is not None

    # 作成したユーザーを取得
    retrieved_user = get_user_by_name(db_session, name=user_name)

    # アサーション: 取得したユーザー情報が正しいことを確認
    assert retrieved_user is not None
    assert retrieved_user.name == user_name
    assert retrieved_user.email == user_email

def test_get_non_existent_user(db_session):
    """
    存在しないユーザーを取得しようとした場合にNoneが返ることをテストする
    """
    retrieved_user = get_user_by_name(db_session, name="Jiro Suzuki")

    # アサーション: ユーザーが存在しないことを確認
    assert retrieved_user is None