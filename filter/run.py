#heart rate and speed are filtered
import __init__

#data=json.loads('{"id":1001,"petname":"abc","speed":50,"lat":83.045,"lon":79.589,"time":125885555,"heartrate":92}')


while True:
    try:
        while True:
            print 1
            data = json.loads(__init__.socket.recv())
            if (data["To"] == 2):
                filter(data)

    except Exception, e:
        print e


