import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='alert')
channel.queue_declare(queue='map')


isdatasend=True
isdata2send=True


def callback(ch, method, properties, body):
    data = json.loads(body)
    mainalert = {}
    mainalert["alert"] = []

    if (isdatasend):
        mainalert["alert"].append(data)

    if (isdatasend & isdata2send):
        channel.basic_publish(exchange='',
                              routing_key='map',
                              body=json.dumps(mainalert))
        print json.dumps(mainalert)