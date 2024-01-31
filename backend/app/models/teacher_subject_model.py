from app import db

class TeacherSubjects(db.Model):
    __tablename__ = 'teacher_subjects'

    teacher_subject_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teacher.teacher_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.subject_id'), nullable=False)

    # Define relationships
    teacher = db.relationship('Teacher', back_populates='teacher_subjects')
    subject = db.relationship('Subject', back_populates='teacher_subjects')