from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Введите путь к файлу адресной строки'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}!'
    return f'Ваш файл находится в: {escape(file)}!'


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
# http://127.0.0.1:5000/%3Cscript%3Ealert(%22I%20am%20haсker%22)%3C/script%3E/

# Без escape открывает окно браузера с alert сообщением
# Возвращает строку
# Ваш файл находится в: <script>alert("I am haсker")</script>!
# Таким образом escape защищает от инъекций нежелательного кода
