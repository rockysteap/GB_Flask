from fastapi import APIRouter
from models import UserIn, User
from database import db, users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
# --- CREATE -----------------------------------------
async def create_user(user_in: UserIn):
    query = users.insert().values(**user_in.dict())
    last_record_id = await db.execute(query)
    return {**user_in.dict(), "id": last_record_id}


@router.get("/", response_model=list[User])
# --- READ ALL ---------------------------------------
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


@router.get("/{user_id}", response_model=User)
# --- READ ONE ---------------------------------------
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


@router.put("/{user_id}", response_model=User)
# --- UPDATE -----------------------------------------
async def update_user(user_id: int, user_in: UserIn):
    query = users.update().where(users.c.id == user_id).values(**user_in.dict())
    await db.execute(query)
    return {**user_in.dict(), "id": user_id}


@router.delete("/{user_id}", response_model=dict)
# --- DELETE -----------------------------------------
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {"message": "User deleted"}
