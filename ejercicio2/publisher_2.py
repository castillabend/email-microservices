import json
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#message = ' '.join(sys.argv[1:]) or "info: Hello World!"

message = json.dumps({'tipo': 'Warning',
                     'codigo': '6789',
                     'body': 'Ojo men, error in server'
                     })
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [*] Sent message: {}".format(message))
# connection.close()


print("Done")
connection.close()




