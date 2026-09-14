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
    conexao = pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )

    cursor = conexao.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS glicohealthbd")

    cursor.close()
    conexao.close()

criar_banco()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app import modelos

# with app.app_context():
#     Base.metadata.create_all(db.engine)