import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check(item):
    print(f"Checking for {item}")
    time.sleep(2)
    return f"{item} = 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check, "masala chai")
        print(result)

asyncio.run(main())