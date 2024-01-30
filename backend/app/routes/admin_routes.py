# app/routes/admin_routes.py
from flask import Blueprint, jsonify, request
from app.models.admin import Admin
from app.services.admin_service import create_admin, get_admin_by_id, get_all_admins, update_admin, delete_admin
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admins')

@admin_bp.route('/admins', methods=['POST'])
def create_admin_route():
    data = request.get_json()
    new_admin = create_admin(
        user_id=data['user_id'],
        join_date=data.get('join_date'),
        department=data.get('department'),
        responsibilities=data.get('responsibilities'),
        address=data.get('address'),
        email=data.get('email'),
        mobile_number=data.get('mobile_number'),
        password_hash=data.get('password_hash')
    )
    return jsonify({'message': 'Admin created successfully', 'admin_id': new_admin.admin_id}), 201

@admin_bp.route('/admins/<int:admin_id>', methods=['GET'])
def get_admin_route(admin_id):
    admin = get_admin_by_id(admin_id)
    if admin:
        admin_data = {
            'admin_id': admin.admin_id,
            'user_id': admin.user_id,
            'join_date': admin.join_date,
            'department': admin.department,
            'responsibilities': admin.responsibilities,
            'address': admin.address,
            'email': admin.email,
            'mobile_number': admin.mobile_number
        }
        return jsonify(admin_data), 200
    else:
        return jsonify({'message': 'Admin not found'}), 404

@admin_bp.route('/admins', methods=['GET'])
def get_all_admins_route():
    admins = get_all_admins()
    admins_data = [{
        'admin_id': admin.admin_id,
        'user_id': admin.user_id,
        'join_date': admin.join_date,
        'department': admin.department,
        'responsibilities': admin.responsibilities,
        'address': admin.address,
        'email': admin.email,
        'mobile_number': admin.mobile_number
    } for admin in admins]
    return jsonify(admins_data), 200

@admin_bp.route('/admins/<int:admin_id>', methods=['PUT'])
def update_admin_route(admin_id):
    admin = get_admin_by_id(admin_id)
    if admin:
        data = request.get_json()
        updated_admin = update_admin(admin, data)
        return jsonify({'message': 'Admin updated successfully', 'admin_id': updated_admin.admin_id}), 200
    else:
        return jsonify({'message': 'Admin not found'}), 404

@admin_bp.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin_route(admin_id):
    admin = get_admin_by_id(admin_id)
    if admin:
        delete_admin(admin)
        return jsonify({'message': 'Admin deleted successfully'}), 200
    else:
        return jsonify({'message': 'Admin not found'}), 404