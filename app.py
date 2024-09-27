import asyncio

from loader import dp, bot
from aiogram.types.bot_command import BotCommand
from utils.db_api.database import create_db
from utils.notify_admins import on_startup_notify

async def on_startup(dispatcher):
    print(" Bot Started!")

    # Создаем БД
    await create_db()

    # Устанавливаем дефолтные команды
    await bot.set_my_commands([BotCommand(command="start", description="Запустити бота"),
                               BotCommand(command="help", description="Допомога"),
                               ])


    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Добавляем новые новости в базу бота
    # await site_api.get_news()

async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
