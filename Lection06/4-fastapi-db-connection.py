# Работа с базой данных
#
# Создание подключения к базе данных
#
#   FastAPI поддерживает различные базы данных,
#   такие как SQLite, PostgreSQL, MySQL и MongoDB.
#   Выбор базы данных зависит от требований и предпочтений проекта.
#
# Подключение к базе данных и миграция базы данных с использованием SQLAlchemy ORM и базы данных SQLite.
# SQLite —
#   это облегченная система управления реляционными базами данных на основе SQL.
#
# Чтобы создать соединение с базой данных, нам нужно определить конфигурацию базы данных
#   и использовать библиотеку ORM (Object-Relational Mapping),
#   такую как Tortoise ORM, SQLAlchemy или Peewee.
#
import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
...
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# В этом примере мы используем SQLAlchemy для создания подключения к базе данных SQLite.
# Переменная DATABASE_URL определяет строку подключения.
#
# Событие запуска используется для создания схемы базы данных.
# Событие выключения используется для удаления ядра базы данных.
#
#
# Подключение к PostgreSQL
#
# Если мы хотим заменить SQLite на PostgreSQL,
#   достаточно заменить данные в константе подключения к БД:

DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Указав тип базы данных, имя пользователя, пароль, хост и название базы данных мы установим с ней соединение.
