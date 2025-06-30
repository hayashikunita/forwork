import asyncio

async def process_data(data):
    print(f"処理中: {data}")
    await asyncio.sleep(1)
    print(f"処理完了: {data}")

async def main():
    data_list = [1, 2, 3, 4, 5]
    await asyncio.gather(*(process_data(data) for data in data_list))

asyncio.run(main())