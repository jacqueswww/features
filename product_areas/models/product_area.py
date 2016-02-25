import datetime
from features_app.db import db


class ProductArea(db.Model):
    __tablename__ = 'product_areas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
