from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types.base import InputFile

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logo_rax = InputFile('images/rax-01.jpg', '')
    await message.answer_photo(photo=logo_rax)
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'ДЛЯ ПРОДОЛЖЕНИЯ РАБОТЫ ВОСПОЛЬЗУЙТЕСЬ КНОПКАМИ МЕНЮ')
