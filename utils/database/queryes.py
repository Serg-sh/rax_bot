from typing import List

from aiogram.types.user import User as TgUser
from sqlalchemy import select

from utils.database.database import get_async_session
from utils.database.models import User


class UserDBQuery:
    #     # Операції з користувачами

    async def add_user(self) -> User:
        """
        Додає нового користувача до БД, якщо він ще не існує
        :param user:
        :return:
        """

        async for session in get_async_session():
            result = await session.execute(select(User).where(User.user_id == TgUser.user_id))
            user = result.scalars().first()
            if user:
                return user
            else:
                user = User(user_id=user.id, full_name=user.full_name)
                session.add(user)
                await session.commit()
            return user


    async def get_user(self, user_id: int) -> User:
        pass


    async def get_all_users(self) -> List[User]:
        pass
