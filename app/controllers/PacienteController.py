from app import db
from app.models.paciente import Paciente

class PacienteController:
    @staticmethod
    def cadastro(formCadastro):
        paciente = Paciente(
            name=formCadastro.name.data,
            username=formCadastro.username.data,
            email=formCadastro.email.data,
            password_hash=formCadastro.password.data,
            rm=False
        )

        db.session.add(paciente)
        db.session.commit()

        print("O usuario {} ({}) - {} fez o cadastro".format(
            formCadastro.name.data,
            formCadastro.username.data,
            formCadastro.email.data
        ))
        
        return True
    
        