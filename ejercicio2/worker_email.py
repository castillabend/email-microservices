###CODIGO PARA USAR EL TERCER ARCHIVO ENVIOEMAIL.PY########
# import pika
# import json
# from ejercicio2.envioemail_2 import enviaremail
#
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.exchange_declare(exchange='logs', exchange_type='fanout')
# results = channel.queue_declare(exclusive=True)
# queue_name = results.method.queue
# channel.queue_bind(exchange='logs', queue=queue_name)
# print("[*] Starting worker with queue {}".format(queue_name))
#
#
# def callback(ch, method, properties, body):
#     print("[*] Message for broker {}: {}".format(queue_name, body))
#
#     j = json.loads(body)
#     print(j)
#     if j ['tipo'] == 'Error':
#         enviaremail(j['tipo'], j['body'], j['to'],j['from'],)
#
#
# channel.basic_consume(callback, queue=queue_name, no_ack=True)
# print("Worker Start")
# channel.start_consuming()

#CODIGO PARA NO USAR EL TERCER ARCHIVO ENVIOEMAIL.PY###
import pika
import json
import smtplib

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
    print(j)
    send_data = '[{}] {} {}'.format(j['tipo'], j['codigo'],j['body'])
    if j['tipo'] == 'Error':
        print('Sending email')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('castillabend@gmail.com', 'reinandoenvida')
        server.sendmail('castillabend@gmail.com', 'castillabend@gmail.com', send_data)
        server.quit()


channel.basic_consume(callback, queue=queue_name, no_ack=True)
print("Worker Start")
channel.start_consuming()


