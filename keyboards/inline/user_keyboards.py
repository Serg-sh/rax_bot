from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import urls
from loader import _


# Клавиатура основного меню
def get_markup_main() -> InlineKeyboardMarkup:
    news_button = InlineKeyboardButton(text=_('Новости компании'),
                                       callback_data='show_news')
    site_button = InlineKeyboardButton(text=_('Сайт компании'),
                                       url=urls.SITE)
    my_account_button = InlineKeyboardButton(text=_('Кабинет клиента'),
                                             url=urls.MY_ACCOUNT)
    # production_button = InlineKeyboardButton(text=_('Наша продукция'),
    #                                          callback_data='production')
    production_button = InlineKeyboardButton(text=_('Наша продукция'),
                                             url=urls.PRODUCTS)
    services_button = InlineKeyboardButton(text=_('Наши услуги'),
                                           callback_data='services')
    # manager_chat_button = InlineKeyboardButton(text=_('Задать вопрос менеджеру'),
    #                                            callback_data='ask_question')
    manager_chat_button = InlineKeyboardButton(text=_('Задать вопрос менеджеру'),
                                               callback_data='chat_with_manager')
    contacts_button = InlineKeyboardButton(text=_('Наши контакты'),
                                           callback_data='contacts')
    about_us_button = InlineKeyboardButton(text=_('О нас'),
                                           callback_data='about_us')

    markup_main = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [news_button],
        [site_button, my_account_button],
        [production_button, services_button],
        [manager_chat_button],
        [contacts_button],
        [about_us_button]
    ], )
    return markup_main


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
def get_markup_my_profile() -> InlineKeyboardMarkup:
    set_phone_button = InlineKeyboardButton(text=_('Изменить телефон'),
                                            callback_data='get_user_phone')
    set_email_button = InlineKeyboardButton(text=_('Изменить email'),
                                            callback_data='get_user_email')
    set_company_name_button = InlineKeyboardButton(text=_('Изменить название компании'),
                                                   callback_data='get_user_company')
    set_password_button = InlineKeyboardButton(text=_('Изменить пароль'),
                                               callback_data='get_user_password')
    set_language_button = InlineKeyboardButton(text=_('Изменить язык'),
                                               callback_data='get_user_language')

    markup_my_profile = InlineKeyboardMarkup(inline_keyboard=[
        [set_phone_button, set_email_button],
        [set_company_name_button],
        [set_language_button],
        [set_password_button],
    ], )
    return markup_my_profile


# Клавиатура новости
prev_button = InlineKeyboardButton(text='⬅', callback_data='prev_news')
details_button = InlineKeyboardButton(text='Больше новостей на сайте', url=urls.NEWS)
next_button = InlineKeyboardButton(text='➡', callback_data='next_news')

markup_news = InlineKeyboardMarkup(inline_keyboard=[
    [prev_button, next_button],
    [details_button],
    [button_back_to_main_menu],
])

# Клавиатура языки
ru_button = InlineKeyboardButton(text='Русский', callback_data='ru_language')
en_button = InlineKeyboardButton(text='English', callback_data='en_language')
uk_button = InlineKeyboardButton(text='Українська', callback_data='uk_language')

markup_languages = InlineKeyboardMarkup(inline_keyboard=[
    [uk_button],
    [ru_button],
    [en_button],
])
