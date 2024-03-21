from datetime import date, timedelta
from random import choice, randint, uniform
from passlib.hash import pbkdf2_sha256
from decimal import Decimal

from models import OrderStatus
from database import db, users, items, orders

USERS_IN_DB = 10
ITEMS_IN_DB = 20
ORDERS_IN_DB = 5
MIN_PRICE, MAX_PRICE = 1, 1_000_000
MAX_AGE_OF_ORDER_IN_DAYS = 50


async def populate():
    for i in range(USERS_IN_DB):
        query = users.insert().values(firstname=f'Firstname_{i}', lastname=f'Lastname_{i}', email=f'mail{i}@mail.ru',
                                      password_hash=pbkdf2_sha256.hash(f'pa$${i}word'))
        await db.execute(query)

    for i in range(ITEMS_IN_DB):
        query = items.insert().values(title=f'Title_{i}', description=f'Description_{i}',
                                      price=round(Decimal(uniform(MIN_PRICE, MAX_PRICE)), 2))
        await db.execute(query)

    for i in range(ORDERS_IN_DB):
        query = orders.insert().values(user_id=randint(1, USERS_IN_DB), item_id=randint(1, ITEMS_IN_DB),
                                       date=date.today() - timedelta(days=randint(0, MAX_AGE_OF_ORDER_IN_DAYS)),
                                       status=choice(list(OrderStatus)))
        await db.execute(query)
