__author__ = 'linas'


import datetime

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wind.db'
db = SQLAlchemy(app)


class WindPoint(db.Model):

    __tablename__ = 'windpoint'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(255))
    ts = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    strenght_knts = db.Column(db.Float(), default=0.0)
    direction = db.Column(db.String(3), default="???")

    def __init__(self, service, strenght_knts, direction, ts=None):
        self.service = service
        if ts:
            self.ts = ts
        else:
            self.ts = datetime.datetime.utcnow()
        self.strenght_knts = strenght_knts
        self.direction = direction

    def __repr__(self):
        return str({'Service': self.service, 'ts': self.ts, 'knts':self.strenght_knts, 'direction': self.direction})

