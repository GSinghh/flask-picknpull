from ..extensions import db
from sqlalchemy import ForeignKey

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    start_year = db.Column(db.String(16), nullable=True, unique=False)
    end_year = db.Column(db.String(16), nullable=True, unique=False)
    postal_code = db.Column(db.String(16), nullable=False, unique=False)
    distance = db.Column(db.String(16), nullable=False, unique=False)
    make = db.Column(db.String(16), nullable=False, unique=False)
    model = db.Column(db.String(16), nullable=False, unique=False)
    
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User', back_populates='vehicles')
    
    results = db.relationship('Result', back_populates='vehicle', cascade='delete, delete-orphan', uselist=False)
    
    @classmethod
    def get_vehicles_by_id(cls, user_id_param: int):
        vehicles = cls.query.filter_by(user_id = user_id_param).all()
        return vehicles
    
    @staticmethod
    def validate_years(start_year, end_year):
        if start_year != "" and end_year == "":
            return start_year
        elif start_year == "" and end_year != "":
            return end_year
        else:
            return f"{start_year}-{end_year}"
    
    def __repr__(self) -> str:
        return f"{self.validate_years(self.start_year, self.end_year)} {self.make} {self.model}"
    
    def serialize(self):
        return {"id": self.id,
                "start_year": self.start_year,
                "end_year": self.end_year,
                "postal_code": self.postal_code,
                "distance": self.distance,
                "make": self.make, 
                "model": self.model}
    
