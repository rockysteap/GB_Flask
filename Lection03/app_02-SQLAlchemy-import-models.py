from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

# 🔥 Важно!
# Теперь класс не получает приложение Flask app при инициализации.
# Для инициализации баз данных необходимо выполнить строку db.init_app(app)

db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)
