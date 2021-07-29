# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
users_mailing_button = InlineKeyboardButton(text='Создать рассылку для пользователей',
                                            callback_data='users_mailing')
managers_mailing_button = InlineKeyboardButton(text='Создать рассылку для менеджеров',
                                               callback_data='managers_mailing')


markup_manager_main = InlineKeyboardMarkup(inline_keyboard=[
    [production_button],
    [users_mailing_button],
    [managers_mailing_button],
], )
