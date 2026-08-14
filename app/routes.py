from app import app
from flask import render_template, redirect, flash, url_for
from app.forms.cadastro_form import CadastroForm
from app.controllers.UsuarioController import UserController


@app.route("/", methods=["GET", "POST"])
def inicio():
    form = CadastroForm()
    mostrar_cadastro = False

    if form.validate_on_submit():
        if UserController.cadastro(form):
            flash("Cadastro efetuado com sucesso!")
            return redirect(url_for("home"))
        flash("Erro nas credenciais.")
        mostrar_cadastro = True
    elif form.is_submitted():
        mostrar_cadastro = True

    return render_template("index.html", form=form, mostrar_cadastro=mostrar_cadastro)

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("inicio.html")