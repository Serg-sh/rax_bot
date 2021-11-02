# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


def get_markup_admin_main() -> InlineKeyboardMarkup:
    production_button = InlineKeyboardButton(text=_('Наша продукция'),
                                             callback_data='production')
    mailing_button_for_clients = InlineKeyboardButton(text=_('Создать рассылку для клиентов'),
                                                      callback_data='clients_mailing')
    mailing_button_for_admins = InlineKeyboardButton(text=_('Рассылка для админов'),
                                                     callback_data='admins_mailing')
    mailing_button_for_managers = InlineKeyboardButton(text=_('Рассылка для менеджеров'),
                                                       callback_data='managers_mailing')
    statistics_button = InlineKeyboardButton(text=_('Статистика бота'),
                                             callback_data='bot_statistics')
    add_admin_button = InlineKeyboardButton(text=_('Добавить администратора'),
                                            callback_data='add_admin')
    add_manager_button = InlineKeyboardButton(text=_('Добавить менеджера'),
                                              callback_data='add_manager')

    markup_admin_main = InlineKeyboardMarkup(inline_keyboard=[
        [production_button],
        [mailing_button_for_clients],
        [mailing_button_for_admins, mailing_button_for_managers],
        [statistics_button],
        [add_admin_button, add_manager_button],
    ], )
    return markup_admin_main


# Кнопка назад в меню администратора
def get_markup_to_admin_menu() -> InlineKeyboardMarkup:
    button_back_to_admin_menu = InlineKeyboardButton(text=_('Назад в админ-меню'),
                                                     callback_data='back_to_admin_menu')

    markup_to_admin_menu = InlineKeyboardMarkup(inline_keyboard=[
        [button_back_to_admin_menu]
    ])
    return markup_to_admin_menu


# показать всех пользователей
def get_markup_show_all_users() -> InlineKeyboardMarkup:
    button_show_all_users = InlineKeyboardButton(text=_('Показать всех пользователей'),
                                                 callback_data='show_all_user')

    markup_show_all_users = InlineKeyboardMarkup(inline_keyboard=[
        [button_show_all_users]
    ])
    return markup_show_all_users
