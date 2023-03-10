from sqlalchemy import Column, INT, VARCHAR,DECIMAL,BOOLEAN, ForeignKey, TIMESTAMP, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session
from pydantic import BaseModel, Field, EmailStr
from pydantic.types import Decimal
import csv
from csv import reader, DictReader, writer, DictWriter


class Base (DeclarativeBase):
    pk = Column('id', INT, primary_key=True)
    engine = create_engine('postgresql://olgi7:postgres@localhost:5432/bh37')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')
    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def scalars(cls, sql, session: Session = None):
        return session.scalars(sql).all()

    @classmethod
    @create_session
    def execute(cls, sql, session: Session = None):
        return session.execute(sql).all()

    def dict(self):
        data = self.__dict__
        data['id'] = data['pk']
        del data['pk']
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    @property
    def category(self):
        with self.session() as session:
            return session.get(Category, self.category_id)

class Category(Base):

    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    name = Column(VARCHAR(128), nullable=False, unique=True)
    price = Column(DECIMAL(8,2), nullable=False)
    descr = Column(VARCHAR(4096), nullable=True)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)


class Chat(Base):

    name = Column(VARCHAR(255), nullable=False, unique=True)

class User(Base):

    name = Column(VARCHAR(255), nullable=False, unique=True)


class ChatMember(Base):
    # name = Column(VARCHAR(128), nullable=False, unique=True)
    # price = Column(DECIMAL(8,2), nullable=False)
    # descr = Column(VARCHAR(4096), nullable=True)
    # is_published = Column(BOOLEAN, default=False)
    chat_id = Column(INT, ForeignKey('chat.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
class Message(Base):
    # name = Column(VARCHAR(128), nullable=False, unique=True)
    # price = Column(DECIMAL(8,2), nullable=False)
    text = Column(VARCHAR(1024), nullable=True)
    date_created = Column(TIMESTAMP, nullable=False)

    # is_published = Column(BOOLEAN, default=False)
    chat_id = Column(INT, ForeignKey('chat.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)



class OrderItems(Base):
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)

class Products(Base):
    # name = Column(VARCHAR(128), nullable=False, unique=True)
    price = Column(DECIMAL(8,2), nullable=False)
    title = Column(VARCHAR(36), nullable=True)
    descr = Column(VARCHAR(140), nullable=True)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

class ProductsModel(BaseModel):
    price: Decimal = Field(max_digits=6, decimal_places=2)
    title: str
    descr: str = Field(default=None)

#  Написать функцию, которая будет заполнять любую таблицу на основании файла CSV через SQLAlchemy, предварительно
# валидируя с помощью pydantic
with open('products.csv', 'r', encoding= 'utf-8') as file:
    reader = DictReader(file)

# Написать функцию выгрузки из таблицы в файл CSV с использованием SQLAlchemy
with open('products.csv', 'w', encoding= 'utf-8') as file:
    w = DictWriter(file, fieldnames=("price", "title", "descr"))
    w.writeheader()
    # w.writer()

class Orders(Base):
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)
class Categories(Base):
    name = Column(VARCHAR(24), nullable=False, unique=True)

class CategoriesModel(BaseModel):
    name: str

#  Написать функцию, которая будет заполнять любую таблицу на основании файла CSV через SQLAlchemy, предварительно
# валидируя с помощью pydantic
with open('categories.csv', 'r', encoding= 'utf-8') as file:
    reader = DictReader(file)

#Написать функцию выгрузки из таблицы в файл CSV с использованием SQLAlchemy
with open('categiries.csv', 'w', encoding= 'utf-8') as file:
    w = DictWriter(file, fieldnames=("name"))
    w.writeheader()
    # w.writer()

class Users(Base):
    name = Column(VARCHAR(24), nullable=False, unique=True)
    email = Column(VARCHAR(24), unique=True)

class UsersModel(BaseModel):
    name: str
    email: EmailStr


#  Написать функцию, которая будет заполнять любую таблицу на основании файла CSV через SQLAlchemy, предварительно
# валидируя с помощью pydantic
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = DictReader(file)

# Написать функцию выгрузки из таблицы в файл CSV с использованием SQLAlchemy
with open('users.csv', 'w', encoding= 'utf-8') as file:
    w = DictWriter(file, fieldnames=("name", "email"))
    w.writeheader()
    # w.writer()
class Statuses(Base):
    name = Column(VARCHAR(10), nullable=False, unique=True)

class StatusesModel(BaseModel):
    name: str


#  Написать функцию, которая будет заполнять любую таблицу на основании файла CSV через SQLAlchemy, предварительно
# валидируя с помощью pydantic
with open('statuses.csv', 'r', encoding='utf-8') as file:
    reader = DictReader(file)

# Написать функцию выгрузки из таблицы в файл CSV с использованием SQLAlchemy
with open('statuses.csv', 'w', encoding= 'utf-8') as file:
    w = DictWriter(file, fieldnames=("name"))
    w.writeheader()
    # w.writer()















