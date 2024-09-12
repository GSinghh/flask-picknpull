from flask import Blueprint 
from flask_restful import Api, Resource
from ..models.vehicle import Vehicle
from ..extensions import db

vehicles = Blueprint("vehicles",  __name__)
api = Api(vehicles)

class Vehicles(Resource):
    def get(self):
        pass
    
    def post(self):
        pass
    
    def delete(self):
        pass
    
api.add_resource(vehicles, "/vehicles")