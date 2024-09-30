import requests

from config import api_url_news_en, api_url_productions

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


# Получает список новостей с сайта(версия без записи в БД) добавленно определение языка
async def get_news(language="en") -> list:
    link = get_link_with_language(language, api_url_news_en)
    request = requests.get(link, headers=headers)
    data = request.json()
    list_news = data.get('rows')
    return list_news


# Получает список продукции с сайта (каждый продукт в словаре)
def get_productions(language='en'):
    link = get_link_with_language(language, api_url_productions)
    request = requests.get(link, headers=headers)
    data = request.json()
    list_productions = data.get('rows')  # список словарей(на каждый продукт)
    return list_productions