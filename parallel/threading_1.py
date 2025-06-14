import threading
import time


def write_mail(number):
    print(f"書き込み({number})番目：こんにちは")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：げんきですか？")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：さようなら")
    time.sleep(0.03)

def send_mail(number):
    print(f"送付({number}番目)")
    time.sleep(5)

def check_response(number):
    hoge=0
    # 無駄な計算
    for i in range(1, 100000000):
        hoge += i/3 + i/5 + i/7 + i/9 + i/11
    print(f"確認OK({number}番目)")

def task(thread_num):
    write_mail(thread_num)
    send_mail(thread_num)
    check_response(thread_num)

if __name__ == '__main__':
    start_time=time.time()
    t1 = threading.Thread(target=task, args=(1,))# 引数を与える時はこんな感じで
    t2 = threading.Thread(target=task, args=(2,))
    t3 = threading.Thread(target=task, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(f"かかった時間：{time.time()-start_time}s")
