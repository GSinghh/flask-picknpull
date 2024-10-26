from ..extensions import db

class Make(db.Model):
    __tablename__ = "makes"
    id = db.Column(db.Integer, primary_key=True)
    make_name = db.Column(db.String(16), nullable=True, unique=True)
    make_code = db.Column(db.String(8), nullable=False, unique=True)