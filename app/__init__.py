from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .extensions import db
from .routes.user_routes import main
from .routes.hardware_info_routes import hardware


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(hardware)
    migate = Migrate(app, db)
    return app

