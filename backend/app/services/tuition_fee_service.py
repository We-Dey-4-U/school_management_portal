# backend/app/services/tuition_fee_service.py
#from app.models.payment import Payment
from app.models.tuition_fee import TuitionFee
from app import db

def create_tuition_fee(student_id, amount, due_date, is_paid=False, payment_id=None):
    new_tuition_fee = TuitionFee(
        student_id=student_id,
        amount=amount,
        due_date=due_date,
        is_paid=is_paid,
        payment_id=payment_id
    )
    db.session.add(new_tuition_fee)
    db.session.commit()
    return new_tuition_fee

def get_tuition_fee_by_id(fee_id):
    return TuitionFee.query.get(fee_id)

def get_all_tuition_fees():
    return TuitionFee.query.all()

def update_tuition_fee(tuition_fee, data):
    tuition_fee.student_id = data.get('student_id', tuition_fee.student_id)
    tuition_fee.amount = data.get('amount', tuition_fee.amount)
    tuition_fee.due_date = data.get('due_date', tuition_fee.due_date)
    tuition_fee.is_paid = data.get('is_paid', tuition_fee.is_paid)
    tuition_fee.payment_id = data.get('payment_id', tuition_fee.payment_id)

    db.session.commit()
    return tuition_fee

def delete_tuition_fee(tuition_fee):
    db.session.delete(tuition_fee)
    db.session.commit()