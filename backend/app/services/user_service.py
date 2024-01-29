# backend/app/services/user_service.py

from app.models.user import User  # Change 'users' to 'User'
from app import db

def create_user(username, password, email, role):
    new_user = User(
        username=username,
        password=password,
        email=email,
        role=role
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_all_users():
    return User.query.all()

def update_user(user, data):
    user.username = data.get('username', user.username)
    user.password = data.get('password', user.password)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)

    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()