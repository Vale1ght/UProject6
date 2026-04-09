import asyncio
import logging

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config_reader import config
from handlers import get_handlers_router


async def main() -> None:
    bot = Bot(token=config.bot_token, 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    main_router = get_handlers_router()
    dp.include_router(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())