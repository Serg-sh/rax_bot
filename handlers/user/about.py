from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from data.texts import ABOUT_US_0_UK, ABOUT_US_1_UK, ABOUT_US_2_UK
from data.texts import ABOUT_US_0_EN, ABOUT_US_1_EN, ABOUT_US_2_EN
from keyboard.inline.user_kb import InlineKeyboardBack
from loader import bot, _
from utils.database.models import User
from utils.database.queryes import UserDBQuery

about_router = Router()
db = UserDBQuery()
back_kb = InlineKeyboardBack()


@about_router.callback_query(F.data == 'about_us')
async def show_about_us(call: CallbackQuery):
    bot_username = (await bot.me()).username
    bot_link = f'https://t.me/{bot_username}'
    user: User = await db.get_user(user_id=call.from_user.id)

    img_about_1 = FSInputFile('data/images/img_about_1.jpg')
    img_about_2 = FSInputFile('data/images/img_about_2.jpg')
    text_about_0 = ABOUT_US_0_UK
    text_about_1 = ABOUT_US_1_UK
    text_about_2 = ABOUT_US_2_UK

    match user.languages:
        case "en":
            text_about_0 = ABOUT_US_0_EN
            text_about_1 = ABOUT_US_1_EN
            text_about_2 = ABOUT_US_2_EN
        case _:
            pass

    await call.message.answer(text=text_about_0,
                              parse_mode='HTML')
    await call.message.answer_photo(photo=img_about_1,
                                    parse_mode='HTML')
    await call.message.answer(text=text_about_1,
                              parse_mode='HTML')
    await call.message.answer_photo(photo=img_about_2,
                                    parse_mode='HTML')
    await call.message.answer(text=text_about_2,
                              parse_mode='HTML')
    await call.message.answer(text=f'{_("Посилання на бот")}:\n{bot_link}\n',
                              reply_markup=back_kb.get_markup_to_main_menu())
