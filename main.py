import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, registration, profile, create_workout, get_workouts, delete_workout
from database.create import create

import config

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.TOKEN)

    dp.include_routers(start.router, registration.router, profile.router, create_workout.router, get_workouts.router, delete_workout.router)
    
    await dp.start_polling(bot)
    
asyncio.run(create())
asyncio.run(main())