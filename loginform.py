from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username1 = StringField('Id астронавта', validators=[DataRequired()])
    password1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username2 = StringField('Id капитана', validators=[DataRequired()])
    password2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
