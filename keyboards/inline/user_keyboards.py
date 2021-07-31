from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import urls

news_button = InlineKeyboardButton(text='Новости компании', callback_data='news')
site_button = InlineKeyboardButton(text='Сайт компании', callback_data='site')
my_account_button = InlineKeyboardButton(text='Кабинет клиента', callback_data='my_account')
production_button = InlineKeyboardButton(text='Наша продукция', url=urls.PRODUCTS)
manager_chat_button = InlineKeyboardButton(text='Задать вопрос менеджеру', callback_data='chat_online')
contacts_button = InlineKeyboardButton(text='Наши контакты', callback_data='contacts')
about_us_button = InlineKeyboardButton(text='О нас', callback_data='about_us')


main_markup = InlineKeyboardMarkup(inline_keyboard=[
    [news_button],
    [site_button, my_account_button],
    [production_button],
    [manager_chat_button],
    [contacts_button],
    [about_us_button]
])
