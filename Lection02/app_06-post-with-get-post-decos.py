# GET и POST запросы нужны, чтобы отправлять данные на сервер.
# GET запросы используются, чтобы получать данные, а POST — чтобы отправлять.

# Вместо одной функции submit(), которая обрабатывает и get и post запросы были созданы две.
# В первой использован декоратор get и она отвечает за отрисовку формы.
# Вторая функция имеет декоратор post с тем же самым аргументом, что и у get.
# Внутри читаем данные формы без лишних проверок метода запроса.

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/submit  # 123
# Hello 123!

# Если закомментировать submit_get(), форма, соответственно, не откроется:

# Not Found
# The requested URL was not found on the server.
# If you entered the URL manually please check your spelling and try again.

# Если закомментировать submit_post(), то при отправке имени получим:

# Method Not Allowed
# The method is not allowed for the requested URL.
