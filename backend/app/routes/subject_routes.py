from flask import Blueprint, jsonify, request
from app.services.subject_service import create_subject, get_subject_by_id, get_all_subjects, update_subject, delete_subject
from app import db

subject_bp = Blueprint('subject', __name__, url_prefix='/api/subjects')

@subject_bp.route('/subjects', methods=['POST'])
def create_subject_route():
    data = request.get_json()
    new_subject = create_subject(**data)
    return jsonify({'message': 'Subject created successfully', 'subject_id': new_subject.subject_id}), 201

@subject_bp.route('/subjects/<int:subject_id>', methods=['GET'])
def get_subject_route(subject_id):
    subject = get_subject_by_id(subject_id)
    if subject:
        subject_data = {
            'subject_id': subject.subject_id,
            'subject_name': subject.subject_name
        }
        return jsonify(subject_data), 200
    else:
        return jsonify({'message': 'Subject not found'}), 404

@subject_bp.route('/subjects', methods=['GET'])
def get_all_subjects_route():
    subjects = get_all_subjects()
    subjects_data = [{
        'subject_id': subject.subject_id,
        'subject_name': subject.subject_name
    } for subject in subjects]
    return jsonify(subjects_data), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['PUT'])
def update_subject_route(subject_id):
    subject = get_subject_by_id(subject_id)
    if subject:
        data = request.get_json()
        updated_subject = update_subject(subject, data)
        return jsonify({'message': 'Subject updated successfully', 'subject_id': updated_subject.subject_id}), 200
    else:
        return jsonify({'message': 'Subject not found'}), 404

@subject_bp.route('/subjects/<int:subject_id>', methods=['DELETE'])
def delete_subject_route(subject_id):
    subject = get_subject_by_id(subject_id)
    if subject:
        delete_subject(subject)
        return jsonify({'message': 'Subject deleted successfully'}), 200
    else:
        return jsonify({'message': 'Subject not found'}), 404