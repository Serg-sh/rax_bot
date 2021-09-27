from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.my_profile_handlers import check_user_data
from keyboards.inline.chat_keyboards import chat_callback, check_busy_manager, get_id_manager, chat_keyboard, \
    cancel_chat, cancel_chat_callback
from loader import dp, bot


@dp.callback_query_handler(text_contains='chat_with_manager')
async def chat_with_manager(call: CallbackQuery):
    if await check_user_data(call.from_user.id):
        await call.message.answer(f'{call.from_user.full_name}. \n'
                                  f'Для связи с менеджером, укажите контактные данные '
                                  f'в разделе мой профиль.')
        return
    text = 'Для открытия или завершения чата\nСделайте выбор.'
    kb_chat = await chat_keyboard(messages='many')
    if not kb_chat:
        await call.message.answer('В данный момент все менеджеры заняты!\nПопробуйте позже.')
        return
    await call.message.answer(text, reply_markup=kb_chat)


@dp.callback_query_handler(chat_callback.filter(messages='many', as_user='yes'))
async def send_to_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.edit_text('Вы обратились в чат ДДАП-РАКС.\nЖдем ответа менеджера!')

    user_id = int(callback_data.get('user_id'))
    if not await check_busy_manager(user_id):
        manager_id = await get_id_manager()
    else:
        manager_id = user_id

    if not manager_id:
        await call.message.edit_text('К сожалению, сейчас нет свободных менеджеров.\nПопробуйте позже.')
        await state.reset_state()
        return

    await state.set_state('wait_in_chat')
    await state.update_data(second_id=manager_id)

    kb = await chat_keyboard(messages='many', user_id=call.from_user.id)

    await bot.send_message(manager_id,
                           f'С вами хочет связаться пользователь {call.from_user.full_name}',
                           reply_markup=kb
                           )


@dp.callback_query_handler(chat_callback.filter(messages='many', as_user='no'))
async def answer_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    second_id = int(callback_data.get('user_id'))
    user_state = dp.current_state(user=second_id, chat=second_id)

    if str(await user_state.get_state()) != 'wait_in_chat':
        await call.message.edit_text('К сожалению, пользователь уже передумал.')
        return

    await state.set_state('in_chat')
    await user_state.set_state('in_chat')

    await state.update_data(second_id=second_id)

    keyboard = cancel_chat(second_id)
    keyboard_second_user = cancel_chat(call.from_user.id)

    await call.message.edit_text('Вы на связи с пользователем!\n'
                                 'Чтобы завершить общение нажмите на кнопку.',
                                 reply_markup=keyboard)
    await bot.send_message(second_id,
                           'Менеджер на связи! Можете писать сюда свое сообщение. \n'
                           'Чтобы завершить общение нажмите на кнопку.',
                           reply_markup=keyboard_second_user
                           )


@dp.message_handler(state='wait_in_chat', content_types=types.ContentTypes.ANY)
async def not_in_chat(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')

    keyboard = cancel_chat(second_id)
    await message.answer('Дождитесь ответа менеджара или отмените сеанс', reply_markup=keyboard)


@dp.callback_query_handler(cancel_chat_callback.filter(), state=['in_chat', 'wait_in_chat', None])
async def exit_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    user_id = int(callback_data.get('user_id'))
    second_state = dp.current_state(user=user_id, chat=user_id)
    if await second_state.get_state() is not None:
        data_second = await second_state.get_data()
        second_id = data_second.get('second_id')
        if int(second_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, 'Пользователь завершил сеанс')

    await call.message.edit_text('Вы завершили сеанс')
    await state.reset_state()
