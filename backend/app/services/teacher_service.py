# backend/app/services/teacher_service.py
from app.models.teacher import Teacher
from app import db

def create_teacher(user_id, name, qualifications, contact_number, email, address, hire_date):
    new_teacher = Teacher(
        user_id=user_id,
        name=name,
        qualifications=qualifications,
        contact_number=contact_number,
        email=email,
        address=address,
        hire_date=hire_date
    )
    db.session.add(new_teacher)
    db.session.commit()
    return new_teacher

def get_teacher_by_id(teacher_id):
    return Teacher.query.get(teacher_id)

def get_all_teachers():
    return Teacher.query.all()

def update_teacher(teacher, data):
    teacher.user_id = data.get('user_id', teacher.user_id)
    teacher.name = data.get('name', teacher.name)
    teacher.qualifications = data.get('qualifications', teacher.qualifications)
    teacher.contact_number = data.get('contact_number', teacher.contact_number)
    teacher.email = data.get('email', teacher.email)
    teacher.address = data.get('address', teacher.address)
    teacher.hire_date = data.get('hire_date', teacher.hire_date)

    db.session.commit()
    return teacher

def delete_teacher(teacher):
    db.session.delete(teacher)
    db.session.commit()