from flask import Blueprint, jsonify, request
from app.services.class_service import create_class, get_class_by_id, get_all_classes, update_class, delete_class
from app import db

class_bp = Blueprint('class', __name__, url_prefix='/api/classes')

@class_bp.route('/classes', methods=['POST'])
def create_class_route():
    data = request.get_json()
    new_class = create_class(
        teacher_id=data.get('teacher_id'),
        subject_id=data.get('subject_id'),
        grade_level=data.get('grade_level'),
        room_number=data.get('room_number'),
        schedule_day=data.get('schedule_day'),
        class_start_time=data.get('class_start_time'),
        class_end_time=data.get('class_end_time'),
        teacher_name=data.get('teacher_name'),  # Add this line
        subject_name=data.get('subject_name')  # Add this line
    )
    return jsonify({'message': 'Class created successfully', 'class_id': new_class.class_id}), 201

@class_bp.route('/classes/<int:class_id>', methods=['GET'])
def get_class_route(class_id):
    class_instance = get_class_by_id(class_id)
    if class_instance:
        class_data = {
            'class_id': class_instance.class_id,
            'teacher_id': class_instance.teacher_id,
            'subject_id': class_instance.subject_id,
            'grade_level': class_instance.grade_level,
            'room_number': class_instance.room_number,
            'schedule_day': class_instance.schedule_day,
            'class_start_time': class_instance.class_start_time.strftime('%H:%M:%S'),
            'class_end_time': class_instance.class_end_time.strftime('%H:%M:%S'),
            'teacher_name': class_instance.teacher_name,
            'subject_name': class_instance.schedule_name,
        }
        return jsonify(class_data), 200
    else:
        return jsonify({'message': 'Class not found'}), 404

@class_bp.route('/classes', methods=['GET'])
def get_all_classes_route():
    classes = get_all_classes()
    classes_data = [{
        'class_id': class_instance.class_id,
        'teacher_id': class_instance.teacher_id,
        'subject_id': class_instance.subject_id,
        'grade_level': class_instance.grade_level,
        'room_number': class_instance.room_number,
        'schedule_day': class_instance.schedule_day,
        'class_start_time': class_instance.class_start_time.strftime('%H:%M:%S'),
        'class_end_time': class_instance.class_end_time.strftime('%H:%M:%S'),
        'teacher_name': class_instance.teacher_name,
        'subject_name': class_instance.schedule_name,
    } for class_instance in classes]
    return jsonify(classes_data), 200

@class_bp.route('/classes/<int:class_id>', methods=['PUT'])
def update_class_route(class_id):
    class_instance = get_class_by_id(class_id)
    if class_instance:
        data = request.get_json()
        updated_class = update_class(class_instance, data)
        return jsonify({'message': 'Class updated successfully', 'class_id': updated_class.class_id}), 200
    else:
        return jsonify({'message': 'Class not found'}), 404

@class_bp.route('/classes/<int:class_id>', methods=['DELETE'])
def delete_class_route(class_id):
    class_instance = get_class_by_id(class_id)
    if class_instance:
        delete_class(class_instance)
        return jsonify({'message': 'Class deleted successfully'}), 200
    else:
        return jsonify({'message': 'Class not found'}), 404