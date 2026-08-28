from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm (FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message="Por favor, insira seu nome de usuário")])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira sua senha")])
    remember_me = BooleanField("Lembrar da próxima vez")
    submit = SubmitField('Entrar')