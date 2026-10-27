from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)


def criar_banco():
    import os
    # Copie exatamente os mesmos dados da nuvem para cá como segurança
    host = os.getenv("DB_HOST", "COLE_AQUI_O_HOST_LONGO_DO_AIVEN")
    user = os.getenv("DB_USER", "avnadmin")
    password = os.getenv("DB_PASSWORD", "COLE_AQUI_A_SENHA_DO_AIVEN")
    port = int(os.getenv("DB_PORT", "COLE_AQUI_A_PORTA_DO_AIVEN_EX_24681"))
    db_name = os.getenv("DB_NAME", "defaultdb")

    try:
        # Se for o link do Aiven, não precisamos criar o banco porque ele já existe (defaultdb)
        if "localhost" in host:
            conexao = pymysql.connect(
                host=host,
                user=user,
                password=password,
                port=port
            )
            cursor = conexao.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.close()
            conexao.close()
        else:
            print("Rodando na nuvem. Ignorando criação automática de banco.")
    except Exception as e:
        print(f"Aviso na inicialização do banco: {e}")

criar_banco()



db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app import modelos

# with app.app_context():
#     Base.metadata.create_all(db.engine)