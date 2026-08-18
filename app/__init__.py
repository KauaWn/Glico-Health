from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app) #protege os forms contra ataques CSRF
db = SQLAlchemy(app)

# login_manager = LoginManager(app) #biblioteca para gerenciar sessões de login, sendo essencial para memória de sessão e autenticação de usuários para funcionalidades como remember me, logout, etc.
# login_manager.init_app(app)
# login_manager.login_view = "login"  # Define a rota de login padrão
# @login_manager.user_loader
# def load_user(user_id):
#     # procurar o usuário no MySQL pelo ID
#     usuario = buscar_usuario_por_id(user_id)

#     return usuario

from app import routes, models #sem ela, o Flask cria a aplicação mas nunca registra a rota /
from app.models.usuario import Usuario
from app.models.questionario import Questionario

with app.app_context():
   db.create_all()