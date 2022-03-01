
import asyncio


async def loop_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

res = loop_numbers()
asyncio.run(res)
