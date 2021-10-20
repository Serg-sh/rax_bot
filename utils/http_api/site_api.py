from typing import List

import requests

from data import config
from utils.db_api import database

db = database.DBCommands()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (HTML, like Gecko) "
                  "Chrome/47.0.2526.106 Safari/537.36"
}

news_url = config.api_url_news_ru


async def get_news() -> List:
    request = requests.get(news_url, headers=headers)
    data = request.json()
    list_news = data.get('rows')
    for news in list_news[::-1]:
        await db.add_new_news(news)
    return list_news
