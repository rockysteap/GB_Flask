# Категории сообщений в flash позволяют различать типы сообщений и выводить их по-разному.
# Категория по умолчанию message.
# Но вторым аргументом можно передавать и другие категории, например warning, success и другие.

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'2428dceeb689192ebfd4a901ed81d55f5d311bcfe888bdab7f19a94560cc1a02'
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return '<h2>Hi!</h2>'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
