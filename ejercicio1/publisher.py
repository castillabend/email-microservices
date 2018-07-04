import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="importers")
channel.basic_publish(
    exchange="",
    routing_key="importers",
    body=json.dumps({'subject': 'Hello World',
                     'from': 'castillabend@gmail.com',
                     #'cc': 'jmmdaya@gmail.com',
                     'destine': 'castillabend@gmail.com',
                     'body': ' The world is mine, you know'})
)
print("Done")
connection.close()
