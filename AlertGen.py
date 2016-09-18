import json
import time
data=json.loads('{"lon": 79.589, "alertmsg": "Pet moves out", "time": 125885555, "lat": 83.045, "petname": "abc", "id": 1001}')


isdatasend=True
isdata2send=True

time.sleep(0.5)

mainalert={}
mainalert["alert"]=[]

if(isdatasend):
    mainalert["alert"].append(data)

if(isdatasend & isdata2send):
    print json.dumps(mainalert)