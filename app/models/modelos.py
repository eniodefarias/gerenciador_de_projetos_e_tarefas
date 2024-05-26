from app import db


#         /models
#             __init__.py
#             user.py  # Este é o seu modelos.py para o usuário


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    # Outros campos...

class Projeto(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    # Outros campos...

class Atividade(db.Model):
    __tablename__ = 'atividades'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'))
    # Outros campos...
