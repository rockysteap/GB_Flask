from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemy —
# это мощный инструмент для работы с базами данных в приложениях Flask.
# Он предоставляет простой и удобный интерфейс для создания моделей,
# выполнения запросов и управления данными.

app = Flask(__name__)

# Варианты подключений к различным БД:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/db_name'


db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)
