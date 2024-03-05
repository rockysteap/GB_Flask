# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.

from flask import Flask, render_template, request

app = Flask(__name__)

warez = [
    ['group', 'name', 'desc', 'id'],
    ['Настольные игры', 'Диноостров', 'Описание "Диноостров"', 'board_dino'],
    ['Настольные игры', 'Каркассон', 'Описание "Каркассон"', 'board_kark'],
    ['Настольные игры', 'Шакал', 'Описание "Шакал"', 'board_jakal'],
    ['Сувениры', 'Календарь', 'Описание "Календарь"', 'souv_cal'],
    ['Сувениры', 'Кружка', 'Описание "Кружка"', 'souv_mug'],
    ['Сувениры', 'Сумка', 'Описание "Сумка"', 'souv_bag'],
]


def parse_wares_to_dict() -> list:
    # Преобразуем список warez в словарь, взяв значения warez[0] в качестве ключей
    res = []
    for val_lst_index in range(1, len(warez)):
        new_dict = {}
        for i in range(len(warez[0])):
            new_dict[warez[0][i]] = warez[val_lst_index][i]
        res.append(new_dict)
    return res


@app.route('/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)


@app.route('/categories/')
def categories():
    _warez = parse_wares_to_dict()

    context = {
        'title': 'Категории',
        'categories': [
            'Настольные игры',
            'Сувениры',
        ],
        'warez': _warez,
    }
    return render_template('categories.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'О нас',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'Контакты',
    }
    return render_template('contacts.html', **context)


@app.route('/warez/item/', methods=['GET', 'POST'])
def item():
    selected_item = request.args.get('selected_from_cats')
    _warez = parse_wares_to_dict()
    show_item = {}
    for item_dict in _warez:
        if item_dict['name'] == selected_item:
            show_item = dict(item_dict)
    context = {
        'title': 'Карточка товара',
        'selected': selected_item,
        'item': show_item,
    }
    return render_template('item.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
