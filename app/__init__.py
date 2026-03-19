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

    # Create tables + run migrations for new columns
    with app.app_context():
        db.create_all()
        _run_migrations()

    return app


def _run_migrations():
    """Додає нові колонки до існуючих таблиць (безпечно, якщо вже є)."""
    from sqlalchemy import text
    migrations = [
        "ALTER TABLE boxes ADD COLUMN max_fill_pct FLOAT DEFAULT 80.0",
        "ALTER TABLE boxes ADD COLUMN weight FLOAT DEFAULT 0.0",
        "ALTER TABLE orders ADD COLUMN order_date TEXT",
        "ALTER TABLE orders ADD COLUMN comment TEXT DEFAULT ''",
        "ALTER TABLE order_items ADD COLUMN extra_comment TEXT DEFAULT ''",
        "ALTER TABLE stock_log ADD COLUMN log_type TEXT DEFAULT 'pick'",
    ]
    for sql in migrations:
        try:
            db.session.execute(text(sql))
            db.session.commit()
        except Exception:
            db.session.rollback()
