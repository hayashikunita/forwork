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
    await asyncio.gather(goodbye(), hello(), hello()) # タスクも同様


# # >>> asyncio.run(main()>>> asyncio.run(main())
# you say,
# I say,
# I say,
# hello
# hello
# goodbye