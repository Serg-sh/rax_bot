from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.manager_keyboards import markup_manager_main
from keyboards.inline import manager_keyboards as mkb
from loader import dp
from utils.db_api import database

db = database.DBCommands()

MANAGERS = db.get_managers_user_id()

@dp.message_handler(Text('Панель менеджера'), user_id=MANAGERS)
async def show_manager_panel(message: Message):
    await message.answer(text='Меню менеджера', reply_markup=markup_manager_main)


@dp.message_handler(Command('manager'), user_id=MANAGERS)
async def show_mp(message: Message):
    await show_manager_panel(message)


@dp.callback_query_handler(text_contains='back_to_manager_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(mkb.markup_manager_main)
