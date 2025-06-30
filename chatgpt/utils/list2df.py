import pandas as pd


def list2df(data):
    # リストのリスト
    # data = [
    #     [1, 'Alice', 25],
    #     [2, 'Bob', 30],
    #     [3, 'Charlie', 35]
    # ]

    # DataFrameに変換
    # columns引数で列名を指定
    df_from_list_of_lists = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

    print("--- リストのリストをDataFrameに (各内部リストが1行) ---")
    print(df_from_list_of_lists)
    print("\n")

    return df_from_list_of_lists


    # import pandas as pd

    # data = [
    #     ['Apple', 100],
    #     ['Banana', 50],
    #     ['Orange', 120]
    # ]
    # columns = ['Item', 'Price']
    # index = ['A', 'B', 'C'] # 行のラベル

    # df_with_index = pd.DataFrame(data, columns=columns, index=index)

    # print("--- Indexを指定してDataFrameに ---")
    # print(df_with_index)
    # print("\n")