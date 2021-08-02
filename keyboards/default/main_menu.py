from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = KeyboardButton(text='Главное меню')
admin_panel = KeyboardButton(text='Панель администратора')
manager_panel = KeyboardButton(text='Панель менеджера')

markup_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
], resize_keyboard=True, one_time_keyboard=False)

markup_admin_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [admin_panel],
    [manager_panel],
], resize_keyboard=True, one_time_keyboard=False)

markup_manager_main = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [manager_panel],
], resize_keyboard=True, one_time_keyboard=False)