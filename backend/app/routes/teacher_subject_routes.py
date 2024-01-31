from flask import Blueprint, jsonify, request
from app.services.teacher_subject_service import create_teacher_subject, get_teacher_subject_by_id, get_all_teacher_subjects, update_teacher_subject, delete_teacher_subject
from app import db

teacher_subject_bp = Blueprint('teacher_subject', __name__, url_prefix='/api/teacher_subjects')

@teacher_subject_bp.route('/teacher_subjects', methods=['POST'])
def create_teacher_subject_route():
    data = request.get_json()
    new_teacher_subject = create_teacher_subject(
        teacher_id=data.get('teacher_id'),
        subject_id=data.get('subject_id')
    )
    return jsonify({'message': 'Teacher-Subject association created successfully', 'teacher_subject_id': new_teacher_subject.teacher_subject_id}), 201

@teacher_subject_bp.route('/teacher_subjects/<int:teacher_subject_id>', methods=['GET'])
def get_teacher_subject_route(teacher_subject_id):
    teacher_subject = get_teacher_subject_by_id(teacher_subject_id)
    if teacher_subject:
        teacher_subject_data = {
            'teacher_subject_id': teacher_subject.teacher_subject_id,
            'teacher_id': teacher_subject.teacher_id,
            'subject_id': teacher_subject.subject_id
        }
        return jsonify(teacher_subject_data), 200
    else:
        return jsonify({'message': 'Teacher-Subject association not found'}), 404

@teacher_subject_bp.route('/teacher_subjects', methods=['GET'])
def get_all_teacher_subjects_route():
    teacher_subjects = get_all_teacher_subjects()
    teacher_subjects_data = [{
        'teacher_subject_id': ts.teacher_subject_id,
        'teacher_id': ts.teacher_id,
        'subject_id': ts.subject_id
    } for ts in teacher_subjects]
    return jsonify(teacher_subjects_data), 200

@teacher_subject_bp.route('/teacher_subjects/<int:teacher_subject_id>', methods=['PUT'])
def update_teacher_subject_route(teacher_subject_id):
    teacher_subject = get_teacher_subject_by_id(teacher_subject_id)
    if teacher_subject:
        data = request.get_json()
        updated_teacher_subject = update_teacher_subject(teacher_subject, data)
        return jsonify({'message': 'Teacher-Subject association updated successfully', 'teacher_subject_id': updated_teacher_subject.teacher_subject_id}), 200
    else:
        return jsonify({'message': 'Teacher-Subject association not found'}), 404

@teacher_subject_bp.route('/teacher_subjects/<int:teacher_subject_id>', methods=['DELETE'])
def delete_teacher_subject_route(teacher_subject_id):
    teacher_subject = get_teacher_subject_by_id(teacher_subject_id)
    if teacher_subject:
        delete_teacher_subject(teacher_subject)
        return jsonify({'message': 'Teacher-Subject association deleted successfully'}), 200
    else:
        return jsonify({'message': 'Teacher-Subject association not found'}), 404