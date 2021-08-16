from typing import List

from aiogram import types
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import Column, Integer, BigInteger, String, Sequence, Boolean
from sqlalchemy import sql

from data.config import db_host, db_user, db_pass, db_name

db = Gino()


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    languages = Column(String(2))
    is_admin = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    email = Column(String(100))
    phone = Column(String(20))
    company_name = Column(String(200))
    password = Column(String(200))
    query: sql.Select


class Production(db.Model):
    __tablename__ = 'productions'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(200))
    text = Column(String)
    photo = Column(String(250))
    drawing = Column(String(250))
    price = Column(Integer)
    query: sql.Select


class News(db.Model):
    __tablename__ = 'news'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(200))
    text = Column(String)
    date = Column(String(10))
    query: sql.Select


class DBCommands:
    async def get_user(self, user_id) -> User:
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self) -> User:
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.full_name = user.full_name
        await new_user.create()
        return new_user

    async def set_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def set_email(self, email):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(email=email).apply()

    async def set_phone(self, phone):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(phone=phone).apply()

    async def set_company_name(self, company_name):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(company_name=company_name).apply()

    async def set_password(self, password):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(password=password).apply()

    async def count_users(self):
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def get_news(self):
        news = await News.query.gino.all()
        return news[:3:-1]

    async def get_productions(self):
        productions = await Production.query.gino.all()
        return productions

    # Возвращает список строк ид админив
    async def get_admins_user_id(self) -> List:
        admins = await User.query.where(User.is_admin == True).gino.all()
        admins_id = list(str(user.user_id) for user in admins)
        return admins_id

    # Возвращает список строк ид менеджеров
    async def get_managers_user_id(self) -> List:
        managers = list(await User.query.where(User.is_manager == True).gino.all())
        managers_id = list(str(user.user_id) for user in managers)
        return managers_id

    async def get_clients_user_id(self) -> List:
        clients_all = list(await User.query.where(User.is_manager == False).gino.all())
        clients = list(user for user in clients_all if user.is_admin == False)
        clients_id = list(str(user.user_id) for user in clients)
        return clients_id


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    await db.gino.create_all()
