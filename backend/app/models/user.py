# backend/app/models/user.py
from app import db

class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum('admin', 'teacher', 'student', 'parent'), nullable=False)

    # Establish the relationship with the Parent model
    parent = db.relationship('Parent', back_populates='user')
    teacher = db.relationship('Teacher', back_populates='user', uselist=False)  # Add this line
    admin = db.relationship('Admin', back_populates='user', uselist=False)
    #student = db.relationship('Student', back_populates='user', uselist=False)  # Add this line

    #communication_sent = db.relationship('Communication', back_populates='sender', foreign_keys='Communication.sender_id', lazy='dynamic')
    #communication_received = db.relationship('Communication', back_populates='recipient', foreign_keys='Communication.recipient_id', lazy='dynamic')

    #payments = db.relationship('Payment', back_populates='user', lazy='dynamic')


    # Add index to user_id
    __table_args__ = (db.Index('idx_user_id', 'user_id'),)