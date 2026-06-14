import asyncio

async def reading(name: str, delay: float) -> str:
    print(f"The reading of the {name} has started ")

    await asyncio.sleep(delay)
    return f" the reading of the {name} has finished !"

async def main():
    results = await asyncio.gather(
        reading("book1", 2),
        reading("book2", 4),
        reading("book3", 3),
    )
    print(results)

asyncio.run(main())


