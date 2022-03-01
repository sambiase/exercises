import asyncio


async def main():
    print('This is first line')
    await asyncio.sleep(3)
    print('This is second line')
    await asyncio.sleep(3)


res = main()
asyncio.run(res)
