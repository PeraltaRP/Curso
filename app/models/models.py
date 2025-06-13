from app import db
from datetime import datetime, timezone

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    nome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), nullable=True, unique=True)
    assunto = db.Column(db.String(200), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)
    respondido = db.Column(db.Integer, default=0)  # 0 = Não respondido, 1 = Respondido



