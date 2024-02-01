from app.models.grades_model import Grades
from app import db

def create_grade(data):
    new_grade = Grades(**data)
    db.session.add(new_grade)
    db.session.commit()
    return new_grade

def get_all_grades():
    return Grades.query.all()

def get_grade_by_id(grade_id):
    return Grades.query.get(grade_id)

def update_grade(grade_id, data):
    grade = Grades.query.get(grade_id)
    if grade:
        for key, value in data.items():
            setattr(grade, key, value)
        db.session.commit()
    return grade

def delete_grade(grade_id):
    grade = Grades.query.get(grade_id)
    if grade:
        db.session.delete(grade)
        db.session.commit()
    return grade