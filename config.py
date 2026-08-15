import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://NOMEDOUSUARIOBD:BOTEASENHA@localhost:3306/glicohealth'

