from flask import Flask
from Lection03.models import db, User, Post

app = Flask(__name__)

# Путь к БД в случае запуска команд из консоли (на одном уровне с файлом wsgi.py)
# 'sqlite:///mydb.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lection03.db'

# Путь к БД при обращении из файла (запуск из app_run.py)
# '../' -> выйти из instance директории урока,
# '../' -> выйти из директории урока в корень проекта
# 'instance/' -> зайти в директорию instance в корне проекта)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydb.db'

db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


# Выполняем из командной строки: 'flask ini-db'
# 🔥 Внимание!
# В wsgi.py файле корневой директории проекта необходимо
# корректно указать ссылку на текущий файл.


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


# Выполняем из командной строки: 'flask add-john'


@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')


# Выполняем из командной строки: 'flask edit-john'


@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')


# Выполняем из командной строки: 'flask del-john'


@app.cli.command("fill-db")
def fill_tables():
    count = 5

    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)

    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}',
                        content=f'Post content {post}', author=author)
        db.session.add(new_post)

    # Передаем в БД
    db.session.commit()


# Выполняем из командной строки: 'flask fill-db'


if __name__ == '__main__':
    app.run(debug=True)
