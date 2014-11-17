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

    def __init__(self, service):
        self.service = service
        self.ts = datetime.datetime.utcnow()

    def __repr__(self):
        return '<Service:\t\t{}, TS:\t\t{}>'.format(self.service, self.ts)

