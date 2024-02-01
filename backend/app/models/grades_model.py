# Import necessary modules
from app import db
from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
#from sqlalchemy.orm import declarative_base, registry, relationship, Session

#mapper_registry = registry()
#Base = declarative_base()

#class Grades(Base):

# Define the Grades model
class Grades(db.Model):
    __tablename__ = 'Grades'
 # Columns for Grades table
    grade_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.student_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.class_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.subject_id'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('Exams.exam_id'), nullable=False)
    grade_value = db.Column(db.String(5), nullable=False)
    student_name = db.Column(db.String(50))  # Add this column for student name
    subject_name = db.Column(db.String(50))  # Add this column for subject name

    # Define relationships
    student = db.relationship('Student', back_populates='grades')
    class_instance = db.relationship('Classes', back_populates='grades')
    subject = db.relationship('Subject', back_populates='grades')
    exam = relationship('Exams', back_populates='grades', primaryjoin="Grades.exam_id == Exams.exam_id") 
    
    def serialize(self):
        return {
            'grade_id': self.grade_id,
            'student_id': self.student_id,
            'class_id': self.class_id,
            'subject_id': self.subject_id,
            'exam_id': self.exam_id,
            'grade_value': self.grade_value,
            'student_name': self.student_name,
            'subject_name': self.subject_name,
            # Add other attributes as needed
        }

    def __repr__(self):
        return f"<Grades {self.grade_id} - Student: {self.student_name} - Subject: {self.subject_name}>"