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
    await goodbye()
    await hello()

# >>> asyncio.run(main())
# you say,
# goodbye
# I say,
# hello