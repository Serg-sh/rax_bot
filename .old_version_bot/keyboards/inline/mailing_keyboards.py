from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import _


def get_markup_mailing() -> InlineKeyboardMarkup:
    confirm_button = InlineKeyboardButton(text=_('Разослать рассылку'), callback_data='confirm_mailing')
    cancel_button = InlineKeyboardButton(text=_('Отменить'), callback_data='cancel_mailing')
    markup_mailing = InlineKeyboardMarkup(inline_keyboard=[
        [cancel_button, confirm_button],

    ])
    return markup_mailing


def get_markup_lang_mailing() -> InlineKeyboardMarkup:
    all_clients = InlineKeyboardButton(text=_('Для всех пользователей'), callback_data='all_clients_mailing')
    uk_clients = InlineKeyboardButton(text='Українська', callback_data='uk_clients_mailing')
    # ru_clients = InlineKeyboardButton(text='Русский', callback_data='ru_clients_mailing')
    en_clients = InlineKeyboardButton(text='English', callback_data='en_clients_mailing')
    markup_lang_mailing = InlineKeyboardMarkup(inline_keyboard=[
        [all_clients],
        [uk_clients, en_clients],
    ])
    return markup_lang_mailing
