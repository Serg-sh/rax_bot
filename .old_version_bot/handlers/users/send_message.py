from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboard.inline.chat_keyboards import chat_keyboard, chat_callback
from loader import dp, bot, _


@dp.callback_query_handler(text_contains='message_to_manager')
async def ask_manager(call: CallbackQuery):
    text = _('Для отправки сообщения менеджеру, нажмите на кнопку ниже!')
    keyboard = await chat_keyboard(messages='one')
    await call.message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(chat_callback.filter(messages='one'))
async def send_to_manager(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get('user_id'))

    await call.message.answer(_('Отпаравьте Ваш вопрос'))
    await state.set_state('wait_for_ask')
    await state.update_data(second_id=user_id)


@dp.message_handler(state='wait_for_ask')
async def get_support_message(message: Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')

    await bot.send_message(second_id,
                           f'{_("Вам пришло сообщение")}!\n'
                           f'{_("Для ответа нажмите кнопку ниже")}')
    keyboard = await chat_keyboard(messages='one', user_id=message.from_user.id)
    await message.answer(_('Сообщение отпрвлено, ожидайте ответа.'))
    await message.copy_to(second_id, reply_markup=keyboard)
    await state.reset_state()

