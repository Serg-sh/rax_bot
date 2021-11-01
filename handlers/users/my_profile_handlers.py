import bcrypt
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

import keyboards.inline.user_keyboards as ukb
from loader import dp
from states.states import SetUserProfile
from utils.db_api import database

db = database.DBCommands()


@dp.callback_query_handler(text_contains='my_profile')
@dp.message_handler(Text('Мой профиль'))
async def show_my_profile(message: Message):
    user_id = int(message.from_user.id)
    user = await db.get_user(user_id)
    await message.answer(text=f'ИД: <b>{user_id}</b>\n'
                              f'Имя: <b>{user.full_name}</b>\n'
                              f'Язык: <b>{user.languages}</b>\n'
                              f'Телефон: <b>{(user.phone if user.phone else "Не указан")}</b>\n'
                              f'Email: <b>{(user.email if user.email else "Не указан")}</b>\n'
                              f'Компания: <b>{(user.company_name if user.company_name else "Не указана")}</b>\n'
                              f'Пароль: <b>{("Установлен" if user.password else "Неустановлен")}</b>\n',
                         reply_markup=ukb.markup_my_profile)


async def check_user_data(user_id):
    user = await db.get_user(user_id)
    return not user.phone or not user.email or not user.company_name


# Изменение телефона в профиле
@dp.callback_query_handler(text_contains='get_user_phone')
async def get_user_phone(call: CallbackQuery):
    await call.message.answer(text='Пришлите Ваш контактный номер телефона.')
    await SetUserProfile.GetPhone.set()


@dp.message_handler(state=SetUserProfile.GetPhone)
async def set_user_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.reset_state()
    await db.set_phone(phone=phone)
    await message.answer(text=f'Телефон {phone} успешно записан в Ваш профиль')
    await show_my_profile(message)


# Изменение языка
@dp.callback_query_handler(text_contains='get_user_language')
async def get_user_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text='<b>Выберите язык</b>', reply_markup=ukb.markup_languages)


@dp.callback_query_handler(text_contains='ru_language')
async def set_user_lang_ru(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await db.set_language(language='ru')



@dp.callback_query_handler(text_contains='uk_language')
async def set_user_lang_uk(call: CallbackQuery):
    pass


@dp.callback_query_handler(text_contains='en_language')
async def set_user_lang_en(call: CallbackQuery):
    pass


# Изменение email в профиле
@dp.callback_query_handler(text_contains='get_user_email')
async def get_user_email(call: CallbackQuery):
    await call.message.answer(text='Пришлите Ваш email.')
    await SetUserProfile.GetEmail.set()


@dp.message_handler(state=SetUserProfile.GetEmail)
async def set_user_email(message: Message, state: FSMContext):
    email = message.text
    await state.reset_state()
    await db.set_email(email=email)
    await message.answer(text=f'Email {email} успешно записан в Ваш профиль')
    await show_my_profile(message)


# Изменение названия компании в профиле
@dp.callback_query_handler(text_contains='get_user_company')
async def get_user_company(call: CallbackQuery):
    await call.message.answer(text='Пришлите название Вашей компании.')
    await SetUserProfile.GetCompany.set()


@dp.message_handler(state=SetUserProfile.GetCompany)
async def set_user_company(message: Message, state: FSMContext):
    company_name = message.text
    await state.reset_state()
    await db.set_company_name(company_name=company_name)
    await message.answer(text=f'Компания {company_name} успешно записана в Ваш профиль')
    await show_my_profile(message)


# Изменение пароля в профиле
@dp.callback_query_handler(text_contains='get_user_password')
async def get_user_password(call: CallbackQuery):
    await call.message.answer(text='Пришлите Ваш пароль.')
    await SetUserProfile.GetPassword.set()


@dp.message_handler(state=SetUserProfile.GetPassword)
async def set_user_password(message: Message, state: FSMContext):
    await state.reset_state()
    password = message.text
    # шифрование пароля (хеш пароля + соль)
    hash_and_salt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # запись пароля в базу
    await db.set_password(password=hash_and_salt)

    await message.answer(text=f"Пароль успешно изменен")
    # для примера проверки пароля взят input()
    # user = await db.get_user(types.User.get_current().id)
    # print('Пароль:')
    # valid = bcrypt.checkpw(input().encode(), user.password)
    # print(valid)

    await show_my_profile(message)
