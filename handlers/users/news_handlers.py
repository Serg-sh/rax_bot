from aiogram.types import CallbackQuery

import keyboards.inline.user_keyboards as ukb
from loader import dp
from utils.db_api import database
from utils.http_api import site_api

db = database.DBCommands()





@dp.callback_query_handler(text_contains='show_news')
async def show_news(call: CallbackQuery, news_id: int = None):
    # возможно переделать функционал через heapq - https://t.me/python_tricks/56
    # что-бы отображалось только 3-5 последних новостей
    user_language = await db.get_language()
    all_news = await db.get_all_news()
    news = all_news[-1]
    if news_id:
        news = await db.get_news(news_id=news_id)
    url_news = site_api.get_link_with_language(user_language, news.api_link)
    text = f'<b>{news.title}</b>\n' \
           f'{url_news}\n' \
           f'ИД: {news.id}'
    await call.message.edit_text(text=text, reply_markup=ukb.get_markup_news())


@dp.callback_query_handler(text_contains='next_news')
async def next_news(call: CallbackQuery):
    news_id = get_news_id(call) - 1
    all_news = await db.get_all_news()
    list_id_news = [news.id for news in all_news]
    while True:
        if await db.get_news(news_id=news_id):
            await show_news(call, news_id=news_id)
            break
        news_id -= 1
        if news_id < list_id_news[0]:
            await show_news(call)
            return


def get_news_id(call):
    text = call.message.text
    text_id = text.find('ИД:')
    news_id = int(text[text_id + 4:])
    return news_id


@dp.callback_query_handler(text_contains='prev_news')
async def prev_news(call: CallbackQuery):
    news_id = get_news_id(call) + 1
    all_news = await db.get_all_news()
    list_id_news = [news.id for news in all_news]
    while True:
        if news_id > list_id_news[-1]:
            await show_news(call, news_id=list_id_news[0])
            return
        if await db.get_news(news_id=news_id):
            await show_news(call, news_id=news_id)
            break
        news_id += 1
