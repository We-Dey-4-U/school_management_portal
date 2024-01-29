# backend/app/services/parent_service.py

from app.models.parent import Parent  # Change 'parent' to 'Parent'
from app import db

def create_parent(user_id, parent_name, contact_number, email):
    new_parent = Parent(
        user_id=user_id,
        parent_name=parent_name,
        contact_number=contact_number,
        email=email
    )
    db.session.add(new_parent)
    db.session.commit()
    return new_parent

def get_parent_by_id(parent_id):
    return Parent.query.get(parent_id)

def get_all_parents():
    return Parent.query.all()

def update_parent(parent, data):
    parent.user_id = data.get('user_id', parent.user_id)
    parent.parent_name = data.get('parent_name', parent.parent_name)
    parent.contact_number = data.get('contact_number', parent.contact_number)
    parent.email = data.get('email', parent.email)

    db.session.commit()
    return parent

def delete_parent(parent):
    db.session.delete(parent)
    db.session.commit()