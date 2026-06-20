from app import app
from flask import render_template, redirect, flash
from app.forms.cadastro_form import CadastroForm
from app.controllers.UsuarioController import UserController


@app.route("/")
def home():
    return render_template("index.html")


#se fosse usar em uma rota diferente
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        if UserController.cadastro(form):
             flash("Cadastro efetuado com sucesso!")
             return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/cadastro')
    return render_template('cadastro.html', title='Login', form=form)