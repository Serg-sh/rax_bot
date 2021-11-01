from typing import Tuple, Any, Optional

from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api import database

db = database.DBCommands()


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> Optional[str]:
        return await db.get_language()


def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n

