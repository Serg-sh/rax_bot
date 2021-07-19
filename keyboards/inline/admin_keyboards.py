# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
mailing_button = InlineKeyboardButton(text='Создать рассылку', callback_data='mailing')
statistics_button = InlineKeyboardButton(text='Статистика бота', callback_data='statistics')


markup_admin_main = InlineKeyboardMarkup(inline_keyboard=[
    [production_button],
    [mailing_button],
    [statistics_button],
], )