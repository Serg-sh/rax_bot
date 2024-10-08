# from aiogram import Router
# from aiogram.types import CallbackQuery
#
# from keyboard.inline.user_kb import InlineKeyboardUser
# from utils.database.queryes import UserDBQuery
# from loader import _
#
# db = UserDBQuery()
# chat_router = Router()
# user_kb = InlineKeyboardUser()
#
#
# @chat_router.callback_query(F.data == 'chat_with_manager')
# async def chat_with_manager(call: CallbackQuery):
#     if await check_user_data(call.from_user.id):
#         await call.message.answer(text=f'{call.from_user.full_name}. \n'
#                                        f'{_("Для связи с менеджером, укажите контактные данные")} '
#                                        f'{_("в разделе мой профиль")}.',
#                                   reply_markup=ukb.get_markup_main())
#         return
#     text = f'{_("Для открытия или завершения чата")} \n {_("Сделайте выбор")}.'
#     kb_chat = await chat_keyboard(messages='many')
#     if not kb_chat:
#         await call.message.answer(text=f'{_("В данный момент все менеджеры заняты")}!\n {_("Попробуйте позже")}.')
#         return
#     await call.message.answer(text, reply_markup=kb_chat)
#

# @dp.callback_query_handler(chat_callback.filter(messages='many', as_user='yes'))
# async def send_to_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
#     await call.message.edit_text(f'{_("Вы обратились в чат ДДАП-РАКС")}.\n {_("Ждем ответа менеджера")}!')
#
#     user_id = int(callback_data.get('user_id'))
#     if not await check_busy_manager(user_id):
#         manager_id = await get_id_manager()
#     else:
#         manager_id = user_id
#
#     if not manager_id:
#         await call.message.edit_text(f'{_("В данный момент все менеджеры заняты")}.\n {_("Попробуйте позже")}.')
#         await state.reset_state()
#         return
#
#     await state.set_state('wait_in_chat')
#     await state.update_data(second_id=manager_id)
#
#     kb = await chat_keyboard(messages='many', user_id=call.from_user.id)
#     user = await db.get_user(call.from_user.id)
#
#     await bot.send_message(manager_id,
#                            f'{_("С вами хочет связаться пользователь")}:\n'
#                            f'<b>{user.full_name}</b>\n'
#                            f'<b>{_("Компания")}:</b> {user.company_name}\n'
#                            f'<b>{_("Телефон")}.:</b> {user.phone}\n'
#                            f'<b>{_("Email")}:</b> {user.email}',
#                            reply_markup=kb
#                            )
#
#
# @dp.callback_query_handler(chat_callback.filter(messages='many', as_user='no'))
# async def answer_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
#     second_id = int(callback_data.get('user_id'))
#     user_state = dp.current_state(user=second_id, chat=second_id)
#
#     if str(await user_state.get_state()) != 'wait_in_chat':
#         await call.message.edit_text(_('Пользователь завершил сеанс.'))
#         return
#
#     await state.set_state('in_chat')
#     await user_state.set_state('in_chat')
#
#     await state.update_data(second_id=second_id)
#
#     keyboard = cancel_chat(second_id)
#     keyboard_second_user = cancel_chat(call.from_user.id)
#
#     await call.message.edit_text(f'{_("Вы на связи с пользователем")}!\n'
#                                  f'{_("Чтобы завершить общение нажмите на кнопку")}.',
#                                  reply_markup=keyboard)
#     await bot.send_message(second_id,
#                            f'<b>{_("Менеджер")}, {call.from_user.full_name} {_("на связи")}!</b>\n'
#                            f'{_("Можете задать Ваш вопрос")}.'
#                            f'{_("Для закрытия чата с медеджером, нажмите на кнопку")}.',
#                            reply_markup=keyboard_second_user
#                            )
#
#
# @dp.message_handler(state='wait_in_chat', content_types=types.ContentTypes.ANY)
# async def not_in_chat(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     second_id = data.get('second_id')
#
#     keyboard = cancel_chat(second_id)
#     await message.answer(_('Дождитесь ответа менеджара или отмените сеанс'), reply_markup=keyboard)
#
#
# @dp.callback_query_handler(cancel_chat_callback.filter(), state=['in_chat', 'wait_in_chat', None])
# async def exit_chat(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
#     user_id = int(callback_data.get('user_id'))
#     second_state = dp.current_state(user=user_id, chat=user_id)
#     if await second_state.get_state() is not None:
#         data_second = await second_state.get_data()
#         second_id = data_second.get('second_id')
#         if int(second_id) == call.from_user.id:
#             await second_state.reset_state()
#             await bot.send_message(user_id, _('Пользователь завершил сеанс'))
#
#     await call.message.edit_text(_('Вы завершили сеанс'))
#     await state.reset_state()