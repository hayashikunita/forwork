import threading
import time

# 複数のスレッドから共有されるカウンター
counter = 0
# ロックオブジェクトを作成
lock = threading.Lock()

def increment_counter():
    """
    カウンターを10万回インクリメントする
    """
    global counter
    for _ in range(100000):
        # with文を使うと、ブロックを抜ける際に自動でロックが解放される
        with lock:
            counter += 1

# --- メインの処理 ---
if __name__ == "__main__":
    threads = []
    num_threads = 10

    # 5つのスレッドを作成
    for i in range(num_threads):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    # 全てのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

    print(f"期待されるカウンターの値: {100000 * num_threads}")
    print(f"実際のカウンターの値: {counter}")
    
    # Lockを使わない場合の値と比較（コメントを外して試してみてください）
    # if counter == 100000 * num_threads:
    #     print("Lockが正常に機能し、データは保護されました。")
    # else:
    #     print("Lockがないため、競合状態が発生し、値が正しくありません。")