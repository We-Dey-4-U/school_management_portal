# Import necessary modules
from flask import Blueprint, request, jsonify
from app.services.exam_service import create_exam, get_exam_by_id, get_all_exams, update_exam, delete_exam

# Create a Blueprint for exams
exam_bp = Blueprint('exams', __name__, url_prefix='/api/exams')

# Define routes
@exam_bp.route('/exams', methods=['POST'])
def create_exam_route():
    data = request.json
    new_exam = create_exam(**data)
    return jsonify(new_exam.serialize()), 201

@exam_bp.route('/exams', methods=['GET'])
def get_all_exams_route():
    exams = get_all_exams()
    return jsonify([exam.serialize() for exam in exams])

@exam_bp.route('/exams/<int:exam_id>', methods=['GET'])
def get_exam_by_id_route(exam_id):
    exam = get_exam_by_id(exam_id)
    if exam:
        return jsonify(exam.serialize())
    return jsonify({'message': 'Exam not found'}), 404

@exam_bp.route('/exams/<int:exam_id>', methods=['PUT'])
def update_exam_route(exam_id):
    exam = get_exam_by_id(exam_id)
    if exam:
        data = request.json
        updated_exam = update_exam(exam, data)
        return jsonify(updated_exam.serialize())
    return jsonify({'message': 'Exam not found'}), 404

@exam_bp.route('/exams/<int:exam_id>', methods=['DELETE'])
def delete_exam_route(exam_id):
    exam = get_exam_by_id(exam_id)
    if exam:
        delete_exam(exam)
        return jsonify({'message': 'Exam deleted successfully'})
    return jsonify({'message': 'Exam not found'}), 404