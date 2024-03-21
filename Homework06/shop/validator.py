from fastapi import HTTPException
from enum import Enum

from database import db, users, items, orders


class DBTableEnum(Enum):
    users = 'users'
    items = 'items'
    orders = 'orders'


async def validate_id(id_to_find: int, db_table_name: DBTableEnum):
    validator_to_call = globals()[f'_validate_{db_table_name.value}_id']
    await validator_to_call(id_to_find)


async def _validate_users_id(id_in: int) -> None:
    if len(await db.fetch_all(query=users.select().where(users.c.id == id_in))) == 0:
        raise HTTPException(status_code=422, detail=f'Пользователь с id={id_in} отсутствует в БД')


async def _validate_items_id(id_in: int) -> None:
    if len(await db.fetch_all(query=items.select().where(items.c.id == id_in))) == 0:
        raise HTTPException(status_code=422, detail=f'Товар с id={id_in} отсутствует в БД')


async def _validate_orders_id(id_in: int) -> None:
    if len(await db.fetch_all(query=orders.select().where(orders.c.id == id_in))) == 0:
        raise HTTPException(status_code=422, detail=f'Заказ с id={id_in} отсутствует в БД')
