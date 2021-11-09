from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, CallbackQuery

import keyboards.inline.admin_keyboards as akb
from data.config import ADMINS
from loader import dp, _
from states.states import SetPermissions
from utils.db_api import database
from utils.db_api.database import User

db = database.DBCommands()


def print_users(list_users):
    text = ''
    for user in list_users:
        text += f'{user.user_id} - {user.full_name}\n' \
                f'● <b>Email:</b> {user.email}\n' \
                f'● <b>Tel:</b> {user.phone}\n'
    return text


@dp.message_handler(Command('admin'), user_id=ADMINS)
@dp.message_handler(Text('Панель администратора'), user_id=ADMINS)
@dp.message_handler(Text('Admin panel'), user_id=ADMINS)
@dp.message_handler(Text('Панель адміністратора'), user_id=ADMINS)
async def show_admin_panel(message: Message):
    await message.answer(text=_('Меню администратора'), reply_markup=akb.get_markup_admin_main())


@dp.callback_query_handler(text_contains='back_to_admin_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(akb.get_markup_admin_main())


# статистика бота
@dp.callback_query_handler(text_contains='bot_statistics')
async def show_bot_statistics(call: CallbackQuery):
    total_users = await db.count_users()
    is_admin_users = await User.query.where(User.is_admin is True).gino.all()
    is_manager_users = await User.query.where(User.is_manager is True).gino.all()
    await call.message.answer(text=f'<strong>{_("Колличество пользователей бота")}:</strong> <i>{total_users}</i>\n')
    await call.message.answer(text=f'<b>{_("Администраторы бота")}:</b>\n'
                                   f'{print_users(is_admin_users)}')
    await call.message.answer(text=f'<b>{_("Менеджеры бота")}:</b>\n'
                                   f'{print_users(is_manager_users)}',
                              reply_markup=akb.get_markup_show_all_users())


@dp.callback_query_handler(text_contains='show_all_user')
async def show_all_user(call: CallbackQuery):
    users = await db.get_all_users()
    text = f''
    for user in users:
        text += f'<strong>{_("ИД клиента")}: {user.user_id}\n</strong>' \
                f'    ● <b>{_("Имя")}: </b>{user.full_name}\n' \
                f'    ● <b>{_("Компания")}: </b>{user.company_name}\n' \
                f'    ● <b>{_("Телефон")}.: </b>{user.phone}\n' \
                f'    ● <b>Email: </b>{user.email}\n'
    await call.message.answer(text=text)


# Установка прав администратора
@dp.callback_query_handler(text_contains='add_admin')
async def get_id_admin(call: CallbackQuery):
    await call.message.answer(_('Пришлите ИД пользователя.'))
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
        await message.answer(f'{_("Пользователь")} {user_in_db.full_name}\n{_("назначен администратором")}.')
    else:
        await message.answer(f'{_("Что - то пошло не так")}\n'
                             f'{_("пользователь с ИД")} {user_id} {_("не зарегистрирован")}\n'
                             f'{_("или введен не корректный ИД")}')
    await state.reset_state()


# Установка прав менеджера
@dp.callback_query_handler(text_contains='add_manager')
async def get_id_manager(call: CallbackQuery):
    await call.message.answer(_('Пришлите ИД пользователя.'))
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
        await message.answer(f'{_("Пользователь")} {user_in_db.full_name}\n{_("назначен менеджером")}.')
    else:
        await message.answer(f'{_("Что - то пошло не так")}\n'
                             f'{_("пользователь с ИД")} {user_id} {_("не зарегистрирован")}\n'
                             f'{_("или введен не корректный ИД")}')
    await state.reset_state()
