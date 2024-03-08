# POST запросы используются для отправки данных на сервер.
# Они отличаются от GET запросов тем, что данные, передаваемые в POST запросах, не видны в URL.
# Также POST запросы могут содержать большее количество данных, чем GET.
# Для того чтобы передать данные в POST запросе, обычно используют HTML форму (тег <form>).

# У формы нужно указать атрибут method="post" для правильной обработки сервером.
# См. form.html
# В данном примере мы создаем HTML-форму с полем "name" и кнопкой "submit".
# При нажатии на кнопку страница отправляет POST-запрос на указанный URL, в данном случае "/submit".

# В Python-коде функция, ассоциированная с URL "/submit",
# использует функцию request.form.get() для получения данных, переданных через форму.
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/submit  # Alex
# Hello Alex!
