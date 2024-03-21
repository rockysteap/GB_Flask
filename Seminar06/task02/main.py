# Задание №2.
# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
#   ○ ID (автоматически генерируется при создании пользователя)
#   ○ Имя (строка, не менее 2 символов)
#   ○ Фамилия (строка, не менее 2 символов)
#   ○ Дата рождения (строка в формате "YYYY-MM-DD")
#   ○ Email (строка, валидный email)
#   ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
#   ○ Добавление пользователя в базу данных
#   ○ Получение списка всех пользователей в базе данных
#   ○ Получение пользователя по ID
#   ○ Обновление пользователя по ID
#   ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

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
