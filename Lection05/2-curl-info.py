# Отправка запросов через curl
#
# 🔥 Важно!
# Отправлять необходимо
#
# Для тестирования POST, PUT и DELETE запросов воспользуемся curl.
#
# Curl (client URL) — это инструмент командной строки на основе библиотеки libcurl для
# передачи данных с сервера и на сервер при помощи различных протоколов, в том числе
# HTTP, HTTPS, FTP, FTPS, IMAP, IMAPS, POP3, POP3S, SMTP и SMTPS.
# Он очень популярен в сфере автоматизации и скриптов благодаря широкому диапазону функций
# и поддерживаемых протоколов.
#
"""
# ● POST запрос
"""
# Для отправки POST запроса нашему серверу введём в терминале следующую строку:
"""
curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept:
application/json' -H 'Content-Type: application/json' -d
'{"name": "BestSale", "description": "The best of the best",
"price": 9.99, "tax": 0.99}'

# Ниже тот же запрос, но без символа перехода на новую строку
curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'

# Ответ от сервера:
# {"name":"BestSale","description":"The best of the best","price":9.99,"tax":0.99}
"""
# Эта строка отправляет POST запрос на URL-адрес «http://127.0.0.1:8000/items/» с
# данными JSON, содержащими поля «имя», «описание», «цена» и «налог» вместе с
# соответствующими значениями. Заголовки «accept» и «Content-Type» имеют
# значение «application/json», мы пересылаем запросом json объект на сервер и хотим
# получить json в качестве ответа.
#
"""
# ● PUT запрос
"""
# Для отправки PUT запроса нашему серверу введём в терминале следующую строку:
"""
curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
application/json' -H 'Content-Type: application/json' -d
'{"name": "NewName", "description": "New description of the
object", "price": 77.7, "tax": 10.01}'

# Ниже тот же запрос, но без символа перехода на новую строку
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'

# Ответ от сервера:
# {"item_id":42,"item":{"name":"NewName","description":"New description of the object","price":77.7,"tax":10.01}}
"""
# Эта строка отправляет HTTP-запрос PUT на локальный сервер по адресу http://127.0.0.1:8000/,
# обновляя элемент с идентификатором 42 новой информацией, предоставленной в формате JSON,
# такой, как имя, описание, цена и налог.
# Мы можем опускать необязательные поля объекта Item в запросе.
# Ответ от сервера будет 200.
# А вот отсутствие обязательных параметров приведёт к ответу 422 Unprocessable Entity.
"""
# Хороший короткий PUT запрос:
curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
application/json' -H 'Content-Type: application/json' -d
'{"name": "NewName", "price": 77.7}'

# Ниже тот же запрос в одну строку
curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "price": 77.7}'

Ответ от сервера:
# {"item_id":42,"item":{"name":"NewName","description":null,"price":77.7,"tax":null}}
"""
#
"""
# Плохой PUT запрос:
curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
application/json' -H 'Content-Type: application/json' -d
'{"name": "NewName", "tax": 77.7}'

# Ниже тот же запрос в одну строку
curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "tax": 77.7}'

Ответ от сервера с ошибкой (так как не передали обязательный параметр price):
#  {"detail":[{"type":"missing",
    "loc":["body","price"],
    "msg":"Field required",
    "input":{"name":"NewName","tax":77.7},
    "url":"https://errors.pydantic.dev/2.6/v/missing"}]}
"""
# В данном запросе отсутствует обязательное поле price.
# Его мы сделали обязательным в классе Item строкой price: float.
# Код состояния ответа HTTP 422 Unprocessable Entity указывает, что сервер
# понимает тип содержимого в теле запроса и синтаксис запроса является
# правильным, но серверу не удалось обработать инструкции содержимого.
#
"""
# ● DELETE запрос
"""
# Чтобы удалить объект, нужен лишь его идентификатор, без передачи самого объекта.
# Curl будет выглядеть следующим образом:
"""
curl -X 'DELETE' 'http://127.0.0.1:8000/items/13' -H 'accept: application/json'

Ответ от сервера:
# {"item_id":13}
"""
# Запрос DELETE сообщает серверу о желании удалить объект с id 13
