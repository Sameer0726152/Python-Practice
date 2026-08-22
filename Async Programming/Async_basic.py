import asyncio
async def brew(name):
    print(f"Start brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready!")
async def main():
    await asyncio.gather(brew("Masala Chai"), brew("Ginger Chai"), brew("Green Tea"))
asyncio.run(main())