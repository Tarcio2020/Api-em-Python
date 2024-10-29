from repository import contact_repository

class ContactService:

    @staticmethod
    def get_all_contacts():
        return ContactRepository.get_all()

    @staticmethod
    def get_contact_by_id(contact_id):
        return ContactRepository.get_by_id(contact_id)

    @staticmethod
    def create_contact(contact_data):
        return ContactRepository.create(contact_data)

    @staticmethod
    def update_contact(contact_id, updated_data):
        contact = ContactRepository.get_by_id(contact_id)
        if contact:
            return ContactRepository.update(contact, updated_data)
        return None

    @staticmethod
    def delete_contact(contact_id):
        contact = ContactRepository.get_by_id(contact_id)
        if contact:
            return ContactRepository.delete(contact)
        return None
