# Обработка запросов
# Современные приложения должны уметь обрабатывать отправляемые от клиентов данные.
# Это может быть информация из адресной строки, данные формы или даже наборы байт
# — файлы разных типов.

# Обработка GET запросов
# До этого момента мы работали только с GET запросами.
# Представления реагировали на url адреса и получали из них данные в виде переменных.
# Через адресную строку можно передавать только текстовые данные.
# У самой строки есть ограничение на длину.
# А данные передаются либо как часть адреса, либо как пара ключ-значение после знака вопрос.

# 🔥 Важно!
# Обработка GET запросов является поведением по умолчанию для представлений.

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'


if __name__ == '__main__':
    app.run(debug=True)

# В первую очередь мы импортировали request — глобальный объект Flask,
# который даёт доступ к локальной информации для каждого контекста запроса.

# Т.е. request содержит данные, которую клиент передаёт на сторону сервера.

# Дополнительные параметры собираются в словаре args объекта request.
# И раз перед нами словарь, можно получить значение обратившись к ключу через метод get().

# Перейдём по адресу
# http://127.0.0.1:5000/get/
# и увидим следующий вывод:

# Привет, новичок.
# ImmutableMultiDict([])  # Неизменяемый словарь

# Перейдём по адресу
# http://127.0.0.1:5000/get/?name=alex&age=13&level=80
# и увидим следующий вывод:

# Похоже ты опытный игрок, раз имеешь уровень 80
# ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level', '80')])

# 🔥 Важно!
# Используйте метод get для поиска значения внутри request.args.
# Так вы избежите ошибок обращения к несуществующему ключу.
# Строку формирует пользователь, а он может не знать об обязательных ключах.
# Альтернатива — блок try с обработкой KeyError.
