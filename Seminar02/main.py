import os

from flask import Flask, render_template, request, session, abort, redirect, url_for, flash
from markupsafe import escape
from werkzeug.utils import secure_filename

from tasks import TASKS

app = Flask(__name__)
app.secret_key = b'2428dceeb689192ebfd4a901ed81d55f5d311bcfe888bdab7f19a94560cc1a02'


@app.route('/')
def index():
    context = {'title': TASKS[0]['name'], 'data': TASKS}
    return render_template('base.html', **context)


@app.route('/task01/')
def task01():
    context = {'title': TASKS[1]['name'], 'data': TASKS}
    return render_template('task01.html', **context)


@app.route('/task02/', methods=['GET', 'POST'])
def task02():
    _filename = session.setdefault('image', None)
    if request.method == 'POST':
        file = request.files.get('file')
        _filename = secure_filename(file.filename)
        if _filename.endswith('.jpg') or _filename.endswith('.png'):
            session['image'] = _filename
        # в случа отсутствия создадим 'uploads'
        os.makedirs('static/uploads', exist_ok=True)
        path = os.path.join(os.path.abspath('static/uploads'), _filename)
        file.save(path)
    context = {'title': TASKS[2]['name'], 'data': TASKS, 'image': session['image']}
    return render_template('task02.html', **context)


@app.route('/task03/', methods=['GET', 'POST'])
def task03():
    context = {'title': TASKS[3]['name'], 'data': TASKS}
    account = {'login': 'admin', 'password': '123'}
    if request.method == 'POST':
        auth_login = request.form.get('auth_login')
        auth_password = request.form.get('auth_password')
        if account['login'] == auth_login and account['password'] == auth_password:
            message = f'Добрый день, {account['login']}!'
            return render_template('task03.html', **context, message=message)
        else:
            message = f'Авторизация неуспешна.'
            return render_template('task03.html', **context, message=message)
    return render_template('task03.html', **context)


@app.route('/task04/', methods=['GET', 'POST'])
def task04():
    context = {'title': TASKS[4]['name'], 'data': TASKS}
    if request.method == 'POST':
        text = request.form.get('text')
        message = f'Введенный текст состоит из {len(text)} знаков.'
        return render_template('task04.html', **context, message=message)
    return render_template('task04.html', **context)


@app.route('/task05/', methods=['GET', 'POST'])
def task05():
    context = {'title': TASKS[5]['name'], 'data': TASKS}
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')
        if operation == '/' and num2 == '0':
            message = f'ZeroDivisionError: division by zero - Ошибка: деление на ноль'
        else:
            result = round(eval(f'{num1} {operation} {num2}'), 10)
            message = f'{num1} {operation} {num2} = {result}'
        return render_template('task05.html', **context, message=message)
    return render_template('task05.html', **context)


@app.route('/task06/', methods=['GET', 'POST'])
def task06():
    context = {'title': TASKS[6]['name'], 'data': TASKS}
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not 18 <= int(age) <= 99:
            abort(403)
        else:
            message = f'Добро пожаловать, {name}!'
        return render_template('task06.html', **context, message=message)
    return render_template('task06.html', **context)


@app.route('/task07/', methods=['GET', 'POST'])
def task07():
    context = {'title': TASKS[7]['name'], 'data': TASKS}
    if request.method == 'POST':
        num = request.form.get('num')
        return redirect(url_for('task07_redirected', num=num))
    return render_template('task07.html', **context)


@app.route('/task07_redirected/')
def task07_redirected():
    context = {'title': TASKS[7]['name'], 'data': TASKS}
    num = request.args['num']
    message = f'Число {num} в квадрате = {float(num) * float(num)}'
    return render_template('task07_redirected.html', **context, message=message)


@app.route('/task08/', methods=['GET', 'POST'])
def task08():
    context = {'title': TASKS[8]['name'], 'data': TASKS}
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('task08_redirected', name=name))
    return render_template('task08.html', **context)


@app.route('/task08_redirected/')
def task08_redirected():
    context = {'title': TASKS[8]['name'], 'data': TASKS}
    name = request.args['name']
    if name:
        message = f'Привет, {name}!'
        flash(message, 'success')
    else:
        message = f'Введите имя!'
        flash(message, 'error')
    return render_template('task08_redirected.html', **context)


@app.route('/task09/', methods=['GET', 'POST'])
def task09():
    context = {'title': TASKS[9]['name'], 'data': TASKS}
    message = f'Задание ушло в раздел домашних.'
    flash(message, 'success')
    return render_template('task09.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
