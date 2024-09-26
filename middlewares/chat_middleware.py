from aiogram import types, BaseMiddleware
from aiogram.dispatcher.event.bases import CancelHandler




class ChatMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        from loader import dp
        # Для начала достанем состояние текущего пользователя,
        # так как state: FSMContext нам сюда не прилетит
        state = dp.current_state(chat=message.from_user.id, user=message.from_user.id)

        # Получим строчное значение стейта и сравним его
        state_str = str(await state.get_state())
        if state_str == 'in_chat':
            # Заберем айди второго пользователя и отправим ему сообщение
            data = await state.get_data()
            second_id = data.get('second_id')
            await message.copy_to(second_id)

            # Не пропустим дальше обработку в хендлеры
            raise CancelHandler()
