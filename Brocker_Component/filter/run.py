#heart rate and speed are filtered
import __init__

#data=json.loads('{"id":1001,"petname":"abc","speed":50,"lat":83.045,"lon":79.589,"time":125885555,"heartrate":92}')


while True:
    try:
        while True:
            print 1
            __init__.channel.basic_consume(__init__.callback,
                                  queue='filter',
                                  no_ack=True)

            __init__.channel.start_consuming()

    except Exception, e:
        print e


