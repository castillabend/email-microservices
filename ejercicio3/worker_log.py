import sys
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='direct')
results = channel.queue_declare(exclusive=True)
queue_name = results.method.queue


channel.queue_bind(exchange='logs', routing_key='Error', queue=queue_name)
channel.queue_bind(exchange='logs', routing_key='Warning', queue=queue_name)
channel.queue_bind(exchange='logs', routing_key='Debug', queue=queue_name)
channel.queue_bind(exchange='logs', routing_key='Info', queue=queue_name)
#print("[*] Starting logs...")
print("[*] Starting worker with queue {}".format(queue_name))


def callback(ch, method, properties, body):
    print("[*]  [{}] {}".format(method.routing_key, body))
    j = json.loads(body)
    obj = open('Logs.txt', 'a')
    obj.write(str(j['tipo'])+' '+str(j['codigo'])+':  '+str(j['body'])+'\n')
    obj.close()


channel.basic_consume(callback, queue=queue_name, no_ack=True)
print("Worker Log Start")
channel.start_consuming()









