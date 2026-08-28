from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import DataRequired

class AssociarPaciente (FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message="Por favor, insira um email.")])
    submit = SubmitField('Associar Paciente')