from app import app
from flask import render_template #redirect, flash
# from app.forms.login_form import LoginForm
# from app.controllers.AuthenticationControllers import AuthenticationController


@app.route("/")
def home():
    return render_template("index.html")