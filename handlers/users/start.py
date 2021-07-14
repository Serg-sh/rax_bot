from asyncio import sleep

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from keyboards.inline.user_keyboards import main_markup
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logo_rax = InputFile('images/logo_rax.jpg')
    await message.answer_photo(photo=logo_rax, parse_mode='HTML')
    await sleep(0.3)
    await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                         f'ДЛЯ ПРОДОЛЖЕНИЯ РАБОТЫ ВОСПОЛЬЗУЙТЕСЬ КНОПКАМИ МЕНЮ \n',
                         reply_markup=main_markup)
