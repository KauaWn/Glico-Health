import secrets
#from urllib.parse import quote_plus
class Config:
    SECRET_KEY = secrets.token_hex(16) 
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "labinfo"
    DB_NAME = "glicohealthbd"
    #senha_com_arroba = "" 
    #senha_seg = quote_plus(senha_com_arroba)
    SQLALCHEMY_DATABASE_URI = (f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

