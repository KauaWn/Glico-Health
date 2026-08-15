from app import app
from flask import render_template, redirect, flash, url_for

from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.controllers.UsuarioController import UserController


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()

    if form.validate_on_submit():
        if UserController.cadastro(form):
            flash("Cadastro efetuado com sucesso!")
            return redirect(url_for("home"))

        flash("Erro nas credenciais.")

    return render_template("cadastro.html", form=form)


# @app.route("/home")
# def home():
#     return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")