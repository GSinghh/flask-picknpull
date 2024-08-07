from .. import db


class User(db.Model):
    __table__name = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(32), nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}, email: {self.email}, phone_number: {self.phone_number}"
