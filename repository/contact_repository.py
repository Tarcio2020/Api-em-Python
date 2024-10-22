from config import db
from entity import contact_entity

# Classe que lida com operações no banco de dados
class ContactRepository:
    
    @staticmethod
    def get_all():
        return Contact.query.all()

    @staticmethod
    def get_by_id(contact_id):
        return Contact.query.get(contact_id)

    @staticmethod
    def create(contact_data):
        contact = Contact(**contact_data)
        db.session.add(contact)
        db.session.commit()
        return contact

    @staticmethod
    def update(contact, updated_data):
        for key, value in updated_data.items():
            setattr(contact, key, value)
        db.session.commit()
        return contact

    @staticmethod
    def delete(contact):
        db.session.delete(contact)
        db.session.commit()
