import asyncio
import time
import threading
i = 0
def logger():
    global i
    while i < 5:
        time.sleep(1)
        print("Logging data")
        i += 1
async def main():
    await asyncio.sleep(3)
    print("All tasks done")
threading.Thread(target = logger).start()
asyncio.run(main())