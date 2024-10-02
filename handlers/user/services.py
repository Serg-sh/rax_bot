from aiogram import Router, F
from aiogram.types import CallbackQuery

from data.texts import SERVICES_UK, SERVICES_EN
from keyboard.inline.user_kb import InlineKeyboardBack
from utils.database.queryes import UserDBQuery

services_router = Router()
back_kb = InlineKeyboardBack()
db = UserDBQuery()


@services_router.callback_query(F.data == 'services')
async def show_services(call: CallbackQuery):
    user = await db.get_user(user_id=call.from_user.id)
    text = SERVICES_UK

    match user.languages:
        case "en":
            text = SERVICES_EN
        case _:
            pass

    await call.message.answer(text=text,
                              parse_mode='HTML',
                              reply_markup=back_kb.get_markup_to_main_menu())
