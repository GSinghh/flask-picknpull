from flask import Flask
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://user:password@localhost:5432/postgres"
    )
    db.init_app(app)


if __name__ == "__main__":
    create_app()
