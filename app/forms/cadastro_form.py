from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class CadastroForm(FlaskForm):
    name = StringField('Como você deseja ser chamado?', validators=[DataRequired(message="Por favor, insira um nome.")])
    username = StringField('Nome de Usuario', validators=[DataRequired(message="Por favor, insira um nome de usuário.")])
    email = StringField('Email', validators=[DataRequired(message="Por favor, insira um email.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira uma senha.")])
    confirm_password = PasswordField('Confirmar senha:', validators=[DataRequired(message="Por favor, confirme sua senha."), EqualTo('password')])
    submit = SubmitField('Cadastrar')