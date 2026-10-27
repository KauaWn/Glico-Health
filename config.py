import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "glicohealth-development-key")
    
    # Busca os dados da nuvem (Vercel). Se não existirem, usa os dados do seu PC local
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo")
    DB_NAME = os.getenv("DB_NAME", "glicohealthbd")
    DB_PORT = os.getenv("DB_PORT", "3306")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
