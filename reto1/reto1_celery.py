import json
import smtplib
from celery import Celery
from kombu import Exchange, Queue

app = Celery('reto1_celery', backend='amqp://quest:quest@localhost', broker='amqp://localhost')

exchange = Exchange('custom_exchange', type='fanout')

app.conf.task_default_queue = 'fanout'
app.conf.task_default_exchange = exchange
                                                                                                # app.conf.task_default_routing_key = 'fanout'


app.conf.task_queues = (
    Queue('log', exchange=exchange, routing_key='fanout'),
                                                                                            # Queue('videos', exchange, routing_key='media.video'),
                                                                                                # Queue('images', exchange, routing_key='media.image')
)
                                                                                               #channel = connection.channel()
                                                                                                #channel.exchange_declare(exchange='logs', exchange_type='direct')
                                                                                                #results = channel.queue_declare(exclusive=True)
                                                                                                #queue_name = results.method.queue


                                                                                                #channel.queue_bind(exchange='logs', routing_key='Error')

@app.task(bind=True)
def worker_email(message):
                                                                                                 # print("[*] Message for broker {}: {}".format( message))

    j = json.loads(message)
    print(j)
    send_data = '[{}] {} {}'.format(j['tipo'], j['codigo'], j['body'])
    if j['tipo'] == 'Error':
        print('Sending email')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('castillabend@gmail.com', 'reinandoenvida')
        server.sendmail('castillabend@gmail.com', 'castillabend@gmail.com', send_data)
        server.quit()


@app.task(bind=True)
def worker_logs(message):
                                                                                                    #print("[*] Message for broker {}: {}".format(body))
    j = json.loads(message)
    obj = open('Logs.txt', 'a')
    obj.write(str(j['tipo'])+' '+str(j['codigo'])+':  '+str(j['body'])+'\n')
    obj.close()


def publisher():
        message = json.dumps({'tipo': 'Error',
                              'codigo': '6789',
                              'body': 'Ojo men, error in server'
                              })
        worker_email.delay(message)
        worker_logs.delay(message)










# ***********************************************************
#
#
# Broadcast(name='queue_name', Exchange(name='queue_name', type='fanout')
#
# ********************************************
# default_exchange = Exchange('default', type='direct')
# media_exchange = Exchange('media', type='direct')
#
# app.conf.task_queues = (
#     Queue('default', default_exchange, routing_key='default'),
#     Queue('videos', media_exchange, routing_key='media.video'),
#     Queue('images', media_exchange, routing_key='media.image')
# )
# app.conf.task_default_queue = 'default'
# app.conf.task_default_exchange = 'default'
# app.conf.task_default_routing_key = 'default'
#
#
# **********************************************
#
# from kombu.common import Broadcast
# from kombu import Exchange
#
#
# exchange = Exchange('custom_exchange', type='fanout')
#
# CELERY_QUEUES = (
#     Broadcast(name='bcast', exchange=exchange),
# )