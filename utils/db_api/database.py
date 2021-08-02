from aiogram import types, Bot

from gino import Gino
from gino.schema import GinoSchemaVisitor

from sqlalchemy import Column, Integer, BigInteger, String, Sequence, Boolean
from sqlalchemy import sql

from data.config import db_host, db_user, db_pass

db = Gino()


class User(db.Model):
    __tablename__ ='users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id =Column(BigInteger)
    full_name = Column(String(100))
    languages = Column(String(2))
    is_admin = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    username = Column(String(50))
    password = Column(String(200))
    query: sql.Select

class Production(db.Model):
    __tablename__ = 'productions'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(200))
    text = Column(String)
    photo = Column(String(250))
    price = Column(Integer)

class News(db.Model):
    __tablename__ = 'news'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(200))
    text = Column(String)
    date = Column(String(10))


class DBCommands:
    async def get_users(self, user_id) -> User:
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

