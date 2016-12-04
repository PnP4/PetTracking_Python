import __init__
import json
#data=json.loads('{"lon": 79.589, "alertmsg": "Pet moves out", "time": 125885555, "lat": 83.045, "petname": "abc", "id": 1001}')
while True:
    try:
        while True:
            data = json.loads(__init__.socket.recv())
            if (data["To"] == 4):
                genalert(data)

    except Exception, e:
        print e