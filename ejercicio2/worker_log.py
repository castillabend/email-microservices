import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
results = channel.queue_declare(exclusive=True)
queue_name = results.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
print("[*] Starting worker with queue {}".format(queue_name))


def callback(ch, method, properties, body):
    print("[*] Message for broker {}: {}".format(queue_name, body))
    j = json.loads(body)
    obj = open('Logs.txt', 'a')
    obj.write(str(j['tipo'])+' '+str(j['codigo'])+':  '+str(j['body'])+'\n')
    obj.close()


channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()





