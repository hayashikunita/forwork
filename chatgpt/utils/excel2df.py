import pandas as pd
import os

def excel2dataframe(file_path, sheet_name=None, header=0, skip_rows=None):
    """
    Excelファイルからデータを読み込み、Pandas DataFrameに変換する関数。

    Args:
        file_path (str): 読み込むExcelファイルのパス。
        sheet_name (str or int or list or None, optional):
            読み込むシートの名前またはインデックス。
            - None: 最初のシートを読み込む (デフォルト)。
            - str: シート名 (例: 'Sheet1')。
            - int: シートのインデックス (0から始まる、例: 0)。
            - list: 複数のシート名またはインデックスのリスト。
                    この場合、戻り値は {シート名: DataFrame} の辞書になる。
        header (int or list of int or None, optional):
            ヘッダーとして使用する行番号 (0から始まる)。
            - 0: 最初の行をヘッダーとして使用 (デフォルト)。
            - None: ヘッダーなし。
            - list: 複数行をヘッダーとして使用 (MultiIndexになる)。
        skip_rows (int or list or None, optional):
            読み込み時にスキップする行数 (先頭から)。

    Returns:
        pandas.DataFrame or dict:
            Excelデータが格納されたDataFrame。
            複数のシートを読み込む場合は、{シート名: DataFrame} の辞書。
            ファイルが見つからない場合はNone。
    """
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません - {file_path}")
        return None

    try:
        if sheet_name is None:
            # 最初のシートを読み込む場合
            df = pd.read_excel(
                file_path,
                header=header,
                skiprows=skip_rows
            )
            print(f"'{file_path}' の最初のシートをDataFrameに変換しました。")
            return df
        elif isinstance(sheet_name, (str, int)):
            # 特定のシートを読み込む場合
            df = pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                header=header,
                skiprows=skip_rows
            )
            print(f"'{file_path}' のシート '{sheet_name}' をDataFrameに変換しました。")
            return df
        elif isinstance(sheet_name, list):
            # 複数のシートを読み込む場合 (辞書で返される)
            dfs = pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                header=header,
                skiprows=skip_rows
            )
            print(f"'{file_path}' の指定された複数のシートをDataFrame辞書に変換しました。")
            return dfs
        else:
            print("エラー: 'sheet_name' の指定が不正です。str, int, list of (str or int) または None を指定してください。")
            return None

    except Exception as e:
        print(f"Excelファイルの読み込み中にエラーが発生しました: {e}")
        return None