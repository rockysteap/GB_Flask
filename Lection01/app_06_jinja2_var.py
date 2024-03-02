from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон'
    }
    return render_template('index2.html', **context)


# index1.html необходимо разместить в '/static/templates'

if __name__ == '__main__':
    app.run(debug=True)
