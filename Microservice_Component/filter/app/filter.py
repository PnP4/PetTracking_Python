#heart rate and speed are filtered
import json
import requests




def getlocationdata(data):
    lat = data["lat"]
    lon = data["lon"]
    return lat,lon

def senddata():
    data = json.loads(
        '{"id":1001,"petname":"abc","speed":50,"lat":83.045,"lon":79.589,"time":125885555,"heartrate":92}')
    url = "http://localhost:5003"
    lat,lon=getlocationdata(data)

    filterddata={}
    filterddata["id"] = data["id"]
    filterddata["petname"] = data["petname"]
    filterddata["lat"] = lat
    filterddata["lon"] = lon
    filterddata["time"] = data["time"]

    print json.dumps(filterddata)
    requests.post(url, json=filterddata)
