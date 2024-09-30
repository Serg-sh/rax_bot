from asyncio import sleep
from aiogram import types
from aiogram.types import InputFile

from config import ADMINS
from keyboard.default.main_menu import get_markup
from loader import dp, _
from utils.database.queryes import UserDBQuery

db = UserDBQuery()


@dp.message_handler(text_contains='start')
async def bot_start(message: types.Message):
    user = await message.from_user
    user = await db.add_user(user)
    logo_rax = InputFile('data/images/logo_rax.jpg')
    await message.answer_photo(photo=logo_rax, parse_mode='HTML')
    await sleep(0.1)
    managers = await db.get_managers_user_id()
    admins = await db.get_admins_user_id()
    admins.extend(ADMINS)
    await message.answer(f'{_("Доброго дня")}!  {message.from_user.full_name}!\n\n'
                         f'🇺🇦🇺🇦🇺🇦 {_("МИ З УКРАЇНИ")} 🇺🇦🇺🇦🇺🇦\n\n'
                         f'{_("ПРИВЕТСТВУЕМ ВАС В ТЕЛЕГРАММ БОТЕ ДДАП-РАКС")} \n\n'
                         f'{_("Для продолжения работы воспользуйтесь ГЛАВНЫМ МЕНЮ")}.\n',
                         reply_markup=get_markup(user.user_id,
                                                 admins_id=admins,
                                                 managers_id=managers))



