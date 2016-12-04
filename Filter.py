#heart rate and speed are filtered

import json
from nanomsg import Socket, BUS


#data=json.loads('{"id":1001,"petname":"abc","speed":50,"lat":83.045,"lon":79.589,"time":125885555,"heartrate":92}')
socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')

def getlocationdata(data):
    lat = data["lat"]
    lon = data["lon"]
    return lat,lon

while True:
    try:
        while True:
            data = json.loads(socket.recv())
            if (recv_data["To"] == 2):
                lat,lon=getlocationdata(data)
                filterddata={}
                filterddata["id"] = data["id"]
                filterddata["petname"] = data["petname"]
                filterddata["lat"] = lat
                filterddata["lon"] = lon
                filterddata["time"] = data["time"]
                filterddata["To"] = 3
                socket.send(json.dumps(filterddata))
                print json.dumps(filterddata)

    except Exception, e:
        print e
