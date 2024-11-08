from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from states.registration import Registration
from app.users import users, auth
from database.database import create_user
from keyboards.keyboards import main_builder

router = Router()

@router.callback_query(F.data == 'registration')
async def registration_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.name)
    await callback.message.answer('<b>Введите ваше имя</b>', parse_mode='html')

@router.message(Registration.name)
async def registration_enter_name(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await state.set_state(Registration.surname)
    await message.answer('<b>Введите вашу фамилию</b>', parse_mode='html')

@router.message(Registration.surname)
async def registration_enter_surname(message: Message, state: FSMContext):
    await state.update_data({'surname': message.text})
    await state.set_state(Registration.patronymic)
    await message.answer('<b>Введите ваше отчество</b>', parse_mode='html')

@router.message(Registration.patronymic)
async def registration_enter_patronymic(message: Message, state: FSMContext):
    await state.update_data({'patronymic': message.text})
    await state.set_state(Registration.email)
    await message.answer('<b>Введите вашу почту</b>', parse_mode='html')

@router.message(Registration.email)
async def registration_enter_email(message: Message, state: FSMContext):
    await state.update_data({'email': message.text})
    await state.set_state(Registration.password)
    await message.answer('<b>Придумайте пароль</b>', parse_mode='html')

@router.message(Registration.password)
async def registration_enter_password(message: Message, state: FSMContext):
    data = await state.get_data()
    data['password'] = message.text
    await state.clear()

    registration_response = await users.registration(data)
    if registration_response:
        if 'response' in registration_response:
            auth_response = await auth.auth(data['email'], data['password'])
            if auth_response:
                if 'access_token' in auth_response:
                    await create_user(message.from_user.id, auth_response['access_token'])
                    await users.become_trainer(auth_response['access_token'])
                    await message.answer('<b>Вы успешно зарегистрировались!</b>', 
                                         reply_markup=(await main_builder()).as_markup(resize_keyboard=True),
                                         parse_mode='html')
                else:
                    await message.answer(f"<b>Произошла ошибка!\nДетали:</b>\n<code>{registration_response}</code>",
                                 parse_mode='html')
            else:
                await message.answer('<b>Произошла непредвиденная ошибка!\nОбратитесь к администратору</b>', parse_mode='html')
        else:
            await message.answer(f"<b>Произошла ошибка!\nДетали:</b>\n<code>{registration_response}</code>",
                                 parse_mode='html')
    else:
        await message.answer('<b>Произошла непредвиденная ошибка!\nОбратитесь к администратору</b>', parse_mode='html')