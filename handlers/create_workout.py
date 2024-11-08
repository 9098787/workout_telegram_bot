from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.workouts import CreateWorkout
from app.workouts import workouts
from database.database import get_token

router = Router()

@router.message(F.text == '➕Создать тренировку')
async def create_workout(message: Message, state: FSMContext):
    await state.set_state(CreateWorkout.title)
    await message.answer('<b>Введите название тренировки</b>', parse_mode='html')

@router.message(CreateWorkout.title)
async def create_workout_title(message: Message, state: FSMContext):
    await state.update_data({'title': message.text})
    await state.set_state(CreateWorkout.description)
    await message.answer('<b>Введите описание тренировки</b>', parse_mode='html')

@router.message(CreateWorkout.description)
async def create_workout_title(message: Message, state: FSMContext):
    data = await state.get_data()
    data['description'] = message.text
    await state.clear()

    create_workout_response = await workouts.create_workout(await get_token(message.from_user.id), data)
    if create_workout_response:
        await message.answer('<b>Тренировка успешно создана!</b>', parse_mode='html')
    else:
        await message.answer('<b>Произошла непредвиденная ошибка!\nОбратитесь к администратору</b>', parse_mode='html')