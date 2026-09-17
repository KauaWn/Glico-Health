from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import DataRequired, Email

class AssociarPaciente (FlaskForm):
    email = EmailField('Email', validators=[
        DataRequired(message="Por favor, insira um email."),
        Email(message="Insira um endereço de email válido.")
    ])
    submit = SubmitField('Associar Paciente')