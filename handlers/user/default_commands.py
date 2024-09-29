from aiogram import types, Router
from aiogram.filters import Command

from utils.database.queryes import UserDBQuery
from loader import _


command_router = Router()
db = UserDBQuery()


@command_router.message(Command("start"))
async def command_start(message: types.Message):
    user = message.from_user
    await db.add_user(message.from_user)
    await message.answer(f"{user.full_name}," + _(" Вітаю!"))


@command_router.message(Command("help"))
async def command_help(message: types.Message):
    user = message.from_user
    await message.answer(f"{user.full_name}, чим допомогти?")





