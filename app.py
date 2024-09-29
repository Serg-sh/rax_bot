import asyncio
from typing import List

from aiogram import Router
from aiogram.types.bot_command import BotCommand

from handlers.user.default_commands import command_router
from handlers.user.echo import echo_router
from loader import dp, bot, _
from utils.database.database import create_db

# встановлюємо роутери
my_routers: List[Router] = [echo_router,
                            command_router, ]

dp.include_routers(*my_routers[::-1])


async def on_startup(dispatcher):
    print(" Bot Started!")

    # Создаем БД
    await create_db()

    # Устанавливаем дефолтные команды

    await bot.set_my_commands([BotCommand(command="start", description=_("Запустити бота")),
                               BotCommand(command="help", description=_("Допомога")),
                               ])


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
