# 参考②：
# https://techgrowup.net/python-asyncio-2/#toc4


import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("こんにちは！")

async def main():
    task = asyncio.create_task(say_hello())
    print("タスクをスケジュールしました")
    await task

asyncio.run(main())