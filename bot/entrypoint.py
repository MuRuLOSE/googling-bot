'''Entrypoint for bot. Just dispatcher.'''

import asyncio
from os import getenv
from dotenv import load_dotenv
from .utils import PATH

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode

from .handlers import standart, search

env = load_dotenv(PATH + '.env')

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(
        standart.router,
        search.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())