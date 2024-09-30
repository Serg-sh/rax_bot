from aiogram.types import Update
from aiogram.utils.i18n import I18nMiddleware, I18n

from config import I18N_DOMAIN, LOCALES_DIR
from utils.database.queryes import UserDBQuery

db = UserDBQuery()

# Ініціалізація i18n middleware
i18n = I18n(path=LOCALES_DIR, default_locale="uk", domain=I18N_DOMAIN)


class MyI18nMiddleware(I18nMiddleware):

    async def get_locale(self, event, data) -> str:
        """
        Визначення мови користувача
        :param event:
        :param data:
        :return: str: User.languages або default_locale
        """
        if isinstance(event, Update):
            user_id = event.event.from_user.id
            user = await db.get_user(user_id)
            if user:
                return user.languages
        return "uk"


def setup_middleware():
    return MyI18nMiddleware(i18n)
