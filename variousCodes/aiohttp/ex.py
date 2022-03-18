import asyncio
import time


async def nums():
    for i in range(5):
        await asyncio.sleep(2)
        print(i)


start_time = time.time()
end_time = time.time()
print(f'Start Time: {start_time}')
asyncio.run(nums())
print(f'End Time: {end_time}')