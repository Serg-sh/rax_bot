from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from loader import _

echo_router = Router()


@echo_router.message()
async def bot_echo(message: Message):
    await message.answer(f"{_("Відлуння вашого повідомлення")}.\n <code>{message.text}</code>",
                         parse_mode="HTML")


@echo_router.callback_query()
async def bot_echo_call(call: CallbackQuery):

    text = f'{_("Відлуння вашого callback_query")}.\n' \
           f'{_("Зміст повідомлення")}:\n' \
           f'<code>{call.data.title()}</code>'

    await call.message.answer(text=text, parse_mode="HTML")
