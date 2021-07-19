from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/menu - Главаное меню",
            "/admin_panel - Панель администратора",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))
