from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) =}<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") =}<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) =}<br>'
    return text


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/test_url_for/123/
# В num лежит 123

# Функция url_for("test_url", num=42)
#   сгенерирует следующий URL ='/test_url_for/42/'

# Функция url_for("test_url", num=42, data="new_data")
#   сгенерирует следующий URL ='/test_url_for/42/?data=new_data'

# Функция url_for("test_url", num=42, data="new_data", pi=3.14515)
#   сгенерирует следующий URL ='/test_url_for/42/?data=new_data&pi=3.14515'

# Функция 'url_for' принимает имя view функции в качестве первого аргумента
# и любое количество ключевых аргументов.

# Каждый ключ соответствует переменной в URL адресе.
# Отсутствующие в адресе переменные добавляются к адресу в качестве параметров запроса,
# т.е. после знака вопрос '?', как пары ключ-значение, разделённые символом &.

# 🔥 Внимание!
# Первый параметр совпадает с названием функции-представления, а не с адресом внутри route.
# Таким образом изменение маршрутов автоматически изменит генерируемые url без лишних правок.
# Ведь имена view функций останутся прежними.
