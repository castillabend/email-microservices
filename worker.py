import pika
import json
from envioemail import enviaremail

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
channel.queue_declare(queue="importers")


def importers(ch, method, properties, body):
    j = json.loads(body)
    print(j)
    enviaremail(j['subject'], j['destine'], j['from'], j['body']) #, j['cc']


channel.basic_consume(importers, queue="importers", no_ack=True)
print("Worker Start")
channel.start_consuming()
