__author__ = 'linas'

Get all the data:
    curl  http://localhost:5000/

You can add data points like this:
    curl -i -H "Content-Type: application/json" -X POST -d '{"service":"windguru", "knts": 15, "direction":"N"}' http://localhot:5000/

