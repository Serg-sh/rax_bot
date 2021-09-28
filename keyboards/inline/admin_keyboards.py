# Клавиатура основного меню
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

production_button = InlineKeyboardButton(text='Наша продукция', callback_data='production')
mailing_button_for_clients = InlineKeyboardButton(text='Создать рассылку для клиентов',
                                                  callback_data='clients_mailing')
mailing_button_for_admins = InlineKeyboardButton(text='Рассылка для админов',
                                                 callback_data='admins_mailing')
mailing_button_for_managers = InlineKeyboardButton(text='Рассылка для менеджеров',
                                                   callback_data='managers_mailing')
statistics_button = InlineKeyboardButton(text='Статистика бота', callback_data='bot_statistics')
add_admin_button = InlineKeyboardButton(text='Добавить администратора', callback_data='add_admin')
add_manager_button = InlineKeyboardButton(text='Добавить менеджера', callback_data='add_manager')

markup_admin_main = InlineKeyboardMarkup(inline_keyboard=[
    [production_button],
    [mailing_button_for_clients],
    [mailing_button_for_admins, mailing_button_for_managers],
    [statistics_button],
    [add_admin_button, add_manager_button],
], )

# Кнопка назад в меню администратора
button_back_to_admin_menu = InlineKeyboardButton(text='Назад в админ-меню', callback_data='back_to_admin_menu')
markup_to_admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [button_back_to_admin_menu]
])

# показать всех пользователей
button_show_all_users = InlineKeyboardButton(text='Показать всех пользователей', callback_data='show_all_user')
markup_show_all_users = InlineKeyboardMarkup(inline_keyboard=[
    [button_show_all_users]
])