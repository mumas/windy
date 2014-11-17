__author__ = 'linas'


POST:
    http://host/data/addpoint
    POST data is URL encoded

    service=windguru&timedate=2013-01-01T06%3A00&strenght_knts=15&direction=N

service is the service that we record
strenght_knts is \in {0, 100}
direction is one of {N, NNE, NE, ENE, E, ESE, SE, SSE, S, SSW, SW, WSW, W, WNW, NW, NNW}

timedate is time in minutes resolution (default is current timedate)
