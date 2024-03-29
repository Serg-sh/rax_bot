from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


def get_markup_manager_main() -> InlineKeyboardMarkup:
    """
    Возвращает инлайн клавиатуру основного меню менеджера
    :return: InlineKeyboardMarkup
    """
    # production_button = InlineKeyboardButton(text=_('Наша продукция'), callback_data='production')
    clients_mailing_button = InlineKeyboardButton(text=_('Создать рассылку для пользователей'),
                                                  callback_data='choice_mailing_language')
    managers_mailing_button = InlineKeyboardButton(text=_('Создать рассылку для менеджеров'),
                                                   callback_data='managers_mailing')

    markup_manager_main = InlineKeyboardMarkup(inline_keyboard=[
        # [production_button],
        [clients_mailing_button],
        [managers_mailing_button],
    ], )
    return markup_manager_main


# Кнопка назад в меню менеджера
def get_button_back_to_manager_menu():
    return InlineKeyboardButton(text=_('Назад в меню менджера'),
                                callback_data='back_to_manager_menu')


def get_markup_to_manager_menu() -> InlineKeyboardMarkup:
    """
    Возвращает инлайн клавиатуру с кнопкой назад в меню менеджера
    :return: InlineKeyboardMarkup
    """

    markup_to_manager_menu = InlineKeyboardMarkup(inline_keyboard=[
        [get_button_back_to_manager_menu()]
    ])
    return markup_to_manager_menu
