from asyncio import sleep

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboard.inline.admin_kb import InlineKeyboardAdmin
from keyboard.inline.manager_kb import InlineManagerKB
from keyboard.inline.user_kb import InlineKeyboardMailing
from states.states import MailingAdmins, MailingManagers, MailingClients
from utils.database.queryes import UserDBQuery
from loader import _, bot

db = UserDBQuery()
mailing_router = Router()
admin_kb = InlineKeyboardAdmin()
managers_kb = InlineManagerKB()
mailing_kb = InlineKeyboardMailing()


# Розсилка для адмінів
@mailing_router.callback_query(F.data == 'admins_mailing')
async def mailing_to_admins(call: CallbackQuery, state: FSMContext):
    await state.set_state(MailingAdmins.Text)
    await call.message.answer(f"{_('Надішліть текст розсилки')}")


@mailing_router.message(StateFilter(MailingAdmins.Text))
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await state.set_state(MailingAdmins.SendToAdmins)
    await message.answer(text=f'<b>{_("Текст розсилки")}</b>:\n\n{text}',
                         reply_markup=mailing_kb.get_markup_mailing(),
                         parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingAdmins.SendToAdmins), F.data == 'confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.clear()
    await call.message.edit_reply_markup()
    admins_id = await db.get_admins_user_id()
    for admin_id in admins_id:
        try:
            await bot.send_message(chat_id=admin_id, text=text)
            await sleep(0.05)
        except Exception:
            pass
    await call.message.answer(text=f"{_('Розсилка виконана')}.",
                              reply_markup=admin_kb.get_markup_to_admin_menu(),
                              parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingAdmins.SendToAdmins), F.data == 'cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_reply_markup()
    await call.message.answer(text=f"{_('Розсилка скасована')}.",
                              reply_markup=admin_kb.get_markup_to_admin_menu())


# Рассылка для менеджеров
@mailing_router.callback_query(F.data == 'managers_mailing')
async def mailing_to_managers(call: CallbackQuery, state: FSMContext):
    await state.set_state(MailingManagers.Text)
    await call.message.answer(text=f"{_('Надішліть текст розсилки')}",
                              parse_mode='HTML')


@mailing_router.message(StateFilter(MailingManagers.Text))
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await state.set_state(MailingManagers.SendToManagers)
    await message.answer(text=f'{_("Текст розсилки")}:\n\n{text}',
                         reply_markup=mailing_kb.get_markup_mailing(),
                         parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingManagers.SendToManagers), F.data == 'confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.clear()
    await call.message.edit_reply_markup()
    managers_id = await db.get_managers_user_id()
    for user_id in managers_id:
        try:
            await bot.send_message(chat_id=user_id, text=text)
            await sleep(0.05)
        except Exception:
            pass
    await call.message.answer(text=f"{_('Розсилка виконана')}",
                              reply_markup=managers_kb.get_markup_to_manager_menu(),
                              parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingManagers.SendToManagers), F.data == 'cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_reply_markup()
    await call.message.answer(text=f"{_('Розсилка скасована')}.",
                              reply_markup=managers_kb.get_markup_to_manager_menu(),
                              parse_mode='HTML')


# Рассылка для клиентов
@mailing_router.callback_query(F.data == 'choice_mailing_language')
async def choice_mailing_language(call: CallbackQuery):
    await call.message.answer(text=f"{'Оберіть мову розсилки'}",
                              reply_markup=mailing_kb.get_markup_lang_mailing(),
                              parse_mode='HTML')


@mailing_router.callback_query(F.data == 'all_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language="None")
    await state.set_state(MailingClients.Text)
    await call.message.answer(text=f"{_('Надішліть текст розсилки')}",
                              parse_mode='HTML')


@mailing_router.callback_query(F.data == 'uk_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='uk')
    await state.set_state(MailingClients.Text)
    await call.message.answer(text=f"{_('Надішліть текст розсилки')}",
                              parse_mode='HTML')


@mailing_router.callback_query(F.data == 'en_clients_mailing')
async def mailing_to_clients(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='en')
    await state.set_state(MailingClients.Text)
    await call.message.answer(text=f"{_('Надішліть текст розсилки')}",
                              parse_mode='HTML')


@mailing_router.message(StateFilter(MailingClients.Text))
async def enter_text(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await state.set_state(MailingClients.SendToClients)
    await message.answer(text=f'{_("Текст розсилки")}:\n\n{text}',
                         reply_markup=mailing_kb.get_markup_mailing(),
                         parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingClients.SendToClients), F.data == 'confirm_mailing')
async def send_mailing(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    lang = data.get('language')
    await state.clear()
    await call.message.edit_reply_markup()
    users = await db.get_all_users()
    for user in users:
        if user.languages == lang:
            try:
                await bot.send_message(chat_id=user.user_id, text=text, parse_mode='HTML')
                await sleep(0.05)
            except Exception:
                pass
        elif lang == 'None':
            try:
                await bot.send_message(chat_id=user.user_id, text=text, parse_mode='HTML')
                await sleep(0.05)
            except Exception:
                pass



    await call.message.answer(text=f'{_("Розсилка виконана")} {_("для")} {len(users)} {_("користувачам")}',
                              reply_markup=managers_kb.get_markup_to_manager_menu(),
                              parse_mode='HTML')


@mailing_router.callback_query(StateFilter(MailingClients.SendToClients), F.data == 'cancel_mailing')
async def cancel_mailing(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_reply_markup()
    await call.message.answer(text=f"{_('Розсилка скасована')}.",
                              reply_markup=managers_kb.get_markup_to_manager_menu(),
                              parse_mode='HTML')
