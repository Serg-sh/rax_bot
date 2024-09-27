from aiogram.types.bot_command import BotCommand


async def set_default_commands(bot):
    return await bot.set_my_commands(
        [
            BotCommand(command='start', description="Запустить бота"),
            BotCommand('menu', "Главное меню"),
            BotCommand('admin', "Панль администратора"),
            BotCommand('manager', "Панль менеджера"),
            BotCommand('help', "Вывести справку"),
        ]

    )
