# backend/app/models/tuition_fee.py
from app import db
from app.models.student import Student  # Import the Student model
#from app.models.payment import Payment  # Import the Payment model

class TuitionFee(db.Model):
    __tablename__ = 'TuitionFee'
    fee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.student_id'), nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    due_date = db.Column(db.DATE, nullable=False)
    is_paid = db.Column(db.Boolean, nullable=False, default=False)
    payment_id = db.Column(db.VARCHAR(50), unique=True)

    # Establish the relationship with the Student model
    student = db.relationship('Student', back_populates='tuition_fees')
    # Establish the relationship with the Payment model
    payments = db.relationship('Payment', back_populates='tuition_fee', uselist=False)


    def __repr__(self):
        return f'<TuitionFee {self.fee_id}>'