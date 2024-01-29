# backend/app/services/payment_service.py
from app.models.payment import Payment
from app.models.tuition_fee import TuitionFee
from app import db

def create_payment(parent_id, student_id, amount, payment_date, tuition_fee_id):
    # Create a new payment with the provided tuition_fee_id
    new_payment = Payment(
        parent_id=parent_id,
        student_id=student_id,
        amount=amount,
        payment_date=payment_date,
        tuition_fee_id=tuition_fee_id
    )

    db.session.add(new_payment)
    db.session.commit()

    return new_payment

def get_payment_by_id(payment_id):
    return Payment.query.get(payment_id)

def get_all_payments():
    return Payment.query.all()

def update_payment(payment, data):
    payment.parent_id = data.get('parent_id', payment.parent_id)
    payment.student_id = data.get('student_id', payment.student_id)
    payment.tuition_fee_id = data.get('tuition_fee_id', payment.tuition_fee_id)
    payment.amount = data.get('amount', payment.amount)
    payment.payment_date = data.get('payment_date', payment.payment_date)
    payment.payment_id = data.get('payment_id', payment.payment_id)

    db.session.commit()
    return payment

def delete_payment(payment):
    db.session.delete(payment)
    db.session.commit()