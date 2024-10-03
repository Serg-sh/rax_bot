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
        :return:Повертає створеного або наявного user: User
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
        :return: user: User
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.user_id == user_id))
            user = result.scalars().first()
            return user

    async def get_all_users(self) -> List[User]:
        """
        Повертає список всіх користувачів з бази
        :return: List[User]
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.is_admin == False, User.is_manager == False))
            users = result.scalars().all()
            return list(users)

    async def get_managers_user_id(self) -> List[int]:
        """
        Повертає список id всіх менеджерів з бази
        :return: List[int]
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.is_manager == True))
            managers = result.scalars().all()
            managers_id = []
            for manager in managers:
                managers_id.append(manager.user_id)
            return managers_id

    async def get_admins_user_id(self) -> List[int]:
        """
        Повертає список id всіх адміністраторів з бази
        :return: List[int]
        """
        async for session in get_async_session():
            result = await session.execute(select(User).where(User.is_admin == True))
            admins = result.scalars().all()
            admins_id = []
            for admin in admins:
                admins_id.append(admin.user_id)
            return admins_id


    async def update_user(self, user_id: int, **fields) -> User:
        """
        Оновлює значення полів у користувача з user_id у БД
        :param user_id:
        :param fields: name_field=value
        :return: оновлений user: User
        """
        async for session in get_async_session():
            res = await session.execute(select(User).where(User.user_id == user_id))
            user = res.scalars().first()
            for field, value in fields.items():
                if hasattr(user, field):
                    setattr(user, field, value)
                else:
                    raise ValueError(f"Поле '{field}' не існує у моделі User")
            await session.commit()
            return user
