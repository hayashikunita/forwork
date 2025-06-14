import pytest
from botocore.exceptions import NoCredentialsError
from moto import mock_aws
import boto3

# @pytest.fixture()



@pytest.fixture
def setup_s3():
    with mock_aws():

    
        """S3の設定を初期化するフィクスチャー"""
        s3_client = boto3.client('s3',
        aws_access_key_id="test",
        aws_secret_access_key="test" ,
        region_name='ap-northeast-1')

        # バケット作成
        s3_client.create_bucket(
            Bucket="bucket1",
            CreateBucketConfiguration={"LocationConstraint": "ap-northeast-1"},
        )

        yield s3_client


@pytest.fixture
def insert_data_s3(setup_s3):
    """テストデータを挿入するフィクスチャー"""
    # テストデータ定義
    test_data = ["This is a test file."]
    key = "test-key/test.txt"

    # テストデータを挿入
    for item in test_data:
        setup_s3.put_object(Bucket="bucket1", Key=key, Body=item)

    yield



# S3 からデータを取得する関数
def get_s3_object(bucket_name, key):
    try:
        s3 = boto3.client("s3")
        response = s3.get_object(Bucket=bucket_name, Key=key)
        print(response)
        return response["Body"].read().decode("utf-8")

    except NoCredentialsError:
        return "No AWS credentials found"
    except Exception as e:
        return str(e)


# テストコード
@mock_aws
def test_get_s3_object(insert_data_s3):
    # モック S3 環境をセットアップ
    s3 = boto3.client("s3", region_name="ap-northeast-1")
    bucket_name = "bucket1"
    key = "test-key/test.txt"
    content = "This is a test file."

    # 関数をテスト
    result = get_s3_object(bucket_name, key)
    assert result == content

    # 存在しないキーのテスト
    non_existent_key = "non-existent-key"
    result = get_s3_object(bucket_name, non_existent_key)
    assert "NoSuchKey" in result