from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='📝Зарегистрироваться', callback_data='registration'))

    await message.answer('<b>Добро пожаловать!\nДля использования бота необходимо пройти регистрацию</b>',
                         reply_markup=builder.as_markup(),
                         parse_mode='html')