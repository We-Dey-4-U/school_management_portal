from app import db
from sqlalchemy.orm import relationship

class Classes(db.Model):
    __tablename__ = 'Classes'

    class_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teacher.teacher_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.subject_id'), nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(10))
    schedule_day = db.Column(db.String(15))
    class_start_time = db.Column(db.Time, nullable=False)
    class_end_time = db.Column(db.Time, nullable=False)
    teacher_name = db.Column(db.String(50), nullable=False)
    subject_name = db.Column(db.String(50), nullable=False)

    teacher = db.relationship('Teacher', back_populates='classes_taught')
    subject = db.relationship('Subject', back_populates='classes_associated')
    exams_associated = relationship('Exams', back_populates='classes_instance')
    grades = db.relationship('Grades', back_populates='class_instance')
    def __repr__(self):
        return f"<Classes {self.class_id}>"