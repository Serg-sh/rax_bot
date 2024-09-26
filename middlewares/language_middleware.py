from aiogram.utils.i18n import I18nMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Any

from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api.database import db  # Імпортуємо методи для роботи з базою даних

class MyACLMiddleware(I18nMiddleware):
    # Метод для отримання локалі користувача
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        # Отримуємо користувача з бази даних
        user = await db.add_new_user()  # Використовуємо функцію з вашої бази
        if user and user.languages:
            return user.languages  # Повертаємо мову користувача
        return 'uk'  # Мова за замовчуванням, якщо не вказано

# Функція для налаштування middleware
def setup_middleware():
    # Ініціалізація ACLMiddleware на основі I18nMiddleware
    i18n = MyACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    return i18n

