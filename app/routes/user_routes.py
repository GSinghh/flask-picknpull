from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from ..models.user import User
from ..extensions import db

main = Blueprint("main", __name__)
api = Api(main)


class Users(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data.get("email")
            number = data.get("number")
            
            user = User(email=email, number=number)
            db.session.add(user)
            db.session.commit()
            return {"message": f"User with email: {email} and number: {number} added succesfully",
                    "response_code": 200}
        except Exception as e:
            return {"error": f"Exception: {e}", 
                    "response_code": 500}

    def get(self):
        try:
            all_users = User.query.all()
            if all_users:
                return jsonify([user.serialize() for user in all_users])        
            else:
                return {"error": "Users not Found",
                        "response_code": 404}
        except Exception as e:
            return {"error": f"Exception: {e}", 
                    "response_code": 500}

    def delete(self):
        try:
            data = request.get_json()
            email = data.get("email")
            number = data.get("number")
            found_user = User.query.filter_by(email=email, number=number).first()
            
            if found_user:
                db.session.delete(found_user)
                db.session.commit()
                return {"Message": f"User with email: {email} and number: {number} deleted",
                        "response_code": 200}
            else:
                return {"Error": "User Not Found",
                        "response_code": 404}
        except Exception as e:
            return {"Error": f"{e}", "response_code": 500}

        
api.add_resource(Users, "/users")
