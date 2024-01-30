from app.models.subject import Subject
from app import db

def create_subject(subject_name):
    new_subject = Subject(subject_name=subject_name)
    db.session.add(new_subject)
    db.session.commit()
    return new_subject

def get_subject_by_id(subject_id):
    return Subject.query.get(subject_id)

def get_all_subjects():
    return Subject.query.all()

def update_subject(subject, data):
    subject.subject_name = data.get('subject_name', subject.subject_name)
    db.session.commit()
    return subject

def delete_subject(subject):
    db.session.delete(subject)
    db.session.commit()