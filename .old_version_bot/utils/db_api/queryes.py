
# from aiogram.types.user import User as Tg_user
# from sqlalchemy import select
#
# from utils.db_api.database import get_async_session
# from utils.db_api.models import User


# class UserDBQuery:
# #     # Операції з користувачами
#
#     async def add_new_user(self, user) -> User:
#         """
#         Додає нового користувача до БД, якщо він ще не існує
#         """
#
#         print(user.user_id)
#         async for session in get_async_session():
#             result = await session.execute(select(User).where(User.user_id == user.user_id))
#             user = result.scalars().first()
#             if user:
#                 return user
#             else:
#                 user = User(user_id=user.id, full_name=user.full_name)
#                 session.add(user)
#                 await session.commit()
#             return user


#
#     async def get_user(self, user_id) -> User:
#         """
#         Повертає об'єкт User з БД за user_id
#         """
#         return await User.query.where(User.user_id == user_id).gino.first()
#
#     async def get_all_users(self) -> List[User]:
#         """
#         Повертає список всіх користувачів з БД
#         """
#         return await User.query.gino.all()
#
#
#     async def count_users(self) -> int:
#         """
#         Повертає кількість користувачів у БД
#         """
#         return await db.func.count(User.id).gino.scalar()
#
#     async def get_admins_user_id(self) -> List[str]:
#         """
#         Повертає список ID користувачів з правами адміністратора
#         """
#         admins = await User.query.where(User.is_admin == True).gino.all()
#         return [str(user.user_id) for user in admins]
#
#     async def get_managers_user_id(self) -> List[str]:
#         """
#         Повертає список ID менеджерів
#         """
#         managers = await User.query.where(User.is_manager == True).gino.all()
#         return [str(user.user_id) for user in managers]
#
#     async def get_clients_user_id(self, language=None) -> List[str]:
#         """
#         Повертає список ID клієнтів (не адміністратори та не менеджери)
#         """
#         clients_query = User.query.where((User.is_manager == False) & (User.is_admin == False))
#         if language:
#             clients_query = clients_query.where(User.languages == language)
#         clients = await clients_query.gino.all()
#         return [str(user.user_id) for user in clients]
#
#     # Операції з новинами
#     async def get_news(self, title=None, news_id=None) -> News:
#         """
#         Повертає об'єкт News за назвою або ID
#         """
#         if title:
#             return await News.query.where(News.title == title).gino.first()
#         return await News.query.where(News.id == news_id).gino.first()
#
#     async def get_all_news(self) -> List[News]:
#         """
#         Повертає список всіх новин
#         """
#         return await News.query.order_by(News.id).gino.all()
#
#     async def add_new_news(self, news) -> News:
#         """
#         Додає нову новину до БД, якщо такої ще немає
#         """
#         title = news['title']
#         old_news = await self.get_news(title=title)
#         if old_news:
#             return old_news
#         new_news = News(title=news['title'], text=news['body'], date=news['created'], api_link=news['api_link'])
#         await new_news.create()
#         return new_news
#
#     # Операції з мовними параметрами
#     async def set_language(self, language: str):
#         """
#         Оновлює мову користувача
#         """
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(languages=language).apply()
#
#     async def get_language(self) -> str:
#         """
#         Повертає мову поточного користувача
#         """
#         user = types.User.get_current()
#         user = await self.get_user(user.id)
#         return user.languages
#
#     # Операції з особистими даними користувача
#     async def set_email(self, email: str):
#         """
#         Оновлює email користувача
#         """
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(email=email).apply()
#
#     async def set_phone(self, phone: str):
#         """
#         Оновлює телефон користувача
#         """
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(phone=phone).apply()
#
#     async def set_company_name(self, company_name: str):
#         """
#         Оновлює назву компанії користувача
#         """
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(company_name=company_name).apply()
#
#     async def set_password(self, password: bytes):
#         """
#         Оновлює пароль користувача
#         """
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(password=password).apply()
#
#     # Операції з продукцією
#     async def get_productions(self) -> List[Production]:
#         """
#         Повертає список всіх продуктів
#         """
#         return await Production.query.gino.all()