import pandas as pd
from xbrl_parser import XBRLParser



def xbrl2df(path):
    # XBRLパーサーを初期化
    parser = XBRLParser()

    # XBRLファイルをパース (EDINETからダウンロードしたファイルなどを指定)
    # ここではサンプルとして 'your_xbrl_file.xbrl' としています
    # 実際にご自身のファイルパスに置き換えてください
    path = 'path/to/your_xbrl_file.xbrl'

    try:
        with open(path, 'r', encoding='utf-8') as f:
            xbrl = parser.parse(f)

        # 主要な財務データ（ファクト）をDataFrameに変換
        df = xbrl.to_dataframe()

        # DataFrameの最初の5行を表示
        print("--- 財務データ (Facts) ---")
        print(df.head())

        # DataFrameの情報を表示
        print("\n--- DataFrame情報 ---")
        df.info()

        return df

    except FileNotFoundError:
        print("エラー: XBRLファイルが見つかりません。ファイルパスを確認してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")