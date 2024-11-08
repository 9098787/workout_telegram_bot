from aiogram import Router, F
from aiogram.types import Message

from keyboards.keyboards import registration_builder, main_builder
from database.database import get_users

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    if message.from_user.id not in (await get_users()):
        await message.answer('<b>Добро пожаловать!\nДля использования бота необходимо пройти регистрацию</b>',
                            reply_markup=(await registration_builder()).as_markup(),
                            parse_mode='html')
    else:
        await message.answer('<b>Добро пожаловать!</b>',
                            reply_markup=(await main_builder()).as_markup(resize_keyboard=True),
                            parse_mode='html',
                            )