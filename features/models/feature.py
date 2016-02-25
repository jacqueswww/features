from features_app.db import db 
# from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import func


class Feature(db.Model):
    __tablename__ = "features"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))
    descripton = db.Column(db.String())

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    client_priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime(timezone=True), default=func.now())
 
    # additional meta:
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    modified_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    created_by = db.relationship("User", foreign_keys=[created_by_id])
    modified_by = db.relationship("User", foreign_keys=[modified_by_id])

    date_created =  db.Column(db.DateTime(timezone=True), default=func.now())
    date_modified =  db.Column(db.DateTime(timezone=True))
