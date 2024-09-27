from aiogram import Bot, Dispatcher
from aiogram.types.bot_command import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

import config

bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())


async def on_startup(dispatcher):
    print(" Bot Started!")

    # Создаем БД
    await create_db()

    # Устанавливаем дефолтные команды
    await bot.set_my_commands([BotCommand(command="start", description="Запустити бота"),
                               BotCommand(command="help", description="Допомога"),
                               ])