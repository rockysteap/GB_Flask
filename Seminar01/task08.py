# Задание №8.
# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('auth.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


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
    return render_template('students_table_task08.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
