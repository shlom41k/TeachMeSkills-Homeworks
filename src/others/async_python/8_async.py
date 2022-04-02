import requests
from time import time

import asyncio
import aiohttp


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    folder = "pictures/"
    filename = folder + response.url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    t0 = time()
    url = "https://loremflickr.com/320/240"

    for i in range(10):
        write_file(get_file(url))
        print(f"File {i + 1} downloaded successfully")

    print(f"Total time: {time() - t0}")


# if __name__ == "__main__":
#     main()


#########################################################################




def write_image(data):
    folder = "pictures/"
    filename = folder + "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)
    print(f"File '{filename}' downloaded successfully")


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    t0 = time()
    asyncio.run(main2())
    print(f"Total time: {time() - t0}")

