import asyncio

async def print_list():
    lista = [a**2 for a in range(5)]
    for i in lista:
        print(i)
        await asyncio.sleep(2)

asyncio.run(print_list())