from app import app
from flask import render_template, redirect, flash
from app.forms.cadastro_form import CadastroForm
from app.controllers.UsuarioController import UserController


@app.route("/", methods=["GET", "POST"])
def home():
    form = CadastroForm()
    mostrar_cadastro = False

    if form.validate_on_submit():
        if UserController.cadastro(form):
            flash("Cadastro efetuado com sucesso!")
            return redirect('/')
        flash("Erro nas credenciais.")
        mostrar_cadastro = True
    elif form.is_submitted():
        mostrar_cadastro = True

    return render_template("index.html", form=form, mostrar_cadastro=mostrar_cadastro)