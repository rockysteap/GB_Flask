# Перенаправления во Flask позволяют перенаправлять пользователя с одной страницы на другую.
# Это может быть полезно, например, для перенаправления пользователя после успешной отправки
# формы или для перенаправления пользователя на страницу авторизации при попытке доступа к
# защищенной странице без авторизации.

# Для перенаправления во Flask используется функция redirect().
# Она принимает URL-адрес, на который нужно перенаправить пользователя.
# И возвращает объект ответа, который перенаправляет пользователя на указанный адрес.

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external/')
def external_redirect():
    return redirect('https://www.python.org')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)

# http://127.0.0.1:5000/redirect/123
# формируется адрес http://127.0.0.1:5000/hello/123 и выводится 'Привет, 123!'
