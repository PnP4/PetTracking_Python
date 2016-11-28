import __init__
#data=json.loads('{"lon": 79.589, "alertmsg": "Pet moves out", "time": 125885555, "lat": 83.045, "petname": "abc", "id": 1001}')
while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='alert',
                                  no_ack=True)

            __init__.channel.start_consuming()

    except Exception, e:
        print e