from datetime import date

from app import db
# from app.models.usuario import Usuario
from flask import session
from app.modelos import Usuario, Paciente, Cuidador, Responsavel
from sqlalchemy import select


class UsuarioController:
    @staticmethod
    def cadastro(formCadastro):
        usuario = Usuario(
            name=formCadastro.name.data,
            username=formCadastro.username.data,
            email=formCadastro.email.data,
            passw_hash=formCadastro.password.data,
            remember_me=False
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
            usuario_id = session.get('usuario_id')

            if not usuario_id:
                print("Erro: Nenhum usuário encontrado na sessão.")
                return False

            # Busca o usuário
            usuario_atual = db.session.get(Usuario, usuario_id)

            if not usuario_atual:
                print("Erro: Usuário não encontrado no banco de dados.")
                return False

            # Salva os papéis através dos relacionamentos
            for papel in lista_papeis:

                if papel == "paciente":
                    db.session.add(
                        Paciente(id_usuario=usuario_id)
                    )

                elif papel == "cuidador":
                    db.session.add(
                        Cuidador(id_usuario=usuario_id)
                    )

                elif papel == "responsavel":
                    db.session.add(
                        Responsavel(id_usuario=usuario_id)
                    )

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
            questionario = db.session.scalars(select(Paciente).where(Paciente.id_usuario == usuario_id)).first()
            
            if not questionario:
                print("Erro: Questionário não encontrado para o usuário.")
                return False

            # Atualiza os dados do questionário
            # Dados da data de nascimento
            dia = int(form_paciente.dia.data)
            mes = int(form_paciente.mes.data)
            ano = int(form_paciente.ano.data)

            questionario.nascimento = date(
                ano,
                mes,
                dia
            )
            generos = {
                "masculino": "M",
                "feminino": "F",
                "outro": "O"
            }

            questionario.genero = generos.get(
                form_paciente.sexo.data
            )

            tipos_diabetes = {
                "tipo_1": "tipo1",
                "tipo_2": "tipo2",
                "gestacional": "gestacional"
            }

            questionario.tipo_diabete = tipos_diabetes.get(
                form_paciente.tipo_diabetes.data
            )

            db.session.commit()

            print(f"Questionário do paciente {usuario_id} salvo com sucesso!")
            return True

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar questionário do paciente: {e}")
            return False
