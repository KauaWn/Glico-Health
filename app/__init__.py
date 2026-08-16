from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app) #protege os forms contra ataques CSRF
db = SQLAlchemy(app)

from app import routes, models #sem ela, o Flask cria a aplicação mas nunca registra a rota /
from app.models.usuario import Usuario

with app.app_context():
   db.create_all()