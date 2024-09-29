from typing import List

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from config import BOT_TOKEN

from midleware.language import setup_middleware




bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


i18n = setup_middleware()

dp.update.middleware(i18n)


_ = i18n.i18n.gettext


