# backend/app/services/student_service.py

from app import db
from app.models.student import Student

class StudentService:
    @staticmethod
    def create_student(user_id, parent_id, name, date_of_birth, grade_level, contact_number, address, guardian_name, guardian_contact_number, admission_date, graduation_date):
        new_student = Student(
            user_id=user_id,
            parent_id=parent_id,  # Include parent_id when creating a new student
            name=name,
            date_of_birth=date_of_birth,
            grade_level=grade_level,
            contact_number=contact_number,
            address=address,
            guardian_name=guardian_name,
            guardian_contact_number=guardian_contact_number,
            admission_date=admission_date,
            graduation_date=graduation_date
        )
        db.session.add(new_student)
        db.session.commit()
        return new_student

    @staticmethod
    def get_students():
        return Student.query.all()

    @staticmethod
    def update_student(student_id, name, date_of_birth, grade_level, contact_number, address, guardian_name, guardian_contact_number, admission_date, graduation_date):
        student = Student.query.get(student_id)
        if not student:
            return None

        student.name = name
        student.date_of_birth = date_of_birth
        student.grade_level = grade_level
        student.contact_number = contact_number
        student.address = address
        student.guardian_name = guardian_name
        student.guardian_contact_number = guardian_contact_number
        student.admission_date = admission_date
        student.graduation_date = graduation_date

        db.session.commit()
        return student

    @staticmethod
    def delete_student(student_id):
        student = Student.query.get(student_id)
        if student:
            db.session.delete(student)
            db.session.commit()

# Additional methods as needed...