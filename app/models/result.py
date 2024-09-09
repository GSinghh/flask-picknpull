from ..extensions import db

class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    make = db.Column(db.String, nullable=False)
    row = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    date_added = db.Column(db.String, nullable=False)
    
    parent = db.relationship('Vehicle', back_populates='owner')