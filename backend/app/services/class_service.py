from app.models.class_model import Classes
from app import db

def create_class(teacher_id, subject_id, grade_level, room_number, schedule_day, class_start_time, class_end_time, teacher_name, subject_name):
    new_class = Classes(
        teacher_id=teacher_id,
        subject_id=subject_id,
        grade_level=grade_level,
        room_number=room_number,
        schedule_day=schedule_day,
        class_start_time=class_start_time,
        class_end_time=class_end_time,
        teacher_name=teacher_name,
        subject_name=subject_name
    )
    db.session.add(new_class)
    db.session.commit()
    return new_class

def get_class_by_id(class_id):
    return Classes.query.get(class_id)

def get_all_classes():
    return Classes.query.all()

def update_class(class_instance, data):
    class_instance.teacher_id = data.get('teacher_id', class_instance.teacher_id)
    class_instance.subject_id = data.get('subject_id', class_instance.subject_id)
    class_instance.grade_level = data.get('grade_level', class_instance.grade_level)
    class_instance.room_number = data.get('room_number', class_instance.room_number)
    class_instance.schedule_day = data.get('schedule_day', class_instance.schedule_day)
    class_instance.class_start_time = data.get('class_start_time', class_instance.class_start_time)
    class_instance.class_end_time = data.get('class_end_time', class_instance.class_end_time)
    class_instance.teacher_name = data.get('teacher_name', class_instance.teacher_name)
    class_instance.subject_name = data.get('subject_name', class_instance.subject_name)

    db.session.commit()
    return class_instance

def delete_class(class_instance):
    db.session.delete(class_instance)
    db.session.commit()