from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboard.inline.admin_kb import InlineKeyboardAdmin
from states.states import SetPermissions
from utils.database.models import User
from utils.database.queryes import UserDBQuery
from loader import _

db = UserDBQuery()
admin_router = Router()
admin_kb = InlineKeyboardAdmin()


def print_users(list_users):
    text = ''
    for user in list_users:
        text += f'{user.user_id} - {user.full_name}\n' \
                f'● <b>Email:</b> {user.email}\n' \
                f'● <b>Tel:</b> {user.phone}\n'
    return text


@admin_router.message(Command('admin'))
@admin_router.message(F.text == 'Admin panel')
@admin_router.message(F.text == 'Меню адміністратора')
async def show_admin_panel(message: Message):
    await message.answer(text=f"{_('Меню адміністратора')}",
                         reply_markup=admin_kb.get_markup_admin_main(),
                         parse_mode='HTML')


@admin_router.callback_query(F.data == 'back_to_admin_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=admin_kb.get_markup_admin_main())


# статистика бота
@admin_router.callback_query(F.data == 'bot_statistics')
async def show_bot_statistics(call: CallbackQuery):
    total_users = len(await db.get_all_users())
    is_admin_users = [user for user in await db.get_all_users() if user.is_admin]
    is_manager_users = [user for user in await db.get_all_users() if user.is_manager]
    await call.message.answer(text=f'<strong>{_("Кількість користувачів")}:</strong> <i>{total_users}</i>\n',
                              parse_mode='HTML')
    await call.message.answer(text=f'<b>{_("Адміністратори")}:</b>\n'
                                   f'{print_users(is_admin_users)}',
                              parse_mode='HTML')
    await call.message.answer(text=f'<b>{_("Менеджери")}:</b>\n'
                                   f'{print_users(is_manager_users)}',
                              reply_markup=admin_kb.get_markup_show_all_users(),
                              parse_mode='HTML')


@admin_router.callback_query(F.data == 'show_all_user')
async def show_all_user(call: CallbackQuery):
    users = await db.get_all_users()
    text = f''
    for user in [user for user in users if not user.is_admin and not not user.is_manager]:
        text += f'<strong>ID {_("клієнта")}: {user.user_id}\n</strong>' \
                f'    ● <b>{_("Імʼя")}: </b>{user.full_name}\n' \
                f'    ● <b>{_("Компанія")}: </b>{user.company_name}\n' \
                f'    ● <b>{_("Телефон")}.: </b>{user.phone}\n' \
                f'    ● <b>Email: </b>{user.email}\n'
    await call.message.answer(text=text,
                              reply_markup=admin_kb.get_markup_to_admin_menu(),
                              parse_mode='HTML')


# Установка прав администратора
@admin_router.callback_query(F.data == 'add_admin')
async def get_id_admin(call: CallbackQuery, state: FSMContext):
    await state.set_state(SetPermissions.GetAdminId)
    await call.message.answer(text=f"{_('Надішліть ID користувача')}",
                              parse_mode='HTML')


@admin_router.message(StateFilter(SetPermissions.GetAdminId))
async def set_admin_permissions(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except ValueError:
        user_id = None
    user: User = await db.get_user(user_id)
    await state.clear()
    if user:
        await db.update_user(user_id=user.user_id, is_admin=True)
        await message.answer(text=f'{_("Користувач")} {user.full_name} {_("id")}: {user.user_id}\n'
                                  f'{_("призначений адміністратором")}',
                             reply_markup=admin_kb.get_markup_to_admin_menu(),
                             parse_mode='HTML')
    else:
        await message.answer(text=f'{_("Користувач з ID")} {user_id} {_("не зареєстрований")},\n'
                                  f'{_("або ID не вірний")}',
                             reply_markup=admin_kb.get_markup_to_admin_menu(),
                             parse_mode='HTML')


# Установка прав менеджера
@admin_router.callback_query(F.data == 'add_manager')
async def get_id_manager(call: CallbackQuery, state: FSMContext):
    await state.set_state(SetPermissions.GetManagerId)
    await call.message.answer(text=f"{_('Надішліть ID користувача')}",
                              parse_mode='HTML')


@admin_router.message(StateFilter(SetPermissions.GetManagerId))
async def set_manager_permissions(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except ValueError:
        user_id = None
    user: User = await db.get_user(user_id)
    await state.clear()
    if user:
        await db.update_user(user_id=user.user_id, is_manager=True)
        await message.answer(text=f'{_("Користувач")} {user.full_name} {_("id")}: {user.user_id}\n'
                                  f'{_("призначений менеджером")}',
                             reply_markup=admin_kb.get_markup_to_admin_menu(),
                             parse_mode='HTML')
    else:
        await message.answer(text=f'{_("Користувач з ID")} {user_id} {_("не зареєстрований")},\n'
                                  f'{_("або ID не вірний")}',
                             reply_markup=admin_kb.get_markup_to_admin_menu(),
                             parse_mode='HTML')
