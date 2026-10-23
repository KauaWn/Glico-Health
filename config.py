import os
from urllib.parse import quote_plus
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "glicohealth-development-key")
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "labinfo"
    DB_NAME = "glicohealthbd"
    #senha_com_arroba = "" 
    # senha_seg = quote_plus(DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = (f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

