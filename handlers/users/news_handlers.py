import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import keyboards.inline.user_keyboards as ukb
from loader import dp
from utils.db_api import database
from utils.http_api import site_api

db = database.DBCommands()


@dp.callback_query_handler(text_contains='show_news')
async def show_news(call: CallbackQuery, state: FSMContext):
    # возможно переделать функционал через heapq - https://t.me/python_tricks/56
    # что-бы отображалось только 3-5 последних новостей
    user_language = await db.get_language()
    data = dict(await state.get_data("list_news"))
    if data:
        all_news = data["list_news"]
    else:
        user_language = await db.get_language()
        all_news = await site_api.get_news(language=user_language)
        all_news = all_news[:5]  # опоределяет кол-во последних новостей
    news = all_news[0]
    await state.set_data({"list_news": all_news})
    text = f'<b>{news["title"]}</b>\n' \
           f'{datetime.datetime.fromtimestamp(int(news["created"])).strftime("%d-%m-%Y")}\n' \
           f'{site_api.get_link_with_language(user_language, news["api_link"])}'
    text = text.replace("</p>", "").replace("<p>", "")
    await call.message.edit_text(text=text, reply_markup=ukb.get_markup_news(user_language))


@dp.callback_query_handler(text_contains='next_news')
async def next_news(call: CallbackQuery, state: FSMContext):
    data = dict(await state.get_data("list_news"))
    all_news = data["list_news"]
    all_news.append(all_news.pop(0))  # сдвигает элементы списка влево на 1
    await state.set_data({"list_news": all_news})
    await show_news(call, state)


@dp.callback_query_handler(text_contains='prev_news')
async def prev_news(call: CallbackQuery, state: FSMContext):
    data = dict(await state.get_data("list_news"))
    all_news = data["list_news"]
    all_news.insert(0, all_news.pop())  # сдвигает элементы списка вправо на 1
    await state.set_data({"list_news": all_news})
    await show_news(call, state)
