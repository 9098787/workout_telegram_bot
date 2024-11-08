from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

async def registration_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='📝Зарегистрироваться', callback_data='registration'))
    return builder

async def main_builder() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text='👤Профиль'))
    builder.add(KeyboardButton(text='🏃‍♂️Мои тренировки'))
    builder.add(KeyboardButton(text='➕Создать тренировку'))
    builder.add(KeyboardButton(text='💬Помощь'))
    builder.adjust(1, 2, 1)
    return builder

async def delete_workout_builder(workout_id: str) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='🗑Удалить', callback_data=f'delete|{workout_id}'))
    return builder