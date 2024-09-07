from ..extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    number = db.Column(db.String(32), nullable=False, unique=True)
    vehicles = db.relationship('Vehicle', back_populates='owner', cascade='all, delete-orphan')
    
    def __repr__(self) -> str:
        return f"id: {self.id}, email: {self.email}, phone_number: {self.number}"

    def serialize(self):
        return {"id": self.id, "email": self.email, "number": self.number}
