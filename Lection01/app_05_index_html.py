from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    # return render_template('index.html')
    # Вернет ошибку, т.к. flask не видит 'index.html' в корне проекта
    return render_template('index1.html')
    # index1.html необходимо разместить в '/static/templates'

if __name__ == '__main__':
    app.run(debug=True)
