# backend/app/routes/communication_routes.py

from flask import Blueprint, jsonify, request
from app import db
from app.models.communication import Communication
from app.models.user import User
from datetime import datetime

communication_bp = Blueprint('communication_bp', __name__, url_prefix='/api/communication')

@communication_bp.route('/communication', methods=['POST'])
def create_message():
    data = request.get_json()

    # Check if sender and recipient exist
    sender = User.query.get(data.get('sender_id'))
    recipient = User.query.get(data.get('recipient_id'))
    
    if sender is None or recipient is None:
        return jsonify({'error': 'Sender or recipient does not exist'}), 400

    # Parse timestamp if needed
    try:
        timestamp = datetime.strptime(data.get('timestamp'), '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid timestamp format'}), 400

    new_message = Communication(
        sender_id=data.get('sender_id'),
        recipient_id=data.get('recipient_id'),
        message=data.get('content'),  # Changed from 'content' to 'message'
        sent_at=timestamp,
        is_read=data.get('is_read', False),
        attachment_url=data.get('attachment_url')
    )

    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({'message': 'Message created successfully'}), 201

@communication_bp.route('/communication', methods=['GET'])
def get_messages():
    messages = Communication.query.all()
    messages_data = [{
        'communication_id': message.communication_id,  # Updated from 'message_id' to 'communication_id'
        'sender_id': message.sender_id,
        'recipient_id': message.recipient_id,
        'sent_at': message.sent_at,  # Updated from 'timestamp' to 'sent_at'
        'message': message.message,  # Updated from 'message' to 'message'
        'is_read': message.is_read,
        'attachment_url': message.attachment_url,
        'sender_username': message.sender.username if message.sender else None,
        'recipient_username': message.recipient.username if message.recipient else None,
    } for message in messages]
    return jsonify(messages_data), 200