# app/services/admin_service.py
from app.models.admin import Admin
from app import db

def create_admin(user_id, join_date, department, responsibilities, address, email, mobile_number, password_hash):
    new_admin = Admin(
        user_id=user_id,
        join_date=join_date,
        department=department,
        responsibilities=responsibilities,
        address=address,
        email=email,
        mobile_number=mobile_number,
        password_hash=password_hash
    )
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def get_admin_by_id(admin_id):
    return Admin.query.get(admin_id)

def get_all_admins():
    return Admin.query.all()

def update_admin(admin, data):
    admin.user_id = data.get('user_id', admin.user_id)
    admin.join_date = data.get('join_date', admin.join_date)
    admin.department = data.get('department', admin.department)
    admin.responsibilities = data.get('responsibilities', admin.responsibilities)
    admin.address = data.get('address', admin.address)
    admin.email = data.get('email', admin.email)
    admin.mobile_number = data.get('mobile_number', admin.mobile_number)
    admin.password_hash = data.get('password_hash', admin.password_hash)

    db.session.commit()
    return admin

def delete_admin(admin):
    db.session.delete(admin)
    db.session.commit()