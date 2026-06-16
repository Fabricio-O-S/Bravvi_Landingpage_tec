from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    """
    Modelo de representação dos leads capturados na Landing Page.
    Seguindo o padrão de nomenclatura snake_case para propriedades e tabelas.
    """
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    whatsapp = db.Column(db.String(20), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Método auxiliar para converter o modelo para um dicionário JSON."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'whatsapp': self.whatsapp,
            'industry': self.industry,
            'message': self.message,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __repr__(self):
        return f'<Lead {self.email}>'
