import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.db_api import database
from loader import _

chat_callback = CallbackData('ask_chat', 'messages', 'user_id', 'as_user')
cancel_chat_callback = CallbackData('cancel_chat', 'user_id')

db = database.DBCommands()


async def check_busy_manager(manager_id):
    state = dp.current_state(chat=manager_id, user=manager_id)
    state_str = str(await state.get_state())
    if state_str == 'in_chat':
        return
    else:
        return manager_id


async def get_id_manager():
    managers_id = await db.get_managers_user_id()
    random.shuffle(managers_id)
    for manager_id in managers_id:
        manager_id = await check_busy_manager(manager_id)
        if manager_id:
            return manager_id
        else:
            return


async def chat_keyboard(messages, user_id=None) -> InlineKeyboardMarkup:
    managers_id = await db.get_managers_user_id()
    if user_id:
        contact_id = int(user_id)
        as_user = 'no'
        text = _('Ответить пользователю')
    else:
        contact_id = await get_id_manager()
        as_user = 'yes'
        if messages == 'many' and contact_id is None:
            return False
        elif messages == 'one' and contact_id is None:
            contact_id = random.choice(managers_id)

        if messages == 'one':
            text = _('Написать 1 сообщение менеджеру')
        else:
            text = _('Начать чат с менеджером')

    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=text,
                                      callback_data=chat_callback.new(messages=messages,
                                                                      user_id=contact_id,
                                                                      as_user=as_user)
                                      )
                 )

    if messages == 'many':
        # Кнопка завершения сеанса, если передумали
        keyboard.add(InlineKeyboardButton(text=_('Завершить сеанс'),
                                          callback_data=cancel_chat_callback.new(user_id=contact_id)
                                          )
                     )

    return keyboard


def cancel_chat(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_('Завершить сеанс'),
                                 callback_data=cancel_chat_callback.new(user_id=user_id))
        ]
    ]
    )
