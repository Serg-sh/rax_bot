from sqlalchemy import Column, Integer, BigInteger, String, Sequence, Boolean, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger, nullable=False, unique=True)
    full_name = Column(String(100), nullable=False)
    languages = Column(String(2), default='uk')
    is_admin = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    email = Column(String(100), nullable=True, unique=True)
    phone = Column(String(20), nullable=True)
    company_name = Column(String(200), nullable=True)
    password = Column(LargeBinary(), nullable=False)


class Production(BaseModel):
    __tablename__ = 'production'
    id = Column(Integer, Sequence('prod_id_seq'), primary_key=True)
    name = Column(String(200))
    text = Column(String)
    photo = Column(String(250))
    drawing = Column(String(250))
    price = Column(Integer)


class News(BaseModel):
    __tablename__ = 'news'
    id = Column(Integer, Sequence('news_id_seq'), primary_key=True)
    title = Column(String(500))
    text = Column(String)
    date = Column(String(10))
    api_link = Column(String(300))