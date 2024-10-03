from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import _


class InlineKeyboardAdmin:
    def get_button_back_to_admin_menu(self):
        return InlineKeyboardButton(text=f"{_('Назад у адмін меню')}",
                                    callback_data='back_to_admin_menu')

    def get_markup_admin_main(self) -> InlineKeyboardMarkup:
        """
        Возвращает инлайн клавиатуру основного меню администратора
        :return: InlineKeyboardMarkup
        """
        # production_button = InlineKeyboardButton(text=_('Наша продукция'),
        #                                          callback_data='production')
        mailing_button_for_clients = InlineKeyboardButton(text=f"{_('Створити розсилку для користувачів')}",
                                                          callback_data='choice_mailing_language')
        mailing_button_for_admins = InlineKeyboardButton(text=f"{_('Створити розсилку для адмінів')}",
                                                         callback_data='admins_mailing')
        mailing_button_for_managers = InlineKeyboardButton(text=f"{_('Створити розсилку для менеджерів')}",
                                                           callback_data='managers_mailing')
        statistics_button = InlineKeyboardButton(text=f"{_('Статистика боту')}",
                                                 callback_data='bot_statistics')
        add_admin_button = InlineKeyboardButton(text=f"{_('Додати адміністратора')}",
                                                callback_data='add_admin')
        add_manager_button = InlineKeyboardButton(text=f"{_('Додати менеджера')}",
                                                  callback_data='add_manager')

        markup_admin_main = InlineKeyboardMarkup(inline_keyboard=[
            # [production_button],
            [mailing_button_for_clients],
            [mailing_button_for_admins, mailing_button_for_managers],
            [statistics_button],
            [add_admin_button, add_manager_button],
        ], )
        return markup_admin_main


    # Кнопка назад в меню администратора
    def get_markup_to_admin_menu(self) -> InlineKeyboardMarkup:
        """
        Возвращает инлайн клавиатуру с кнопкой назад в меню администратора
        :return: InlineKeyboardMarkup
        """

        markup_to_admin_menu = InlineKeyboardMarkup(inline_keyboard=[
            [self.get_button_back_to_admin_menu()]
        ])
        return markup_to_admin_menu

    # показать всех пользователей
    def get_markup_show_all_users(self) -> InlineKeyboardMarkup:
        """
        Возвращает инлайн клавиатуру с кнопкой показать всех пользователей
        :return: InlineKeyboardMarkup
        """
        button_show_all_users = InlineKeyboardButton(text=f"{_('Показати всіх користувачів')}",
                                                     callback_data='show_all_user')
        button = self.get_button_back_to_admin_menu()

        markup_show_all_users = InlineKeyboardMarkup(inline_keyboard=[
            [button_show_all_users],
            [button],
        ])
        return markup_show_all_users