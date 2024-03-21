# Задание №6
# Необходимо создать базу данных для интернет-магазина.
# База данных должна состоять из трех таблиц: товары, заказы и пользователи.
# Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах.
# Таблица пользователи должна содержать информацию о зарегистрированных пользователях магазина.
# Таблица заказы должна содержать информацию о заказах, сделанных пользователями.
#   ○ Таблица пользователей должна содержать следующие поля:
#       id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
#   ○ Таблица товаров должна содержать следующие поля:
#       id (PRIMARY KEY), название, описание и цена.
#   ○ Таблица заказов должна содержать следующие поля:
#       id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY),
#       дата заказа и статус заказа.
# Создайте модели pydantic для получения новых данных
#   и возврата существующих в БД для каждой из трёх таблиц (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц
#   через создание маршрутов, REST API (итого 15 маршрутов).
#   ○ Чтение всех
#   ○ Чтение одного
#   ○ Запись
#   ○ Изменение
#   ○ Удаление
#
# Ушло в ДЗ.
#
#     # Памятка (https://giters.com/encode/databases/issues/277):
#     # Для десериализации объекта <databases.backends.common.records.Record>,
#     # пришедшего, к примеру, после такого запроса:
#     # result = await db.fetch_all(query=users.select().where(users.c.id == order_in.user_id))
#     # можно использовать следующий код, чтобы получить все значения данной записи:
#     # deserialized_data = [User(**data).dict() for data in result]  # где User - модель pydantic
#     # print(deserialized_data)  # list[dict]
