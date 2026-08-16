from app import db
from app.models.usuario import Usuario
class AuthenticationController:
    def login(form):
        print("O usuario {} fez o login, lembrar={}".format(
            form.username.data,
            form.rm.data
        ))

        usuario = Usuario.query.filter_by(username=form.username.data).first()

        if not usuario:
            return "Usuário não encontrado"

        if usuario.password_hash != form.password.data:
            return "Senha incorreta"

        usuario.rm = form.rm.data
        db.session.commit()

        return True