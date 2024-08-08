from flask import Blueprint
from ..models.user import User
from ..extensions import db

main = Blueprint("main", __name__)


@main.route("/signup/<email>/<number>")
def signup_user(email, number):
    Users = User(email=email, number=number)
    db.session.add(Users)
    db.session.commit()

    return "User added successfully"
