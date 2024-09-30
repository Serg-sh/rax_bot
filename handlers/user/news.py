from datetime import datetime

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboard.inline.user_kb import InlineKeyboardNews
from utils.database.models import User
from utils.database.queryes import UserDBQuery
from utils.http.site_api import get_news, get_link_with_language

db = UserDBQuery()
news_router = Router()
kb_news = InlineKeyboardNews()


@news_router.callback_query(F.data == "show_news")
async def show_news(call: CallbackQuery, state: FSMContext):
    user: User = await db.get_user(call.from_user.id)
    user_language = user.languages
    data = dict(await state.get_data())

    if data:
        all_news = data["list_news"]
    else:
        all_news = await get_news(language=user_language)
        all_news = all_news[:5]  # кількість останніх новин

    news = all_news[0]

    await state.set_data({"list_news": all_news})

    text = f'<b>{news["title"]}</b>\n' \
           f'{datetime.fromtimestamp(int(news["created"])).strftime("%d-%m-%Y")}\n' \
           f'{get_link_with_language(user_language, news["api_link"])}'
    text = text.replace("</p>", "").replace("<p>", "")
    await call.message.edit_text(text=text, reply_markup=kb_news.get_markup_news(user_language), parse_mode="HTML")


@news_router.callback_query(F.data == 'next_news')
async def next_news(call: CallbackQuery, state: FSMContext):
    data = dict(await state.get_data())
    all_news = data['list_news']
    all_news.append(all_news.pop(0))  # зсуває елементи спуску вліво на 1
    await state.set_data({"list_news": all_news})
    await show_news(call, state)


@news_router.callback_query(F.data == 'prev_news')
async def prev_news(call: CallbackQuery, state: FSMContext):
    data = dict(await state.get_data())
    all_news = data["list_news"]
    all_news.insert(0, all_news.pop())  # зсуває елементи спуску вправо на 1
    await state.set_data({"list_news": all_news})
    await show_news(call, state)
