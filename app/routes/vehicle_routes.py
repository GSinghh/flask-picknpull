from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models.vehicle import Vehicle
from ..models.user import User
from ..extensions import db


vehicles_bp = Blueprint("vehicles",  __name__)
api = Api(vehicles_bp)

class Vehicles(Resource):
    def get(self):
        try:
            data = request.get_json()
            number = data.get("number")
            user_id = User.get_id_by_number(number)
            vehicles = Vehicle.getVehicles(user_id)
            return {"Vehicles": f"Vehicles: {vehicles}"}
        except Exception as e:
            return {"error": f"An error occured: {e}"}
            
    def post(self):
        try:
            data = request.get_json()
            
            number = data.get("number")
            user_id = User.get_id_by_number(number)
            
            start_year = data.get("start_year")
            end_year = data.get("end_year")
            postal_code = data.get("postal_code")
            distance = data.get("distance")
            make = data.get("make")
            model = data.get("model")
            
            vehicle = Vehicle(start_year=start_year, end_year=end_year, postal_code=postal_code, distance=distance, make=make, model=model, user_id=user_id)
            db.session.add(vehicle)
            db.session.commit()
            
            return {"message": f"{start_year + " " +  end_year} {make} {model} Added"}
        except Exception as e:
            return {"error": f"Error Occured: {e}"}
    
    def delete(self):
        pass
    
api.add_resource(Vehicles, "/vehicles")