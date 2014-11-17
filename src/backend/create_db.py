__author__ = 'linas'

from orm import db, WindPoint
db.create_all()

w1 = WindPoint(service="test", strenght_knts=15, direction='N')
db.session.add(w1)

db.session.commit()
