from typing import List
from sqlalchemy import select

from utils.database.database import get_async_session
from utils.database.models import User


class UserDBQuery:
    # Операції з користувачами

    async def add_user(self, current_user) -> User:
        """
        Додає нового користувача до БД, якщо він ще не існує
        :param current_user:
        :param user:
        :return:
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.user_id == current_user.id))
            user = result.scalars().first()
            if user:
                return user
            else:
                user = User(user_id=current_user.id, full_name=current_user.full_name)
                session.add(user)
                await session.commit()
            return user

    async def get_user(self, user_id) -> User:
        """
        повертає User з user_id
        :param user_id:
        :return:
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.user_id == user_id))
            user = result.scalars().first()
            return user

    async def get_all_users(self) -> List[User]:
        async for session in get_async_session():
            result = await session.execute(select(User))
            users = result.scalars().all()
            return list(users)
