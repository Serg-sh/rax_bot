from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message, InputFile

import data.texts as txt
import keyboards.inline.user_keyboards as ukb
from loader import dp, bot, _
from utils.db_api import database

db = database.DBCommands()


@dp.message_handler(Text('Главное меню'))
@dp.message_handler(Text('Main Menu'))
@dp.message_handler(Text('Головне меню'))
async def show_main_menu(message: Message):
    await message.answer(text=_('Главное меню'), reply_markup=ukb.get_markup_main())


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await show_main_menu(message)


@dp.callback_query_handler(text_contains='back_to_main_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Главное меню'), reply_markup=ukb.get_markup_main())


@dp.callback_query_handler(text_contains='services')
async def show_services(call: CallbackQuery):
    await call.message.answer(text=txt.SERVICES_RU,
                              parse_mode='HTML',
                              reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='about_us')
async def show_about_us(call: CallbackQuery):
    bot_username = (await bot.me).username
    bot_link = f'https://t.me/{bot_username}'
    values_ru_1 = InputFile('data/images/VALUES_RU_1.png')
    await call.message.answer(text=txt.ABOUT_US_RU,
                              parse_mode='HTML')
    await call.message.answer_photo(photo=values_ru_1, parse_mode='HTML')
    await call.message.answer(text=txt.ABOUT_US_1_RU, parse_mode='HTML')
    await call.message.answer(text=f'{_("Поделиться ссылкой на БОТ ДДАП-РАКС")}\n'
                                   f'{bot_link}',
                              reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='contacts')
async def show_contacts(call: CallbackQuery):
    await call.message.answer_venue(48.5260340474648, 34.610616658895474,
                                    title=txt.COMPANY_RU,
                                    address=txt.COMPANY_ADDRESS_RU
                                    )
    await call.message.answer_contact(phone_number=txt.TEL,
                                      first_name=txt.EMAIL,
                                      reply_markup=ukb.get_markup_to_main_menu())


@dp.callback_query_handler(text_contains='ask_question')
async def ask_question(call: CallbackQuery):
    await call.message.edit_reply_markup(ukb.get_markup_chat_message())
