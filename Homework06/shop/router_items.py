from fastapi import APIRouter

from models import Item, ItemIn
from database import db, items
from validator import DBTableEnum, validate_id

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=Item)
# --- CREATE -----------------------------------------
async def create_item(item_in: ItemIn):
    query = items.insert().values(**item_in.dict())
    last_record_id = await db.execute(query)
    return {**item_in.dict(), "id": last_record_id}


@router.get("/", response_model=list[Item])
# --- READ ALL ---------------------------------------
async def read_items():
    query = items.select()
    return await db.fetch_all(query)


@router.get("/{item_id}", response_model=Item)
# --- READ ONE ---------------------------------------
async def read_item(item_id: int):
    await validate_id(item_id, DBTableEnum.items)
    query = items.select().where(items.c.id == item_id)
    return await db.fetch_one(query)


@router.put("/{item_id}", response_model=Item)
# --- UPDATE -----------------------------------------
async def update_item(item_id: int, item_in: ItemIn):
    await validate_id(item_id, DBTableEnum.items)
    query = items.update().where(items.c.id == item_id).values(**item_in.dict())
    await db.execute(query)
    return {**item_in.dict(), "id": item_id}


@router.delete("/{item_id}", response_model=dict)
# --- DELETE -----------------------------------------
async def delete_item(item_id: int):
    await validate_id(item_id, DBTableEnum.items)
    query = items.delete().where(items.c.id == item_id)
    await db.execute(query)
    return {"message": "Item successfully deleted"}
