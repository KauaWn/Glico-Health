from app import app
from flask import render_template, redirect, flash, url_for
from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.controllers.UsuarioController import UserController
from app.controllers.AuthenticationController import AuthenticationController


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formCadastro = CadastroForm()
    if formCadastro.validate_on_submit():
        if UserController.cadastro(formCadastro):
            flash("Cadastro efetuado com sucesso!")
            return redirect(url_for("login"))

        flash("Erro nas credenciais.")
    return render_template("cadastro.html", form=formCadastro)


@app.route("/login", methods=["GET", "POST"])
def login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        if AuthenticationController.login(formLogin):
             flash("Login efetuado com sucesso!")
             return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/login')
    return render_template('login.html', title='Login', form=formLogin)