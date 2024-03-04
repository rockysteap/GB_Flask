# Задание №2.
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в веб приложение:
# ○ страницу "about"
# ○ страницу "contact".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/about/')
def about():
    return 'About page'


@app.route('/contact/')
def contact():
    return 'Contact page'


if __name__ == '__main__':
    app.run(debug=True)
