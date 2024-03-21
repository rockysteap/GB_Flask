# Задание №4.
# Напишите API для управления списком задач.
# Для этого создайте модель Task со следующими полями:
#   ○ id: int (первичный ключ)
#   ○ title: str (название задачи)
#   ○ description: str (описание задачи)
#   ○ done: bool (статус выполнения задачи)
# Погружение в Python
# Задание №4 (продолжение)
# API должно поддерживать следующие операции:
#   ○ Получение списка всех задач: GET /tasks/
#   ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
#   ○ Создание новой задачи: POST /tasks/
#   ○ Обновление информации о задаче: PUT /tasks/{task_id}/
#   ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from uvicorn import run as uvi_run
from router_tasks import router as tasks_router

app = FastAPI()
app.include_router(tasks_router)


@app.get("/", tags=["Redirect to Swagger"], response_class=RedirectResponse)
async def redirect_index():
    return "http://127.0.0.1:8000/docs"


if __name__ == "__main__":
    uvi_run("main:app", host="127.0.0.1", port=8000, reload=True)
