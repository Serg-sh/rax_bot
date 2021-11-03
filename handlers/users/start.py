from asyncio import sleep
from typing import List

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile, Message, ReplyKeyboardMarkup

from data.config import ADMINS
from handlers.users.my_profile_handlers import show_my_profile, check_user_data
from keyboards.default import main_menu as mmkb
from loader import dp, _
from utils.db_api import database

db = database.DBCommands()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logo_rax = InputFile('data/images/logo_rax.jpg')
    await message.answer_photo(photo=logo_rax, parse_mode='HTML')
    await sleep(0.1)
    await db.add_new_user()
    managers = await db.get_managers_user_id()
    admins = await db.get_admins_user_id()
    admins.extend(ADMINS)
    await message.answer(f'{_("Добрый День")}!  {message.from_user.full_name}!\n\n'
                         f'{_("ПРИВЕТСТВУЕМ ВАС В ТЕЛЕГРАММ БОТЕ ДДАП-РАКС")} \n\n'
                         f'{_("Для продолжения работы воспользуйтесь ГЛАВНЫМ МЕНЮ")}.\n',
                         reply_markup=get_markup(message,
                                                 admins_id=admins,
                                                 managers_id=managers))
    await sleep(1)
    if await check_user_data(message.from_user.id):
        await message.answer(f'{message.from_user.full_name}. \n'
                             f'{_("Вы не указали контактные данные")},'
                             f'{_("укажите их в личном профиле")}.')
        await show_my_profile(message)


def get_markup(message: Message, admins_id: List, managers_id: List) -> ReplyKeyboardMarkup:
    user_id = str(message.from_user.id)
    if user_id in admins_id:
        return mmkb.get_markup_admin_main_menu()
    elif user_id in managers_id:
        return mmkb.get_markup_manager_main()
    else:
        return mmkb.get_markup_main_menu()
