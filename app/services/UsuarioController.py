from datetime import date

from app import db
from datetime import date 
from flask import session
from app.modelos import Usuario, Paciente, Cuidador, Responsavel
from sqlalchemy import select
import sqlalchemy as sa

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
                        Cuidador(id_usuario=usuario_id, tipo_cuidador=None)  # Inicialmente sem tipo definido
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

    @staticmethod
    def salvar_tipo_cuidador(tipo_cuidador):
        try:
            usuario_id = session.get('usuario_id')
            if not usuario_id:
                print("Erro: Nenhum usuário encontrado na sessão.")
                return False

            # Busca o cuidador existente para atualizar
            cuidador = db.session.scalars(select(Cuidador).where(Cuidador.id_usuario == usuario_id)).first()
            
            if not cuidador:
                print("Erro: Cuidador não encontrado para o usuário.")
                return False

            # Atualiza o tipo de cuidador
            cuidador.tipo_cuidador = tipo_cuidador

            db.session.commit()

            print(f"Tipo de cuidador do usuário {usuario_id} salvo com sucesso!")
            return True

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar tipo de cuidador: {e}")
            return False

    @staticmethod
    def salvar_dados_profissional(conselho_profissional, registro_profissional):
        try:
            usuario_id = session.get('usuario_id')
            if not usuario_id:
                print("Erro: Nenhum usuário encontrado na sessão.")
                return False

            # Busca o cuidador existente para atualizar
            cuidador = db.session.scalars(select(Cuidador).where(Cuidador.id_usuario == usuario_id)).first()
            
            if not cuidador:
                print("Erro: Cuidador não encontrado para o usuário.")
                return False

            # Atualiza os dados profissionais
            cuidador.conselho_profissional = conselho_profissional
            cuidador.registro_profissional = registro_profissional

            db.session.commit()

            print(f"Dados profissionais do cuidador {usuario_id} salvos com sucesso!")
            return True

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar dados profissionais: {e}")
            return False

    @staticmethod
    def buscar_usuario_login(): #função que faz a busca pelo usuário
        usuario_id = session.get('usuario_id')

        if not usuario_id:
            print ("Erro: Nenhum usuário encontrado.")
            return None 

        usuario = db.session.get(Usuario, usuario_id)

        if not usuario:
            print("Erro: Nenhum usuário cadastrado no banco de dados.")
            return None

        return usuario 

    @staticmethod
    def buscar_paciente_login():
        usuario_id = session.get('usuario_id')

        if not usuario_id:
            print("Erro: Nenhum usuário encontrado.")
            return None

        query = sa.select(Paciente).where(Paciente.id_usuario == usuario_id)
        paciente = db.session.scalars(query).first()

        if not paciente:
            print("Erro: Paciente não cadastrado no banco de dados.")
            return None

        if paciente.genero == 'F':
            genero = 'Feminino'
        elif paciente.genero == 'M':
            genero = 'Masculino'
        else:
            genero = 'Não informado'

        if paciente.tipo_diabete.value == 'tipo1':
            tipo_diabete = 'Tipo 1'
        elif paciente.tipo_diabete.value == 'tipo2':
            tipo_diabete = 'Tipo 2'
        elif paciente.tipo_diabete.value == 'gestacional':
            tipo_diabete = 'Gestacional'
        else: 
            tipo_diabete = 'Não informado'

        if paciente.nascimento: 
            hoje = date.today()

            idade = hoje.year - paciente.nascimento.year

            if (hoje.month, hoje.day) < (paciente.nascimento.month, paciente.nascimento.day):
                idade -= 1
        else:
            idade = None 

        return paciente, genero, tipo_diabete, idade 