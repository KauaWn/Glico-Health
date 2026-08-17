from app import db
from app.models.usuario import Usuario
from flask import session

class UsuarioController:
    @staticmethod
    def cadastro(formCadastro):
        usuario = Usuario(
            name=formCadastro.name.data,
            username=formCadastro.username.data,
            email=formCadastro.email.data,
            password_hash=formCadastro.password.data,
            # rm=False
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
            
            db.session.commit()
            return True
            
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar papéis no banco: {e}")
            return False
    
        