# backend/app/models/admin.py
from app import db
from app.models.user import User  # Import the User model

class Admin(db.Model):
    __tablename__ = 'Admin'
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), unique=True, nullable=False)
    join_date = db.Column(db.DATE, default=db.func.current_date(), nullable=False)
    department = db.Column(db.VARCHAR(100))
    responsibilities = db.Column(db.TEXT)
    address = db.Column(db.VARCHAR(255))
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    mobile_number = db.Column(db.VARCHAR(20))
    password_hash = db.Column(db.VARCHAR(255), nullable=False)

    # Establish the relationship with the User model
    user = db.relationship('User', back_populates='admin')

    def __repr__(self):
        return f'<Admin {self.admin_id}>'