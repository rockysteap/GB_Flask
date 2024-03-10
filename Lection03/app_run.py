from datetime import datetime, timedelta

from flask import Flask, render_template, jsonify
from Lection03.models import db, User, Post

app = Flask(__name__)

# Путь к БД в случае запуска команд из консоли (на одном уровне с файлом wsgi.py)
# 'sqlite:///mydb.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

# Путь к БД при обращении из файла (запуск из app_console.py)
# '../' -> выйти из instance директории урока,
# '../' -> выйти из директории урока в корень проекта
# 'instance/' -> зайти в директорию instance в корне проекта)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/lection03.db'

db.init_app(app)


@app.route('/')
def index():
    return f'Hi!'


@app.route('/data/')
def data():
    return f'Your data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id,
                         'title': post.title,
                         'content': post.content,
                         'created_at': post.created_at}
                        for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404


@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.now() - timedelta(days=7)  # timedelta(minutes=7) -> jsonify -> 'error'
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id,
                         'title': post.title,
                         'content': post.content,
                         'created_at': post.created_at}
                        for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


if __name__ == '__main__':
    app.run(debug=True)
