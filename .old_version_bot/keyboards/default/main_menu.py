from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loader import _


def get_markup_main_menu() -> ReplyKeyboardMarkup:
    main_menu_ubtn = KeyboardButton(text=_('Главное меню'))
    my_profile_ubtn = KeyboardButton(text=_('Мой профиль'))

    markup_main_menu = ReplyKeyboardMarkup(keyboard=[
        [main_menu_ubtn],
        [my_profile_ubtn],
    ], resize_keyboard=True, one_time_keyboard=False)
    return markup_main_menu


def get_markup_admin_main_menu() -> ReplyKeyboardMarkup:
    main_menu_abtn = KeyboardButton(text=_('Главное меню'))
    admin_panel_abtn = KeyboardButton(text=_('Панель администратора'))
    manager_panel_abtn = KeyboardButton(text=_('Панель менеджера'))
    my_profile_abtn = KeyboardButton(text=_('Мой профиль'))

    markup_admin_main_menu = ReplyKeyboardMarkup(keyboard=[
        [main_menu_abtn],
        [admin_panel_abtn, manager_panel_abtn],
        [my_profile_abtn],
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup_admin_main_menu


def get_markup_manager_main() -> ReplyKeyboardMarkup:
    main_menu_mbtn = KeyboardButton(text=_('Главное меню'))
    manager_panel_mbtn = KeyboardButton(text=_('Панель менеджера'))
    my_profile_mbtn = KeyboardButton(text=_('Мой профиль'))

    markup_manager_main = ReplyKeyboardMarkup(keyboard=[
        [main_menu_mbtn],
        [manager_panel_mbtn],
        [my_profile_mbtn],
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup_manager_main
