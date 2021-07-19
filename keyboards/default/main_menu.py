from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = KeyboardButton(text='Главное меню')

markup_main_menu = ReplyKeyboardMarkup(keyboard=[
    [main_menu],
], resize_keyboard=True, one_time_keyboard=True)

