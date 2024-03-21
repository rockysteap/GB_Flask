# Создайте модель Task со следующими полями:
#   ○ id: int (первичный ключ)
#   ○ title: str (название задачи)
#   ○ description: str (описание задачи)
#   ○ done: bool (статус выполнения задачи)

from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field(title="Наименование задачи", min_length=3, max_length=50)
    description: str = Field(title="Описание задачи", min_length=3, max_length=50)
    done: bool = Field(title="Статус выполнения задачи")


class Task(TaskIn):
    id: int = Field(title="ID")
