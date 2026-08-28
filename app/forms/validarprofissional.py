from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ValidarProfissional (FlaskForm):
    conselhoprofissional = StringField('Conselho Regional', validators=[DataRequired(message="Por favor, insira um Conselho Regionbal. Ex: CRM")])
    registroprofissional = StringField('Número de Registro', validators=[DataRequired(message="Por favor, insira o seu número de registro")])
    submit = SubmitField('Entrar')