# Задание №4.
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to our homepage!'


@app.route('/len/<s>/')
def add(s):
    return f'Длина строки "{s}" = {len(s)} символов'


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/len/Такая%20вот%20строка/  # Длина строки "Такая вот строка" = 16 символов
