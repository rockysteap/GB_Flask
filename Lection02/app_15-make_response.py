# Во всех прошлых примерах мы возвращали из view функций обычный текст,
# текст форматированный как HTML,  динамически сгенерированные страницы
# через render_template и даже запросы переадресации благодаря функциям redirect() и url_for().

# Каждый раз Flask неявно формировал объект ответа - response.
# Если же мы хотим внести изменения в ответ, можно воспользоваться функцией make_response().

from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    # Используя render_template пробрасываем контекст в шаблон, но не возвращаем его,
    # а передаём результат в функцию make_response.
    # Ответ сформирован, но мы можем внести в него изменения перед возвратом.

    # Добавим в заголовки пару ключ-значение и установим куки для имени пользователя.
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
