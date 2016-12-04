import json
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')


isdatasend=True
isdata2send=True

def genalert(data):
    mainalert = {}
    mainalert["alert"] = []

    if (isdatasend):
        mainalert["alert"].append(data)
        mainalert["To"]= 5

    if (isdatasend & isdata2send):
        socket.send(json.dumps(mainalert))
        print json.dumps(mainalert)
