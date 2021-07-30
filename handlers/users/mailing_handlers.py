from asyncio import sleep

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

import keyboards.inline.mailing_keyboards as mk
from data.config import ADMINS
from loader import dp, bot
from states.states import Mailing


# Рассылка для админов
@dp.callback_query_handler(user_id=ADMINS, text_contains='admins_mailing')
async def mailing_to_admins(call: CallbackQuery):
    await call.message.answer('Пришлите текст рассылки')
    await Mailing.Text.set()


@dp.message_handler(user_id=ADMINS, state=Mailing.Text)
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(f'Текст рассылки:\n\n{text}', reply_markup=mk.markup_mailing)
    await Mailing.SendToAdmins.set()


@dp.callback_query_handler(user_id=ADMINS, state=Mailing.SendToAdmins, text_contains='confirm_mailing_admins')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()
    await call.message.edit_reply_markup()
    for admin_id in ADMINS:
        try:
            await bot.send_message(chat_id=admin_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer('Рассылка выполнена.')


@dp.callback_query_handler(user_id=ADMINS, state=Mailing.SendToAdmins, text_contains='cancel_mailing_admins')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_reply_markup()
    await call.message.answer('Рассылка отменена.')