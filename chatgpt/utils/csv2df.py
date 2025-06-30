import pandas as pd
import os

def csv_to_dataframe(file_path, encoding='utf-8', sep=',', header='infer', skip_rows=None):
    """
    CSVファイルからデータを読み込み、Pandas DataFrameに変換する関数。

    Args:
        file_path (str): 読み込むCSVファイルのパス。
        encoding (str, optional): ファイルのエンコーディング (例: 'utf-8', 'shift_jis', 'cp932')。
                                  デフォルトは 'utf-8'。
        sep (str, optional): 列の区切り文字 (セパレータ)。デフォルトは ',' (カンマ)。
                             タブ区切りなら '\t'。
        header (int or list of int or 'infer' or None, optional):
            ヘッダーとして使用する行番号 (0から始まる)。
            - 'infer': 最初の行をヘッダーとして推測する (デフォルト)。
            - 0: 最初の行をヘッダーとして使用。
            - None: ヘッダーなし。
            - list: 複数行をヘッダーとして使用 (MultiIndexになる)。
        skip_rows (int or list or None, optional):
            読み込み時にスキップする行数 (先頭から)。

    Returns:
        pandas.DataFrame or None:
            CSVデータが格納されたDataFrame。
            ファイルが見つからない場合や読み込みエラーが発生した場合は None。
    """
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません - {file_path}")
        return None

    try:
        df = pd.read_csv(
            file_path,
            encoding=encoding,
            sep=sep,
            header=header,
            skiprows=skip_rows
        )
        print(f"'{file_path}' をDataFrameに変換しました。")
        return df
    except UnicodeDecodeError:
        print(f"エラー: エンコーディング '{encoding}' でファイルをデコードできませんでした。")
        print("おそらくファイルのエンコーディングが異なります。'shift_jis' や 'cp932' を試してみてください。")
        return None
    except Exception as e:
        print(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
        return None

### **使用例**

if __name__ == "__main__":
    # 1. 練習用のCSVファイルを作成 (もし手元にない場合)
    sample_data = {
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']
    }
    sample_df = pd.DataFrame(sample_data)
    sample_csv_path = 'sample_data.csv'
    sample_df.to_csv(sample_csv_path, index=False, encoding='utf-8')
    print(f"\n'{sample_csv_path}' を作成しました。\n")

    # 2. CSVファイルをDataFrameに変換する

    # CSVファイルのパス (スクリプトと同じディレクトリにあると仮定)
    # 別の場所にある場合は、絶対パスまたは適切な相対パスを指定してください
    # csv_file_path = '/path/to/your/data.csv'
    csv_file_path = sample_csv_path

    print("--- 基本的な読み込み例 (UTF-8エンコーディング、カンマ区切り) ---")
    df_basic = csv_to_dataframe(csv_file_path)
    if df_basic is not None:
        print("DataFrameの先頭5行:\n", df_basic.head())
        print("\nDataFrameの情報を確認:\n", df_basic.info())

    print("\n--- Shift-JIS エンコーディングのCSVを読み込む例 (もしCSVがShift-JISの場合) ---")
    # Shift-JISで保存されたCSVファイルを想定
    # encoding='shift_jis' を指定
    # df_shift_jis = csv_to_dataframe('my_shift_jis_data.csv', encoding='shift_jis')
    # if df_shift_jis is not None:
    #     print("Shift-JIS DataFrame:\n", df_shift_jis)

    print("\n--- タブ区切りCSVを読み込む例 (もしCSVがタブ区切りTSVの場合) ---")
    # タブ区切りCSVファイルを想定
    # sep='\t' を指定
    # df_tsv = csv_to_dataframe('my_tab_separated_data.tsv', sep='\t')
    # if df_tsv is not None:
    #     print("TSV DataFrame:\n", df_tsv)

    print("\n--- ヘッダーなしのCSVを読み込む例 ---")
    # ヘッダーなしのCSVファイルを想定
    # header=None を指定すると、列名が自動的に 0, 1, 2... となる
    # (ここではサンプルデータにヘッダーがあるため、ID, Nameなどがデータ行になります)
    df_no_header = csv_to_dataframe(csv_file_path, header=None)
    if df_no_header is not None:
        print("ヘッダーなしのDataFrame:\n", df_no_header)

    print("\n--- 先頭行をスキップして読み込む例 (例: 最初の2行をスキップ) ---")
    # CSVファイルの先頭に不要な情報がある場合などに使用
    df_skipped_rows = csv_to_dataframe(csv_file_path, skip_rows=1) # 0から始まるので1は2行目をスキップ
    if df_skipped_rows is not None:
        print("スキップ行を指定したDataFrame:\n", df_skipped_rows)