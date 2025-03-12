from app.adapters.database import db

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(9), unique=True, nullable=False)
    logradouro = db.Column(db.String(200))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    localidade = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    ibge = db.Column(db.String(10))
    gia = db.Column(db.String(10))
    ddd = db.Column(db.String(3))
    siafi = db.Column(db.String(10))
    alterado = db.Column(db.String(10), default=None)