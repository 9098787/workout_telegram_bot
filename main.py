import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, registration, profile
from database.create import create

import config

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.TOKEN)

    dp.include_routers(start.router, registration.router, profile.router)
    
    await dp.start_polling(bot)
    
asyncio.run(create())
asyncio.run(main())