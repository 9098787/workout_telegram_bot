from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.workouts import workouts
from database.database import get_token

router = Router()

@router.callback_query(F.data.startswith('delete|'))
async def delete_workout(callback: CallbackQuery):
    workout_id = callback.data.split('|')[1]
    delete_workout_response = await workouts.delete_workout(await get_token(callback.from_user.id), workout_id)

    if delete_workout_response:
        await callback.message.answer('<b>Тренировка успешно удалена!</b>', parse_mode='html')
    else:
        await callback.message.answer('<b>Произошла непредвиденная ошибка!\nОбратитесь к администратору</b>', parse_mode='html')