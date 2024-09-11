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
    
    user_id = db.Column(db.Integer, ForeignKey('users.id'), unique=True)
    user = db.relationship('User', back_populates='vehicles')
    
    results = db.relationship('Result', back_populates='vehicle', cascade='delete-orphan', uselist=False)