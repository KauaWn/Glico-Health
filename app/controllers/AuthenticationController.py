from app import db
from app.models.paciente import Paciente
class AuthenticationController:
    def login(form):
        print("O usuario {} fez o login, lembrar={}".format(
            form.username.data,
            form.rm.data
        ))

        usuario = Paciente.query.filter_by(username=form.username.data).first()

        if usuario and usuario.password_hash == form.password.data:
            usuario.rm = form.rm.data
            db.session.commit()
            return True
        return False