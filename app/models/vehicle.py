from ..extensions import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    start_year = db.Column(db.String, nullable=False, unique=False)
    end_year = db.Column(db.String, nullable=False, unique=False)
    postal_code = db.Column(db.String, nullable=False, unique=False)
    distance = db.Column(db.String, nullable=False, unique=False)
    make = db.Column(db.String, nullable=False, unique=False)
    model = db.Column(db.String, nullable=False, unique=False)
    
    owner = db.relationship('User', back_populates='vehicles')
    
    results = db.relationship('Result', back_populates='vehicles', cascade='')