# Задание №7.
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to our homepage!'


@app.route('/news/')
def news():
    _news = [
        {
            'title': 'Заголовок1',
            'info': 'Новость1',
            'date': '02.03.2024'
        },
        {
            'title': 'Заголовок2',
            'info': 'Новость2',
            'date': '02.03.2024'
        },
        {
            'title': 'Заголовок3',
            'info': 'Новость3',
            'date': '02.03.2024'
        },
    ]
    context = {
        'title': 'Новости',
        'news': _news
    }
    # Вывод в 3 столбца (bootstrap настройки из лекции)
    # return render_template('news.html', **context)
    # Вывод в 1 столбец
    return render_template('news2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
