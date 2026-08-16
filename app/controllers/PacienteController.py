from app import db
from app.models.usuario import Usuario

class PacienteController:
    @staticmethod
    def cadastro(formCadastro):
        usuario = Usuario(
            name=formCadastro.name.data,
            username=formCadastro.username.data,
            email=formCadastro.email.data,
            password_hash=formCadastro.password.data,
            rm=False
        )

        db.session.add(usuario)
        db.session.commit()

        print("O usuario {} ({}) - {} fez o cadastro".format(
            formCadastro.name.data,
            formCadastro.username.data,
            formCadastro.email.data
        ))
        
        return True
    
        