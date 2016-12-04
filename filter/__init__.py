import json
from nanomsg import Socket, BUS


socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')


def getlocationdata(data):
    lat = data["lat"]
    lon = data["lon"]
    return lat,lon


def filter(data):
    print 2
    lat, lon = getlocationdata(data)

    filtereddata = {}
    filtereddata["id"] = data["id"]
    filtereddata["petname"] = data["petname"]
    filtereddata["lat"] = lat
    filtereddata["lon"] = lon
    filtereddata["time"] = data["time"]
    print json.dumps(data)
    socket.send(json.dumps(filterddata))