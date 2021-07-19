from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

import data.texts as txt
import keyboards.inline.user_keyboards as ukb
from loader import dp


@dp.message_handler(Text('Главное меню'))
async def show_main_menu(message: Message):
    await message.answer(text='Главное меню', reply_markup=ukb.markup_main)


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await show_main_menu(message)


@dp.callback_query_handler(text_contains='back_to_main_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(ukb.markup_main)


@dp.callback_query_handler(text_contains='services')
async def show_services(call: CallbackQuery):
    await call.message.answer(text=txt.SERVICES,
                              parse_mode='HTML',
                              reply_markup=ukb.markup_to_main_menu)


@dp.callback_query_handler(text_contains='about_us')
async def show_about_us(call: CallbackQuery):
    await call.message.answer(text=txt.ABOUT_US,
                              parse_mode='HTML',
                              reply_markup=ukb.markup_to_main_menu)


@dp.callback_query_handler(text_contains='contacts')
async def show_contacts(call: CallbackQuery):
    await call.message.answer_venue(48.5260340474648, 34.610616658895474,
                                    title=txt.COMPANY,
                                    address=txt.COMPANY_ADDRESS
                                    )

    await call.message.answer_contact(phone_number=txt.TEL,
                                      first_name=txt.EMAIL,
                                      reply_markup=ukb.markup_to_main_menu)


@dp.callback_query_handler(text_contains='ask_question')
async def ask_question(call: CallbackQuery):
    await call.message.edit_reply_markup(ukb.markup_chat_message)



