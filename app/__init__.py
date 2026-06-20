from flask import Flask
from flask_wtf import CSRFProtect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app) #protege os forms contra ataques CSRF


from app import routes #sem ela, o Flask cria a aplicação mas nunca registra a rota /