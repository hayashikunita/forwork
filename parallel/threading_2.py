import threading
import time

def task_runner(task_name, duration):
    """
    指定された時間、何らかのタスクを実行する関数をシミュレートします。
    """
    print(f"[{time.strftime('%H:%M:%S')}] タスク '{task_name}': 開始 (処理に{duration}秒かかります)")
    time.sleep(duration)  # I/O処理などの時間のかかる処理を模倣
    print(f"[{time.strftime('%H:%M:%S')}] タスク '{task_name}': 完了")

# --- メインの処理 ---
if __name__ == "__main__":
    print(f"[{time.strftime('%H:%M:%S')}] メインプログラム: 開始")

    # 実行したいタスクのリスト
    tasks = [
        ("データのダウンロード", 3),
        ("画像の処理", 5),
        ("レポートの生成", 2),
    ]

    threads = []
    # 各タスクに対してスレッドを作成
    for name, duration in tasks:
        # targetに関数を、argsに関数の引数を指定
        thread = threading.Thread(target=task_runner, args=(name, duration))
        threads.append(thread)
        thread.start() # スレッドを開始

    print(f"[{time.strftime('%H:%M:%S')}] メインプログラム: 全てのタスクを開始しました。完了を待ちます。")

    # 全てのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

    print(f"[{time.strftime('%H:%M:%S')}] メインプログラム: 全てのタスクが完了しました。")