import random

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import SITE, MY_ACCOUNT, NEWS, PRODUCTS
from loader import _, dp
from utils.database.queryes import UserDBQuery
from utils.http.site_api import get_link_with_language

db = UserDBQuery()


class ChatCallback(CallbackData, prefix="my"):
    # ask_chat: str
    messages: str
    user_id: int
    as_user: str


class CancelCallback(CallbackData, prefix="my"):
    cancel_chat: str
    user_id: int


class InlineKeyboardUser:

    # Клавиатура основного меню
    def get_markup_main(self) -> InlineKeyboardMarkup:
        news_button = InlineKeyboardButton(text=_('Наші новини'),
                                           callback_data='show_news')
        site_button = InlineKeyboardButton(text=_('Наш сайт'),
                                           url=SITE)
        my_account_button = InlineKeyboardButton(text=_('Кабінет клієнта'),
                                                 web_app=WebAppInfo(url=MY_ACCOUNT))
        production_button = InlineKeyboardButton(text=_('Наша продукція'),
                                                 web_app=WebAppInfo(url=PRODUCTS))
        services_button = InlineKeyboardButton(text=_('Наші послуги'),
                                               callback_data='services')
        manager_chat_button = InlineKeyboardButton(text=_('Запит до менеджера'),
                                                   callback_data='message_to_manager')
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

    # Клавиатура мой профиль
    def get_markup_my_profile(self) -> InlineKeyboardMarkup:
        set_phone_button = InlineKeyboardButton(text=_("Змінити № телефону"),
                                                callback_data='get_user_phone')
        set_email_button = InlineKeyboardButton(text=_("Змінити email"),
                                                callback_data='get_user_email')
        set_company_name_button = InlineKeyboardButton(text=_("Змінити назву компанії"),
                                                       callback_data='get_user_company')
        set_password_button = InlineKeyboardButton(text=_("Змінити пароль"),
                                                   callback_data='get_user_password')
        set_language_button = InlineKeyboardButton(text=_("Змінити мову"),
                                                   callback_data='get_user_language')

        markup_my_profile = InlineKeyboardMarkup(inline_keyboard=[
            [set_phone_button, set_email_button],
            [set_company_name_button],
            [set_language_button],
            [set_password_button],
        ], )
        return markup_my_profile

    # Клавіатура вибору мови
    def get_markup_languages(self) -> InlineKeyboardMarkup:
        en_button = InlineKeyboardButton(text='English', callback_data='en_language')
        uk_button = InlineKeyboardButton(text='Українська', callback_data='uk_language')

        markup_languages = InlineKeyboardMarkup(inline_keyboard=[
            [uk_button],
            [en_button],
        ])
        return markup_languages


class InlineKeyboardBack:
    # Клавиатура назад в меню
    def get_markup_to_main_menu(self) -> InlineKeyboardMarkup:
        button_back_to_main = InlineKeyboardButton(text=_('Назад у меню'),
                                                   callback_data='back_to_main_menu')

        markup_to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
            [button_back_to_main]
        ])
        return markup_to_main_menu


class InlineKeyboardNews:
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


class InlineKeyboardMailing:
    # Клавіатура для розсилок

    def get_markup_mailing(self) -> InlineKeyboardMarkup:
        confirm_button = InlineKeyboardButton(text=f"{_('Розіслати розсилку')}",
                                              callback_data='confirm_mailing')
        cancel_button = InlineKeyboardButton(text=_('Відмінити'),
                                             callback_data='cancel_mailing')
        markup_mailing = InlineKeyboardMarkup(inline_keyboard=[
            [cancel_button, confirm_button],

        ])
        return markup_mailing

    def get_markup_lang_mailing(self) -> InlineKeyboardMarkup:
        all_clients = InlineKeyboardButton(text=_('Для всіх користувачів'), callback_data='all_clients_mailing')
        uk_clients = InlineKeyboardButton(text='Українська', callback_data='uk_clients_mailing')
        en_clients = InlineKeyboardButton(text='English', callback_data='en_clients_mailing')
        markup_lang_mailing = InlineKeyboardMarkup(inline_keyboard=[
            [all_clients],
            [uk_clients, en_clients],
        ])
        return markup_lang_mailing


class InlineKeyboardChat:
    # Клавіатури чату з менеджером

    async def check_busy_manager(self, manager_id):
        # state = dp.current_state(chat=manager_id, user=manager_id)
        state = dp.message.__getstate__()
        state_str = str(state)
        if state_str == 'in_chat':
            return
        else:
            return manager_id

    async def get_id_manager(self) -> InlineKeyboardMarkup:
        managers_id = await db.get_managers_user_id()
        random.shuffle(managers_id)
        for manager_id in managers_id:
            manager_id = await self.check_busy_manager(manager_id)
            if manager_id:
                return manager_id
            else:
                return

    async def chat_keyboard(self, messages, user_id=None):
        managers_id = await db.get_managers_user_id()
        if user_id:
            contact_id = int(user_id)
            as_user = 'no'
            text = f"{_('Відповісти користувачу')}"
        else:
            contact_id = await self.get_id_manager()
            as_user = 'yes'
            if messages == 'many' and contact_id is None:
                return False
            elif messages == 'one' and contact_id is None:
                contact_id = random.choice(managers_id)

            if messages == 'one':
                text = f"{_('Відправити питання менеджеру')}"
            else:
                text = f"{_('Почати чат з менеджером')}"

        chat_callback = ChatCallback(messages=messages, user_id=contact_id, as_user=as_user).pack()
        cancel_chat_callback = CancelCallback(cancel_chat='cancel_chat', user_id=contact_id).pack()

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text,
                                                                               callback_data=chat_callback
                                                                               )],
                                                         [InlineKeyboardButton(text=f"{_('Завершити чат')}",
                                                                               callback_data=cancel_chat_callback
                                                                               )]
                                                         ]
                                        )

        if messages == 'many':
            # Кнопка завершения сеанса, если передумали

            cancel_chat_callback = CancelCallback(user_id=contact_id).pack()

            keyboard.add(InlineKeyboardButton(text=f"{_('Завершити чат')}",
                                              callback_data=cancel_chat_callback
                                              )
                         )

        return keyboard

    def cancel_chat(self, user_id):
        cancel_chat_callback = CancelCallback(user_id=user_id).pack()
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{_('Завершити чат')}",
                                     callback_data=cancel_chat_callback)
            ]
        ]
        )
