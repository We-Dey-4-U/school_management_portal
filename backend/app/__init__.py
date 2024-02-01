# backend/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    # Import and register blueprints
    from app.routes.user_routes import user_bp
    from app.routes.communication_routes import communication_bp
    from app.routes.parent_routes import parent_bp  # Import parent_bp
    from app.routes.student_routes import student_bp
    from app.routes.tuition_fee_routes import tuition_fee_bp
    from app.routes.payment_routes import payment_bp
    from app.routes.teacher_routes import teacher_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.subject_routes import subject_bp
    from app.routes.class_routes import class_bp
    from app.routes.teacher_subject_routes import teacher_subject_bp
    from app.routes.exam_routes import exam_bp
    from app.routes.grades_routes import grade_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(communication_bp)
    app.register_blueprint(parent_bp)  # Register parent_bp
    app.register_blueprint(student_bp)
    app.register_blueprint(tuition_fee_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(subject_bp)
    app.register_blueprint(class_bp)
    app.register_blueprint(teacher_subject_bp)
    app.register_blueprint(exam_bp) 
    app.register_blueprint(grade_bp)

    return app