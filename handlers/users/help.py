from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, _


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (f'{_("Список команд")}: ',
            f'/start - {_("Запустить бота")}',
            f'/menu - {_("Главаное меню")}',
            f'/admin - {_("Панель администратора")}',
            f'/manager - {_("Панель менеджера")}',
            f'/help - {_("Получить справку")}',
            f'<b>ver. 1.2.1</b>')
    
    await message.answer("\n".join(text))
