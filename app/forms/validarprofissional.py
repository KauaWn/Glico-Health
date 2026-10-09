from re import IGNORECASE
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

UFS = "AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO"
FORMATO_REGISTRO = rf"^(?:(?:{UFS})\d{{6}}|\d{{6}}(?:{UFS}))$"

class ValidarProfissional (FlaskForm):
    conselhoprofissional = StringField('Conselho Regional', validators=[DataRequired(message="Por favor, insira um Conselho Regional. Ex: CRM")])
    registroprofissional = StringField('Número de Registro', filters=[lambda valor: (valor or "").strip().upper()], validators=[
        DataRequired(message="Por favor, insira o seu número de registro"),
        Regexp(
            FORMATO_REGISTRO,
            flags=IGNORECASE,
            message="O registro deve ter uma UF válida e seis números, como RN123456 ou 123456RN.",
        ),
    ])
    submit = SubmitField('Entrar')