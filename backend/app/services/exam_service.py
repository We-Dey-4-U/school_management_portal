# Import necessary modules
from app.models.exam_model import Exams
from app import db

# Define services
def create_exam(subject_id, class_id, date, room_number, subject_name):
    new_exam = Exams(
        subject_id=subject_id,
        class_id=class_id,
        date=date,
        room_number=room_number,
        subject_name=subject_name
    )
    db.session.add(new_exam)
    db.session.commit()
    return new_exam

def get_exam_by_id(exam_id):
    return Exams.query.get(exam_id)

def get_all_exams():
    return Exams.query.all()

def update_exam(exam_instance, data):
    exam_instance.subject_id = data.get('subject_id', exam_instance.subject_id)
    exam_instance.class_id = data.get('class_id', exam_instance.class_id)
    exam_instance.date = data.get('date', exam_instance.date)

    db.session.commit()
    return exam_instance

def delete_exam(exam_instance):
    db.session.delete(exam_instance)
    db.session.commit()