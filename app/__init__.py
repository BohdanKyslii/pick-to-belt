import os
from flask import Flask
from .models import db


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "static"),
    )

    # Config
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(base_dir, 'data', 'pick_to_belt.db')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pick-to-belt-secret")
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max upload

    # Init DB
    db.init_app(app)

    # Register routes
    from .routes import bp
    app.register_blueprint(bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
