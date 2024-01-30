from app import db

class Subject(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Subject(subject_id={self.subject_id}, subject_name={self.subject_name})"