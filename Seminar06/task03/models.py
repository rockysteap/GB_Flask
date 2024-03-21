# Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
from enum import StrEnum

from fastapi import HTTPException
from pydantic import BaseModel, Field


class Status(StrEnum):
    TODO = "не выполнена"
    DONE = "выполнена"

    @classmethod
    def _missing_(cls, value: str):
        value = value.lower()
        for member in cls:
            if member == value:
                return member
        raise HTTPException(status_code=422, detail=f'{value} is not a member of Status(StrEnum)')


class TaskIn(BaseModel, use_enum_values=True):
    title: str = Field(title="Наименование задачи", min_length=3, max_length=50)
    description: str = Field(title="Описание задачи", min_length=3, max_length=50)
    status: Status = Field(title="Статус задачи")


class Task(TaskIn, use_enum_values=True):
    id: int = Field(title="ID")
