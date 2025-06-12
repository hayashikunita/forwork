import asyncio  

async def greet():
    print("こんにちは！")
    await asyncio.sleep(1)
    print("非同期処理が完了しました！")  

asyncio.run(greet())
