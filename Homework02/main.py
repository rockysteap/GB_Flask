# Создать страницу, на которой будет форма для ввода имени и электронной почты.
# При отправке которой будет создан cookie файл с данными пользователя.
#
# Также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
#
# На странице приветствия должна быть кнопка "Выйти".
#
# При нажатии на кнопку будет удален cookie файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, make_response, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('auth'))


@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    context = {'title': 'Авторизация'}
    if request.method == 'POST':
        username = request.form.get('auth_username')
        email = request.form.get('auth_email')
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    response = make_response(render_template('auth.html', **context))
    return response


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
