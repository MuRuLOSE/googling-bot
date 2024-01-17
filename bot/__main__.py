import logging
import sys
import asyncio

from .entrypoint import main

async def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await main()

if __name__ == '__main__':
    asyncio.run(run())
