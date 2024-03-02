from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/if/')
def html_index():
    context = {
        'title': 'Ветвление',
        'user': 'Крутой хакер!',
        'number': 7,
    }
    return render_template('show_if.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
