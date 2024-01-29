# backend/app/models/communication.py

from app import db

class Communication(db.Model):
    communication_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)
    attachment_url = db.Column(db.String(255))

    # Establish relationship with User model for sender and recipient
    sender = db.relationship('User', foreign_keys=[sender_id])
    recipient = db.relationship('User', foreign_keys=[recipient_id])

    def __repr__(self):
        return f'<Communication {self.communication_id}>'