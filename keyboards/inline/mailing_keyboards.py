from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


def get_markup_mailing() -> InlineKeyboardMarkup:
    confirm_button = InlineKeyboardButton(text=_('Разослать рассылку'), callback_data='confirm_mailing')
    cancel_button = InlineKeyboardButton(text=_('Отменить'), callback_data='cancel_mailing')
    markup_mailing = InlineKeyboardMarkup(inline_keyboard=[
        [cancel_button, confirm_button],

    ])
    return markup_mailing
