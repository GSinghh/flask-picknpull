from ..extensions import db

class Model(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(32), nullable=False, unique=True)
    model_code = db.Column(db.String(8), nullable=False, unique=True)