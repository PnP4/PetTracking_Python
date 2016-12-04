import __init__
import json

#data=json.loads('{"lat": 83.045, "petname": "abc", "lon": 79.589, "id": 1001, "time": 125885555}')

while True:
    try:
        while True:
            data = json.loads(__init__.socket.recv())
            if (data["To"] == 3):
                check(data)


    except Exception, e:
        print e
