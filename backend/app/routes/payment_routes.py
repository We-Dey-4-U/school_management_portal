# backend/app/routes/payment_routes.py
from flask import Blueprint, jsonify, request
from app.services.payment_service import create_payment, get_payment_by_id, get_all_payments, update_payment, delete_payment
from app import db

payment_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

@payment_bp.route('/payments', methods=['POST'])
def create_payment_route():
    data = request.get_json()
    tuition_fee_id = data.get('tuition_fee_id')  # Extract tuition_fee_id from the request payload
    new_payment = create_payment(
        parent_id=data['parent_id'],
        student_id=data['student_id'],
        amount=data['amount'],
        payment_date=data['payment_date'],
        tuition_fee_id=tuition_fee_id
    )
    if new_payment:
        return jsonify({'message': 'Payment created successfully'}), 201
    else:
        return jsonify({'message': 'Failed to create payment. TuitionFee not found for the given parent_id and student_id.'}), 400

@payment_bp.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_route(payment_id):
    payment = get_payment_by_id(payment_id)
    if payment:
        payment_data = {
            'payment_id': payment.payment_id,
            'parent_id': payment.parent_id,
            'student_id': payment.student_id,
            'amount': payment.amount,
            'payment_date': payment.payment_date
        }
        return jsonify(payment_data), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404

@payment_bp.route('/payments', methods=['GET'])
def get_payments_route():
    payments = get_all_payments()
    payments_data = [{
        'payment_id': payment.payment_id,
        'parent_id': payment.parent_id,
        'student_id': payment.student_id,
        'amount': payment.amount,
        'payment_date': payment.payment_date
    } for payment in payments]
    return jsonify(payments_data), 200

@payment_bp.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment_route(payment_id):
    payment = get_payment_by_id(payment_id)
    if payment:
        data = request.get_json()
        updated_payment = update_payment(payment, data)
        return jsonify({'message': 'Payment updated successfully'}), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404

@payment_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment_route(payment_id):
    payment = get_payment_by_id(payment_id)
    if payment:
        delete_payment(payment)
        return jsonify({'message': 'Payment deleted successfully'}), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404