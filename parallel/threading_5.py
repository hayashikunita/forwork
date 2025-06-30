# https://qiita.com/ryo0819/items/4fd9e6c5e95bb18c6794

import threading
import time

def task(name, delay):
    """
    スレッドで実行するタスク
    """
    print(f"スレッド {name}: 開始")
    for i in range(3):
        print(f"スレッド {name}: 処理中 ({i+1}/3)")
        time.sleep(delay)
    print(f"スレッド {name}: 終了")

if __name__ == "__main__":
    print("メインスレッド: 開始")

    # スレッド1の作成と開始
    thread1 = threading.Thread(target=task, args=("A", 1), name="Thread-A")
    thread1.start()

    # スレッド2の作成と開始
    thread2 = threading.Thread(target=task, args=("B", 0.5), name="Thread-B")
    thread2.start()

    # スレッドが終了するのを待つ
    thread1.join()
    thread2.join()

    print("メインスレッド: 全てのスレッドが終了しました")
    print("メインスレッド: 終了")
