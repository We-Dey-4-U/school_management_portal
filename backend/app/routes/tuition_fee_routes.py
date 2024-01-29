# backend/app/routes/tuition_fee_routes.py
from flask import Blueprint, jsonify, request
from app.models.tuition_fee import TuitionFee
from app import db

tuition_fee_bp = Blueprint('tuition_fee', __name__, url_prefix='/api/tuition-fees')

@tuition_fee_bp.route('/tuition-fees', methods=['POST'])
def create_tuition_fee():
    data = request.get_json()
    new_tuition_fee = TuitionFee(
        student_id=data['student_id'],
        amount=data['amount'],
        due_date=data['due_date'],
        is_paid=data.get('is_paid', False),
        payment_id=data.get('payment_id')
    )
    db.session.add(new_tuition_fee)
    db.session.commit()
    return jsonify({'message': 'Tuition Fee created successfully'}), 201

@tuition_fee_bp.route('/tuition-fees/<int:fee_id>', methods=['GET'])
def get_tuition_fee(fee_id):
    tuition_fee = TuitionFee.query.get(fee_id)
    if tuition_fee:
        tuition_fee_data = {
            'fee_id': tuition_fee.fee_id,
            'student_id': tuition_fee.student_id,
            'amount': tuition_fee.amount,
            'due_date': tuition_fee.due_date,
            'is_paid': tuition_fee.is_paid,
            'payment_id': tuition_fee.payment_id
        }
        return jsonify(tuition_fee_data), 200
    else:
        return jsonify({'message': 'Tuition Fee not found'}), 404

@tuition_fee_bp.route('/tuition-fees', methods=['GET'])
def get_tuition_fees():
    tuition_fees = TuitionFee.query.all()
    tuition_fees_data = [{
        'fee_id': fee.fee_id,
        'student_id': fee.student_id,
        'amount': fee.amount,
        'due_date': fee.due_date,
        'is_paid': fee.is_paid,
        'payment_id': fee.payment_id
    } for fee in tuition_fees]
    return jsonify(tuition_fees_data), 200

@tuition_fee_bp.route('/tuition-fees/<int:fee_id>', methods=['PUT'])
def update_tuition_fee(fee_id):
    tuition_fee = TuitionFee.query.get_or_404(fee_id)
    data = request.get_json()
    
    tuition_fee.student_id = data.get('student_id', tuition_fee.student_id)
    tuition_fee.amount = data.get('amount', tuition_fee.amount)
    tuition_fee.due_date = data.get('due_date', tuition_fee.due_date)
    tuition_fee.is_paid = data.get('is_paid', tuition_fee.is_paid)
    tuition_fee.payment_id = data.get('payment_id', tuition_fee.payment_id)

    db.session.commit()
    return jsonify({'message': 'Tuition Fee updated successfully'}), 200

@tuition_fee_bp.route('/tuition-fees/<int:fee_id>', methods=['DELETE'])
def delete_tuition_fee(fee_id):
    tuition_fee = TuitionFee.query.get_or_404(fee_id)
    db.session.delete(tuition_fee)
    db.session.commit()
    return jsonify({'message': 'Tuition Fee deleted successfully'}), 200