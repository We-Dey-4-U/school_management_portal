# backend/app/models/student.py
from app import db

class Student(db.Model):
    __tablename__ = 'Student'  # Updated table name

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('Parent.parent_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    guardian_name = db.Column(db.String(100))
    guardian_contact_number = db.Column(db.String(20))
    admission_date = db.Column(db.Date)
    graduation_date = db.Column(db.Date)

    user = db.relationship('User', foreign_keys=[user_id], backref='student', primaryjoin='Student.user_id == User.user_id')
    parent = db.relationship('Parent', back_populates='students')  # Adjust the backref name here
    tuition_fees = db.relationship('TuitionFee', back_populates='student', lazy='dynamic')
    payments = db.relationship('Payment', back_populates='student', lazy='dynamic')