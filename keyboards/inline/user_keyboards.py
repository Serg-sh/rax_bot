from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, inline_keyboard

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
    production_button = InlineKeyboardButton(text=_('Наша продукция'),
                                             callback_data='productions_menu')
    # production_button = InlineKeyboardButton(text=_('Наша продукция'),
    #                                          url=urls.PRODUCTS)
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


# Клавиатура назад в меню
def get_markup_to_main_menu() -> InlineKeyboardMarkup:
    button_back_to_main = InlineKeyboardButton(text=_('Назад в меню'),
                                               callback_data='back_to_main_menu')

    markup_to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
        [button_back_to_main]
    ])
    return markup_to_main_menu


# Клавиатура чат - сообщение медеджеру
def get_markup_chat_message() -> InlineKeyboardMarkup:
    manager_message_button = InlineKeyboardButton(text=_('Написать 1 сообщение менеджеру'),
                                                  callback_data='message_to_manager')
    manager_chat_button = InlineKeyboardButton(text=_('Начать чат с менеджером'),
                                               callback_data='chat_with_manager')
    button_back_to_main_ = InlineKeyboardButton(text=_('Назад в меню'),
                                                callback_data='back_to_main_menu')

    markup_chat_message = InlineKeyboardMarkup(inline_keyboard=[
        [manager_chat_button],
        [button_back_to_main_]
    ], )
    return markup_chat_message


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
def get_markup_news() -> InlineKeyboardMarkup:
    prev_button = InlineKeyboardButton(text='⬅',
                                       callback_data='prev_news')
    details_button = InlineKeyboardButton(text=_('Больше новостей на сайте'),
                                          url=urls.NEWS)
    next_button = InlineKeyboardButton(text='➡',
                                       callback_data='next_news')
    button_back_to_main_menu = InlineKeyboardButton(text=_('Назад в меню'),
                                                    callback_data='back_to_main_menu')

    markup_news = InlineKeyboardMarkup(inline_keyboard=[
        [prev_button, next_button],
        [details_button],
        [button_back_to_main_menu],
    ])
    return markup_news


# Клавиатура языки
def get_markup_languages() -> InlineKeyboardMarkup:
    ru_button = InlineKeyboardButton(text='Русский', callback_data='ru_language')
    en_button = InlineKeyboardButton(text='English', callback_data='en_language')
    uk_button = InlineKeyboardButton(text='Українська', callback_data='uk_language')

    markup_languages = InlineKeyboardMarkup(inline_keyboard=[
        [uk_button],
        [ru_button],
        [en_button],
    ])
    return markup_languages


# Клавиатура для раздела "продукция"
def get_markup_prod_menu() -> InlineKeyboardMarkup:
    products_on_site_btn = InlineKeyboardButton(text=_('Вся продукция на сайте'), url=urls.PRODUCTS)
    products_uk_sng_btn = InlineKeyboardButton(text=_('Для Украины и СНГ'), callback_data='region_uk_sng')
    products_eu_btn = InlineKeyboardButton(text=_('Для Европы'), callback_data='region_eu')
    products_na_btn = InlineKeyboardButton(text=_('Для Северной Америки'), callback_data='region_na')
    button_back_to_main_menu = InlineKeyboardButton(text=_('Назад в меню'), callback_data='back_to_main_menu')

    markup_prod_menu = InlineKeyboardMarkup(inline_keyboard=[
        [products_on_site_btn],
        [products_uk_sng_btn],
        [products_eu_btn],
        [products_na_btn],
        [button_back_to_main_menu],
    ])
    return markup_prod_menu

