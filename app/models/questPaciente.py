from app import db
from datetime import datetime

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    papeis = db.Column(db.String(200), nullable=False)
    data_resposta = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    dia = db.Column(db.Integer, nullable=True)
    mes = db.Column(db.Integer, nullable=True)
    ano = db.Column(db.Integer, nullable=True)
    sexo = db.Column(db.String(50), nullable=True)
    tipo_diabetes = db.Column(db.String(50), nullable=True)
