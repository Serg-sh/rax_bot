from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

import keyboards.inline.user_keyboards as ukb
from loader import dp
from utils.db_api import database

db = database.DBCommands()


@dp.callback_query_handler(text_contains='news')
async def show_news(call: CallbackQuery):
    await call.message.edit_reply_markup(ukb.markup_news)

