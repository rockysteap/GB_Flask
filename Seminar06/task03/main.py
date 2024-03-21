# Задача 3.
# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с задачами.

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from uvicorn import run as uvi_run
from router_users import router as users_router


app = FastAPI()
app.include_router(users_router)


@app.get("/", tags=["Redirect to Swagger"], response_class=RedirectResponse)
async def redirect_index():
    return "http://127.0.0.1:8000/docs"


if __name__ == "__main__":
    uvi_run("main:app", host="127.0.0.1", port=8000, reload=True)
