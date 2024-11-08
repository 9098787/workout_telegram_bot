from aiogram import Router, F
from aiogram.types import Message

from app.workouts import workouts
from database.database import get_token
from keyboards.keyboards import delete_workout_builder

router = Router()

@router.message(F.text == '🏃‍♂️Мои тренировки')
async def get_workouts(message: Message):
    user_workouts = await workouts.get_workouts(await get_token(message.from_user.id))
    if user_workouts:
        if user_workouts['items']:
            for workout in user_workouts['items']:
                await message.answer(f"<b>ℹ️ID: {workout['id']}\n\n🪪Название тренировки: <code>{workout['title']}</code>\n📝Описание:\n<code>{workout['description']}</code></b>",
                                     reply_markup=(await delete_workout_builder(workout['id'])).as_markup(),
                                      parse_mode='html')
        else:
            await message.answer('<b>У вас нет добавленных тренировок</b>', parse_mode='html')
    else:
        await message.answer('<b>Произошла непредвиденная ошибка!\nОбратитесь к администратору</b>', parse_mode='html')