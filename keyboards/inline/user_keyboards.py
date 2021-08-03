from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import urls

# Клавиатура основного меню
news_button = InlineKeyboardButton(text='Новости компании', url=urls.NEWS)
site_button = InlineKeyboardButton(text='Сайт компании', url=urls.SITE)
my_account_button = InlineKeyboardButton(text='Кабинет клиента', url=urls.MY_ACCOUNT)
production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
services_button = InlineKeyboardButton(text='Наши услуги', callback_data='services')
# manager_chat_button = InlineKeyboardButton(text='Задать вопрос менеджеру', callback_data='ask_question')
manager_chat_button = InlineKeyboardButton(text='Задать вопрос менеджеру', callback_data='chat_with_manager')
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
button_back_to_main_menu = InlineKeyboardButton(text='Назад в меню', callback_data='back_to_main_menu')
markup_to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [button_back_to_main_menu]
])

manager_message_button = InlineKeyboardButton(text='Написать 1 сообщение менеджеру', callback_data='message_to_manager')
manager_chat_button = InlineKeyboardButton(text='Начать чат с менеджером', callback_data='chat_with_manager')

# Клавиатура чат - сообщение медеджеру
markup_chat_message = InlineKeyboardMarkup(inline_keyboard=[
    [manager_chat_button],
    [button_back_to_main_menu]
], )

# Клавиатура мой профиль
set_phone_button = InlineKeyboardButton(text='Изменить телефон', callback_data='get_user_phone')
set_email_button = InlineKeyboardButton(text='Изменить email', callback_data='get_user_email')
set_company_name_button = InlineKeyboardButton(text='Изменить название компании', callback_data='get_user_company')
set_password_button = InlineKeyboardButton(text='Изменить пароль', callback_data='get_user_password')


markup_my_profile = InlineKeyboardMarkup(inline_keyboard=[
    [set_phone_button, set_email_button],
    [set_company_name_button],
    [set_password_button],
], )