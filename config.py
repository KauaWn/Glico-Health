import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "glicohealth-development-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Substitua com os dados reais do seu banco na nuvem (Aiven)
        db_host = os.getenv("DB_HOST", "COLE_AQUI_O_HOST_LONGO_DO_AIVEN")
        db_user = os.getenv("DB_USER", "avnadmin")
        db_password = os.getenv("DB_PASSWORD", "COLE_AQUI_A_SENHA_DO_AIVEN")
        db_name = os.getenv("DB_NAME", "defaultdb")
        db_port = os.getenv("DB_PORT", "COLE_AQUI_A_PORTA_DO_AIVEN")
        
        return f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
