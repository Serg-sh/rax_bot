from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message

from data.config import MANAGERS
from keyboards.inline.manager_keyboards import markup_manager_main
from loader import dp


@dp.message_handler(Text('Панель менеджера'), user_id=MANAGERS)
async def show_manager_panel(message: Message):
    await message.answer(text='Меню менеджера', reply_markup=markup_manager_main)


@dp.message_handler(Command('manager'), user_id=MANAGERS)
async def show_mp(message: Message):
    await show_manager_panel(message)
