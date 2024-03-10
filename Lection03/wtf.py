# Flask-WTForm —
# это модуль для Flask, который предоставляет инструменты для работы
# с формами веб-приложений на Python.
# Flask-WTForm позволяет легко создавать и обрабатывать формы,
# валидировать данные, защищать приложение от атак CSRF и многое другое.

# CSRF (cross-site request forgery — «межсайтовая подделка запросов»).

from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect

from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c56cd00d1a08c65029f644cdba4002dc308eee2506f963bb6c7d88281fc2e229'
csrf = CSRFProtect(app)
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return f'Hi!'


@app.route('/data/')
def data():
    return f'Your data!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt  # Декоратор-исключение (отправка формы без токена)
def my_form():
    return f'No CSRF protection!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():

        # Здесь получил ошибку об отсутствии email_validator
        # -> установил 'pip install email-validator'

        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
