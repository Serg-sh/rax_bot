from aiogram.utils import executor
import middlewares
import filters
import handlers
from loader import dp
from utils.db_api.database import create_db
from utils.http_api import site_api
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Сождаем БД
    await create_db()

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Добавляем новые новости в базу бота
    await site_api.get_news()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
