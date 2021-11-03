from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f'{_("Эхо Вашего сообщения без состояния")}.\n'
                         f'{message.text}')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{_("Эхо в состоянии")} <code>{state}</code>.\n'
                         f'\n{_("Содержание сообщения")}:\n'
                         f'<code>{message}</code>')
