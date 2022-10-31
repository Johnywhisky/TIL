# Sync & Async (동기와 비동기)

## Blocking과 Non-Blocking

### CPU Bound
프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한되는 것을 의미하며 정말 복잡한 수학 수식을 계산할 때 실행 속도가 느려지는 것도 cpu bound의 하나이다.

``` python
def cpu_bound():
	ans = 0
	for i in range(100):
    	ans += i
    	for j in range(100):
        	ans += j
        	for k in range(100):
            	ans += k
    return ans

if __name__ == "__main__":
	print(cpu_bound()) # 49999950
```

### I/O Bound
프로그램이 실행될 때 속도가 I/O에 의해 제한됨을 의미하며 사용자 액션에 의한 속도 뿐만 아니라 컴퓨터와 컴퓨터 간의 통신에도 발생 -> Network I/O Bound도 여기에 포함된다.

``` python
import requests

def io_bound():
	res = requests.get("https://google.com") # Network bound 발생

    return res

if __name__ == "__main__":
	print(io_bound())
```

### Blocking
Bound에 의해 코드가 멈추게 되는 현상을 의미한다.

## Sync(동기)와 Async(비동기)
### Sync
코드가 동기적으로 동작한다는 것은 작성된 순서대로 수행됨을 의미한다.
``` python
import time

def delivery(mealtime):
        time.sleep(mealtime)

def main():
    delivery(5)
    delivery(3)
	delivery(7) # 함수 사이 사이에 I/O bound 발생 -> Blocking programming

if __name__ == "__main__":
	s = time.time()
    main()
    print(time.time() - s) # => 약 15.x초 소요
```

### Async
코드가 비동기적으로 동작한다는 것은 동시에 수행됨을 의미한다. -> 동시성 프로그래밍

``` python
import time, asyncio

async def delivery(mealtime):
        await asyncio.sleep(mealtime)

async def main():
        await asyncio.gather(
                delivery(5),
                delivery(3),
                delivery(7)
        ) # 함수 동시 실행 -> Bound 발생 X -> Non-blocking programming

if __name__ == "__main__":
        s = time.time()
        asyncio.run(main())
        print(time.time() - s) # => 약 7.x초 소요
```

## 코루틴과 제너레이터
### Sub-routine
서브루틴이란 하나의 진입점과 하나의 탈출점이 있는 루틴(예를 들어 함수)
``` python
import time

def delivery(mealtime): # <- 진입점
	time.sleep(mealtime)
    return # <- 탈출점
```

### coroutine
코루틴이란 다양한 진입점과 다양한 탈출점이 있는 루틴을 의미. 파이선에서는 async-await로 구현되어있는 함수를 코루틴으로 정의한다. `await`는 항상 `async` 함수 내에서 사용되어야 하며 또한 awaitable object와 함께 사용되야 한다.

``` python
import time, asyncio

# coroutine
async def delivery(mealtime): # <- 진입점
	await asyncio.sleep(mealtime) # <- 진입점이자 탈출점
    return # <- 탈출점

# Sub-routine
async def main(): # <- 진입점
	await asyncio.gather(
		delivery(5),
        delivery(3),
        delivery(7)
	)
    return # <- 탈출점

if __name__ == "__main__":
	# main routine 진입점
    s = time.time()
    asyncio.run(main())
    print(time.time() - s) # => 약 7.x초 소요
    # main routine 탈출점
```

## Awaitable Object
어웨이터블 객체에는 코루틴, 테스크, 퓨처가 있다.

### 테스크(Task)
테스크는 코루틴을 동시에 `예약`하는데 사용된다.
``` python
import asyncio

async def nested():
	return 42
	
async def main():
	task = asyncio.create_task(nested())

	await task

if __name__ == "__main__":
	asyncio.run(main())
```

### 퓨처(Future)
비동기 연산의 최종 결과를 나타내는 특별한 저수준 어웨이터블 객체이다. 다른 스레드 또는 프로세스에서 작동 중인 코루틴 함수가 해결될 때까지 기다리는 존재이다.

## 비동기 함수 활용
### Crawler
``` python
import requests, asyncio, aiohttp

async def fetcher(session, url):
	async with session.get(url) as res:
		return await res.text()

async def main():
	urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

	async with aiohttp.ClientSession() as session:
		res = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # 동시에 세 사이트에 request 요청을 수행함
		print(res)

if __name__ == "__main__":
	asyncio.run(main())
```

### 코루틴(async func)은 멀티 스레드이다?
답은 아니다. 코루틴은 단일 스레드에서 동작한다.