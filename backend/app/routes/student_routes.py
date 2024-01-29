# backend/app/routes/student_routes.py

from flask import Blueprint, jsonify, request
from app.services.student_service import StudentService

student_bp = Blueprint('student_bp', __name__, url_prefix='/api/students')

@student_bp.route('/create', methods=['POST'])
def create_student():
    data = request.get_json()
    student = StudentService.create_student(
        user_id=data['user_id'],
        parent_id=data['parent_id'],
        name=data['name'],
        date_of_birth=data['date_of_birth'],
        grade_level=data['grade_level'],
        contact_number=data['contact_number'],
        address=data['address'],
        guardian_name=data['guardian_name'],
        guardian_contact_number=data['guardian_contact_number'],
        admission_date=data['admission_date'],
        graduation_date=data['graduation_date']
    )
    return jsonify({'student_id': student.student_id}), 201

@student_bp.route('/get', methods=['GET'])
def get_students():
    students = StudentService.get_students()
    students_data = [{
        'student_id': student.student_id,
        'name': student.name,
        'date_of_birth': student.date_of_birth,
        'grade_level': student.grade_level,
        'contact_number': student.contact_number,
        'address': student.address,
        'guardian_name': student.guardian_name,
        'guardian_contact_number': student.guardian_contact_number,
        'admission_date': student.admission_date,
        'graduation_date': student.graduation_date,
        'user_id': student.user_id,
        'parent_id': student.parent_id
    } for student in students]
    return jsonify(students_data), 200

@student_bp.route('/update/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    updated_student = StudentService.update_student(
        student_id,
        name=data['name'],
        date_of_birth=data['date_of_birth'],
        grade_level=data['grade_level'],
        contact_number=data['contact_number'],
        address=data['address'],
        guardian_name=data['guardian_name'],
        guardian_contact_number=data['guardian_contact_number'],
        admission_date=data['admission_date'],
        graduation_date=data['graduation_date']
    )
    return jsonify({'student_id': updated_student.student_id}), 200

@student_bp.route('/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    StudentService.delete_student(student_id)
    return jsonify({'message': 'Student deleted successfully'}), 200