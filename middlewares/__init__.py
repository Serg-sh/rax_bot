from aiogram import Dispatcher

from loader import dp
from .chat_middleware import ChatMiddleware
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ChatMiddleware())
