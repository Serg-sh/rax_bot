from asyncio import sleep

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import keyboards.inline.mailing_keyboards as mk
from keyboards.inline import admin_keyboards as akb
from keyboards.inline import manager_keyboards as mkb
from loader import dp, bot, _
from states.states import MailingAdmins, MailingManagers, MailingClients
from utils.db_api import database

db = database.DBCommands()


# Рассылка для админов
@dp.callback_query_handler(text_contains='admins_mailing')
async def mailing_to_admins(call: CallbackQuery):
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingAdmins.Text.set()


@dp.message_handler(state=MailingAdmins.Text)
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(text=f'{_("Текст рассылки")}:\n\n{text}',
                         reply_markup=mk.get_markup_mailing())
    await MailingAdmins.SendToAdmins.set()


@dp.callback_query_handler(state=MailingAdmins.SendToAdmins, text_contains='confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()
    await call.message.edit_reply_markup()
    admins_id = await db.get_admins_user_id()
    for admin_id in admins_id:
        try:
            await bot.send_message(chat_id=admin_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(text=_('Рассылка выполнена.'),
                              reply_markup=akb.get_markup_to_admin_menu())


@dp.callback_query_handler(state=MailingAdmins.SendToAdmins, text_contains='cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Рассылка отменена.'),
                              reply_markup=akb.get_markup_to_admin_menu())


# Рассылка для менеджеров
@dp.callback_query_handler(text_contains='managers_mailing')
async def mailing_to_managers(call: CallbackQuery):
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingManagers.Text.set()


@dp.message_handler(state=MailingManagers.Text)
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(text=f'{_("Текст рассылки")}:\n\n{text}',
                         reply_markup=mk.get_markup_mailing())
    await MailingManagers.SendToManagers.set()


@dp.callback_query_handler(state=MailingManagers.SendToManagers, text_contains='confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()
    await call.message.edit_reply_markup()
    managers_id = await db.get_managers_user_id()
    for user_id in managers_id:
        try:
            await bot.send_message(chat_id=user_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(text=_('Рассылка выполнена.'),
                              reply_markup=mkb.get_markup_to_manager_menu())


@dp.callback_query_handler(state=MailingManagers.SendToManagers, text_contains='cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Рассылка отменена.'),
                              reply_markup=mkb.get_markup_to_manager_menu())


# Рассылка для клиентов
@dp.callback_query_handler(text_contains='choice_mailing_language')
async def choice_mailing_language(call: CallbackQuery):
    await call.message.answer(text='Выберите язык рассылки',
                              reply_markup=mk.get_markup_lang_mailing())


@dp.callback_query_handler(text_contains='all_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language=None)
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingClients.Text.set()


@dp.callback_query_handler(text_contains='ru_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='ru')
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingClients.Text.set()


@dp.callback_query_handler(text_contains='uk_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='uk')
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingClients.Text.set()


@dp.callback_query_handler(text_contains='en_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='en')
    await call.message.answer(_('Пришлите текст рассылки'))
    await MailingClients.Text.set()


@dp.message_handler(state=MailingClients.Text)
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(text=f'{_("Текст рассылки")}:\n\n{text}',
                         reply_markup=mk.get_markup_mailing())
    await MailingClients.SendToClients.set()


@dp.callback_query_handler(state=MailingClients.SendToClients, text_contains='confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    lang = data.get('language')
    await state.reset_state()
    await call.message.edit_reply_markup()
    clients_id = await db.get_clients_user_id(language=lang)
    for client_id in clients_id:
        try:
            await bot.send_message(chat_id=client_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(text=f'{_("Рассылка выполнена")} {_("для")} {len(clients_id)} {_("пользователей")}',
                              reply_markup=mkb.get_markup_to_manager_menu())


@dp.callback_query_handler(state=MailingClients.SendToClients, text_contains='cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Рассылка отменена.'),
                              reply_markup=mkb.get_markup_to_manager_menu())
