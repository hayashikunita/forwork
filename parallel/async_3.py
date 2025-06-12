import asyncio

async def task_1():
    print("タスク1開始")
    await asyncio.sleep(2)
    print("タスク1終了")

async def task_2():
    print("タスク2開始")
    await asyncio.sleep(1)
    print("タスク2終了")

async def main():
    await asyncio.gather(task_1(), task_2())

    # task_1() →
    # task_2() →

asyncio.run(main())