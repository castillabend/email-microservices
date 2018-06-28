from celery import Celery


app = Celery('prueba', backend= 'amqp://quest:quest@localhost',broker= 'amqp://localhost')

@app.task
def add(x, y):
    return x + y