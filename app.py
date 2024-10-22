# app.py

from config import app, db
from repository.contact_repository import ContactRepository
from entity.contact_entity import Contact
from controller.contact_controller import contact_controller

# Inicializando o banco de dados
with app.app_context():
    db.create_all()  # Isso cria as tabelas no banco de dados

# Registrando o blueprint
app.register_blueprint(contact_controller)

if __name__ == '__main__':
    app.run(debug=True)
