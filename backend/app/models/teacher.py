# backend/app/models/teacher.py
from app import db
from app.models.user import User  # Import the User model

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    qualifications = db.Column(db.Text)
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    hire_date = db.Column(db.DATE)

    # Establish the relationship with the User model
    user = db.relationship('User', back_populates='teacher')

    def __repr__(self):
        return f'<Teacher {self.teacher_id}>'