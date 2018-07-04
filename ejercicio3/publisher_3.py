import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='direct')

message = json.dumps({'tipo': 'Error',
                     'codigo': '123456789',
                     'body': 'Ojo men, error in server'
                     })
j = json.loads(message)
channel.basic_publish(exchange='logs', routing_key=j['tipo'], body=message)
print(" [*] Sent message: {}".format(message))
print("Done")
connection.close()







