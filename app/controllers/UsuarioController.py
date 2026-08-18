from app import db
from app.models.usuario import Usuario
from app.models.questionario import Questionario
from flask import session

class UsuarioController:
    @staticmethod
    def cadastro(formCadastro):
        usuario = Usuario(
            name=formCadastro.name.data,
            username=formCadastro.username.data,
            email=formCadastro.email.data,
            password_hash=formCadastro.password.data,
            rm=False,
            papel="Pendente"
        )

        db.session.add(usuario)
        db.session.commit()
    
        session['usuario_id'] = usuario.id

        print("O usuario {} ({}) - {} fez o cadastro".format(
            formCadastro.name.data,
            formCadastro.username.data,
            formCadastro.email.data
        ))
        
        return True

    @staticmethod
    def salvar_papeis(lista_papeis):
        try:
            # verifica o id do usuario
            usuario_id = session.get('usuario_id')
            if not usuario_id:
                print("Erro: Nenhum usuário encontrado na sessão.")
                return False

            # busca o usuario
            usuario_atual = Usuario.query.get(usuario_id)
            if not usuario_atual:
                print("Erro: Usuário não encontrado no banco de dados.")
                return False

            papeis_string = ", ".join(lista_papeis)
            usuario_atual.papel = papeis_string
            
            # Salva também no questionário
            questionario = Questionario(
                usuario_id=usuario_id,
                papeis=papeis_string
            )
            db.session.add(questionario)
            db.session.commit()
            
            return True
            
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar papéis no banco: {e}")
            return False

    @staticmethod
    def salvar_questionario_paciente(form_paciente):
        try:
            usuario_id = session.get('usuario_id')
            if not usuario_id:
                print("Erro: Nenhum usuário encontrado na sessão.")
                return False

            # Busca o questionário existente para atualizar
            questionario = Questionario.query.filter_by(usuario_id=usuario_id).first()
            
            if not questionario:
                print("Erro: Questionário não encontrado para o usuário.")
                return False

            # Atualiza os dados do questionário
            questionario.dia = int(form_paciente.dia.data)
            questionario.mes = int(form_paciente.mes.data)
            questionario.ano = int(form_paciente.ano.data)
            questionario.sexo = form_paciente.sexo.data
            questionario.tipo_diabetes = form_paciente.tipo_diabetes.data

            db.session.commit()

            print(f"Questionário do paciente {usuario_id} salvo com sucesso!")
            return True

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar questionário do paciente: {e}")
            return False
