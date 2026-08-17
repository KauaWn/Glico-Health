from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

class DadosPacienteForm(FlaskForm):
    dia = SelectField('Dia', choices=[('', 'Dia')] + [(str(i), f"{i:02d}") for i in range(1, 32)], validators=[DataRequired()])
    mes = SelectField('Mês', choices=[('', 'Mês'),
        ('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'),
        ('5', 'Maio'), ('6', 'Junho'), ('7', 'Julho'), ('8', 'Agosto'),
        ('9', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')
    ], validators=[DataRequired()])
    # ano atual (2026) até 1920
    ano = SelectField('Ano', choices=[('', 'Ano')] + [(str(i), str(i)) for i in range(2026, 1919, -1)], validators=[DataRequired()])
    
    sexo = SelectField(
        'Sexo', 
        choices=[
            ('nao_informar', 'Prefiro não informar'),
            ('masculino', 'Masculino'), 
            ('feminino', 'Feminino')
        ],
        validators=[DataRequired()]
    )
    
    tipo_diabetes = SelectField(
        'Tipo de Diabetes', 
        choices=[
            ('tipo_1', 'Tipo 1'), 
            ('tipo_2', 'Tipo 2'), 
            ('gestacional', 'Gestacional')
        ],
        validators=[DataRequired()]
    )
