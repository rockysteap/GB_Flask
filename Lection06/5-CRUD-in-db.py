# Операции CRUD —
#   это основные функции, которые используются в любом приложении, управляемом базой данных.
#   Они используются для создания, чтения, обновления и удаления данных из базы данных.
#   В FastAPI с SQLAlchemy ORM мы можем создавать эти операции, используя функции и методы Python.
#   ● CREATE, Создать: добавление новых записей в базу данных.
#   ● READ, Прочитать: получение записей из базы данных.
#   ● UPDATE, Обновить: изменение существующих записей в базе данных.
#   ● DELETE, Удалить: удаление записей из базы данных.
#
# Для работы с базой данных в операциях CRUD с SQLAlchemy ORM
#   нам необходимо сначала установить соединение с базой данных.
#   Мы можем использовать любую базу данных по нашему выбору,
#   такую как MySQL, PostgreSQL или SQLite.
#
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uvicorn import run as uvi_run

# Сохраняем путь к БД в константу
DATABASE_URL = "sqlite:///mydatabase.db"

# Создаем экземпляр модуля database и указываем на нашу базу
database = databases.Database(DATABASE_URL)

# Формируем метаданные на основе ОРМ (объектно-реляционной модели) sqlalchemy
metadata = sqlalchemy.MetaData()

# Формируем модель(таблицу) для БД
users = sqlalchemy.Table(
    "users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

# Инициализируем движок БД
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Передаем метаданные в созданный движок, происходит формирования таблиц БД
metadata.create_all(engine)

app = FastAPI()


#
# 💡 Внимание!
# По умолчанию SQLite разрешает взаимодействовать с ним только одному потоку,
#   предполагая, что каждый поток будет обрабатывать независимый запрос.
#   Это сделано для предотвращения случайного использования одного и
#   того же соединения для разных вещей (для разных запросов).
#   Но в FastAPI при использовании обычных функций (def) несколько потоков
#   могут взаимодействовать с базой данных для одного и того же запроса,
#   поэтому нам нужно сообщить SQLite, что он должен разрешать это с помощью
#   connect_args={"check_same_thread": False}.
#
# Создание моделей для взаимодействия с таблицей в БД.
#
# Создадим две модели данных Pydantic:
#
class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# Первая модель нужна для получения информации о пользователе от клиента.
# А вторая используется для возврата данных о пользователе из БД клиенту.
#
# Добавление тестовых пользователей в БД
# Прежде чем работать над созданием API и проходить всю цепочку CRUD
#   для клиента сгенерируем несколько тестовых пользователей в базе данных.
#
@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


#
# Принимаем целое число count и создаём в БД указанное число пользователей с именами и почтами.
# Теперь мы готовы не только разрабатывать CRUD, но и тестировать его.
#
# 🔥 Важно!
# Не забудьте перейти по адресу http://127.0.0.1:8000/fake_users/25, чтобы добавить пользователей.
#
# 💡 Внимание!
# В реальном проекте подобные функции должны быть отключены перед запуском в продакшн.


if __name__ == '__main__':
    uvi_run('5-CRUD-in-db:app', host='127.0.0.1', port=8000, reload=True)
