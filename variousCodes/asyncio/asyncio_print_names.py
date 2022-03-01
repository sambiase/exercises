import asyncio


async def names():
    times = ['fla', 'bota', 'flu']
    for i in times:
        print(f'Time: {i}')
        await asyncio.sleep(3)


print(asyncio.run(names()))
