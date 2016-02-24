import datetime
from features_app.db import db


class Feature(db.DynamicDocument):
    title = db.StringField(max_length=2048, index=True)
    descripton = db.StringField()
    client = db.StringField(index=True)
    client_priority = db.IntField()
    target_date = db.DateTimeField(default=datetime.datetime.now)

    # additional meta:
    created_by = db.StringField()
    modified_by = db.StringField()
    date_created =  db.DateTimeField(default=datetime.datetime.now)
    date_modified =  db.DateTimeField()
