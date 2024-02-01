from flask import Blueprint, request, jsonify
from app.services.grades_service import create_grade, get_all_grades, get_grade_by_id, update_grade, delete_grade

grade_bp = Blueprint('grades', __name__, url_prefix='/grades')

@grade_bp.route('/grades', methods=['POST'])
def create_new_grade():
    data = request.json
    new_grade = create_grade(data)
    return jsonify(new_grade.serialize()), 201

@grade_bp.route('/grades', methods=['GET'])
def get_all_grades_list():
    grades = get_all_grades()
    return jsonify([grade.serialize() for grade in grades])

@grade_bp.route('/grades/<int:grade_id>', methods=['GET'])
def get_grade_details(grade_id):
    grade = get_grade_by_id(grade_id)
    if grade:
        return jsonify(grade.serialize())
    else:
        return jsonify({'message': 'Grade not found'}), 404

@grade_bp.route('/grades/<int:grade_id>', methods=['PUT'])
def update_grade_details(grade_id):
    data = request.json
    updated_grade = update_grade(grade_id, data)
    return jsonify(updated_grade.serialize())

@grade_bp.route('/grades/<int:grade_id>', methods=['DELETE'])
def delete_grade_entry(grade_id):
    deleted_grade = delete_grade(grade_id)
    return jsonify(deleted_grade.serialize())