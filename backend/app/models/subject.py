from app import db
from sqlalchemy.orm import relationship

class Subject(db.Model):
    __tablename__ = 'Subject'
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.String(50), nullable=False)

    #__table_args__ = (Index('idx_subject_id', 'subject_id'),)

    # Relationship with Classes
    classes_associated = relationship('Classes', back_populates='subject')
    teacher_subjects = relationship('TeacherSubjects', back_populates='subject')
    exams_associated = relationship('Exams', back_populates='subject')

    def __repr__(self):
        return f"Subject(subject_id={self.subject_id}, subject_name={self.subject_name})"