from flask import Blueprint, request
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
            number = data['number']
            user_id = User.get_id_by_number(number)
            vehicles = Vehicle.get_vehicles_by_id(user_id)
            if not vehicles:
                return {"Message": "No Vehicles Found"}
            else:
                return {"Current Vehicles": f"Vehicles: {vehicles}"} 
        except KeyError as key: 
            return {"Key Error": f"{key} not found"}    
        except Exception as e:
            return {"error": f"An error occured: {e}"}
            
    def post(self):
        try:
            data = request.get_json()
            
            number = data['number']
            user_id = User.get_id_by_number(number)
            
            start_year = data['start_year']
            end_year = data['end_year']
            postal_code = data['postal_code']
            distance = data['distance']
            make = data['make']
            model = data['model']            
            vehicle = Vehicle(start_year=start_year, end_year=end_year, postal_code=postal_code, distance=distance, make=make, model=model, user_id=user_id)
            db.session.add(vehicle)
            db.session.commit()
            
            return {"message": f"{vehicle.validate_years(start_year, end_year)} {make} {model} Added"}
        except KeyError as key: 
            return {"Key Error": f"{key} not found"}
        except Exception as e:
            return {"error": f"Error Occured: {e}"}
        
    
    def delete(self):
        pass
    
api.add_resource(Vehicles, "/vehicles")