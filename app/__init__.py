from flask import Flask

app = Flask(__name__)

from app import routes #sem ela, o Flask cria a aplicação mas nunca registra a rota /