# Формирование CRUD.
#
# Создадим необходимые маршруты для реализации REST API.
#
# ------------
# <editor-fold desc="Код из файла 5">
from typing import List

import databases
import sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uvicorn import run as uvi_run

app = FastAPI()

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# </editor-fold>
# ------------
#
# ➢ Создание пользователя в БД,
#       CREATE
#
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    # query = users.insert().values(name=user.name, email=user.email)
    # То же самое можно сделать следующим способом:
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    print(f"{last_record_id=}")
    return {**user.dict(), "id": last_record_id}


# Мы определяем маршрут "/users/" для создания нового пользователя.
# В параметре функции мы ожидаем объект типа UserIn, который содержит имя и email пользователя.
# Затем мы создаем SQL-запрос на добавление новой записи в таблицу "users" с указанными данными.
# Выполняем запрос и возвращаем данные созданного пользователя, включая его ID.
#
# ➢ Чтение пользователей из БД,
#       READ
#
@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# Мы определяем маршрут "/users/" для чтения всех пользователей.
# В функции мы создаем SQL-запрос на выборку всех записей из таблицы "users".
# Выполняем запрос и возвращаем полученные данные в виде списка объектов типа User.
#
# ➢ Чтение одного пользователя из БД,
#       READ
#
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


# Мы определяем маршрут "/users/{user_id}" для чтения одного пользователя по его ID.
# В параметре функции мы ожидаем передачу ID пользователя.
# Затем мы создаем SQL-запрос на выборку записи из таблицы "users" с указанным ID.
# Выполняем запрос и возвращаем полученные данные в виде объекта типа User.
#
# ➢ Обновление пользователя в БД,
#       UPDATE
#
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# Мы определяем маршрут "/users/{user_id}" для обновления данных пользователя по его ID.
# В параметре функции мы ожидаем передачу ID пользователя и объекта типа UserIn,
#   который содержит новые данные пользователя.
# Затем мы создаем SQL-запрос на обновление записи в таблице "users" с указанным ID
#   и новыми данными.
# Выполняем запрос и возвращаем обновленные данные пользователя.
#
# ➢ Удаление пользователя из БД,
#       DELETE
#
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}


# Мы определяем маршрут "/users/{user_id}" для удаления пользователя по его ID.
# В параметре функции мы ожидаем передачу ID пользователя.
# Затем мы создаем SQL-запрос на удаление записи из таблицы "users" с указанным ID.
# Выполняем запрос и возвращаем сообщение об успешном удалении пользователя.

if __name__ == "__main__":
    uvi_run("6-CRUD-REST_API:app", host="127.0.0.1", port=8000, reload=True)
