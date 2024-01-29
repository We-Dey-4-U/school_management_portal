# backend/app/services/communication_service.py

from app.models.communication import Communication  # Change 'communications' to 'Communication'
from app import db

def create_message(sender_id, recipient_id, timestamp, content, is_read=False, attachment_url=None):
    new_message = Communication(
        sender_id=sender_id,
        recipient_id=recipient_id,
        timestamp=timestamp,
        content=content,
        is_read=is_read,
        attachment_url=attachment_url
    )
    db.session.add(new_message)
    db.session.commit()

def get_messages():
    messages = Communication.query.all()  # Change 'communications' to 'Communication'
    messages_data = [{
        'message_id': message.communication_id,  # Updated from 'message_id' to 'communication_id'
        'sender_id': message.sender_id,
        'recipient_id': message.recipient_id,
        'timestamp': message.sent_at,  # Updated from 'timestamp' to 'sent_at'
        'content': message.message,  # Updated from 'message' to 'message'
        'is_read': message.is_read,
        'attachment_url': message.attachment_url
    } for message in messages]
    return messages_data