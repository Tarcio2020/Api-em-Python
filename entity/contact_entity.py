from config import db

# Definição da entidade Contact
class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'
