import pandas as pd

# 辞書のリスト
def dict2df(data :dict):

    data = [
        {'ID': 1, 'Name': 'Alice', 'Age': 25},
        {'ID': 2, 'Name': 'Bob', 'Age': 30},
        {'ID': 3, 'Name': 'Charlie', 'Age': 35, 'City': 'Tokyo'} # キーが異なっても対応
    ]

    # DataFrameに変換
    df_from_list_of_dicts = pd.DataFrame(data)

    print("--- 辞書のリストをDataFrameに (各辞書が1行) ---")
    print(df_from_list_of_dicts)
    print("\n")

    return df_from_list_of_dicts