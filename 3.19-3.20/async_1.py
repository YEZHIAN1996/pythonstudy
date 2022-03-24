import time
import random
import asyncio

async def a():
    for i in range(10):
        print(i, 'a')
        await asyncio.sleep(random.random() * 2)
    return 'return a'

async def b():
    for i in range(10):
        print(i, 'b')
        await asyncio.sleep(random.random() * 2)
    return 'return b'
async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result)
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)