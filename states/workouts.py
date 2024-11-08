from aiogram.fsm.state import StatesGroup, State


class CreateWorkout(StatesGroup):
    title = State()
    description = State()