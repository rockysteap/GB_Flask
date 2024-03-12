# "Имя", "Фамилия", "Email", "Пароль".
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    # настройки
    pass_len = 8
    regexp = '(?=.*[a-zA-Zа-яА-Я])(?=.*[0-9])[A-Za-zа-яА-Я\\d]{8,}'
    password_main_message = (f'Пароль должен содержать не менее {pass_len} символов, '
                             f'включая хотя бы одну букву и одну цифру.')
    password_secondary_message = f'Подтверждение должно совпадать с паролем.'

    # поля
    email = StringField('Адрес электронной почты', validators=[DataRequired(), Email()])
    firstname = StringField('Имя', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('Фамилия', validators=[DataRequired(), Length(max=30)])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=pass_len),
                                         Regexp(regexp, message=password_main_message)])
    confirm_password = PasswordField('Подтверждение пароля',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message=password_secondary_message)])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField('Адрес электронной почты', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
