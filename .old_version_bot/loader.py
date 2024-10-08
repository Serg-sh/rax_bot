from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import gettext as get_text
from aiogram.fsm.storage.memory import MemoryStorage
from data import config
from middlewares.chat_middleware import ChatMiddleware
from middlewares.language_middleware import setup_middleware
from middlewares.throttling import ThrottlingMiddleware
from utils.set_bot_commands import set_default_commands

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
# bot = set_default_commands(bot)
dp = Dispatcher(storage=storage)

# dp.update.middleware(setup_middleware())
dp.update.middleware(ThrottlingMiddleware())
dp.update.middleware(ChatMiddleware())

_ = get_text
