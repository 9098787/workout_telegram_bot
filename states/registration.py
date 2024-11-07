from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    email = State()
    password = State()