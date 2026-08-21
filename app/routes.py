from app import app
from flask import render_template, redirect, flash, url_for, request
from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.forms.dados_paciente import DadosPacienteForm
from app.controllers.UsuarioController import UsuarioController
from app.controllers.AuthenticationController import AuthenticationController
from app.forms.papel_form import PapelForm


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formCadastro = CadastroForm()
    if formCadastro.validate_on_submit():
        if UsuarioController.cadastro(formCadastro):
            flash("Cadastro efetuado com sucesso!")
            return redirect(url_for("questionario"))

        flash("Erro nas credenciais.")
    return render_template("cadastro.html", form=formCadastro)


@app.route("/login", methods=["GET", "POST"])
def login():
    formLogin = LoginForm()

    if formLogin.validate_on_submit():
        if AuthenticationController.login(formLogin):
            flash("Login efetuado com sucesso!", "success")
            return redirect(url_for("inicio"))
        else:
            flash("Usuário ou senha incorretos.", "error")

    return render_template("login.html", title="Login", form=formLogin)

@app.route("/questionario", methods=["GET", "POST"])
def questionario():
    form_papel = PapelForm(request.form)
    if request.method == "POST":
        if form_papel.validate_on_submit():
            if UsuarioController.salvar_papeis(form_papel.papeis.data):
                if 'paciente' in form_papel.papeis.data:
                    return redirect(url_for("questionario_paciente"))
                return redirect(url_for("inicio"))
            else:
                flash("Erro ao salvar os papéis no banco.", "error")
        else:
            flash("Por favor, selecione ao menos uma opção antes de continuar.", "warning")

    return render_template("questionario.html", form=form_papel)


@app.route("/questionario/paciente", methods=["GET", "POST"])
def questionario_paciente():
    form_paciente = DadosPacienteForm()
    if form_paciente.validate_on_submit():
        if UsuarioController.salvar_questionario_paciente(form_paciente):
            flash("Questionário respondido com sucesso!", "success")
            return redirect(url_for("login"))
        else:
            flash("Erro ao salvar o questionário.", "error")

    return render_template("quest_paciente.html", form=form_paciente)

@app.route("/questionario/tipo_cuidador", methods=["GET", "POST"])
def quest_tipo_cuidador():
    return render_template("tipo_cuidador.html")