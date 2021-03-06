from aiogram import types
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import Column, Integer, BigInteger, String, Sequence, Boolean, LargeBinary
from sqlalchemy import sql

from data.config import db_host, db_user, db_pass, db_name

db = Gino()


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    languages = Column(String(2), default='uk')
    is_admin = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    email = Column(String(100))
    phone = Column(String(20))
    company_name = Column(String(200))
    password = Column(LargeBinary())
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
    title = Column(String(500))
    text = Column(String)
    date = Column(String(10))
    api_link = Column(String(300))
    query: sql.Select


class DBCommands:
    # Операции с пользователями
    async def get_user(self, user_id) -> User:
        """
        Возвращает клас User из БД по ИД
        :param user_id:
        :return object: User
        """
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def get_all_users(self):
        """
        Возвращает список всех User из БД
        :return list: User
        """
        users = await User.query.gino.all()
        return users

    async def add_new_user(self) -> User:
        """
        Возвращает класс User из БД, проверяя по ИД из телеги,
        если нет в БД, тогда создает новую запись в БД и
        затем возвращает новый объект User
        :return object: User
        """
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.full_name = user.full_name
        await new_user.create()
        return new_user

    async def count_users(self):
        """
        Возвращает количество записей из таблицы users
        :return int:
        """
        total = await db.func.count(User.id).gino.scalar()
        return total

    # Возвращает список строк ид админив
    async def get_admins_user_id(self) -> list[str]:
        """
        Возвращает список строк ид пользователей со
        статусом is_admin == True
        :return list[str]
        """
        admins = await User.query.where(User.is_admin == True).gino.all()
        admins_id = [str(user.user_id) for user in admins]
        return admins_id

    # Возвращает список строк ид менеджеров
    async def get_managers_user_id(self) -> list[str]:
        """
        Возвращает список строк ид пользователей со
        статусом is_manager == True
        :return list[str]
        """
        managers = await User.query.where(User.is_manager == True).gino.all()
        managers_id = [str(user.user_id) for user in managers]
        return managers_id

    async def get_clients_user_id(self, language=None) -> list[str]:
        """
        Возвращает список строк ид пользователей со
        статусом is_manager == False и is_admin == False
        Если language not None фильтрует еще по language
        :param language: str
        :return list[str]
        """
        clients_all = await User.query.where(User.is_manager == False).gino.all()
        clients = [user for user in clients_all if user.is_admin == False]
        if language:
            clients = [user for user in clients if user.languages == language]
        clients_id = [str(user.user_id) for user in clients]
        return clients_id

    # новости
    async def get_news(self, title=None, news_id=None) -> News:
        """
        Возвращает объект News по полю title, если title = None,
        тогда возвращает News по полю news_id, если news_id = None,
        тогда возвращает None
        :param title:
        :param news_id:
        :return object News
        """
        if title:
            news = await News.query.where(News.title == title).gino.first()
            return news
        news = await News.query.where(News.id == news_id).gino.first()
        return news

    async def get_all_news(self) -> list[News]:
        """
        Возвращает список объектов News отсортированный по полю id
        :return: list[News]
        """
        all_news = await News.query.order_by('id').gino.all()
        return all_news

    async def add_new_news(self, news) -> News:
        """
        Проверяет есть ли передаваемая новость в БД
        по news['title'], если есть возвращает ее объектом News,
        если нет, тогда записывает ее в БД и возвращает новый
        объект News
        :param news: dict
        :return: News
        """
        title = news['title']
        old_news = await self.get_news(title=title)
        if old_news:
            return old_news
        new_news = News()
        new_news.title = news['title']
        new_news.text = news['body']
        new_news.date = news['created']
        new_news.api_link = news['api_link']
        await new_news.create()
        return new_news

    # Запись чтение языковых параметров
    async def set_language(self, language):
        """
        Записыват в БД язык интерфейса пользователя,
        ид пользователя берется из types.User.get_current().id
        :param language: str[Union('ru', 'uk', 'en')]
        :return:
        """
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(languages=language).apply()

    async def get_language(self):
        """
        Возвращает строку с языком пользователя,
        пользователь берется из types.User.get_current()
        :return User.languages: str
        """
        user = types.User.get_current()
        user = await self.get_user(user.id)
        return user.languages

    # Запись / чтение личных данных пользователя
    async def set_email(self, email):
        """
        Записыват в БД email пользователя,
        ид пользователя берется из types.User.get_current().id
        :param email: str
        :return:
        """
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(email=email).apply()

    async def set_phone(self, phone):
        """
        Записыват в БД phone пользователя,
        ид пользователя берется из types.User.get_current().id
        :param phone: str
        :return:
        """
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(phone=phone).apply()

    async def set_company_name(self, company_name):
        """
        Записыват в БД название компании пользователя,
        ид пользователя берется из types.User.get_current().id
        :param company_name: str
        :return:
        """
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(company_name=company_name).apply()

    async def set_password(self, password):
        """
        Записыват в БД password пользователя,
        ид пользователя берется из types.User.get_current().id
        :param password: bytes
        :return:
        """
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(password=password).apply()

    async def get_productions(self):
        productions = await Production.query.gino.all()
        return productions


async def create_db():
    """
        Создает БД
    :return:
    """
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    await db.gino.create_all()
