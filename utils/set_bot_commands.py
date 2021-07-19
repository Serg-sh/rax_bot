from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', "Запустить бота"),
            types.BotCommand('menu', "Главное меню"),
            types.BotCommand('admin_panel', "Панль администратора"),
            types.BotCommand('help', "Вывести справку"),
        ]
    )
