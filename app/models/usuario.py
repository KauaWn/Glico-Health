from app import db
# from flask_login import UserMixinS

class Usuario(db.Model, #UserMixin
              ):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=False, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    papel = db.Column(db.String(100), nullable=False)
    rm = db.Column(db.Boolean, default=False)