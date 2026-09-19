from app import app
from flask import render_template, redirect, flash, url_for, request, session, Response
from app.forms.associarpaciente import AssociarPaciente
from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.forms.dados_paciente import DadosPacienteForm
from app.forms.validarprofissional import ValidarProfissional
from app.services.UsuarioController import UsuarioController
from app.services.AuthenticationController import AuthenticationController
from app.forms.papel_form import PapelForm
from datetime import date, time


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/home")
def home():
    usuario = UsuarioController.buscar_usuario_login() #carregar o dado do nome do usuário -- pode ser outros dados
    registros_glicemicos = UsuarioController.buscar_registros_glicemia_login()
    eventos_calendario = UsuarioController.buscar_eventos_calendario_login()
    return render_template(
        "home.html",
        usuario=usuario,
        registros_glicemicos=registros_glicemicos,
        eventos_calendario=eventos_calendario,
    )

#criando o evento no calendario
@app.route("/calendario/evento", methods=["POST"])
def criar_evento_calendario():
    sucesso = UsuarioController.criar_evento_calendario(
        titulo=request.form.get("nome"),
        descricao=request.form.get("descricao"),
        data_evento=request.form.get("data"),
        hora_evento=request.form.get("hora"),
        tipo=request.form.get("tipo"),
    )
    flash(
        "Evento salvo com sucesso!" if sucesso else "Não foi possível salvar o evento.",
        "success" if sucesso else "error",
    )
    return redirect(url_for("home"))


# rota pra editar o evento do usuário
@app.route("/calendario/evento/<int:evento_id>/editar", methods=["POST"])
def editar_evento_calendario(evento_id):
    sucesso = UsuarioController.editar_evento_calendario(
        evento_id=evento_id,
        titulo=request.form.get("nome"),
        descricao=request.form.get("descricao"),
        data_evento=request.form.get("data"),
        hora_evento=request.form.get("hora"),
        tipo=request.form.get("tipo"),
    )
    flash(
        "Evento atualizado com sucesso!" if sucesso else "Não foi possível atualizar o evento.",
        "success" if sucesso else "error",
    )
    return redirect(url_for("home"))

@app.route("/calendario/evento/<int:evento_id>/excluir", methods=["POST"])
def excluir_evento_calendario(evento_id):
    sucesso = UsuarioController.excluir_evento_calendario(evento_id)
    flash(
        "Evento excluído com sucesso!" if sucesso else "Não foi possível excluir o evento.",
        "success" if sucesso else "error",
    )
    return redirect(url_for("home"))

@app.route("/registroglicemia", methods=["GET", "POST"])
def registroglicemia():
    if request.method == "POST":
        sucesso = UsuarioController.registrar_glicemia(
            data_registro=request.form.get("data"),
            hora_registro=request.form.get("hora"),
            medida=request.form.get("glicemia"),
            estado=request.form.get("estado"),
        )
        if sucesso:
            flash("Registro glicêmico salvo com sucesso!", "success")
        else:
            flash("Não foi possível salvar o registro glicêmico.", "error")
        return redirect(url_for("registroglicemia"))

    return render_template(
        "registroglicemia.html",
        data_inicial=request.args.get("data", ""),
    )


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formCadastro = CadastroForm()
    if formCadastro.validate_on_submit():
        if UsuarioController.cadastro(formCadastro):
            return redirect(url_for("questionario"))

        flash("Erro nas credenciais.")
    return render_template("cadastro.html", form=formCadastro)


@app.route("/login", methods=["GET", "POST"])
def login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        if AuthenticationController.login(formLogin):
            return redirect(url_for("home")) #vai para a PÁGINA INICIAL depois do login
        else:
            flash("Usuário ou senha incorretos.", "error")

    return render_template("login.html", title="Login", form=formLogin)

@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "warning")
    return redirect(url_for("login"))

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
            return redirect(url_for("home"))
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


@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    usuario = UsuarioController.buscar_usuario_login()
    if not usuario:
        flash("Sua sessão expirou. Faça login novamente.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        sucesso, mensagem = UsuarioController.atualizar_perfil(
            nome=request.form.get("nome"),
            email=request.form.get("email"),
            peso=request.form.get("peso"),
            foto=request.files.get("foto_perfil"),
        )
        flash(mensagem, "success" if sucesso else "error")
        if sucesso:
            return redirect(url_for("perfil"))

    paciente, genero, tipo_diabete, idade = UsuarioController.buscar_paciente_login()
    return render_template(
        'editperfil.html', 
        usuario=usuario, 
        paciente=paciente, 
        genero=genero,
        tipo_diabete=tipo_diabete,
        idade=idade
    )

@app.route('/foto-perfil')
def foto_perfil():
    usuario = UsuarioController.buscar_usuario_login()

    if not usuario or not usuario.foto_perfil:
        return redirect(url_for('static', filename='img/avatar_borda.png'))

    return Response(usuario.foto_perfil, mimetype=usuario.foto_perfil_tipo or 'image/jpeg')