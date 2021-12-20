import json

import requests

from data import config
from utils.db_api import database

db = database.DBCommands()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (HTML, like Gecko) "
                  "Chrome/47.0.2526.106 Safari/537.36",
    "Content-Type": "application/json",
}


def get_link_with_language(user_language: str, api_link: str):
    user_language += '/'
    if user_language == 'en/':
        user_language = ''
    return api_link[:20] + user_language + api_link[20:]


# Получает список новостей с сайта
async def get_news() -> list:
    request = requests.get(config.api_url_news_ru, headers=headers)
    data = request.json()
    list_news = data.get('rows')
    for news in list_news[::-1]:
        await db.add_new_news(news)
    return list_news


# Получает список продукции с сайта (каждый продукт в словаре)
def get_productions(language='en'):
    link = get_link_with_language(language, config.api_url_productions)
    request = requests.get(link, headers=headers)
    data = request.json()
    list_productions = data.get('rows')  # список словарей(на каждый продукт)
    return list_productions


# Отправка заявки на сайт менеджеру
def send_order(order_data: dict[str, str]):
    """
    Пример данных заявки:\n
    order_data = {'email': 'test@mail.mail',
                  'phone': '+380971112233',\n
                  'company': 'Рога и Копыта',\n
                  'fio': 'Иванов ИИ',\n
                  'comment': 'Комментарий'}
    :param order_data: dict[str, str]
    :return статус код :int
    """
    json_data = json.dumps(order_data)
    request = requests.post(url=config.api_order_url, data=json_data, headers=headers,
                            auth=(config.api_user, config.api_pass))
    return request.status_code
