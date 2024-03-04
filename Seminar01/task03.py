# Задание №3.
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to our homepage!'


@app.route('/sum/<int:n1>/<int:n2>/')
def add(n1, n2):
    return f'Сумма {n1} + {n2} = {n1 + n2}'


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/1/2/  # Сумма 1 + 2 = 3
