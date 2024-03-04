# Задание №5.
# Написать функцию, которая будет выводить на экран HTML страницу с заголовком
# "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to our homepage!'


@app.route('/html/')
def html():
    title = 'Моя первая HTML страница'
    par = 'Привет, мир!'
    return f'<h1>{title}</h1>\n<br><p>{par}</p>'


@app.route('/html2/')
def html2():
    return render_template('hello_world.html')


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/html/
# http://127.0.0.1:5000/html2/
