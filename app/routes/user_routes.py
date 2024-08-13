from flask import Blueprint, jsonify
from ..models.user import User
from ..extensions import db

main = Blueprint("main", __name__)


@main.route("/signup/<email>/<number>")
def signup_user(email, number):
    Users = User(email=email, number=number)
    db.session.add(Users)
    db.session.commit()

    return "User added successfully"


@main.route("/records", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    return jsonify([user.serialize() for user in all_users])


@main.route("/delete/<email>/<number>")
def delete_user(email, number):
    pass
