# pip install aiohttp

import asyncio
import aiohttp
from time import time


# План
# 1 Asyncio фреймворк для создания событийных циклов
# 2 Пример простой асинхронной программы времен Python 3.4
# 3 Синтаксис Async/await на замену @acyncio.coroutine и yield from
# 4 Пример асинхронного скачивания файлов


# @asyncio.coroutine
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.2)


# @asyncio.coroutine
async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        await asyncio.sleep(1)


# @asyncio.coroutine
async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())
