from fastapi import APIRouter

from models import Order, OrderIn
from database import db, orders
from validator import DBTableEnum, validate_id

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=Order)
# --- CREATE -----------------------------------------
async def create_order(order_in: OrderIn):
    await validate_id(order_in.user_id, DBTableEnum.users)
    await validate_id(order_in.item_id, DBTableEnum.items)
    query = orders.insert().values(**order_in.dict())
    last_record_id = await db.execute(query)
    return {**order_in.dict(), "id": last_record_id}


@router.get("/", response_model=list[Order])
# --- READ ALL ---------------------------------------
async def read_orders():
    query = orders.select()
    return await db.fetch_all(query)


@router.get("/{order_id}", response_model=Order)
# --- READ ONE ---------------------------------------
async def read_order(order_id: int):
    await validate_id(order_id, DBTableEnum.orders)
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)


@router.put("/{order_id}", response_model=Order)
# --- UPDATE -----------------------------------------
async def update_order(order_id: int, order_in: OrderIn):
    await validate_id(order_id, DBTableEnum.orders)
    await validate_id(order_in.user_id, DBTableEnum.users)
    await validate_id(order_in.item_id, DBTableEnum.items)
    query = orders.update().where(orders.c.id == order_id).values(**order_in.dict())
    await db.execute(query)
    return {**order_in.dict(), "id": order_id}


@router.delete("/{order_id}", response_model=dict)
# --- DELETE -----------------------------------------
async def delete_order(order_id: int):
    await validate_id(order_id, DBTableEnum.orders)
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {"message": "Order successfully deleted"}
