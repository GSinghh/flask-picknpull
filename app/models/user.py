from ..extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    number = db.Column(db.String(32), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"id: {self.id}, email: {self.email}, phone_number: {self.number}"

    def serialize(self):
        return {"id": self.id, "email": self.email, "number": self.number}

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    start_year = db.Column(db.String, nullable=False, unique=False)
    end_year = db.Column(db.String, nullable=False, unique=False)
    postal_code = db.Column(db.String, nullable=False, unique=False)
    distance = db.Column(db.String, nullable=False, unique=False)
    make = db.Column(db.String, nullable=False, unique=False)
    model = db.Column(db.String, nullable=False, unique=False)
    make_id = db.Column(db.String, nullable=False, unique=False)
    model_id = db.Column(db.String, nullable=False, unique=False)