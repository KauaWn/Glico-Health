from app import app
from flask import render_template, redirect, flash
from app.forms.cadastro_form import CadastroForm
from app.controllers.UsuarioController import UserController


@app.route("/")
def home():
    form = CadastroForm() 
    if form.validate_on_submit():
        if UserController.cadastro(form):
             flash("Cadastro efetuado com sucesso!")
             return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/') 
            
    return render_template("index.html", form=form)