# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
clients_mailing_button = InlineKeyboardButton(text='Создать рассылку для пользователей',
                                              callback_data='clients_mailing')
managers_mailing_button = InlineKeyboardButton(text='Создать рассылку для менеджеров',
                                               callback_data='managers_mailing')


markup_manager_main = InlineKeyboardMarkup(inline_keyboard=[
    [production_button],
    [clients_mailing_button],
    [managers_mailing_button],
], )
