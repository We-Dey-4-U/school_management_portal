# backend/app/models/payment.py
from app import db
from app.models.parent import Parent  # Import the Parent model
from app.models.student import Student  # Import the Student model
#from app.models.tuition_fee import TuitionFee  # Import the TuitionFee model

class Payment(db.Model):
    __tablename__ = 'Payment'
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Parent.parent_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.student_id'), nullable=False)
    tuition_fee_id = db.Column(db.Integer, db.ForeignKey('TuitionFee.fee_id'), nullable=False)  # Add this line
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    payment_date = db.Column(db.DATE, nullable=False)

    # Establish the relationship with the Parent model
    parent = db.relationship('Parent', back_populates='payments')

    # Establish the relationship with the Student model
    student = db.relationship('Student', back_populates='payments')

    # Establish the relationship with the TuitionFee model
    tuition_fee = db.relationship('TuitionFee', back_populates='payments')

    def __repr__(self):
        return f'<Payment {self.payment_id}>'