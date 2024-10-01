import bcrypt
import validators
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboard.inline.user_kb import InlineKeyboardUser
from states.states import SetUserProfile
from utils.database.models import User
from utils.database.queryes import UserDBQuery
from loader import _


my_profile_route = Router()
db = UserDBQuery()
user_kb = InlineKeyboardUser()


@my_profile_route.callback_query(F.data == 'my_profile')
@my_profile_route.message(F.text == 'Мій профіль')
@my_profile_route.message(F.text == 'My profile')
async def show_my_profile(message: Message):
    user_id = int(message.from_user.id)
    user = await db.get_user(user_id)
    await message.answer(text=print_user_info(user),
                         reply_markup=user_kb.get_markup_my_profile(),
                         parse_mode="HTML")


def print_user_info(user: User) -> str:
    return f'<b>{_("ИД")}: </b>{user.user_id}\n' \
           f'<b>{_("Имя")}: </b>{user.full_name}\n' \
           f'<b>{_("Язык")}: </b>{user.languages}\n' \
           f'<b>{_("Телефон")}: </b>{(user.phone if user.phone else _("Відсутній"))}\n' \
           f'<b>{_("Email")}: </b>{(user.email if user.email else _("Відсутній"))}\n' \
           f'<b>{_("Компания")}: </b>{(user.company_name if user.company_name else _("Не вказано"))}\n' \
           f'<b>{_("Пароль")}: </b>{(_("Встановлений") if user.password else _("Відсутній"))}\n'


async def check_user_data(user_id):
    user = await db.get_user(user_id)
    return not user.phone or not user.email or not user.company_name


# Изменение телефона в профиле
@my_profile_route.callback_query(F.data == 'get_user_phone')
async def get_user_phone(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text=_('Надішліть Ваш контактний № телефону'))
    await state.set_state(SetUserProfile.GetPhone)


@my_profile_route.message(StateFilter(SetUserProfile.GetPhone))
async def set_user_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.clear()
    await db.update_user(message.from_user.id,phone=phone)
    await message.answer(text=f'{_("№ тел.:")} {phone} {_("успішно додан до Вашого профілю")}')
    await show_my_profile(message)


# Зміна мови
@my_profile_route.callback_query(F.data == 'get_user_language')
async def get_user_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text=f'<b>{_("Виберіть мову")}</b>',
                              reply_markup=user_kb.get_markup_languages(),
                              parse_mode="HTML")


async def change_lang(call: CallbackQuery, language: str):
    await call.message.edit_reply_markup()
    await db.update_user(call.from_user.id, languages=language)
    user = await db.get_user(call.from_user.id)
    await call.message.edit_text(_('Мій профіль'))
    await call.message.answer(text=print_user_info(user),
                              reply_markup=user_kb.get_markup_my_profile(),
                              parse_mode="HTML")
    await call.message.answer(text=f'<b>{_("Мова успішно змінена")}</b>\n'
                                   f'<b>{_("Натисніть /start для застосування налаштунків")}.</b>',
                              parse_mode="HTML")


@my_profile_route.callback_query(F.data == 'uk_language')
async def set_user_lang_uk(call: CallbackQuery):
    await change_lang(call, 'uk')


@my_profile_route.callback_query(F.data == 'en_language')
async def set_user_lang_en(call: CallbackQuery):
    await change_lang(call, 'en')


# Зміна email
@my_profile_route.callback_query(F.data == 'get_user_email')
async def get_user_email(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text=_('Надішліть Ваш email'))
    await state.set_state(SetUserProfile.GetEmail)


@my_profile_route.message(StateFilter(SetUserProfile.GetEmail))
async def set_user_email(message: Message, state: FSMContext):
    email = message.text
    await state.clear()
    if validators.email(email):
        await db.update_user(message.from_user.id, email=email)
        await message.answer(text=f'Email {email} {_("успішно додан до Вашого профілю")}')
    else:
        await message.answer(text=f"{_('Ви надіслали недійсний email')}!")

    await show_my_profile(message)


# Зміна назви компанії
@my_profile_route.callback_query(F.data == 'get_user_company')
async def get_user_company(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text=_('Надішліть назву Вашої компанії'))
    await state.set_state(SetUserProfile.GetCompany)


@my_profile_route.message(StateFilter(SetUserProfile.GetCompany))
async def set_user_company(message: Message, state: FSMContext):
    company_name = message.text
    await state.clear()
    await db.update_user(message.from_user.id, company_name=company_name)
    await message.answer(text=f'{company_name} {_("успішно додан до Вашого профілю")}')
    await show_my_profile(message)


# Зміна пароля
@my_profile_route.callback_query(F.data == 'get_user_password')
async def get_user_password(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text=_('Надішліть Ваш пароль'))
    await state.set_state(SetUserProfile.GetPassword)


@my_profile_route.message(StateFilter(SetUserProfile.GetPassword))
async def set_user_password(message: Message, state: FSMContext):
    await state.clear()
    password = message.text
    # шифрування пароля (хеш пароля + соль)
    hash_and_salt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # запись пароля в базу
    await db.update_user(message.from_user.id, password=hash_and_salt)

    await message.answer(text=_('Пароль успішно змінено'))
    # для примера проверки пароля взят input()
    # user = await db.get_user(types.User.get_current().id)
    # print('Пароль:')
    # valid = bcrypt.checkpw(input().encode(), user.password)
    # print(valid)

    await show_my_profile(message)