from Lection01.app_01_hello_world import app


if __name__ == "__main__":
    app.run(debug=True)


# WSGI (англ. Web Server Gateway Interface)
# — стандарт взаимодействия между Python-программой,
# выполняющейся на стороне сервера, и самим веб-сервером, например Apache.

# Запуск из командной строки:
# 'flask run' или 'flask run --debug'
