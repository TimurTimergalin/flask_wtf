from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    cap_username = StringField('Логин капитана (или его заместителя)', validators=[DataRequired()])
    cap_password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Доступ')


# Задание 5 пока делать не буду.
# Не понял как добавить эмблему с помощью стилевого файла
