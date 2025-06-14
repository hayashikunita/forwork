import pytest
import boto3
from moto import mock_aws

# setup_eventbridge フィクスチャをここにコピーするか、別のファイルからインポートしてください
@pytest.fixture()
def setup_eventbridge():
    """EventBridgeのモックセットアップ"""
    # 解決策1: moto.mock_aws() でリージョンを指定
    with mock_aws(): # 例として us-east-1 を指定
        eventbridge_client = boto3.client('scheduler', region_name="us-east-1") # boto3.client でもリージョンを指定

        # スケジュールグループを作成
        eventbridge_client.create_schedule_group(
            Name='schedule1',
        )

        yield eventbridge_client


def test_setup_eventbridge_schedule_group_created(setup_eventbridge):
    """
    setup_eventbridge フィクスチャがスケジュールグループを正しく作成することを確認
    """
    client = setup_eventbridge

    response = client.list_schedule_groups()
    
    # 解決策2: 期待値を2に変更するか、特定のグループを検索
    # motoのデフォルトグループ 'default' と作成した 'schedule1' で2つになる
    assert len(response['ScheduleGroups']) == 2 
    
    # より堅牢なチェック: 'schedule1' という名前のグループが存在することを確認
    schedule_group_names = [group['Name'] for group in response['ScheduleGroups']]
    assert 'schedule1' in schedule_group_names


def test_setup_eventbridge_schedule_group_arn_format(setup_eventbridge):
    """
    作成されたスケジュールグループのARNのフォーマットを確認
    (motoのモックが正しくARNを生成しているか)
    """
    client = setup_eventbridge
    response = client.list_schedule_groups()
    
    # 解決策3: 'schedule1' という名前のグループを探してそのARNをチェック
    schedule1_group_arn = None
    for group in response['ScheduleGroups']:
        if group['Name'] == 'schedule1':
            schedule1_group_arn = group['Arn']
            break
            
    assert schedule1_group_arn is not None, "Schedule group 'schedule1' not found."

    # ARNが存在し、特定のパターンにマッチすることを確認
    # 例: arn:aws:scheduler:region:123456789012:schedule-group/schedule1
    assert schedule1_group_arn.startswith('arn:aws:scheduler:')
    assert '/schedule1' in schedule1_group_arn
    assert 'schedule-group' in schedule1_group_arn
    assert 'us-east-1' in schedule1_group_arn # リージョン名が含まれていることを確認