# 参考③：
# https://qiita.com/shota-s123/items/36e365d99c7413f60826

import asyncio

async def say_after(delay, what):
    print(f'before_sleep: {what}')
    await asyncio.sleep(delay)
    print(what)

async def execute():
    print(f'started at {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'ended at {time.strftime("%X")}')

asyncio.run(execute())
