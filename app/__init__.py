from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .routes.user_routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    app.register_blueprint(main)
    migate = Migrate(app, db)
    return app
