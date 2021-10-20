from aiogram.types import CallbackQuery

import keyboards.inline.user_keyboards as ukb
from loader import dp
from utils.db_api import database

db = database.DBCommands()


def language_insert(user_language, api_link):
    user_language += '/'
    if user_language == 'en/':
        user_language = ''
    return api_link[:20] + user_language + api_link[20:]


@dp.callback_query_handler(text_contains='show_news')
async def show_news(call: CallbackQuery):
    await call.message.edit_reply_markup()
    user_language = await db.get_language()
    all_news = await db.get_all_news()
    news = all_news[len(all_news) - 1]
    url_news = language_insert(user_language, news.api_link)
    text = f'<b>{news.title}</b>\n' \
           f'{url_news}\n' \
           f'{news.id}'  # убрать
    await call.message.answer(text=text, reply_markup=ukb.markup_news)


@dp.callback_query_handler(text_contains='next_news')
async def next_news(call: CallbackQuery):
    user_language = await db.get_language()
    all_news = await db.get_all_news()

    news = all_news[len(all_news) - 2]
    url_news = language_insert(user_language, news.api_link)
    text = f'<b>{news.title}</b>\n' \
           f'{url_news}\n' \
           f'{news.id}'  # убрать
    await call.message.edit_text(text=text, reply_markup=ukb.markup_news)


@dp.callback_query_handler(text_contains='prev_news')
async def prev_news(call: CallbackQuery):
    await call.message.answer(text='123')
