from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboard.inline.user_kb import InlineKeyboardChat, ChatCallback
from loader import _, bot
from utils.database.queryes import UserDBQuery

db = UserDBQuery()
message_to_manager_router = Router()
chat_kb = InlineKeyboardChat()


@message_to_manager_router.callback_query(F.data == 'message_to_manager')
async def ask_manager(call: CallbackQuery):
    text = _('Для відправки повідомлення менеджеру натисніть на кнопку')
    keyboard = await chat_kb.chat_keyboard(messages='one')
    await call.message.edit_text(text, reply_markup=keyboard)


@message_to_manager_router.callback_query(ChatCallback.filter(F.messages == 'one'))
async def send_to_manager(call: CallbackQuery, state: FSMContext, callback_data: ChatCallback):
    await call.answer()
    user_id = callback_data.user_id
    await call.message.answer(_('Відправте Ваше питання'))
    await state.set_state('wait_for_ask')
    await state.update_data(second_id=user_id)


@message_to_manager_router.message(StateFilter('wait_for_ask'))
async def get_support_message(message: Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')
    await bot.send_message(second_id,
                           f'{_("Вам прийшло повідомлення")}!\n'
                           f'{_("Для відповіді натисніть кнопку")}')
    keyboard = await chat_kb.chat_keyboard(messages='one', user_id=message.from_user.id)
    await message.answer(f"{_('Повідомлення відправлено, очикуйте відповіді')}")
    await message.copy_to(second_id, reply_markup=keyboard)
    await state.clear()
