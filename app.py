import asyncio
from typing import List

from aiogram import Router
from aiogram.types.bot_command import BotCommand

from handlers.admin.admin import admin_router
from handlers.manager.managers import managers_router
from handlers.user.about import about_router
from handlers.user.contacts import contact_router
from handlers.user.default_commands import command_router
from handlers.user.echo import echo_router
from handlers.user.mailing import mailing_router
from handlers.user.my_profile import my_profile_route
from handlers.user.news import news_router
from handlers.user.services import services_router
from handlers.user.users import user_router
from loader import dp, bot, _
from utils.database.database import create_db

# встановлюємо роутери
my_routers: List[Router] = [echo_router,
                            command_router,
                            user_router,
                            news_router,
                            my_profile_route,
                            contact_router,
                            about_router,
                            services_router,
                            managers_router,
                            mailing_router,
                            admin_router,
                            ]

dp.include_routers(*my_routers[::-1])


async def on_startup(dispatcher):
    print(" Bot Started!")

    # Создаем БД
    await create_db()

    # Устанавливаем дефолтные команды
    await bot.set_my_commands([
        BotCommand(command="start", description=_("Запустити бота")),
        BotCommand(command="admin", description=_("Панель адміністратора")),
        BotCommand(command="manager", description=_("Панель менеджера")),
        BotCommand(command="help", description=_("Допомога")),
    ])


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
