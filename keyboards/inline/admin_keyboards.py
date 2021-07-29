# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
mailing_button_for_users = InlineKeyboardButton(text='Создать рассылку для пользователей',
                                                callback_data='users_mailing')
mailing_button_for_admins = InlineKeyboardButton(text='Рассылка для админов',
                                                 callback_data='admins_mailing')
mailing_button_for_managers = InlineKeyboardButton(text='Рассылка для менеджеров',
                                                   callback_data='managers_mailing')
statistics_button = InlineKeyboardButton(text='Статистика бота', callback_data='statistics')
add_admin_button = InlineKeyboardButton(text='Добавить администратора', callback_data='add_admin')
add_manager_button = InlineKeyboardButton(text='Добавить менеджера', callback_data='add_manager')


markup_admin_main = InlineKeyboardMarkup(inline_keyboard=[
    [production_button],
    [mailing_button_for_users],
    [mailing_button_for_admins, mailing_button_for_managers],
    [statistics_button],
    [add_admin_button, add_manager_button],
], )