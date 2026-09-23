from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CadastroForm(FlaskForm):
    name = StringField('Como você deseja ser chamado?', validators=[DataRequired(message="Por favor, insira um nome.")])
    username = StringField('Nome de Usuario', validators=[DataRequired(message="Por favor, insira um nome de usuário.")])
    email = EmailField('Email', validators=[
        DataRequired(message="Por favor, insira um email."),
        Email(message="Insira um endereço de email válido.")
    ])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira uma senha."), Length(min=8, message="A senha deve ter pelo menos 8 caracteres.")])
    confirm_password = PasswordField(
        'Confirmar senha:',
        validators=[
            DataRequired(message="Por favor, confirme sua senha."),
            EqualTo('password', message="As senhas precisam ser iguais.")
        ]
    )
    submit = SubmitField('Cadastrar')