from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class CadastroForm(FlaskForm):
    name = StringField('Como você deseja ser chamado?', validators=[DataRequired()])
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')