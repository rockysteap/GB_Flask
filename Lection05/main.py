import logging
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)

app = FastAPI()

logger = logging.getLogger(__name__)


# FastAPI позволяет автоматически валидировать данные запроса и ответа
#   с помощью модуля pydantic.
# Класс Item для валидации содержит поля name, description, price и tax.
# Поля name и price обязательны, а поля description и tax необязательны.
# Затем можно использовать этот класс для валидации данных запроса и ответа.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


"""
@app.get("/")
# Добавляет обработчик GET-запросов для корневого URL-адреса.
# Функция read_root() возвращает JSON-объект {"Hello": "World"}.
async def read_root():
    return {"Hello": "World"}
"""


@app.get("/")
# Обработчик GET запроса для корневого маршрута с использованием логирования
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}


@app.get("/items/{item_id}")
# Обработчик GET запроса по пути "/items/{item_id}",
# где item_id — это переменная пути, а q — это параметр запроса.
# Функция возвращает словарь с переданными параметрами.
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
# POST запрос, используя модель данных Item
# Добавляет обработчик POST-запросов для URL-адреса /items/.
# Функция create_item() принимает объект Item и возвращает его же.
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")
# PUT запрос, используя модель данных Item
# Добавляет обработчик PUT-запросов для URL-адреса /items/{item_id}.
# Функция update_item() принимает идентификатор элемента
# и объект Item и возвращает JSON-объект с этими данными.
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
# Добавляет обработчик DELETE-запросов для URL-адреса /items/{item_id}.
# Функция delete_item() принимает идентификатор элемента
# и возвращает JSON-объект с этим идентификатором.
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}

# 🔥 Важно!
# Зачастую операция удаления не удаляет данные из базы данных,
# а изменяет специально созданное поле is_deleted на значение Истина.
# Таким образом, вы сможете восстановить ранее удаленные данные пользователя,
# если он передумает спустя время.
