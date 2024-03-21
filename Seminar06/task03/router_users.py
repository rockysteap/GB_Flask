from fastapi import APIRouter
from models import TaskIn, Task
from database import db, tasks

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=Task)
# --- CREATE -----------------------------------------
async def create_task(task_in: TaskIn):
    query = tasks.insert().values(**task_in.dict())
    last_record_id = await db.execute(query)
    return {**task_in.dict(), "id": last_record_id}


@router.get("/", response_model=list[Task])
# --- READ ALL ---------------------------------------
async def read_tasks():
    query = tasks.select()
    return await db.fetch_all(query)


@router.get("/{task_id}", response_model=Task)
# --- READ ONE ---------------------------------------
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await db.fetch_one(query)


@router.put("/{task_id}", response_model=Task)
# --- UPDATE -----------------------------------------
async def update_task(task_id: int, task_in: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**task_in.dict())
    await db.execute(query)
    return {**task_in.dict(), "id": task_id}


@router.delete("/{task_id}", response_model=dict)
# --- DELETE -----------------------------------------
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await db.execute(query)
    return {"message": "Task deleted"}
