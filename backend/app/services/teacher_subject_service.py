from app.models.teacher_subject_model import TeacherSubjects
from app import db

def create_teacher_subject(teacher_id, subject_id):
    new_teacher_subject = TeacherSubjects(
        teacher_id=teacher_id,
        subject_id=subject_id
    )
    db.session.add(new_teacher_subject)
    db.session.commit()
    return new_teacher_subject

def get_teacher_subject_by_id(teacher_subject_id):
    return TeacherSubjects.query.get(teacher_subject_id)

def get_all_teacher_subjects():
    return TeacherSubjects.query.all()

def update_teacher_subject(teacher_subject_instance, data):
    teacher_subject_instance.teacher_id = data.get('teacher_id', teacher_subject_instance.teacher_id)
    teacher_subject_instance.subject_id = data.get('subject_id', teacher_subject_instance.subject_id)

    db.session.commit()
    return teacher_subject_instance

def delete_teacher_subject(teacher_subject_instance):
    db.session.delete(teacher_subject_instance)
    db.session.commit()