from asyncio import sleep
from typing import List

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile, Message, ReplyKeyboardMarkup

from data.config import ADMINS
from keyboards.default.main_menu import markup_main_menu, markup_admin_main_menu, markup_manager_main
from loader import dp
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
    user = await db.get_user(message.from_user.id)

    await message.answer(f'Добрый День!  {message.from_user.full_name}!\n\n'
                         f'ПРИВЕТСТВУЕМ ВАС В ТЕЛЕГРАММ БОТЕ ДДАП-РАКС\n\n'
                         f'Для продолжения работы воспользуйтесь ГЛАВНЫМ МЕНЮ \n',
                         reply_markup=get_markup(message,
                                                 admins_id=admins,
                                                 managers_id=managers))


def get_markup(message: Message, admins_id: List, managers_id: List) -> ReplyKeyboardMarkup:
    user_id = str(message.from_user.id)
    if user_id in admins_id:
        return markup_admin_main_menu
    elif user_id in managers_id:
        return markup_manager_main
    else:
        return markup_main_menu
