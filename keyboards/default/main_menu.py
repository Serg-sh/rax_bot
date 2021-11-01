from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loader import _

main_menu = KeyboardButton(text='Главное меню')
admin_panel = KeyboardButton(text='Панель администратора')
manager_panel = KeyboardButton(text='Панель менеджера')
my_profile = KeyboardButton(text='Мой профиль')

markup_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [my_profile],
], resize_keyboard=True, one_time_keyboard=False)

markup_admin_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [admin_panel, manager_panel],
    [my_profile],
], resize_keyboard=True, one_time_keyboard=True)

markup_manager_main = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [manager_panel],
    [my_profile],
], resize_keyboard=True, one_time_keyboard=True)
