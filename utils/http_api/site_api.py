import json
from typing import List

import requests

from data import config
from utils.db_api import database

db = database.DBCommands()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (HTML, like Gecko) "
                  "Chrome/47.0.2526.106 Safari/537.36",
    "Content-Type": "application/json",
}


async def get_news() -> List:
    request = requests.get(config.api_url_news_ru, headers=headers)
    data = request.json()
    list_news = data.get('rows')
    for news in list_news[::-1]:
        await db.add_new_news(news)
    return list_news


def send_order(order_data: dict):
    """
  order_data = {'email': 'test@mail',
                'phone': '+380971112233',
                'company': 'Рога и Копыта',
                'fio': 'Иванов ИИ',
                'comment': 'Комментарий'}
    """
    json_data = json.dumps(order_data)
    request = requests.post(url=config.api_order_url, data=json_data, headers=headers,
                            auth=(config.api_user, config.api_pass))
    return request.status_code
