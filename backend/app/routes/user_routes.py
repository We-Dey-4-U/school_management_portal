# backend/app/routes/user_routes.py
from flask import Blueprint, jsonify, request
from app.models.user import User
from app import db

user_bp = Blueprint('users', __name__, url_prefix='/api/users')

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [{
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'role': user.role
        # Add other fields as needed
    } for user in users]
    return jsonify(users_data), 200

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    user.username = data.get('username', user.username)
    user.password = data.get('password', user.password)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200