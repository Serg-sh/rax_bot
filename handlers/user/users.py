from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboard.inline.user_kb import InlineKeyboardUser, InlineKeyboardBack
from loader import _
from utils.database.queryes import UserDBQuery

user_router = Router()
db = UserDBQuery()
user_keyboard = InlineKeyboardUser()
back_keyboard = InlineKeyboardBack()


@user_router.message(F.text == "Головне меню")
@user_router.message(F.text == "Main menu")
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=_('Главное меню'),
                         reply_markup=user_keyboard.get_markup_main())


@user_router.callback_query(F.data == 'back_to_main_menu')
async def back_to_main_menu(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await state.clear()
    await call.message.answer(text=_('Головне меню'), reply_markup=user_keyboard.get_markup_main())