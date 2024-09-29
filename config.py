from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Список админов
MANAGERS = env.list("MANAGERS")  # Список менеджеров

db_host = env.str("HOST_DB")  # адрес хоста базы данных
db_port = env.str("PORT_DB")  # адрес хоста базы данных
db_name = env.str("NAME_DB")  # Имя БД
db_user = env.str("USER_DB")  # юзер бд
db_pass = env.str("PASS_DB")  # пароль БД

api_user = env.str("USER_API")  # юзер для доступа к api
api_pass = env.str("PASS_API")  # пароль для доступа к api

api_url_news_ru = env.str("API_URL_NEWS_RU")  # url для получения новостей с апи сайта на рус. языке
api_url_news_uk = env.str("API_URL_NEWS_UK")  # url для получения новостей с апи сайта на укр. языке
api_url_news_en = env.str("API_URL_NEWS_EN")  # url для получения новостей с апи сайта на анг. языке

api_order_url = env.str("API_ORDER_URL")  # url для отправки заявки через апи сайта

api_url_productions = env.str("API_PRODUCTS_URL")  # url для получения продуктов с апи сайта на анг. языке

I18N_DOMAIN = "bot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"
