# 参考②：
# https://techgrowup.net/python-asyncio-2/#toc4


import asyncio  

async def greet():
    print("こんにちは！")
    await asyncio.sleep(1)
    print("非同期処理が完了しました！")  

asyncio.run(greet())
