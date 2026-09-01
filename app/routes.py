from app import app
from flask import render_template, redirect, flash, url_for, request
from app.forms.associarpaciente import AssociarPaciente
from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.forms.dados_paciente import DadosPacienteForm
from app.forms.validarprofissional import ValidarProfissional
from app.services.UsuarioController import UsuarioController
from app.services.AuthenticationController import AuthenticationController
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
    form_papel = PapelForm()
    if form_papel.validate_on_submit():
        if UsuarioController.salvar_papeis(form_papel.papeis.data):
            if 'paciente' in form_papel.papeis.data:
                return redirect(url_for("questionario_paciente"))
            if 'cuidador' in form_papel.papeis.data:
                return redirect(url_for("quest_tipo_cuidador"))
            if 'responsavel' in form_papel.papeis.data:
                return redirect(url_for("quest_responsavel"))
            return redirect(url_for("inicio"))
        else:
            flash("Erro ao salvar os papéis no banco.", "error")

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
    if request.method == "POST":
        tipo_cuidador = request.form.get("tipo_cuidador")
        UsuarioController.salvar_tipo_cuidador(tipo_cuidador)
        if tipo_cuidador == "profissional":
            print('selecionou prof')
            return redirect(
                url_for("validar_profissional", tipo_cuidador=tipo_cuidador)
            )
        elif tipo_cuidador == "familiar":
            return redirect(
                url_for("quest_verificar_paciente", tipo_cuidador=tipo_cuidador)
            )
    return render_template("tipo_cuidador.html")

@app.route("/verificar_paciente", methods=["GET", "POST"])
def quest_verificar_paciente():
    formAssociarPaciente = AssociarPaciente()
    if formAssociarPaciente.validate_on_submit():
        email = formAssociarPaciente.email.data
        if UsuarioController.associar_paciente(email):
            flash("Paciente associado com sucesso!", "success")
            return redirect(url_for("inicio"))
        else:
            flash("Erro ao associar paciente. Verifique o email.", "error")
    return render_template("verif_paciente.html", form=formAssociarPaciente)

@app.route("/validar_profissional", methods=["GET", "POST"])
def validar_profissional():
    formValidarProf = ValidarProfissional()
    if formValidarProf.validate_on_submit():
        conselho = formValidarProf.conselhoprofissional.data
        registro = formValidarProf.registroprofissional.data
        UsuarioController.salvar_dados_profissional(conselho, registro)
        return redirect(url_for("login")) 
    
    return render_template("validar_profissional.html", form=formValidarProf)

@app.route("/questionario/quest_responsavel", methods=["GET", "POST"])
def quest_responsavel():
    if request.method == "POST":
        tipo_responsavel = request.form.get("tipo_responsavel")
        if tipo_responsavel == "menor_idade":
            print('selecionou menor de idade')
            return redirect(
                url_for("quest_verificar_paciente", tipo_responsavel=tipo_responsavel)
            )
        elif tipo_responsavel == "curatelado":
            return redirect(
                url_for("quest_verificar_paciente", tipo_responsavel=tipo_responsavel)
            )
    return render_template("quest_responsavel.html")