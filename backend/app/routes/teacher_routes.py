# backend/app/routes/teacher_routes.py
from flask import Blueprint, jsonify, request
from app.models.teacher import Teacher
from app import db

teacher_bp = Blueprint('teachers', __name__, url_prefix='/api/teachers')

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    new_teacher = Teacher(
        user_id=data['user_id'],
        name=data['name'],
        qualifications=data['qualifications'],
        contact_number=data['contact_number'],
        email=data['email'],
        address=data['address'],
        hire_date=data['hire_date']
    )
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher created successfully'}), 201

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        teacher_data = {
            'teacher_id': teacher.teacher_id,
            'user_id': teacher.user_id,
            'name': teacher.name,
            'qualifications': teacher.qualifications,
            'contact_number': teacher.contact_number,
            'email': teacher.email,
            'address': teacher.address,
            'hire_date': teacher.hire_date
        }
        return jsonify(teacher_data), 200
    else:
        return jsonify({'message': 'Teacher not found'}), 404

@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teachers_data = [{
        'teacher_id': teacher.teacher_id,
        'user_id': teacher.user_id,
        'name': teacher.name,
        'qualifications': teacher.qualifications,
        'contact_number': teacher.contact_number,
        'email': teacher.email,
        'address': teacher.address,
        'hire_date': teacher.hire_date
    } for teacher in teachers]
    return jsonify(teachers_data), 200

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    data = request.get_json()

    teacher.user_id = data.get('user_id', teacher.user_id)
    teacher.name = data.get('name', teacher.name)
    teacher.qualifications = data.get('qualifications', teacher.qualifications)
    teacher.contact_number = data.get('contact_number', teacher.contact_number)
    teacher.email = data.get('email', teacher.email)
    teacher.address = data.get('address', teacher.address)
    teacher.hire_date = data.get('hire_date', teacher.hire_date)

    db.session.commit()
    return jsonify({'message': 'Teacher updated successfully'}), 200

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher deleted successfully'}), 200