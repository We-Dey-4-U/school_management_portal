# Import necessary modules
from app import db
from sqlalchemy.orm import relationship

# Define the Exams model
class Exams(db.Model):
    __tablename__ = 'exams'

    # Columns for Exams table
    exam_id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.subject_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.class_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    room_number = db.Column(db.String(10))  # Add this column for room number
    subject_name = db.Column(db.String(50))  # Add this column for subject name
    # Define relationships with consistent back_populates
    subject = db.relationship('Subject', back_populates='exams_associated')
    classes_instance = db.relationship('Classes', back_populates='exams_associated')

    def serialize(self):
        return {
            'exam_id': self.exam_id,
            'subject_id': self.subject_id,
            'class_id': self.class_id,
            'date': str(self.date),  # Convert to string or use a specific format
            'room_number': self.room_number,  # Add room number to the serialization
            'subject_name': self.subject_name,  # Add subject name to the serialization
            # Add other attributes as needed
        }

    def __repr__(self):
        return f"<Exams {self.exam_id} - Room: {self.room_number} - Subject: {self.subject_name}>"