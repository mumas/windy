__author__ = 'linas'
from flask import Flask, jsonify
from flask.ext.restful import reqparse, abort, Api, Resource
from orm import WindPoint, db


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

@app.route('/', methods=['GET'])
def index():
    windpoints = WindPoint.query.all()
    return jsonify({'windpoints':  str(windpoints)})

from flask import request

@app.route('/', methods=['POST'])
def create_task():
    if not request.json \
            or not 'service' in request.json\
            or not 'knts' in request.json\
            or not 'direction' in request.json:
        abort(400)

    timestamp = request.json.get('timedate', None)
    windpoint = WindPoint(service=request.json['service'],
                          strenght_knts=request.json['knts'],
                          direction=request.json['direction'],
                          ts=timestamp)

    db.session.add(windpoint)
    db.session.commit()

    return jsonify({'windpoint': str(windpoint)}), 201

if __name__ == '__main__':
    app.run(debug=True)