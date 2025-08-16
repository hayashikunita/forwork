# 参考③：
# https://qiita.com/shota-s123/items/36e365d99c7413f60826

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def execute():
    task_a = asyncio.create_task(factorial('A', 2))
    task_b = asyncio.create_task(factorial('B', 3))
    task_c = asyncio.create_task(factorial('C', 4))

    L = []
    L.append(await task_a)
    L.append(await task_b)
    L.append(await task_c)

    print(L)

asyncio.run(execute())
