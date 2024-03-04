# Задание №6.
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to our homepage!'


@app.route('/students/')
def students():
    _students = [
        {'firstname': 'Алекс', 'lastname': 'Алексеев', 'age': 16, 'avg_score': 77},
        {'firstname': 'Борис', 'lastname': 'Борисов', 'age': 17, 'avg_score': 88},
        {'firstname': 'Вениамин', 'lastname': 'Вениаминов', 'age': 18, 'avg_score': 99},
    ]
    context = {
        'titles': {'firstname': 'Имя', 'lastname': 'Фамилия', 'age': 'Возраст', 'avg_score': 'Средний балл'},
        'students': _students
    }
    # Вывод в 3 столбца (bootstrap настройки из лекции)
    # return render_template('students.html', **context)
    # Вывод в таблице
    return render_template('students_table.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
