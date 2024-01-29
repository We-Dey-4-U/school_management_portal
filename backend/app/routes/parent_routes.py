# backend/app/routes/parent_routes.py
from flask import Blueprint, jsonify, request
from app.models.user import User  # Correct import to use User model
from app.models.parent import Parent
from app import db

parent_bp = Blueprint('parents', __name__, url_prefix='/api/parents')

@parent_bp.route('/parents', methods=['POST'])
def create_parent():
    data = request.get_json()
    new_parent = Parent(
        user_id=data['user_id'],
        parent_name=data['parent_name'],
        contact_number=data.get('contact_number'),
        email=data['email']
    )
    db.session.add(new_parent)
    db.session.commit()
    return jsonify({'message': 'Parent created successfully'}), 201

@parent_bp.route('/parents/<int:parent_id>', methods=['GET'])
def get_parent(parent_id):
    parent = Parent.query.get(parent_id)
    if parent:
        parent_data = {
            'parent_id': parent.parent_id,
            'user_id': parent.user_id,
            'parent_name': parent.parent_name,
            'contact_number': parent.contact_number,
            'email': parent.email
        }
        return jsonify(parent_data), 200
    else:
        return jsonify({'message': 'Parent not found'}), 404

@parent_bp.route('/parents', methods=['GET'])
def get_parents():
    parents = Parent.query.all()
    parents_data = [{
        'parent_id': parent.parent_id,
        'user_id': parent.user_id,
        'parent_name': parent.parent_name,
        'contact_number': parent.contact_number,
        'email': parent.email
    } for parent in parents]
    return jsonify(parents_data), 200

@parent_bp.route('/parents/<int:parent_id>', methods=['PUT'])
def update_parent(parent_id):
    parent = Parent.query.get_or_404(parent_id)
    data = request.get_json()

    parent.user_id = data.get('user_id', parent.user_id)
    parent.parent_name = data.get('parent_name', parent.parent_name)
    parent.contact_number = data.get('contact_number', parent.contact_number)
    parent.email = data.get('email', parent.email)

    db.session.commit()
    return jsonify({'message': 'Parent updated successfully'}), 200

@parent_bp.route('/parents/<int:parent_id>', methods=['DELETE'])
def delete_parent(parent_id):
    parent = Parent.query.get_or_404(parent_id)
    db.session.delete(parent)
    db.session.commit()
    return jsonify({'message': 'Parent deleted successfully'}), 200