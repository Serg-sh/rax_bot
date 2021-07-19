from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = KeyboardButton(text='Главное меню')
admin_panel = KeyboardButton(text='Панель администратора')

markup_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
], resize_keyboard=True, one_time_keyboard=True)

markup_admin_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
    [admin_panel],
], resize_keyboard=True, one_time_keyboard=True)