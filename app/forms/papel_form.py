from flask_wtf import FlaskForm
from wtforms import SelectMultipleField
from wtforms.validators import DataRequired

class PapelForm(FlaskForm):
    papeis = SelectMultipleField(
        'Papéis',
        choices=[('paciente', 'Paciente'), ('cuidador', 'Cuidador'), ('responsavel', 'Responsável legal')],
        validators=[DataRequired(message="Selecione ao menos um papel para continuar.")]
    )
