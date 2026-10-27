import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "glicohealth-development-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Captura os dados em tempo real a cada requisição
        db_host = os.getenv("DB_HOST", "localhost")
        db_user = os.getenv("DB_USER", "root")
        db_password = os.getenv("DB_PASSWORD", "labinfo")
        db_name = os.getenv("DB_NAME", "glicohealthbd")
        db_port = os.getenv("DB_PORT", "3306")
        
        return f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
