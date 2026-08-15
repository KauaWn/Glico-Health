class UserController:
    def cadastro(formCadastro):
        print("O usuario {} fez o cadastro".format(
            formCadastro.username.data
        ))
        return True