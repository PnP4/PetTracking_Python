from math import radians, cos, sin, asin, sqrt
import json

data=json.loads('{"lat": 83.045, "petname": "abc", "lon": 79.589, "id": 1001, "time": 125885555}')

def haversine(lon1, lat1, lon2, lat2):
    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 * 1000  # get as meters
    return c * r

predefinelat=83.045
predefinelon=79.589
maxdistance=50 #in meters

lat= data["lat"]
lon=data["lon"]

curdistance=haversine(predefinelon,predefinelat,lon,lat)

if(curdistance<maxdistance):
    alert = {}
    alert["id"] = data["id"]
    alert["petname"] = data["petname"]
    alert["lat"] = lat
    alert["lon"] = lon
    alert["alertmsg"] = "Pet moves out"
    alert["time"] = data["time"]
    print json.dumps(alert)