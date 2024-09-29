from aiogram import types, Router

echo_router = Router()


@echo_router.message()
async def bot_echo(message: types.Message):
    await message.answer(f"Відлуння вашого повідомлення.\n <code>{message.text}</code>",
                         parse_mode="HTML")