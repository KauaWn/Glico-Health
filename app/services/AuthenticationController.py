from app import db
from app.modelos import Usuario
from flask import session
import sqlalchemy as sa


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
            return "Usuário não encontrado"

        if usuario.passw_hash != form.password.data:
            return "Senha incorreta"

        session['usuario_id'] = usuario.id #faz a identificação DO usuário

        usuario.remember_me = form.remember_me.data
        db.session.commit()

        return True