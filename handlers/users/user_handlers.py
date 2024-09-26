from asyncio import sleep

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InputFile
from aiogram.utils.formatting import Text

import data.texts as txt
import keyboards.inline.user_keyboards as ukb
from loader import dp, bot, _
from utils.db_api import database

db = database.DBCommands()


@dp.message_handler(Text('Главное меню'))
@dp.message_handler(Text('Main Menu'))
@dp.message_handler(Text('Головне меню'))
async def show_main_menu(message: Message):
    await dp.current_state().reset_state()
    await message.answer(text=_('Главное меню'), reply_markup=ukb.get_markup_main())


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await show_main_menu(message)


@dp.callback_query_handler(text_contains='back_to_main_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await dp.current_state().reset_state()
    await call.message.answer(text=_('Главное меню'), reply_markup=ukb.get_markup_main())


@dp.callback_query_handler(text_contains='services')
async def show_services(call: CallbackQuery):
    user_id = call.from_user.id
    user = await db.get_user(user_id=user_id)
    text = txt.SERVICES_RU
    if user.languages == 'en':
        text = txt.SERVICES_EN
    elif user.languages == 'uk':
        text = txt.SERVICES_UK

    await call.message.answer(text=text,
                              parse_mode='HTML',
                              reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='about_us')
async def show_about_us(call: CallbackQuery):
    bot_username = (await bot.me).username
    bot_link = f'https://t.me/{bot_username}'
    values_ru_1 = InputFile('data/images/VALUES_RU_1.png')
    values_en_1 = InputFile('data/images/VALUES_EN_1.png')
    values_uk_1 = InputFile('data/images/VALUES_UK_1.png')
    user_id = call.from_user.id
    user = await db.get_user(user_id=user_id)
    text_about_us = txt.ABOUT_US_0_RU
    text_about_geo = txt.ABOUT_US_1_RU
    img_values = values_ru_1
    if user.languages == 'en':
        text_about_us = txt.ABOUT_US_0_EN
        text_about_geo = txt.ABOUT_US_1_EN
        img_values = values_en_1
    elif user.languages == 'uk':
        text_about_us = txt.ABOUT_US_0_UK
        text_about_geo = txt.ABOUT_US_1_UK
        img_values = values_uk_1

    await call.message.answer(text=text_about_us,
                              parse_mode='HTML')
    await call.message.answer_photo(photo=img_values, parse_mode='HTML')
    await call.message.answer(text=text_about_geo, parse_mode='HTML')
    await sleep(0.5)
    await call.message.answer(text=f'{_("Поделиться ссылкой на БОТ ДДАП-РАКС")}\n'
                                   f'{bot_link}',
                              reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='contacts')
async def show_contacts(call: CallbackQuery):
    user_id = call.from_user.id
    user = await db.get_user(user_id=user_id)
    title = txt.COMPANY_RU
    address = txt.COMPANY_ADDRESS_RU
    if user.languages == 'en':
        title = txt.COMPANY_EN
        address = txt.COMPANY_ADDRESS_EN
    elif user.languages == 'uk':
        title = txt.COMPANY_UK
        address = txt.COMPANY_ADDRESS_UK

    await call.message.answer_venue(48.5260340474648, 34.610616658895474,
                                    title=title,
                                    address=address
                                    )
    await call.message.answer_contact(phone_number=txt.TEL,
                                      first_name=txt.EMAIL,
                                      reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='ask_question')
async def ask_question(call: CallbackQuery):
    await call.message.edit_reply_markup(ukb.get_markup_chat_message())
