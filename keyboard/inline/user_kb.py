from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import SITE, MY_ACCOUNT, NEWS
from loader import _
from utils.http.site_api import get_link_with_language


class InlineKeyboardUser():

    # Клавиатура основного меню
    def get_markup_main(self) -> InlineKeyboardMarkup:
        news_button = InlineKeyboardButton(text=_('Наші новини'),
                                           callback_data='show_news')
        site_button = InlineKeyboardButton(text=_('Наш сайт'),
                                           url=SITE)
        my_account_button = InlineKeyboardButton(text=_('Кабінет клієнта'),
                                                 web_app=WebAppInfo(url=MY_ACCOUNT))
        production_button = InlineKeyboardButton(text=_('Наша продукція'),
                                                 callback_data='productions_menu')
        services_button = InlineKeyboardButton(text=_('Наші послуги'),
                                               callback_data='services')
        manager_chat_button = InlineKeyboardButton(text=_('Запит до менеджера'),
                                                   callback_data='chat_with_manager')
        contacts_button = InlineKeyboardButton(text=_('Наші контакти'),
                                               callback_data='contacts')
        about_us_button = InlineKeyboardButton(text=_('Про нас'),
                                               callback_data='about_us')

        markup_main = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
            [news_button],
            [site_button, my_account_button],
            [production_button, services_button],
            [manager_chat_button],
            [contacts_button],
            [about_us_button],
        ], )
        return markup_main


class InlineKeyboardBack():
    # Клавиатура назад в меню
    def get_markup_to_main_menu(self) -> InlineKeyboardMarkup:
        button_back_to_main = InlineKeyboardButton(text=_('Назад у меню'),
                                                   callback_data='back_to_main_menu')

        markup_to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
            [button_back_to_main]
        ])
        return markup_to_main_menu


class InlineKeyboardNews():
    # Клавиатура новости

    def get_markup_news(self, user_language) -> InlineKeyboardMarkup:
        prev_button = InlineKeyboardButton(text='⬅',
                                           callback_data="prev_news")
        details_button = InlineKeyboardButton(text=_("Більше новин на сайті"),
                                              url=get_link_with_language(user_language=user_language,
                                                                                  api_link=NEWS))
        next_button = InlineKeyboardButton(text='➡',
                                           callback_data='next_news')
        button_back_to_main_menu = InlineKeyboardButton(text=_('Назад у меню'),
                                                        callback_data='back_to_main_menu')

        markup_news = InlineKeyboardMarkup(inline_keyboard=[
            [prev_button, next_button],
            [details_button],
            [button_back_to_main_menu],
        ])
        return markup_news
