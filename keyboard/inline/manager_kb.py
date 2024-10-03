from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


class InlineManagerKB:
    def get_markup_manager_main(self) -> InlineKeyboardMarkup:
        """
        Повертає инлалйн клавіатуру основного меню менеджера
        :return: InlineKeyboardMarkup
        """
        clients_mailing_button = InlineKeyboardButton(text=_('Створити розсилку для користувачів'),
                                                      callback_data='choice_mailing_language',
                                                      parse_mode='HTML')
        managers_mailing_button = InlineKeyboardButton(text=_('Створити розсилку для менеджерів'),
                                                       callback_data='managers_mailing',
                                                       parse_mode='HTML')

        markup_manager_main = InlineKeyboardMarkup(inline_keyboard=[
            [clients_mailing_button],
            [managers_mailing_button],
        ], )
        return markup_manager_main


    # Кнопка назад у меню менеджера
    def get_button_back_to_manager_menu(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=_('Назад у меню менеджера'),
                                    callback_data='back_to_manager_menu',
                                    parse_mode='HTML')

    def get_markup_to_manager_menu(self) -> InlineKeyboardMarkup:
        """
        Повертає клавіатуру з кнопкою назад у меню менеджера
        :return: InlineKeyboardMarkup
        """

        markup_to_manager_menu = InlineKeyboardMarkup(inline_keyboard=[
            [self.get_button_back_to_manager_menu()]
        ])
        return markup_to_manager_menu
