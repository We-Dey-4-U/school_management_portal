# backend/app/models/parent.py
from app import db

class Parent(db.Model):
    __tablename__ = 'Parent'
    parent_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), unique=True, nullable=False)
    parent_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(100), nullable=False)

    # Establish the relationship with the User model
    user = db.relationship('User', back_populates='parent', uselist=False)
    students = db.relationship('Student', back_populates='parent')
    payments = db.relationship('Payment', back_populates='parent', lazy='dynamic')

    def __repr__(self):
        return f'<Parent {self.parent_name}>'