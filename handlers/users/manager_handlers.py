from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, CallbackQuery

from data.config import MANAGERS
from keyboards.inline import manager_keyboards as mkb
from keyboards.inline.manager_keyboards import markup_manager_main
from loader import dp
from utils.db_api import database

db = database.DBCommands()


@dp.message_handler(Command('manager'))
@dp.message_handler(Text('Панель менеджера'))
async def show_manager_panel(message: Message):
    MANAGERS.extend(await db.get_managers_user_id())
    if str(message.from_user.id) in MANAGERS:
        await message.answer(text='Меню менеджера', reply_markup=markup_manager_main)
    else:
        await message.answer(text='Недостаточно прав доступа.')


@dp.callback_query_handler(text_contains='back_to_manager_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(mkb.markup_manager_main)
