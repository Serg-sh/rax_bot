from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, CallbackQuery

import keyboards.inline.admin_keyboards as akb
from data.config import ADMINS
from loader import dp
from utils.db_api import database


db = database.DBCommands()

@dp.message_handler(Text('Панель администратора'), user_id=ADMINS)
async def show_admin_panel(message: Message):
    await message.answer(text='Меню администратора', reply_markup=akb.markup_admin_main)


@dp.message_handler(Command('admin'), user_id=ADMINS)
async def show_ap(message: Message):
    await show_admin_panel(message)

@dp.callback_query_handler(text_contains='back_to_admin_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(akb.markup_admin_main)


@dp.callback_query_handler(text_contains='bot_statistics')
async def show_bot_statistics(call: CallbackQuery):
    total_users = await db.count_users()
    await call.message.answer(f'Колличество пользователей бота: {total_users}', reply_markup=akb.markup_to_admin_menu)



