import time
from aiogram import types, BaseMiddleware
from aiogram.dispatcher.event.bases import CancelHandler


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 5):
        self.rate_limit = limit  # Секунди
        self.cache = {}  # Словник для зберігання часу останніх запитів користувачів
        super().__init__()

    async def __call__(self, handler, *args, **kwargs):
        # Виклик оригінального механізму обмеження
        await super().__call__(handler, *args, **kwargs)

    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        current_time = time.time()

        if user_id in self.cache:
            last_time = self.cache[user_id]
            if current_time - last_time < self.rate_limit:
                await message.answer("Занадто часті запити. Повторіть пізніше.")
                raise CancelHandler()

        self.cache[user_id] = current_time
