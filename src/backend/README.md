__author__ = 'linas'

You can add data points like this:
curl -i -H "Content-Type: application/json" -X POST -d '{"service":"windguru", "knts": 15, "direction":"N"}' http://localhot:5000/
