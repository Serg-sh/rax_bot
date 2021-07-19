import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.config import MANAGERS
from loader import dp

chat_callback = CallbackData('ask_chat', 'messages', 'user_id', 'as_user')
cancel_chat_callback = CallbackData('cancel_chat', 'user_id')


async def check_busy_manager(manager_id):
    state = dp.current_state(chat=manager_id, user=manager_id)
    state_str = str(
        await state.get_state()
    )
    if state_str == 'in_chat':
        return
    else:
        return manager_id


async def get_id_manager():
    random.shuffle(MANAGERS)
    for manager_id in MANAGERS:
        manager_id = await check_busy_manager(manager_id)
        if manager_id:
            return manager_id
    else:
        return


async def chat_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = 'no'
        text = 'Ответить пользователю'
    else:
        contact_id = await get_id_manager()
        as_user = 'yes'
        if messages == 'many' and contact_id is None:
            return False
        elif messages == 'one' and contact_id is None:
            contact_id = random.choice(MANAGERS)

        if messages == 'one':
            text = 'Написать 1 сообщение менеджеру'
        else:
            text = 'Начать чат с менеджером'

    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=text,
                                      callback_data=chat_callback.new(messages=messages,
                                                                      user_id=contact_id,
                                                                      as_user=as_user)
                                      )
                 )

    if messages == 'many':
        # Добавляем кнопку завершения сеанса, если передумали
        keyboard.add(InlineKeyboardButton(text='Завершить сеанс',
                                          callback_data=cancel_chat_callback.new(user_id=contact_id)
                                          )
                     )

    return keyboard


def cancel_chat(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Завершить сеанс',
                                     callback_data=cancel_chat_callback.new(user_id=user_id))
            ]
        ]
    )
