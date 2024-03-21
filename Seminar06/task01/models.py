# Создайте модель User со следующими полями:
#   ○ id: int (идентификатор пользователя, генерируется автоматически)
#   ○ username: str (имя пользователя)
#   ○ email: str (электронная почта пользователя)
#   ○ password: str (пароль пользователя)
# Для валидации данных используйте параметры Field модели User.

from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str = Field(title="Имя пользователя", min_length=3, max_length=50)
    email: EmailStr = Field(title="Адрес эл. почты", max_length=128)
    password: str = Field(title="Пароль", min_length=3, max_length=128)


class User(UserIn):
    id: int = Field(title="ID")
