from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message

import keyboards.inline.admin_keyboards as akb
from data.config import ADMINS
from loader import dp


@dp.message_handler(Text('Панель администратора'), user_id=ADMINS)
async def show_admin_panel(message: Message):
    await message.answer(text='Меню администратора', reply_markup=akb.markup_admin_main)


@dp.message_handler(Command('admin'), user_id=ADMINS)
async def show_ap(message: Message):
    await show_admin_panel(message)
