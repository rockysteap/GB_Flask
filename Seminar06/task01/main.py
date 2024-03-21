# Задание №1
# Разработать API для управления списком пользователей с использованием базы данных SQLite.
# Для этого создайте модель User со следующими полями:
#   ○ id: int (идентификатор пользователя, генерируется автоматически)
#   ○ username: str (имя пользователя)
#   ○ email: str (электронная почта пользователя)
#   ○ password: str (пароль пользователя)
# API должно поддерживать следующие операции:
#   ○ Получение списка всех пользователей: GET /users/
#   ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
#   ○ Создание нового пользователя: POST /users/
#   ○ Обновление информации о пользователе: PUT /users/{user_id}/
#   ○ Удаление пользователя: DELETE /users/{user_id}/
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases

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
