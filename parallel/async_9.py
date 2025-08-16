# 分かりやすい。

# 参考④：
# https://zenn.dev/iharuoru/articles/45dedf1a1b8352
import asyncio

async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def goodbye():
    print('you say,')
    await asyncio.sleep(2) # 2秒かかる
    print('goodbye')

async def main():
    goodbye_task = asyncio.create_task(goodbye())
    hello_task = asyncio.create_task(hello())
    await goodbye_task
    await hello_task

# >>> asyncio.run(main())
# you say,
# I say,
# hello
# goodbye