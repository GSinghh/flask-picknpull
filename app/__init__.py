from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .extensions import db
from .routes.user_routes import main
from .routes.hardware_info_routes import hardware
from celery import Celery


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.Config")
    celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_BACKEND_URL"])
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(hardware)
    migate = Migrate(app, db)
    return app
