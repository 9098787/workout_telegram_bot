from aiogram import Router, F
from aiogram.types import Message

from app.users import users
from database.database import get_token

router = Router()

@router.message(F.text == '👤Профиль')
async def profile(message: Message):
    profile = await users.me(await get_token(message.from_user.id))
    await message.answer(f"<b>👤Профиль:\n\n🪪ФИО: <code>{profile['surname']} {profile['name']} {profile['patronymic']}</code>\n📬Email: {profile['email']}</b>", parse_mode='html')