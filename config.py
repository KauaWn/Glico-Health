import secrets
# from urllib.parse import quote_plus

class Config:
    SECRET_KEY = secrets.token_hex(16) 
    #senha_com_arroba = "" quando a senha tem @, tem q guardar em variavel 
    # senha_seg = quote_plus(senha_com_arroba)
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://usuario:senha@localhost:3306/glicohealth'

