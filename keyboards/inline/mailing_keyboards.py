from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


confirm_button = InlineKeyboardButton(text='Разослать рассылку', callback_data='confirm_mailing_admins')
cancel_button = InlineKeyboardButton(text='Отменить', callback_data='cancel_mailing_admins')

markup_mailing = InlineKeyboardMarkup(inline_keyboard=[
    [cancel_button, confirm_button],

])