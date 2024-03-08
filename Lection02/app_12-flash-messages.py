# Flash сообщения во Flask являются способом передачи информации между запросами.
# Это может быть полезно, например, для вывода сообщений об успешном выполнении операции
# или об ошибках ввода данных.

# Для работы с flash сообщениями используется функция flash().
# Она принимает сообщение и категорию, к которой это сообщение относится,
# и сохраняет его во временном хранилище.

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
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
