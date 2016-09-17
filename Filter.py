#heart rate and speed are filtered

import json


data=json.loads('{"id":1001,"petname":"abc","speed":50,"lat":83.045,"lon":79.589,"time":125885555,"heartrate":92}')

def getlocationdata(data):
    lat = data["lat"]
    lon = data["lon"]
    return lat,lon

lat,lon=getlocationdata(data)

filterddata={}
filterddata["id"] = data["id"]
filterddata["petname"] = data["petname"]
filterddata["lat"] = lat
filterddata["lon"] = lon
filterddata["time"] = data["time"]

print json.dumps(filterddata)
