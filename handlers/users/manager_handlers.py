from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import Text

from data.config import MANAGERS
from keyboards.inline import manager_keyboards as mkb
from loader import dp, _
from utils.db_api import database

db = database.DBCommands()


@dp.message_handler(Command('manager'))
@dp.message_handler(Text('Панель менеджера'))
@dp.message_handler(Text('Manager panel'))
@dp.message_handler(Text('Панель менеджера'))
async def show_manager_panel(message: Message):
    MANAGERS.extend(await db.get_managers_user_id())
    if str(message.from_user.id) in MANAGERS:
        await message.answer(text=_('Меню менеджера'), reply_markup=mkb.get_markup_manager_main())
    else:
        await message.answer(text=_('Недостаточно прав доступа.'))


@dp.callback_query_handler(text_contains='back_to_manager_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.edit_reply_markup(mkb.get_markup_manager_main())
