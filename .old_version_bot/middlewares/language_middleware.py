from aiogram.utils import i18n
from aiogram.utils.i18n import I18nMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Any

from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api.queryes import UserDBQuery


query = UserDBQuery()

class MyACLMiddleware(I18nMiddleware):
    # Метод для отримання локалі користувача
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        # user = await query.add_new_user()
        # if user and user.languages:
        #     return user.languages
        return "uk"

# Функція для налаштування middleware
def setup_middleware():
    # Ініціалізація ACLMiddleware на основі I18nMiddleware
    return MyACLMiddleware(I18N_DOMAIN, LOCALES_DIR)

