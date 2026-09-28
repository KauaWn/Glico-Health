from app import db
from app.modelos import Usuario
from flask import session
import hmac
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash


class AuthenticationController:
    def login(form):
        print("O usuario {} fez o login, lembrar={}".format(
            form.username.data,
            form.remember_me.data
        ))

        query = sa.select(Usuario).where(Usuario.username == form.username.data)
        usuario = db.session.scalars(query).first()

        # usuario = Usuario.query.filter_by(username=form.username.data).first()

        if not usuario:
            return False

        if not usuario.passw_hash:
            return False

        if "$" in usuario.passw_hash:
            if not check_password_hash(usuario.passw_hash, form.password.data):
                return False
        else:
            # Upgrade legacy plaintext passwords only after an exact match.
            if not hmac.compare_digest(
                usuario.passw_hash.encode("utf-8"),
                form.password.data.encode("utf-8"),
            ):
                return False
            usuario.passw_hash = generate_password_hash(form.password.data)

        session['usuario_id'] = usuario.id #faz a identificação DO usuário

        usuario.remember_me = form.remember_me.data
        db.session.commit()

        return True