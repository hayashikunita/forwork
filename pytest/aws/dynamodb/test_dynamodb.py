# https://qiita.com/inacyc_k/items/f123135f0d230792bbdd

import pytest
from moto import mock_aws
import boto3
from botocore.exceptions import ClientError

@pytest.fixture()
def setup_dynamoDB():
    """
    DynamoDBの設定を初期化するフィクスチャー
    """
    with mock_aws():
        dynamodb_resource = boto3.resource('dynamodb', region_name="us-east-1")
        tables = {}

        # テーブル1作成
        tables["table1"] = dynamodb_resource.create_table(
            TableName="table_1",
            KeySchema=[
                {'AttributeName': 'partition_key', 'KeyType': 'HASH'}  # パーティションキー
            ],
            AttributeDefinitions=[
                {'AttributeName': 'partition_key', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        
        # テーブル2作成
        tables["table2"] = dynamodb_resource.create_table(
            TableName="table2",
            KeySchema=[
                {'AttributeName': 'primary_id', 'KeyType': 'HASH'},  # パーティションキー
                {'AttributeName': 'sort_key', 'KeyType': 'RANGE'}  # ソートキー
            ],
            AttributeDefinitions=[
                {'AttributeName': 'primary_id', 'AttributeType': 'S'},
                {'AttributeName': 'sort_key', 'AttributeType': 'S'},
                {'AttributeName': 'alternative_key', 'AttributeType': 'S'}  # LSI のソートキー
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'LSI',
                    'KeySchema': [
                        {'AttributeName': 'primary_id','KeyType': 'HASH'},  # 同じパーティションキー
                        {'AttributeName': 'alternative_key','KeyType': 'RANGE'}  # LSI のソートキー
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'  # 全ての属性を射影
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        yield tables


# テスト: テーブルが正しく作成されるか
def test_table_creation(setup_dynamoDB):
    assert "table1" in setup_dynamoDB
    assert "table2" in setup_dynamoDB
    assert setup_dynamoDB["table1"].table_status == "ACTIVE"
    assert setup_dynamoDB["table2"].table_status == "ACTIVE"

# テスト: データの挿入と取得
def test_insert_and_get_item(setup_dynamoDB):
    table = setup_dynamoDB["table1"]
    
    # データを挿入
    table.put_item(Item={"partition_key": "user123", "name": "Alice", "age": 30})
    
    # データを取得
    response = table.get_item(Key={"partition_key": "user123"})
    item = response.get("Item")
    
    assert item is not None
    assert item["name"] == "Alice"
    assert item["age"] == 30

# テスト: LSI を使用した検索
def test_lsi_query(setup_dynamoDB):
    table = setup_dynamoDB["table2"]
    
    # データを挿入
    table.put_item(Item={"primary_id": "order001", "sort_key": "2023-01-01", "alternative_key": "customer123", "amount": 100})
    table.put_item(Item={"primary_id": "order001", "sort_key": "2023-01-02", "alternative_key": "customer456", "amount": 200})
    
    # LSI を使用して検索
    response = table.query(
        IndexName="LSI",
        KeyConditionExpression="primary_id = :pid AND alternative_key = :alt",
        ExpressionAttributeValues={":pid": "order001", ":alt": "customer123"}
    )
    
    items = response.get("Items", [])
    
    assert len(items) == 1
    assert items[0]["amount"] == 100