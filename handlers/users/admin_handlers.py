from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, CallbackQuery

import keyboards.inline.admin_keyboards as akb
from data.config import ADMINS
from loader import dp
from states.states import SetPermissions
from utils.db_api import database
from utils.db_api.database import User

db = database.DBCommands()


def print_users(list_users):
    text = ''
    for user in list_users:
        text += f'{user.user_id} - {user.full_name}\n' \
                f'● Email: {user.email}\n' \
                f'● Tel: {user.phone}\n'
    return text


@dp.message_handler(Text('Панель администратора'), user_id=ADMINS)
async def show_admin_panel(message: Message):
    await message.answer(text='Меню администратора', reply_markup=akb.markup_admin_main)


@dp.message_handler(Command('admin'), user_id=ADMINS)
async def show_ap(message: Message):
    await show_admin_panel(message)


@dp.callback_query_handler(text_contains='back_to_admin_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(akb.markup_admin_main)


# статистика бота
@dp.callback_query_handler(text_contains='bot_statistics')
async def show_bot_statistics(call: CallbackQuery):
    total_users = await db.count_users()
    is_admin_users = await User.query.where(User.is_admin == True).gino.all()
    is_manager_users = await User.query.where(User.is_manager == True).gino.all()
    await call.message.answer(f'<strong>Колличество пользователей бота:</strong> <i>{total_users}</i>\n')
    await call.message.answer(f'<b>Администраторы бота:</b>\n'
                              f'{print_users(is_admin_users)}')
    await call.message.answer(f'<b>Менеджеры бота:</b>\n'
                              f'{print_users(is_manager_users)}')


# Установка прав администратора
@dp.callback_query_handler(text_contains='add_admin')
async def get_id_admin(call: CallbackQuery):
    await call.message.answer('Пришлите ИД пользователя.')
    await SetPermissions.GetAdminId.set()


@dp.message_handler(state=SetPermissions.GetAdminId)
async def set_admin_permissions(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except ValueError:
        user_id = None
    user_in_db = await db.get_user(user_id)
    if user_in_db:
        await user_in_db.update(is_admin=True).apply()
        await message.answer(f'Пользовать {user_in_db.full_name}\nназначен администратором.')
    else:
        await message.answer(f'Что-то пошло не так\n'
                             f'пользователь с ИД {user_id} не зарегистрирован\n'
                             f'или введен не корректный ИД')
    await state.reset_state()


# Установка прав администратора
@dp.callback_query_handler(text_contains='add_manager')
async def get_id_manager(call: CallbackQuery):
    await call.message.answer('Пришлите ИД пользователя.')
    await SetPermissions.GetManagerId.set()


@dp.message_handler(state=SetPermissions.GetManagerId)
async def set_manager_permissions(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except ValueError:
        user_id = None
    user_in_db = await db.get_user(user_id)
    if user_in_db:
        await user_in_db.update(is_manager=True).apply()
        await message.answer(f'Пользовать {user_in_db.full_name}\nназначен менеджером.')
    else:
        await message.answer(f'Что-то пошло не так\n'
                             f'пользователь с ИД {user_id} не зарегистрирован\n'
                             f'или введен не корректный ИД')
    await state.reset_state()
