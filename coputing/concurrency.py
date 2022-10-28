def cpu_bound():
    ans = 0
    for i in range(1000):
        ans += i
        for j in range(1000):
            ans += j
            for k in range(1000):
                ans += k
                # cpu bound 발생
    return ans


cpu_bound()

# ================================================== #
import requests


def io_bound():
    res = requests.get("https://google.com")
    # Network bound 발생
    return res


io_bound()

# ================================================== #
import time


def delivery(mealtime):
    time.sleep(mealtime)


def sync_main():
    # 함수 사이 사이에 I/O bound 발생 -> Blocking programming
    delivery(5)
    delivery(3)
    delivery(7)


s = time.time()
sync_main()
print(time.time() - s)

# ================================================== #
import asyncio


async def delivery(mealtime):  # <- 진입점
    await asyncio.sleep(mealtime)  # <- 진입점이자 탈출점
    # <- 탈출점


async def async_main():  # <- 진입점
    # 함수 동시 실행 -> Bound 발생 X -> Non-blocking programming
    await asyncio.gather(delivery(5), delivery(3), delivery(7))
    # <- 탈출점


s = time.time()
asyncio.run(async_main())
print(time.time() - s)  # => 약 7.x초 소요


# ================================================== #
async def nested():
    return 42


async def task_coroutine():
    task = asyncio.create_task(nested())

    await task


asyncio.run(task_coroutine())

# ================================================== #
import aiohttp


async def fetcher(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as res:
        return await res.text()


async def async_crawler():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        # 동시에 세 사이트에 request 요청을 수행함
        res = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(res)


if __name__ == "__main__":
    asyncio.run(async_crawler())
