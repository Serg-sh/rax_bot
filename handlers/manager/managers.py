from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from config import MANAGERS
from keyboard.inline.manager_kb import InlineManagerKB
from utils.database.queryes import UserDBQuery
from loader import _

managers_router = Router()
db = UserDBQuery()
manager_kb = InlineManagerKB()


@managers_router.message(F.text == 'Managers menu')
@managers_router.message(F.text == 'Меню менеджера')
async def show_manager_panel(message: Message):
    managers = await db.get_managers_user_id()
    for manager in managers:
        MANAGERS.append(manager)
    if message.from_user.id in MANAGERS:
        await message.answer(text=_('Меню менеджера'), reply_markup=manager_kb.get_markup_manager_main())
    else:
        await message.answer(text=f"{message.from_user.full_name}, {_('у вас немає прав доступу')}")


@managers_router.callback_query(F.data == 'back_to_manager_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.edit_reply_markup(reply_markup=manager_kb.get_markup_manager_main())
