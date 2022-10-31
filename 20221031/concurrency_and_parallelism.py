"""Concurrency Programming
동시성 프로그래밍 기법과 결과 비교
"""
import time

"Sync Programming"
import requests


def sync_fetcher(session: requests.Session, url: str) -> str:
    with session.get(url) as res:
        return res.text


def sync_crawler():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    with requests.Session() as session:
        res = [sync_fetcher(session, url) for url in urls]

    return res


"Concurrency - Coroutine"
import aiohttp, asyncio


async def fetcher(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as res:
        return await res.text()


async def coroutine_crawler():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        # 동시에 세 사이트에 request 요청을 수행함
        # 단일 스레드 내 비동기 동작
        res = await asyncio.gather(*[fetcher(session, url) for url in urls])

        return res


"Parallelism - Multi Threading"
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor


def multi_fetcher(params: Tuple[requests.Session, str]) -> str:
    session, url = params
    with session.get(url) as res:
        return res.text


def multi_crawler():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    executor = ThreadPoolExecutor(max_workers=3)
    # max_workers는 사용할 Thread 개수

    with requests.Session() as session:
        params = [(session, url) for url in urls]

        # 다중 스레드를 만들어 비동기 처리 하는 코드
        res = list(executor.map(multi_fetcher, params))

        return res


if __name__ == "__main__":
    s = time.time()
    sync_crawler()
    print(f"sync crawler execution time: {time.time() - s} s")
    # sync crawler execution time: 1.3129539489746094 s

    s = time.time()
    asyncio.run(coroutine_crawler())
    print(f"coroutine crawler execution time: {time.time() - s} s")
    # coroutine crawler execution time: 0.8310630321502686 s

    s = time.time()
    multi_crawler()
    print(f"multi-thread crawler execution time: {time.time() - s} s")
    # multi-thread crawler execution time: 0.9231858253479004 s
