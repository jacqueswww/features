import datetime
from features_app.db import db


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
