from .run import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(6), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    is_checked_out = db.Column(db.Boolean, default=False)
    checked_out_by = db.Column(db.String(6), nullable=True)
    checked_out_date = db.Column(db.DateTime, nullable=True)
