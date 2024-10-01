from aiogram import Router, F
from aiogram.types import CallbackQuery

from data import texts
from keyboard.inline.user_kb import InlineKeyboardBack
from utils.database.queryes import UserDBQuery

db = UserDBQuery()
contact_router = Router()
back_kb = InlineKeyboardBack()

@contact_router.callback_query(F.data == 'contacts')
async def show_contacts(call: CallbackQuery):
    user = await db.get_user(user_id=call.from_user.id)
    title = texts.COMPANY_UK
    address = texts.COMPANY_ADDRESS_UK

    match user.languages:
        case "en":
            title = texts.COMPANY_EN
            address = texts.COMPANY_ADDRESS_EN
        case _:
            pass

    await call.message.answer(text="http://ddaprax.com")

    await call.message.answer_contact(phone_number=texts.TEL,
                                      first_name=texts.EMAIL,
                                      parse_mode='HTML')

    await call.message.answer_venue(48.5260340474648, 34.610616658895474,
                                    title=title,
                                    address=address,
                                    reply_markup=back_kb.get_markup_to_main_menu(),
                                    )
