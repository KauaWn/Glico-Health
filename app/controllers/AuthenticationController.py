class AuthenticationController:
    def login(form):
        print("O usuario {} fez o login, lembrar={}".format(
            form.username.data,
            form.rm.data
        ))
        return True