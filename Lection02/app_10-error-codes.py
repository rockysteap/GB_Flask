import logging
from flask import Flask, render_template, request, abort

# Закомментируем импорт функции get_blog.
# from Lection02.db import get_blog

# Теперь при попытке найти статью по id получаем сообщение на странице:
# Internal Server Error
# The server encountered an internal error and was unable to complete your request.
# Either the server is overloaded or there is an error in the application.

# Для такого случая необходим обработчик ошибки 500

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    ...
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    ...
    # возвращаем найденную в БД статью


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)
