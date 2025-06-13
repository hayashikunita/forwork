# 参考①：
# https://qiita.com/Toyo_m/items/992b0dcf765ad3082d0b

import asyncio
import time

def write_mail(number):
    print(f"書き込み({number}番目)：こんにちは")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：げんきですか？")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：さようなら")
    time.sleep(0.03)

# 非同期処理を行う関数は、async と付けなければならない
async def send_mail(number):
    print(f"送付({number}番目)")
    await asyncio.sleep(5)

def check_response(number):
    hoge=0
    # 無駄な計算
    for i in range(1, 100000000):
        hoge += i/3 + i/5 + i/7 + i/9 + i/11
    print(f"確認OK({number}番目)")

async def task():
    
    # 書類書き込み（同期処理）
    write_mail(1)
    write_mail(2)
    write_mail(3)

    # メール送付＆待ち(非同期処理) <- ここだけ非同期処理
    await asyncio.gather( # 処理が全部終わるまで待つ
        send_mail(1),
        send_mail(2),
        send_mail(3)
    )

    # 書類チェック（同期処理）
    check_response(1)
    check_response(2)
    check_response(3)


if __name__ == '__main__':
    start_time=time.time()
    asyncio.run(task())
    print(f"かかった時間：{time.time()-start_time}s")
