import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='filter')
channel.queue_declare(queue='checkrange')


def getlocationdata(data):
    lat = data["lat"]
    lon = data["lon"]
    return lat,lon


def callback(ch, method, properties, body):
    print 2
    data = json.loads(body)
    lat, lon = getlocationdata(data)

    filtereddata = {}
    filtereddata["id"] = data["id"]
    filtereddata["petname"] = data["petname"]
    filtereddata["lat"] = lat
    filtereddata["lon"] = lon
    filtereddata["time"] = data["time"]
    print json.dumps(data)
    channel.basic_publish(exchange='',
                          routing_key='checkrange',
                          body=json.dumps(filtereddata))