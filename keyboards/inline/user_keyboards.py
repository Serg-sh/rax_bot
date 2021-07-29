from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import urls


# Клавиатура основного меню
news_button = InlineKeyboardButton(text='Новости компании', url=urls.NEWS)
site_button = InlineKeyboardButton(text='Сайт компании', url=urls.SITE)
my_account_button = InlineKeyboardButton(text='Кабинет клиента', url=urls.MY_ACCOUNT)
production_button = InlineKeyboardButton(text='Наша продукция', url=urls.PRODUCTS)
services_button = InlineKeyboardButton(text='Наши услуги', callback_data='services')
manager_chat_button = InlineKeyboardButton(text='Задать вопрос менеджеру', callback_data='ask_question')
contacts_button = InlineKeyboardButton(text='Наши контакты', callback_data='contacts')
about_us_button = InlineKeyboardButton(text='О нас', callback_data='about_us')


markup_main = InlineKeyboardMarkup(inline_keyboard=[
    [news_button],
    [site_button, my_account_button],
    [production_button, services_button],
    [manager_chat_button],
    [contacts_button],
    [about_us_button]
], )

# Кнопка назад в меню
button_back_to_main_menu = InlineKeyboardButton(text='Назад', callback_data='back_to_main_menu')
markup_to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [button_back_to_main_menu]
])


manager_chat_button = InlineKeyboardButton(text='Написать OFFLINE сообщение менеджеру', callback_data='message_to_manager')
manager_message_button = InlineKeyboardButton(text='Начать ONLINE чат с менеджером', callback_data='chat_with_manager')

# Клавиатура чат - сообщение медеджеру
markup_chat_message = InlineKeyboardMarkup(inline_keyboard=[
    [manager_message_button],
    [manager_chat_button],
    [button_back_to_main_menu]
], )