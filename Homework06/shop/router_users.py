from fastapi import APIRouter
from passlib.hash import pbkdf2_sha256

from models import User, UserIn
from database import db, users
from validator import DBTableEnum, validate_id

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
# --- CREATE -----------------------------------------
async def create_user(user_in: UserIn):
    user_to_db = user_in.dict().copy()
    user_to_db.setdefault('password_hash', pbkdf2_sha256.hash(user_to_db.pop('password')))
    query = users.insert().values(**user_to_db)
    last_record_id = await db.execute(query)
    return {**user_to_db, "id": last_record_id}


@router.get("/", response_model=list[User])
# --- READ ALL ---------------------------------------
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


@router.get("/{user_id}", response_model=User)
# --- READ ONE ---------------------------------------
async def read_user(user_id: int):
    await validate_id(user_id, DBTableEnum.users)
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


@router.put("/{user_id}", response_model=User)
# --- UPDATE -----------------------------------------
async def update_user(user_id: int, user_in: UserIn):
    await validate_id(user_id, DBTableEnum.users)
    user_to_db = user_in.dict().copy()
    user_to_db.setdefault('password_hash', pbkdf2_sha256.hash(user_to_db.pop('password')))
    query = users.update().where(users.c.id == user_id).values(**user_to_db)
    await db.execute(query)
    return {**user_to_db, "id": user_id}


@router.delete("/{user_id}", response_model=dict)
# --- DELETE -----------------------------------------
async def delete_user(user_id: int):
    await validate_id(user_id, DBTableEnum.users)
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {"message": "User successfully deleted"}
