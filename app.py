import asyncio

from loader import dp, bot

from utils.db_api.database import create_db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    print(" Bot Started!")

    # Создаем БД
    await create_db()

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Добавляем новые новости в базу бота
    # await site_api.get_news()

async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
