# WTForms —
# это библиотека Python, которая позволяет создавать HTML-формы,
# а также проводить их валидацию.

# Flask-WTF использует WTForms для создания форм.

# Для создания формы с помощью Flask-WTF необходимо определить класс формы,
# который наследуется от класса FlaskForm.

# Каждое поле формы определяется как экземпляр класса, который наследуется от класса Field.

# WTForms предоставляет множество типов полей для формы.
# Вот некоторые из них:
# ● StringField — строковое поле для ввода текста;
# ● IntegerField — числовое поле для ввода целочисленных значений;
# ● FloatField — числовое поле для ввода дробных значений;
# ● BooleanField — чекбокс;
# ● SelectField — выпадающий список;
# ● DateField — поле для ввода даты;
# ● FileField — поле для загрузки файла.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])


# WTForms позволяет проводить валидацию данных формы.
# Для этого можно использовать готовые валидаторы (DataRequired, Email, Length и т.д.)

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

# 🔥 Важно!
# Для правильной работы кода необходимо отдельно установить валидатор электронной почты.
# Для этого достаточно выполнить команду:
# pip install email-validator

# 💡 Внимание!
# В валидатор EqualTo передаётся строковое имя переменной,
# т.е. то, что стоит слева от знака равно, а не название поля.
