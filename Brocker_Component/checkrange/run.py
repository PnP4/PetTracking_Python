import __init__

#data=json.loads('{"lat": 83.045, "petname": "abc", "lon": 79.589, "id": 1001, "time": 125885555}')

while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='checkrange',
                                  no_ack=True)

            __init__.channel.start_consuming()

    except Exception, e:
        print e
