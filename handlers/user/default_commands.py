from asyncio import sleep

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile

from config import ADMINS
from keyboard.default.main_menu import get_markup
from utils.database.queryes import UserDBQuery
from loader import _


command_router = Router()
db = UserDBQuery()


@command_router.message(Command("start"))
async def command_start(message: types.Message):
    user = message.from_user
    user = await db.add_user(user)
    managers_id = await db.get_managers_user_id()
    admins_id = await db.get_admins_user_id()
    admins_id.extend(ADMINS)
    logo_rax = FSInputFile("data/images/logo_rax.jpg")
    await message.answer_photo(photo=logo_rax, parse_mode='HTML')
    await sleep(0.1)
    await message.answer(f'{_("Доброго дня")}!  {message.from_user.full_name}!\n\n'
                         f'🇺🇦🇺🇦🇺🇦 {_("МИ З УКРАЇНИ")} 🇺🇦🇺🇦🇺🇦\n\n'
                         f'{_("Раді вітати Вас у телеграм боті ДДАП-РАКС")} \n\n'
                         f'{_("Для подальшої роботи натисніть ГОЛОВНЕ МЕНЮ")}.\n',
                         reply_markup=get_markup(user.user_id,
                                                 admins_id=admins_id,
                                                 managers_id=managers_id))


@command_router.message(Command("help"))
async def command_help(message: types.Message):
    user = message.from_user
    await message.answer(f"{user.full_name}, {_("чим допомогти")}?")




