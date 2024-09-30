from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _


def get_markup_main_menu() -> ReplyKeyboardMarkup:
    main_menu_ubtn = KeyboardButton(text=_("Головне меню"))
    my_profile_ubtn = KeyboardButton(text=_("Мій профіль"))

    markup_main_menu = ReplyKeyboardMarkup(keyboard=[
        [main_menu_ubtn],
        [my_profile_ubtn],
    ], resize_keyboard=True, one_time_keyboard=False)
    return markup_main_menu


def get_markup_admin_main_menu() -> ReplyKeyboardMarkup:
    main_menu_abtn = KeyboardButton(text=_("Головне меню"))
    admin_panel_abtn = KeyboardButton(text=_("Меню адміністратора"))
    manager_panel_abtn = KeyboardButton(text=_("Меню менеджера"))
    my_profile_abtn = KeyboardButton(text=_("Мій профіль"))
    markup_admin_main_menu = ReplyKeyboardMarkup(keyboard=[
        [main_menu_abtn],
        [admin_panel_abtn, manager_panel_abtn],
        [my_profile_abtn],
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup_admin_main_menu


def get_markup_manager_main() -> ReplyKeyboardMarkup:
    main_menu_mbtn = KeyboardButton(text=_("Головне меню"))
    manager_panel_mbtn = KeyboardButton(text=_("Меню менеджера"))
    my_profile_mbtn = KeyboardButton(text=_("Мій профіль"))
    markup_manager_main = ReplyKeyboardMarkup(keyboard=[
        [main_menu_mbtn],
        [manager_panel_mbtn],
        [my_profile_mbtn],
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup_manager_main


def get_markup(user_id: int, admins_id: List = (), managers_id: List = ()) -> ReplyKeyboardMarkup:
    if user_id in admins_id:
        return get_markup_admin_main_menu()
    elif user_id in managers_id:
        return get_markup_manager_main()
    else:
        return get_markup_main_menu()
