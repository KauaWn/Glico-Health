from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RedefinirSenhaForm(FlaskForm):
    email = EmailField(
        "E-mail",
        validators=[
            DataRequired(message="Informe seu e-mail."),
            Email(message="Informe um e-mail válido, como nome@dominio.com."),
        ],
    )
    nova_senha = PasswordField(
        "Nova senha",
        validators=[
            DataRequired(message="Informe a nova senha."),
            Length(min=8, message="A senha deve ter pelo menos 8 caracteres."),
        ],
    )
    confirmar_senha = PasswordField(
        "Confirmar nova senha",
        validators=[
            DataRequired(message="Confirme a nova senha."),
            EqualTo("nova_senha", message="As senhas não coincidem."),
        ],
    )
    submit = SubmitField("ALTERAR SENHA")