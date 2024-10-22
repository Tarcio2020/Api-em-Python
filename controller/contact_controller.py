from flask import request, jsonify, Blueprint
from service import contact_service

contact_controller = Blueprint('contact_controller', __name__)

# Rota GET para listar todos os contatos
@contact_controller.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = ContactService.get_all_contacts()
    return jsonify([contact.__dict__ for contact in contacts])

# Rota GET para obter um contato por ID
@contact_controller.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = ContactService.get_contact_by_id(contact_id)
    if contact:
        return jsonify(contact.__dict__)
    return jsonify({"error": "Contact not found"}), 404

# Rota POST para criar um novo contato
@contact_controller.route('/contacts', methods=['POST'])
def create_contact():
    data = request.json
    new_contact = ContactService.create_contact(data)
    return jsonify(new_contact.__dict__), 201

# Rota PUT para atualizar um contato
@contact_controller.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.json
    updated_contact = ContactService.update_contact(contact_id, data)
    if updated_contact:
        return jsonify(updated_contact.__dict__)
    return jsonify({"error": "Contact not found"}), 404

# Rota DELETE para deletar um contato
@contact_controller.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    result = ContactService.delete_contact(contact_id)
    if result:
        return jsonify({"message": "Contact deleted"})
    return jsonify({"error": "Contact not found"}), 404
